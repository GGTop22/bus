import unittest
from Bus import *
from Passenger import *


class TestPass(unittest.TestCase):
    def test_enter1(self):
        bus = Bus(1)
        p = Passenger("Оля", 136)
        p.enter_bus(bus)
        self.assertEqual(bus, p.bus)

    def test_enter2(self):
        bus = Bus(0)
        p = Passenger("Оля", 136)
        p.enter_bus(bus)
        self.assertEqual(None, p.bus)

    def test_enter2a(self):
        bus = Bus(1)
        p = Passenger("Оля", 136)
        p2 = Passenger("Галя", 136)
        p2.enter_bus(bus)
        p.enter_bus(bus)
        self.assertEqual(bus, p2.bus)
        self.assertEqual(None, p.bus)

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
        self.assertEqual(passenger3.bus, None)
        self.assertIn(passenger1, bus.passengers)
        self.assertIn(passenger2, bus.passengers)
        self.assertNotIn(passenger3, bus.passengers)



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
