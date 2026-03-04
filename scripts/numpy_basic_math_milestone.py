"""Milestone script: basic mathematical operations on NumPy arrays.

This script demonstrates:
- Element-wise arithmetic between arrays
- Scalar arithmetic on arrays
- Difference between Python list math and NumPy array math
- Common mistakes (shape mismatch, dtype issues) and error interpretation
"""

import numpy as np


def element_wise_operations() -> None:
    print("\n1) Element-wise array operations")
    first_array = np.array([10, 20, 30, 40], dtype=float)
    second_array = np.array([1, 2, 3, 4], dtype=float)

    print(f"First array:  {first_array}")
    print(f"Second array: {second_array}")
    print(f"Add:      {first_array + second_array}")
    print(f"Subtract: {first_array - second_array}")
    print(f"Multiply: {first_array * second_array}")
    print(f"Divide:   {first_array / second_array}")


def scalar_operations() -> None:
    print("\n2) Scalar operations on arrays")
    base_array = np.array([5, 10, 15, 20], dtype=float)
    scalar_value = 3

    print(f"Base array: {base_array}")
    print(f"Array + {scalar_value}: {base_array + scalar_value}")
    print(f"Array * {scalar_value}: {base_array * scalar_value}")


def list_vs_array_comparison() -> None:
    print("\n3) NumPy arrays vs Python lists")
    first_list = [1, 2, 3]
    second_list = [4, 5, 6]

    print(f"Python list addition (concatenation): {first_list + second_list}")

    first_array = np.array(first_list)
    second_array = np.array(second_list)
    print(f"NumPy array addition (element-wise): {first_array + second_array}")


def common_mistakes_demo() -> None:
    print("\n4) Avoiding common mistakes")

    short_array = np.array([1, 2, 3])
    long_array = np.array([10, 20, 30, 40])
    try:
        _ = short_array + long_array
    except ValueError as error:
        print("Shape mismatch example:")
        print(f"- short_array shape: {short_array.shape}")
        print(f"- long_array shape: {long_array.shape}")
        print(f"- error: {error}")

    numeric_array = np.array([1.0, 2.0, 3.0])
    text_array = np.array(["a", "b", "c"])
    try:
        _ = numeric_array + text_array
    except TypeError as error:
        print("Incompatible dtype example:")
        print(f"- numeric_array dtype: {numeric_array.dtype}")
        print(f"- text_array dtype: {text_array.dtype}")
        print(f"- error: {error}")


def main() -> None:
    print("=== Basic Mathematical Operations on NumPy Arrays ===")
    element_wise_operations()
    scalar_operations()
    list_vs_array_comparison()
    common_mistakes_demo()
    print("\nMilestone demo complete.")


if __name__ == "__main__":
    main()
