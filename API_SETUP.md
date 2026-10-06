# Google Maps Routes API Setup

## Project

Smart Branch Recommendation System

## Purpose

This module calculates the driving distance and estimated travel time from a user's location to each restaurant branch.

## Google Cloud Setup

1. Create a Google Cloud project.
2. Enable the Routes API.
3. Create an API key.
4. Restrict the API key to Routes API.
5. Keep the API key inside the `.env` file.
6. Do not upload the `.env` file to GitHub.

## Required Python Packages

Install the required packages using:

pip install requests python-dotenv pandas

## Environment Variable

Create a `.env` file:

GOOGLE_MAPS_API_KEY=YOUR_API_KEY_HERE

Replace `YOUR_API_KEY_HERE` with the actual Google Maps API key.

## Branch Data

The file `branch_coordinates.csv` stores:

- Branch name
- Franchise name
- Latitude
- Longitude

Example:

branch,franchise,latitude,longitude

McDonalds,McDonalds,12.968472367057545,79.1494390396239

Burger King,Burger King,12.962209496361412,79.13736356845968

## Travel Time Function

The main function is:

get_travel_time(user_lat, user_lon, branch_lat, branch_lon)

It returns:

- Distance in kilometers
- Estimated driving time in minutes

## Multiple Branches

The function:

get_all_branch_travel_times(user_lat, user_lon)

calculates travel information for all branches stored in `branch_coordinates.csv`.

## Testing

Run:

python test_maps.py

The module was tested using two different user locations.

### Test Location 1

Latitude: 12.9698

Longitude: 79.1559

Results:

- McDonald's: 1.57 km, 6 minutes
- Burger King: 2.84 km, 8 minutes

### Test Location 2

Latitude: 12.9165

Longitude: 79.1325

Results:

- McDonald's: 8.12 km, 19 minutes
- Burger King: 6.88 km, 16 minutes

## Security

The API key must not be committed to GitHub.

The `.gitignore` file contains:

.env
__pycache__/
*.pyc

## Output

The module produces the following information for each branch:

- Branch name
- Franchise
- Distance in kilometers
- Estimated driving time in minutes

This output can be passed to the recommendation module to combine travel time with predicted restaurant waiting time.