"""
Calculator Tool for SentinelAI
"""

def calculate_supplies(population: int) -> dict:
    """
    Calculate estimated emergency supplies.

    Args:
        population (int): Number of affected people.

    Returns:
        dict: Estimated supplies.
    """

    return {
        "population": population,
        "water_liters_per_day": population * 3,
        "food_meals_per_day": population,
        "blankets": population,
        "medical_kits": max(1, population // 10),
    }