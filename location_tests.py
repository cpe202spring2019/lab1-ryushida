import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!
    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SF", 23.4, 12.2)
        loc3 = Location("LA", 43.4, 32.1)
        loc4 = loc1

        self.assertFalse(loc1 == loc2)
        self.assertFalse(loc1 == loc3)
        self.assertTrue(loc1 == loc4)

if __name__ == "__main__":
        unittest.main()
