import pytest
from bmi import imperial_to_bmi, metric_to_bmi, categorize_bmi

def test_imperial_to_bmi():
    # Test with valid inputs
    assert imperial_to_bmi(5, 10, 150) == pytest.approx(21.5, 0.1)
    assert imperial_to_bmi(6, 0, 200) == pytest.approx(27.1, 0.1)

    # Test edge cases
    with pytest.raises(ValueError):
        imperial_to_bmi(-5, 10, 150)  # Negative height
    with pytest.raises(ValueError):
        imperial_to_bmi(5, 10, -150)  # Negative weight

def test_metric_to_bmi():
    # Test with valid inputs
    assert metric_to_bmi(1.75, 70) == pytest.approx(22.9, 0.1)
    assert metric_to_bmi(1.8, 90) == pytest.approx(27.8, 0.1)

    # Test edge cases
    with pytest.raises(ValueError):
        metric_to_bmi(-1.75, 70)  # Negative height
    with pytest.raises(ValueError):
        metric_to_bmi(1.75, -70)  # Negative weight

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