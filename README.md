# Package Sorting System

Classifies packages into STANDARD, SPECIAL, or REJECTED categories based on dimensions and mass.

## Classification Rules

**Bulky**: Volume >= 1,000,000 cm³ OR any dimension >= 150 cm  
**Heavy**: Mass >= 20 kg

- **STANDARD**: Neither bulky nor heavy
- **SPECIAL**: Either bulky OR heavy
- **REJECTED**: Both bulky AND heavy

## Installation

```bash
pip install -r requirements.txt
```

Requirements: Python 3.10+, pydantic >= 2.0.0

## Usage

### Interactive Mode

Run the script to sort packages interactively:

```bash
python main.py
```

Example session:
```
Package Sorting System
----------------------------------------
Enter width (cm): 150
Enter height (cm): 50
Enter length (cm): 50
Enter mass (kg): 25

Result: REJECTED
```

### Programmatic Usage

```python
from main import sort

# Standard package
sort(50, 50, 50, 10)  # "STANDARD"

# Bulky package
sort(150, 50, 50, 10)  # "SPECIAL"

# Heavy package
sort(50, 50, 50, 25)  # "SPECIAL"

# Rejected package
sort(150, 100, 100, 25)  # "REJECTED"
```

## Testing

```bash
python -m unittest discover

```