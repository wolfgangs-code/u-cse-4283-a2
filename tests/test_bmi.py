import pytest
from bmi_cli.bmi import imperial_to_bmi, metric_to_bmi, categorize_bmi, categories


# Core mathematical tests
def test_bmi_positives():
    assert False

def test_bmi_zeros():
    assert False

def test_bmi_negatives():
    assert False

# BMI calculation tests
@pytest.mark.parametrize("bmi, expected", [
    (18.4, "Underweight"),
    (18.5, "Normal weight"),
    (24.9, "Normal weight"),
    (25.0, "Overweight"),
    (29.9, "Overweight"),
    (30.0, "Obese"),
])
def test_bmi_category_boundaries(bmi, expected):
    assert categorize_bmi(bmi) == expected