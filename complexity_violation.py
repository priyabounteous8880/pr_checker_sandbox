from typing import Optional

def process_data(data: list[int]) -> list[Optional[int]]:
    result: list[Optional[int]] = []

    for value in data:
        if value > 0:
            if value % 2 == 0:
                result.append(value * 2)
            else:
                result.extend([value] * value)  # Clean loop using list multiplication
        elif value < 0:
            if abs(value) > 10:
                negative_abs = [abs(v) for v in data if v < 0]
                result.extend(negative_abs)
                break  # Avoid further processing since list was reset previously
            else:
                result.append(0)
        else:  # value == 0
            result.append(None)

    return result
