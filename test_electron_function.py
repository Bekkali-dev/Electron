import unittest
from electron_function import calculate_age_from_year
from datetime import date

class TestCalculateAgeFromYear(unittest.TestCase):
    def test_age(self):
        current_year = date.today().year
        self.assertEqual(calculate_age_from_year(current_year - 20), 20)
        self.assertEqual(calculate_age_from_year(current_year - 1), 1)

if __name__ == '__main__':
    unittest.main()