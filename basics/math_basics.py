"""
📌 MODULE: Core Mathematical Logic
🎯 GOAL: Master fundamental mathematical algorithms, parity checks, arithmetic series,
        and time-complexity optimizations.

Complexity Overview:
- Time Complexity: O(1) across parity and direct formula checks; O(N) for iterative series
- Space Complexity: O(1) constant memory usage
"""


# ==============================================================================
# 1. Sum of First N Even Natural Numbers
# ==============================================================================
def sum_of_n_even_numbers(n):
    total = 0
    even = 2

    for _ in range(n):
        total += even
        even += 2

    return total


# ==============================================================================
# 2. Check if a Number is Even
# ==============================================================================
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False



# ==============================================================================
# 3. Check for Prime Number
# ==============================================================================
def is_prime(n):
    if n <= 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True



# ==============================================================================
# 4. Check for Perfect Square
# ==============================================================================
def is_perfect_square(num):
    i = 1
    while i * i <= num:
        if i * i == num:
            return True
        i += 1
    return False



# ==============================================================================
# 5. Decimal to Binary (No Built-ins)
# ==============================================================================
def decimal_to_binary(n):
    if n == 0:
        return "0"

    is_negative = False
    if n < 0:
        is_negative = True
        n = -n

    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2

    if is_negative:
        binary = "-" + binary

    return binary


# ==============================================================================
# 6. Binary to Decimal (No Built-ins)
# ==============================================================================
def binary_to_decimal(binary_str):
    decimal = 0
    power = 0

    for i in range(len(binary_str) - 1, -1, -1):
        if binary_str[i] == "1":
            decimal += 2 ** power
        power += 1

    return decimal


# ==============================================================================
# 7. GCD of Two Numbers (Euclidean Algorithm - Iterative)
# ==============================================================================
def gcd(n, m):
    """
    Calculates the Greatest Common Divisor (GCD) using the Euclidean algorithm.

    Time Complexity:  O(log(min(n, m)))
    Space Complexity: O(1)
    """
    while m != 0:
        n, m = m, n % m
    return n



# ==============================================================================
# DRIVER EXECUTION / TESTING
# ==============================================================================
if __name__ == "__main__":
    print("Sum of first 3 even numbers:", sum_of_n_even_numbers(3))
    print("Sum of first 5 even numbers:", sum_of_n_even_numbers(5))

    print("\n--- 2. Parity Check ---")
    print("Is 4 even?:", is_even(4))
    print("Is 7 even?:", is_even(7))

    print("\n--- 3. Prime Number Check ---")
    print("Is 5 prime?:", is_prime(5))
    print("Is 4 prime?:", is_prime(4))

    print("\n--- 4. Perfect Square Check ---")
    print("Is 16 a perfect square?:", is_perfect_square(16))
    print("Is 14 a perfect square?:", is_perfect_square(14))

    print("\n--- 5. Decimal to Binary ---")
    print("5 in binary:", decimal_to_binary(5))
    print("-5 in binary:", decimal_to_binary(-5))

    print("\n--- 6. Binary to Decimal ---")
    print("'101' in decimal:", binary_to_decimal("101"))
    print("'1101' in decimal:", binary_to_decimal("1101"))

    print("\n--- 7. Greatest Common Divisor (GCD) --")
    print("GCD of 48 and 18:", gcd(48, 18))
    print("GCD of 56 and 98:", gcd(56, 98))

