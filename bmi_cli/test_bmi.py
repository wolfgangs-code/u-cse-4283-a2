import pytest
from bmi import imperial_to_bmi, metric_to_bmi, categorize_bmi

def test_categorize_bmi():
    # Test with valid BMI values
    assert categorize_bmi(18.4) == "Underweight"
    assert categorize_bmi(22.0) == "Normal weight"
    assert categorize_bmi(27.0) == "Overweight"
    assert categorize_bmi(30.5) == "Obese"

    # Test edge cases
    assert categorize_bmi(18.5) == "Normal weight"
    assert categorize_bmi(24.9) == "Normal weight"
    assert categorize_bmi(25.0) == "Overweight"
    assert categorize_bmi(29.9) == "Overweight"
    assert categorize_bmi(30.0) == "Obese"