class Passenger:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.bus = None  # Пассажир изначально не находится в автобусе

    def enter_bus(self, bus):
        if self.bus is None:  # Проверяем, что пассажир не находится в другом автобусе
            self.bus = bus
            bus.take_passenger(self)
            print(f"{self.name} сел в автобус.")

    def exit_bus(self):
        if self.bus is not None:
            self.bus.passengers.remove(self)
            self.bus = None
            print(f"{self.name} вышел из автобуса.")
        else:
            print("Этот пассажир не находится в автобусе.")
