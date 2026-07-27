"""
📌 MODULE: Functional Design & Math Foundations
🎯 GOAL: Master functions, conditional logic, mathematical formulas, and iterative transformations.

Complexity Overview:
- Time Complexity: O(1) for direct math formulas; O(N) for sequence generation; O(log10 N) for digit reduction
- Space Complexity: O(1) across all functions
"""


# ==============================================================================
# 1. Temperature Conversion
# ==============================================================================
def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Converts temperature from Celsius to Fahrenheit.

    Time Complexity:  O(1)
    Space Complexity: O(1)
    """
    return (9 / 5) * celsius + 32


# ==============================================================================
# 2. Geometry Basics
# ==============================================================================
def area_of_rectangle(length: float, breadth: float) -> float:
    """
    Calculates the area of a rectangle.

    Time Complexity:  O(1)
    Space Complexity: O(1)
    """
    return length * breadth


# ==============================================================================
# 3. Kinematics
# ==============================================================================
def distance_travelled(speed: float, time: float) -> float:
    """
    Calculates distance covered given speed and time.

    Time Complexity:  O(1)
    Space Complexity: O(1)
    """
    return speed * time


# ==============================================================================
# 4. Lift Rounds Optimization (Ceiling Division Trick)
# ==============================================================================
def lift_rounds(n: int, capacity: int) -> int:
    """
    Calculates minimum lift trips required to carry N people.
    Formula (n + capacity - 1) // capacity handles ceiling division without floating-point math.

    Time Complexity:  O(1)
    Space Complexity: O(1)
    """
    return (n + capacity - 1) // capacity


# ==============================================================================
# 5. Linear Equation Execution
# ==============================================================================
def line_equation(slope: float, intercept: float, x: float) -> float:
    """
    Solves y = mx + b for a given x.

    Time Complexity:  O(1)
    Space Complexity: O(1)
    """
    return slope * x + intercept


# ==============================================================================
# 6. Manual Comparison (Branching Logic)
# ==============================================================================
def max_of_three(a: float, b: float, c: float) -> float:
    """
    Returns the maximum of three numbers without using Python's built-in max().

    Time Complexity:  O(1)
    Space Complexity: O(1)
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# ==============================================================================
# 7. Calendar Logic
# ==============================================================================
def is_leap_year(year: int) -> bool:
    """
    Checks if a year is a leap year using standard Gregorian rules:
    Divisible by 400 OR (Divisible by 4 AND NOT divisible by 100).

    Time Complexity:  O(1)
    Space Complexity: O(1)
    """
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


# ==============================================================================
# 8. Tiered Rate Calculation (Slab Pricing)
# ==============================================================================
def calculate_electricity_bill(units: float) -> float:
    """
    Calculates total cost based on tiered usage slabs:
    - First 100 units: ₹1.5 / unit
    - Next 100 units (101-200): ₹2.5 / unit
    - Above 200 units: ₹4.0 / unit

    Time Complexity:  O(1)
    Space Complexity: O(1)
    """
    if units <= 100:
        return units * 1.5
    elif units <= 200:
        return (100 * 1.5) + ((units - 100) * 2.5)
    else:
        return (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4.0)


# ==============================================================================
# 9. Triangle Inequality Theorem
# ==============================================================================
def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """
    Determines if three side lengths can form a valid triangle.
    Rule: Sum of any two sides must be strictly greater than the third side.

    Time Complexity:  O(1)
    Space Complexity: O(1)
    """
    return (a + b > c) and (a + c > b) and (b + c > a)


# ==============================================================================
# 10. Iterative Digit Reduction (Digital Root)
# ==============================================================================
def digital_root(n: int) -> int:
    """
    Reduces a number to a single digit by repeatedly summing its digits.

    Time Complexity:  O(log10 N)
    Space Complexity: O(1)
    """
    while n >= 10:
        current_sum = 0
        while n > 0:
            current_sum += n % 10
            n //= 10
        n = current_sum
    return n


# ==============================================================================
# 11. Iterative N-th Fibonacci Number
# ==============================================================================
def fibonacci_number(n: int) -> int:
    """
    Returns the N-th Fibonacci number using iterative state updating.
    Base cases: F(0) = 0, F(1) = 1.

    Time Complexity:  O(N)
    Space Complexity: O(1)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ==============================================================================
# DRIVER EXECUTION / TESTING
# ==============================================================================
if __name__ == "__main__":
    print("--- Basic Formulas ---")
    print("Celsius to Fahrenheit (25°C):", celsius_to_fahrenheit(25))  # 77.0
    print("Area of Rectangle (5 x 3):", area_of_rectangle(5, 3))  # 15.0
    print("Distance Travelled (60 km/h for 2h):", distance_travelled(60, 2))  # 120.0
    print("Lift Rounds (10 people, capacity 3):", lift_rounds(10, 3))  # 4
    print("Line Equation (slope=2, b=3, x=4):", line_equation(2, 3, 4))  # 11.0

    print("\n--- Additional Function Tests ---")
    print("Max of (10, 25, 15):", max_of_three(10, 25, 15))  # 25.0
    print("Is 2024 a Leap Year?:", is_leap_year(2024))  # True
    print("Is 1900 a Leap Year?:", is_leap_year(1900))  # False
    print("Electricity Bill for 250 units: ₹", calculate_electricity_bill(250))  # 600.0
    print("Is valid triangle (3, 4, 5)?:", is_valid_triangle(3, 4, 5))  # True
    print("Digital root of 98:", digital_root(98))  # 8
    print("7th Fibonacci Number:", fibonacci_number(7))  # 13