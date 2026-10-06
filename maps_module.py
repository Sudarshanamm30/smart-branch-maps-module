import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_MAPS_API_KEY not found in .env")

ROUTES_URL = "https://routes.googleapis.com/directions/v2:computeRoutes"


def get_travel_time(user_lat, user_lon, branch_lat, branch_lon):
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "routes.duration,routes.distanceMeters"
    }

    data = {
        "origin": {
            "location": {
                "latLng": {
                    "latitude": user_lat,
                    "longitude": user_lon
                }
            }
        },
        "destination": {
            "location": {
                "latLng": {
                    "latitude": branch_lat,
                    "longitude": branch_lon
                }
            }
        },
        "travelMode": "DRIVE"
    }

    response = requests.post(
        ROUTES_URL,
        headers=headers,
        json=data
    )

    if response.status_code != 200:
        raise Exception(f"Routes API Error: {response.text}")

    result = response.json()

    route = result["routes"][0]

    distance_km = route["distanceMeters"] / 1000
    duration_seconds = int(route["duration"].replace("s", ""))
    travel_time_min = round(duration_seconds / 60)

    return {
        "distance_km": round(distance_km, 2),
        "travel_time_min": travel_time_min
    }


def get_all_branch_travel_times(user_lat, user_lon):
    branches = pd.read_csv("branch_coordinates.csv")

    results = []

    for _, branch in branches.iterrows():

        travel = get_travel_time(
            user_lat,
            user_lon,
            branch["latitude"],
            branch["longitude"]
        )

        results.append({
            "branch": branch["branch"],
            "franchise": branch["franchise"],
            "distance_km": travel["distance_km"],
            "travel_time_min": travel["travel_time_min"]
        })

    return pd.DataFrame(results)


if __name__ == "__main__":

    user_lat = 12.9165
    user_lon = 79.1325

    results = get_all_branch_travel_times(
        user_lat,
        user_lon
    )

    print("\nTravel Results:")
    print(results.to_string(index=False))