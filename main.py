from loader import load_deliveries
from trips_planner import plan_trips
from exporter import export_to_csv

if __name__ == '__main__':
    try:
        deliveries, heavy_deliveries = load_deliveries('sample.csv')
    except FileNotFoundError:
        print('could not read file')
        exit()

    trips = plan_trips(deliveries)

    export_to_csv(trips, heavy_deliveries)