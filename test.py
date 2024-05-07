import unittest
from mrm import Motel

class TestMotelReservationSystem(unittest.TestCase):
    def setUp(self):
        self.motel = Motel(5)
        self.motel.make_reservation("Alice", 101)
        self.motel.make_reservation("Bob", 102)

    
    def test_cancel_reservation(self):
        self.assertTrue(self.motel.cancel_reservation("Alice"))
        self.assertFalse(self.motel.cancel_reservation("Eve"))

    def test_update_reservation(self):
        self.assertTrue(self.motel.update_reservation("Alice", "Alicia"))
        self.assertFalse(self.motel.update_reservation("Eve", "Eva"))

    def test_get_reservation(self):
        self.assertEqual(self.motel.get_reservation(101), {"guest_name": "Alice", "room_number": 101})
        self.assertIsNone(self.motel.get_reservation(103))

    def test_check_room_availability(self):
        self.assertTrue(self.motel.check_room_availability(103))
        self.assertFalse(self.motel.check_room_availability(101))

    def test_check_guest_reservation(self):
        self.assertTrue(self.motel.check_guest_reservation("Alice"))
        self.assertFalse(self.motel.check_guest_reservation("Eve"))

    def test_list_reservations(self):
        self.assertEqual(len(self.motel.list_reservations()), 2)
        self.motel.make_reservation("Eve", 103)
        self.assertEqual(len(self.motel.list_reservations()), 3)

    def test_clear_reservations(self):
        self.motel.clear_reservations()
        self.assertEqual(len(self.motel.list_reservations()), 0)

if __name__ == '__main__':
    unittest.main()
