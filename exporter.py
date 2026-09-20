import csv

def export_to_csv(trips, heavy_deliveries):
    # Number trips sorted by area to display trip ids
    trips_with_ids = list(enumerate(trips, start=1))

    # Create new file 'packages.csv' -> displays packages with trip id (trip package is assigned to)
    with open('packages.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'area', 'priority', 'weight_kg', 'trip_id'])

        for trip_id, trip in trips_with_ids:
            for d in trip.deliveries:
                writer.writerow([d['id'], d['area'], d['priority'], d['weight_kg'], trip_id])

        # Packages with weight > 10 get trip id as null value
        for d in heavy_deliveries:
            writer.writerow([d['id'], d['area'], d['priority'], d['weight_kg'], ''])

    # Export trips to csv file trips.csv -> each row displays trip info
    with open('trips.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['trip_id', 'area', 'total_weight_kg', 'package_count'])

        for trip_id, trip in trips_with_ids:
            writer.writerow([trip_id, trip.area, round(trip.total_weight, 2), len(trip.deliveries)])

    print(f"Exported packages.csv and trips.csv")