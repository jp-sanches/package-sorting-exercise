import unittest
from pydantic import ValidationError
from main import sort, StackType


class TestPackageSorting(unittest.TestCase):
    # STANDARD package tests
    def test_standard_package(self):
        result = sort(10, 10, 10, 5)
        self.assertEqual(result, "STANDARD")

    def test_standard_edge_case_volume(self):
        result = sort(99, 99, 99, 10)  # Volume = 970,299
        self.assertEqual(result, "STANDARD")

    # SPECIAL package tests - Bulky only
    def test_special_bulky_by_volume(self):
        result = sort(100, 100, 100, 10)  # Volume = 1,000,000
        self.assertEqual(result, "SPECIAL")

    def test_special_bulky_by_volume_exceeded(self):
        result = sort(150, 100, 100, 15)  # Volume = 1,500,000
        self.assertEqual(result, "SPECIAL")

    def test_special_bulky_by_width(self):
        result = sort(150, 50, 50, 10)
        self.assertEqual(result, "SPECIAL")

    def test_special_bulky_by_height(self):
        result = sort(50, 150, 50, 10)
        self.assertEqual(result, "SPECIAL")

    def test_special_bulky_by_length(self):
        result = sort(50, 50, 150, 10)
        self.assertEqual(result, "SPECIAL")

    def test_special_bulky_all_dimensios(self):
        result = sort(150, 150, 150, 10)
        self.assertEqual(result, "SPECIAL")

    # SPECIAL package tests - Heavy only
    def test_special_heavy_exact_threshold(self):
        result = sort(50, 50, 50, 20)
        self.assertEqual(result, "SPECIAL")

    def test_special_heavy_exceeded(self):
        result = sort(50, 50, 50, 50)
        self.assertEqual(result, "SPECIAL")

    # REJECTED package tests - Both bulky and heavy
    def test_rejected_bulky_volume_and_heavy(self):
        result = sort(100, 100, 100, 20)  # Volume = 1,000,000, mass = 20
        self.assertEqual(result, "REJECTED")

    def test_rejected_bulky_dimension_and_heavy(self):
        result = sort(150, 50, 50, 20)
        self.assertEqual(result, "REJECTED")

    def test_rejected_multiple_conditions(self):
        result = sort(150, 150, 150, 50)
        self.assertEqual(result, "REJECTED")

    def test_rejected_edge_case_both_thresholds(self):
        result = sort(100, 100, 100, 20)
        self.assertEqual(result, "REJECTED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
