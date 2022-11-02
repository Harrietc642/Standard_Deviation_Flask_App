import math
import numbers
class MyMath():
    """Standard Deviation Calculations based on a list of numbers."""

    def __init__(self,  numbers: list):
        """Init function."""
        self.numbers = numbers

    def average(self) -> float:
        """calculates and returns the average of a list of numbers."""
        sum = 0
        count = 0
        for i in self.numbers:
            sum = sum + float(i)
            count = count + 1
        return (sum / count)

    def StdDev(self) -> float:
        """Calculates the standard deviation of a list of numbers. """
        variance = 0
        for number in self.numbers:
            variance += (float(number) - self.average()) ** 2
            result = math.sqrt(variance / (len(self.numbers) - 1))
        return (result)

    def Max(self) -> float:
        """Retreive the largest number of a list of numbers"""
        max = self.numbers[0]
        for number in self.numbers:
            if number > max:
                max = number
        return(number)
