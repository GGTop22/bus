class Bus:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def disembark_all(self):
        for passenger in self.passengers[:]:
            passenger.exit_bus()
        print("Все пассажиры высажены из автобуса.")

    def take_passenger(self, passenger):
        if self.capacity - len(self.passengers) > 0:
            self.passengers.append(passenger)
            return True
        else:
            return False


    def median_passenger_weight(self):
        if not self.passengers:
            return 0
        weights = [passenger.weight for passenger in self.passengers]
        weights.sort()
        n = len(weights)
        if n % 2 == 0:
            return (weights[n // 2 - 1] + weights[n // 2]) / 2
        else:
            return weights[n // 2]

