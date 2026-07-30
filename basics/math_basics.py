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