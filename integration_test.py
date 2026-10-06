from maps_module import get_all_branch_travel_times

user_lat = 12.9698
user_lon = 79.1559

results = get_all_branch_travel_times(user_lat, user_lon)

for _, row in results.iterrows():
    print({
        "branch": row["branch"],
        "distance_km": row["distance_km"],
        "travel_time_min": row["travel_time_min"]
    })