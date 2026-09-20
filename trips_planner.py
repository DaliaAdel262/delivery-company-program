from Trip import Trip

# Plan trips:
# 1. sort first
# 2. fit packages in trips delivering to same area and fits tightly (best fit)
def plan_trips(deliveries):
    # sort deliveries by priority, area and weight
    # sorting by weight helps place heavy packages first to minimize number of trips with one package
    deliveries.sort(key=lambda d: (d['priority'], d['area'], -d['weight_kg']))

    # assign deliveries to trips
    trips = []
    for delivery in deliveries:
        trip_found = None
        for trip in trips:
            if trip.area == delivery['area'] and trip.can_fit(delivery['weight_kg']):
                if trip_found is None or trip.total_weight > trip_found.total_weight:
                    trip_found = trip

        # if no trip to same area found, create a new trip
        if trip_found is None:
            trip_found = Trip(delivery['area'])
            trips.append(trip_found)

        trip_found.add_delivery(delivery)

    # sort trips by area to make output more readable
    trips.sort(key=lambda t: t.area)

    return trips