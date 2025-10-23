from typing import Literal
from pydantic import ValidationError
from models import Package


StackType = Literal["STANDARD", "SPECIAL", "REJECTED"]


def sort(width: float, height: float, length: float, mass: float) -> StackType:
    """
    Sorts packages into appropriate stacks based on their dimensions and mass.

    Args:
        width: Width of the package in centimeters (must be > 0)
        height: Height of the package in centimeters (must be > 0)
        length: Length of the package in centimeters (must be > 0)
        mass: Mass of the package in kilograms (must be > 0)

    Returns:
        StackType: Stack name - "STANDARD", "SPECIAL", or "REJECTED"

    Raises:
        ValidationError: If any dimension or mass is <= 0 or invalid type

    Rules:
        - Bulky: volume >= 1,000,000 cm³ OR any dimension >= 150 cm
        - Heavy: mass >= 20 kg
        - REJECTED: both bulky AND heavy
        - SPECIAL: either bulky OR heavy (but not both)
        - STANDARD: neither bulky nor heavy
    """
    package = Package(width=width, height=height, length=length, mass=mass)

    if package.is_bulky and package.is_heavy:
        return "REJECTED"

    if package.is_bulky or package.is_heavy:
        return "SPECIAL"

    return "STANDARD"


if __name__ == "__main__":
    print("Package Sorting System")
    print("-" * 40)

    try:
        width = float(input("Enter width (cm): "))
        height = float(input("Enter height (cm): "))
        length = float(input("Enter length (cm): "))
        mass = float(input("Enter mass (kg): "))

        result = sort(width, height, length, mass)
        print(f"\nResult: {result}")

    except ValidationError as e:
        print(f"\nValidation Error:")
        for error in e.errors():
            msg = error["msg"]
            print(f"  - {msg}")

    except ValueError as e:
        print(f"\nError: Invalid input - please enter numeric values only")
        print(f"\nError: {e}")

    except Exception as e:
        print(f"\nUnexpected error: {e}")
