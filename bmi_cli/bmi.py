"""
cwb371 - Wolfgang de Groot
CSE 4283 - Software Testing - Assignment 2
"""

categories = (
    "Underweight",
    "Normal weight",
    "Overweight",
    "Obese"
)

def imperial_to_bmi(feet: int, inches: int, weights: float) -> float:
    kilogram_weight = weights * 0.45
    metric_height = (feet * 12 + inches) * 0.025
    return metric_to_bmi(metric_height, kilogram_weight)

def metric_to_bmi(height: float, weight: float) -> float:
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive values.")
    squared_height = height ** 2
    return weight / squared_height

def categorize_bmi(bmi: float) -> str:
    return NotImplementedError