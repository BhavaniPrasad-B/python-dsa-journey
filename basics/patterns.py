"""
📌 MODULE: Core Loop & Layout Patterns
🎯 GOAL: Master coordinate checking, multi-tasking row execution, and persistent state tracking.

Complexity Overview:
- Time Complexity for all 3 patterns: O(N²)
- Space Complexity for all 3 patterns: O(1) [Streams directly to terminal output]
"""


# ==============================================================================
# PATTERN 1: The Hollow Square (Coordinate Logic)
# ==============================================================================
# 🧠 Key Concept: Matrix Coordinate Evaluation
# Instead of printing blindly, we treat the grid as an (i, j) coordinate plane.
# We check if the current cell touches any of the 4 outer walls.




# ==============================================================================
# PATTERN 2: The Pyramid (Space Management Math)
# ==============================================================================
# 🧠 Key Concept: Sequential Multi-Tasking Loop Execution
# For every single row (i), two separate loops fire in sequence before hitting Enter:
# 1. Print leading spaces: (n - i - 1) times
# 2. Print stars:          (2 * i + 1) times

def print_pyramid(n: int) -> None:
    """
    Prints a centered pyramid of height N.

    Time Complexity:  O(N²) - Linear sweeps per row across N rows
    Space Complexity: O(1) - Dynamic stream output
    """
    print(f"--- Pyramid (N = {n}) ---")
    for i in range(n):
        # 1. Leading spaces for alignment
        for _ in range(n - i - 1):
            print(" ", end="")

        # 2. Odd count of stars per row
        for _ in range(2 * i + 1):
            print("*", end="")

        print()  # Line break engine
    print()


# ==============================================================================
# PATTERN 3: Floyd's Triangle (Persistent State Tracking)
# ==============================================================================
# 🧠 Key Concept: Independent Tracker Outliving Loop Resets
# The variable 'num' is initialized OUTSIDE the loops.
# As the row resets, 'num' maintains its state and keeps incrementing continuously.

def print_floyds_triangle(n: int) -> None:
    """
    Prints Floyd's Triangle up to N rows.

    Time Complexity:  O(N²) - Steps scale as N(N+1)/2
    Space Complexity: O(1) - Only holds one primitive counter in memory
    """
    print(f"--- Floyd's Triangle (N = {n}) ---")
    num = 1  # Global state tracker
    for i in range(n):
        for _ in range(i + 1):
            print(num, end=" ")
            num += 1  # State updates across iterations
        print()  # Line break engine
    print()


# ==============================================================================
# DRIVER EXECUTION / TESTING
# ==============================================================================
if __name__ == "__main__":
    GRID_SIZE = 5

    print_hollow_square(GRID_SIZE)
    print_pyramid(GRID_SIZE)
    print_floyds_triangle(GRID_SIZE)
