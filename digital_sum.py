from decimal import *
from math import sqrt
getcontext().prec = 100
## Set the precision to 100 for Decimal to avoid floating point errors. 

def digital__sum(range_n: int):
    """
    Returns the sum of all digits from the square root of all natural numbers in the range n.

    The function consists of three parts: first, get all natural numbers. If the square root is an iteger, skip the number to save time.
    Second, calculate the square root of each number. This will be done the same time as numbers are added to the list.
    Third, calculate the sum of all digits in the square root by converting the number to a string, splitting it at the decimal point and summing the digits.

    The overall complexity of the function is O(n), since we have to loop through all numbers in the range.
    I use in the function the string split- method to split the decimals off the number, summing them by changing them to integers again afterwards.
    """
    natural_numbers = [Decimal(i).sqrt() for i in range(1, range_n + 1) if not sqrt(i).is_integer()]
    for i in range(len(natural_numbers)):
        natural_numbers[i] = str(natural_numbers[i]).split(".")[1]
        natural_numbers[i] = sum([int(i) for i in natural_numbers[i]])

    return sum(natural_numbers)

print(digital__sum(100))