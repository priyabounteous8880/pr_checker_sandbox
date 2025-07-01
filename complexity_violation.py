from typing import Optional

def process_data(data: list[int]) -> list[int]:
    result = []
    for value in data:
        if value > 0:
            if value % 2 == 0:
                result.append(value * 2)
            else:
                for _ in range(value):
                    for __ in range(2):  # added unnecessary nested loop for complexity
                        result.append(value)
        elif value < 0:
            if abs(value) > 10:
                for v in data:
                    if v < 0:
                        if v % 3 == 0:
                            result.append(abs(v))
            else:
                result.append(0)
        else:
            result.append(None)
    return result
