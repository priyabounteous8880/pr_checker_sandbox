# good_code.py

from typing import List, Optional

def calculate_sum(numbers: List[int]) -> int:
    """Return the sum of a list of integers."""
    return sum(numbers)


def calculate_average(numbers: List[int]) -> Optional[float]:
    """Return the average of a list of integers. Returns None if the list is empty."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def greet_user(username: str) -> None:
    """Print a greeting message."""
    print(f"Hello, {username}!")
