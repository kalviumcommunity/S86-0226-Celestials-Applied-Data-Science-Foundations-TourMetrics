"""Milestone: Understanding NumPy Broadcasting with Simple Examples."""

import numpy as np


def section_title(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def scalar_broadcasting_demo() -> None:
    section_title("1) Broadcasting with Scalars")

    values = np.array([10, 20, 30, 40])
    scalar = 5

    print(f"Array:                        {values}")
    print(f"Array shape:                  {values.shape}")
    print(f"Scalar value:                 {scalar}")
    print(f"Array + scalar:               {values + scalar}")
    print(f"Array - scalar:               {values - scalar}")
    print(f"Array * scalar:               {values * scalar}")

    conceptual_loop = np.empty_like(values)
    for index, value in enumerate(values):
        conceptual_loop[index] = value + scalar

    print(f"Conceptual loop result (+5):  {conceptual_loop}")
    print("Explanation: NumPy stretches the scalar across all elements logically.")


def one_d_broadcasting_demo() -> None:
    section_title("2) Broadcasting Between 1D Arrays")

    print("Successful case:")
    array_a = np.array([1, 2, 3])
    array_b = np.array([10])

    print(f"array_a:       {array_a}, shape={array_a.shape}")
    print(f"array_b:       {array_b}, shape={array_b.shape}")
    print("Prediction: array_b is length 1, so it can stretch to length 3.")
    print(f"array_a + b:   {array_a + array_b}")

    print("\nIncompatible case:")
    array_c = np.array([1, 2, 3])
    array_d = np.array([10, 20])

    print(f"array_c:       {array_c}, shape={array_c.shape}")
    print(f"array_d:       {array_d}, shape={array_d.shape}")
    print("Prediction: lengths 3 and 2 cannot align for broadcasting.")

    try:
        _ = array_c + array_d
    except ValueError as error:
        print(f"Operation failed as expected: {error}")


def two_d_one_d_broadcasting_demo() -> None:
    section_title("3) Broadcasting Between 2D and 1D Arrays")

    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])

    row_adjustment = np.array([100, 200, 300])

    print("Row-wise style behavior (2D + 1D):")
    print(f"matrix shape:                 {matrix.shape}")
    print(f"row_adjustment shape:         {row_adjustment.shape}")
    print("Prediction: 1D array aligns with columns and applies to each row.")
    row_result = matrix + row_adjustment
    print("Result:")
    print(row_result)
    print(f"Output shape:                 {row_result.shape}")

    print("\nColumn-wise style behavior using reshape:")
    column_adjustment = np.array([10, 20, 30]).reshape(3, 1)
    print(f"column_adjustment shape:      {column_adjustment.shape}")
    print("Prediction: each row gets its own single value across all columns.")
    column_result = matrix + column_adjustment
    print("Result:")
    print(column_result)
    print(f"Output shape:                 {column_result.shape}")


def conceptual_rules_demo() -> None:
    section_title("4) Understanding Broadcasting Rules (Conceptually)")

    print("Rule 1: Compare shapes from the rightmost dimension.")
    print("Rule 2: Dimensions are compatible if they are equal or one is 1.")
    print("Rule 3: If a dimension is 1, NumPy can stretch it logically.")
    print("Rule 4: If neither condition holds, operation fails.")

    examples = [
        ((3, 4), (4,), "Works: rightmost dims match (4)."),
        ((3, 4), (1, 4), "Works: 1 can stretch to 3 on the left dimension."),
        ((3, 4), (3, 1), "Works: 1 can stretch to 4 on the right dimension."),
        ((3, 4), (2, 4), "Fails: left dimension 3 vs 2 are incompatible."),
        ((5,), (), "Works: scalar broadcasts to any shape."),
    ]

    print("\nShape reasoning examples:")
    for left_shape, right_shape, explanation in examples:
        print(f"- {left_shape} with {right_shape}: {explanation}")

    print("\nDebugging tip:")
    print("- Print `.shape` for each array before combining them.")
    print("- If needed, reshape with `reshape`, `np.newaxis`, or keepdims patterns.")


def main() -> None:
    print("NumPy Milestone: Understanding Broadcasting with Simple Examples")
    scalar_broadcasting_demo()
    one_d_broadcasting_demo()
    two_d_one_d_broadcasting_demo()
    conceptual_rules_demo()
    print("\nMilestone complete.")


if __name__ == "__main__":
    main()
