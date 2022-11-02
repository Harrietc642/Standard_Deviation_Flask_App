def average(numbers: list) -> float:
    """calculates and returns the average of a list of numbers."""
    sum = 0
    count = 0
    for i in numbers:
        sum = sum + float(i)
        count = count + 1
    
    return (sum / count)
