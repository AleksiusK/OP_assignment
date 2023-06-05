def goldbach_odd_composite_numbers(range_n):
    """
    Returns the first odd composite number that cannot be written as the sum of a prime and twice a square.
    
    One major issue is generating all the required primes to check. The method used is a bit improvised, but works.
    We first generate a list of bool- values from 0 to range_n + 1, where True equals to a prime number at that index.
    0 and 1 are excluded automatically from the list. Then, one by one looping through the numbers from 0 to range_n, we check if the number is a prime.
    We stop the loop at half the number n, as anything more than that cannot be a divisor. All numbers that can be divided with no remainder are marked as False, 
    signaling that the number is not a prime.

    This step has a time complexity of O(n^2), as we need to go through the list n times, and each time we need to go through half of the list.

    Second part of the problem is to generate all the odd composite numbers. As an odd composite is defined as odd integer that is not a prime,
    we can generate the required list by using python's list comprehension, going over all the odd numbers from 3 onwards. Both time and space complexity of this step are O(n).

    Lastly, we need to check if the odd composite numbers can be written according to Goldbach's conjecture. As was stated in the task description,
    the conjecture states that an odd composite number is n = p + 2k**2. From this we can deduce that in order for the conjecture to be broken,
    n - 2k**2 must not be a prime. We could also check if n - p is square ( (n-p)/2 != square ), but that would require us to store both the primes AND the squares in a list, adding to the space complexity.

    """
    
    primes = generate_primes(range_n)
     # Use a set for faster membership checking.
    odd_composites = [i for i in range(3, range_n, 2) if i not in primes] # Generate odd composite numbers from 3 onwards
    for odd_composite in odd_composites:
        square_range = int((odd_composite / 2) ** 0.5) # Loop through the odd composite numbers
        for i in range(square_range, 0, -1):  # Start from the largest possible square. 
            square = 2 * (i**2)
            if odd_composite - square in primes: # Check if the difference is a prime. Break if not
                break
        else: # If the loop is not broken, then the number cannot be written as the sum of a prime and twice a square.
            return odd_composite

def generate_primes(range_n: int):
    primes = [True for _ in range(range_n + 1)]
    primes[0], primes[1] = False, False
    for p in range(len(primes)):
        for i in range(2, int(p/2) + 1):
            if (p % i) == 0:
                primes[p] = False
                break

    primes = [i for i in range(len(primes)) if primes[i] == True]
    return primes

print(goldbach_odd_composite_numbers(10000))