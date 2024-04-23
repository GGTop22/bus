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
        self.assertRaises(ValueError, Bus, "Вася")

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
        self.assertEqual(True, bus.take_passenger(passenger1))
        self.assertEqual(False, bus.take_passenger(passenger1))

    def test_enter_bus(self):
        bus = Bus(2)
        passenger1 = Passenger("Маша", 60)
        passenger2 = Passenger("Саша", 70)
        passenger3 = Passenger("Рома", 80)
        passenger1.enter_bus(bus)
        passenger2.enter_bus(bus)
        passenger3.enter_bus(bus)
        self.assertEqual(passenger1.bus, bus)
        self.assertEqual(passenger2.bus, bus)
        self.assertEqual(passenger3.bus, bus)
        self.assertIn(passenger1, bus.passengers)
        self.assertIn(passenger2, bus.passengers)
        self.assertIn(passenger3, bus.passengers)



    def test_exit_bus(self):
        bus = Bus(2)
        passenger1 = Passenger("Маша", 60)
        passenger2 = Passenger("Саша", 70)
        passenger3 = Passenger("Рома", 80)
        passenger1.enter_bus(bus)
        passenger2.enter_bus(bus)
        passenger3.enter_bus(bus)
        passenger1.exit_bus()
        passenger2.exit_bus()
        passenger3.exit_bus()
        self.assertIsNone(passenger1.bus, bus)
        self.assertIsNone(passenger2.bus, bus)
        self.assertIsNone(passenger3.bus, bus)
        self.assertNotIn(passenger1, bus.passengers)
        self.assertNotIn(passenger2, bus.passengers)
        self.assertNotIn(passenger3, bus.passengers)

if __name__ == '__main__':
    unittest.main()
