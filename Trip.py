# Trip class represents one vehicle trip and tracks deliveries assigned to it
class Trip:
    def __init__(self, area):
        self.area = area
        self.deliveries = []
        self.total_weight = 0

    def can_fit(self, weight_kg):
        return self.total_weight + weight_kg <= 10

    def add_delivery(self, delivery):
        self.deliveries.append(delivery)
        self.total_weight += delivery['weight_kg']