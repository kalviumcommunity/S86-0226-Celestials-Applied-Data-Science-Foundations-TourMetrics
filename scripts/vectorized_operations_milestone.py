"""Milestone: Applying vectorized operations instead of Python loops."""

from time import perf_counter

import numpy as np


def section_title(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def loop_vs_vectorized_demo() -> None:
    section_title("1) Loop-Based vs Vectorized Code")

    base_array = np.array([10, 20, 30, 40, 50], dtype=float)

    loop_result = np.empty_like(base_array)
    for index, value in enumerate(base_array):
        loop_result[index] = (value * 1.2) + 5

    vectorized_result = (base_array * 1.2) + 5

    print(f"Input array:                 {base_array}")
    print(f"Loop-based transformed:      {loop_result}")
    print(f"Vectorized transformed:      {vectorized_result}")
    print(f"Same result?                 {np.allclose(loop_result, vectorized_result)}")

    large_array = np.arange(1_000_000, dtype=float)

    start = perf_counter()
    large_loop = np.empty_like(large_array)
    for index, value in enumerate(large_array):
        large_loop[index] = (value * 1.2) + 5
    loop_time = perf_counter() - start

    start = perf_counter()
    large_vectorized = (large_array * 1.2) + 5
    vectorized_time = perf_counter() - start

    print(f"Loop timing (1,000,000 items):      {loop_time:.6f} seconds")
    print(f"Vectorized timing (same input):     {vectorized_time:.6f} seconds")
    print(f"Speedup factor (loop/vectorized):   {loop_time / vectorized_time:.2f}x")
    print(f"Large results equal?                {np.allclose(large_loop, large_vectorized)}")


def vectorized_arithmetic_demo() -> None:
    section_title("2) Vectorized Arithmetic Operations")

    values = np.array([2, 4, 6, 8, 10], dtype=float)
    adjustments = np.array([1, 1, 2, 2, 3], dtype=float)

    print(f"Values:                    {values}")
    print(f"Adjustments:               {adjustments}")
    print(f"Add scalar (+5):           {values + 5}")
    print(f"Multiply scalar (*3):      {values * 3}")
    print(f"Array + array:             {values + adjustments}")
    print(f"Array - array:             {values - adjustments}")
    print(f"Array * array:             {values * adjustments}")
    print(f"Array / array:             {values / adjustments}")


def vectorized_comparison_demo() -> None:
    section_title("3) Vectorized Comparisons and Conditions")

    scores = np.array([58, 72, 91, 67, 84, 49, 76])

    passed_mask = scores >= 70
    high_distinction_mask = scores >= 85

    print(f"Scores:                         {scores}")
    print(f"Passed mask (>= 70):           {passed_mask}")
    print(f"High distinction mask (>= 85): {high_distinction_mask}")
    print(f"Passed scores only:            {scores[passed_mask]}")

    pass_labels = np.where(scores >= 70, "Pass", "Needs Work")
    print(f"Conditional labels:            {pass_labels}")


def vectorization_mistakes_demo() -> None:
    section_title("4) Avoiding Common Vectorization Mistakes")

    first = np.array([1, 2, 3], dtype=float)
    second = np.array([10, 20, 30, 40], dtype=float)

    try:
        _ = first + second
    except ValueError as error:
        print("Shape mismatch example:")
        print(f"- first shape:  {first.shape}")
        print(f"- second shape: {second.shape}")
        print(f"- error:        {error}")

    matrix = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
    column = np.array([[10], [20]], dtype=float)
    broadcast_result = matrix + column

    print("\nBroadcasting (compatible shapes) example:")
    print(f"Matrix shape:              {matrix.shape}")
    print(f"Column shape:              {column.shape}")
    print("Result (matrix + column):")
    print(broadcast_result)

    print("\nGuideline:")
    print("- Vectorize array-wide arithmetic, comparisons, and transformations.")
    print("- Keep expressions readable.")
    print("- Check array shapes before combining arrays.")


def main() -> None:
    print("NumPy Milestone: Applying Vectorized Operations Instead of Python Loops")
    loop_vs_vectorized_demo()
    vectorized_arithmetic_demo()
    vectorized_comparison_demo()
    vectorization_mistakes_demo()
    print("\nMilestone complete.")


if __name__ == "__main__":
    main()
