from maps_module import get_all_branch_travel_times

test_locations = [
    ("Test Location 1", 12.9698, 79.1559),
    ("Test Location 2", 12.9165, 79.1325)
]

for name, lat, lon in test_locations:
    print("\n" + "=" * 50)
    print(name)
    print("Latitude:", lat)
    print("Longitude:", lon)
    print("=" * 50)

    results = get_all_branch_travel_times(lat, lon)

    print(results.to_string(index=False))