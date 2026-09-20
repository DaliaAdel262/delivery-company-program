import csv

# Load csv, reads it and converts string fields to numeric types 
# Any package heavier than 10kg is flagged to be reported later
def load_deliveries(path):
    deliveries = []
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['priority'] = int(row['priority'])
            row['weight_kg'] = float(row['weight_kg'])
            row['heavy'] = row['weight_kg'] > 10
            deliveries.append(row)

    heavy_deliveries = [d for d in deliveries if d['heavy']]
    valid_deliveries = [d for d in deliveries if not d['heavy']]
    return valid_deliveries, heavy_deliveries