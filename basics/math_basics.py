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
# DRIVER EXECUTION / TESTING
# ==============================================================================
if __name__ == "__main__":
    print("Sum of first 3 even numbers:", sum_of_n_even_numbers(3))   # 12
    print("Sum of first 5 even numbers:", sum_of_n_even_numbers(5))   # 30