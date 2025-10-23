import unittest
from pydantic import ValidationError
from models import Package


class TestPackageModel(unittest.TestCase):
    def test_package_volume_calculation(self):
        package = Package(width=10, height=20, length=30, mass=5)
        self.assertEqual(package.volume, 6000)

    def test_package_is_bulky_by_volume(self):
        package = Package(width=100, height=100, length=100, mass=10)
        self.assertTrue(package.is_bulky)

    def test_package_is_bulky_by_dimension(self):
        package = Package(width=150, height=50, length=50, mass=10)
        self.assertTrue(package.is_bulky)

    def test_package_is_not_bulky(self):
        package = Package(width=50, height=50, length=50, mass=10)
        self.assertFalse(package.is_bulky)

    def test_package_is_heavy(self):
        package = Package(width=50, height=50, length=50, mass=20)
        self.assertTrue(package.is_heavy)

    def test_package_is_not_heavy(self):
        package = Package(width=50, height=50, length=50, mass=10)
        self.assertFalse(package.is_heavy)

    def test_package_negative_value(self):
        with self.assertRaises(ValidationError):
            Package(width=-10, height=50, length=50, mass=10)

    def test_package_zero_value(self):
        with self.assertRaises(ValidationError):
            Package(width=0, height=50, length=50, mass=10)

    def test_invalid_type_string(self):
        with self.assertRaises(ValidationError):
            Package(width="invalid", height=50, length=50, mass=10)

    def test_invalid_type_none(self):
        with self.assertRaises(ValidationError):
            Package(width=None, height=50, length=50, mass=10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
