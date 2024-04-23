from Bus import Bus
from Passenger import Passenger

# Пример использования:

passenger1 = Passenger("Маша", 60)
passenger2 = Passenger("Саша", 70)
passenger3 = Passenger("Рома", 80)

bus = Bus(3)

passenger1.enter_bus(bus)
passenger2.enter_bus(bus)
passenger3.enter_bus(bus)

print(f"Медианный вес пассажиров в автобусе: {bus.median_passenger_weight()}")

passenger2.exit_bus()

print(f"Медианный вес пассажиров в автобусе после выхода пассажира: {bus.median_passenger_weight()}")

bus.disembark_all()

