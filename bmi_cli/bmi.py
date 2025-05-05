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
    return NotImplementedError

def metric_to_bmi(height: float, weight: float) -> float:
    return NotImplementedError

def categorize_bmi(bmi: float) -> str:
    return NotImplementedError