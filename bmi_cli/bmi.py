"""
cwb371 - Wolfgang de Groot
CSE 4283 - Software Testing - Assignment 2
"""

class BMI:
    value: float
    inches: int
    lbs: float

    def __init__(self, feet: int, inches: int, lbs: float):
        self.inches = (feet * 12) + inches
        self.lbs = lbs
        self.value = None

    def imperial_to_bmi(feet: int, inches: int, lbs: float) -> float:
        return NotImplementedError

    def categorize_bmi(bmi: float) -> str:
        return NotImplementedError