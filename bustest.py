import unittest
from Bus import Bus
from Passenger import Passenger


class TestBus(unittest.TestCase):
    def test_median_passenger_weight(self):
        bus = Bus(3)
        passenger1 = Passenger("Маша", 60)
        passenger2 = Passenger("Саша", 70)
        passenger3 = Passenger("Рома", 80)
        passenger1.enter_bus(bus)
        passenger2.enter_bus(bus)
        passenger3.enter_bus(bus)
        self.assertEqual(70, bus.median_passenger_weight())
        passenger2.exit_bus()
        self.assertEqual(70, bus.median_passenger_weight())
        Passenger("Гриша", 80).enter_bus(bus)
        self.assertEqual(80, bus.median_passenger_weight())
        Passenger("Фёдр", 30).enter_bus(bus)
        self.assertEqual(80, bus.median_passenger_weight())

    def test_median2(self):
        bus = Bus(3)
        self.assertEqual(0, bus.median_passenger_weight())

    def test_init(self):
        bus = Bus(3)
        self.assertRaises(ValueError, Bus, -4)
        self.assertRaises(TypeError, Bus, "Вася")

    def test_bus_disembark_all(self):
        bus = Bus(3)
        passenger1 = Passenger("Маша", 60)
        passenger2 = Passenger("Саша", 70)
        passenger3 = Passenger("Рома", 80)
        passenger1.enter_bus(bus)
        passenger2.enter_bus(bus)
        passenger3.enter_bus(bus)
        bus.disembark_all()
        self.assertEqual(len(bus.passengers), 0)
        bus.disembark_all()
        self.assertEqual(len(bus.passengers), 0)

    def test_take_passenger(self):
        bus = Bus(2)
        passenger1 = Passenger("Маша", 60)
        self.assertEqual(True, bus.take_passenger(passenger1))
        passenger2 = Passenger("Саша", 70)
        self.assertEqual(True, bus.take_passenger(passenger2))
        passenger3 = Passenger("Рома", 80)
        self.assertEqual(False, bus.take_passenger(passenger3))

    def test_take_passenger2(self):
        bus = Bus(2)
        passenger1 = Passenger("Маша", 60)
        self.assertEqual(True, bus.take_passenger(passenger1))
        self.assertEqual(False, bus.take_passenger(passenger1))






if __name__ == '__main__':
    unittest.main()
