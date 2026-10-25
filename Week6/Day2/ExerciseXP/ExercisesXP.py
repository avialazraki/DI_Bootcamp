"""Developers Institute - Week 6 Day 2 - NumPy Exercises XP (1-10)."""
import numpy as np


def main():
    # Exercise 1: Create a 1D array from 0 through 9.
    numbers = np.arange(10)
    print('Exercise 1 - Array from 0 to 9:')
    print(repr(numbers))

    # Exercise 2: Convert floats to integers (truncates decimal portions).
    integers = np.array([3.14, 2.17, 0, 1, 2]).astype(int)
    print('\nExercise 2 - Integer array:')
    print(repr(integers))

    # Exercise 3: Make a 3-by-3 array containing 1 through 9.
    matrix_3x3 = np.arange(1, 10).reshape(3, 3)
    print('\nExercise 3 - 3x3 matrix:')
    print(repr(matrix_3x3))

    # Exercise 4: Generate reproducible random numbers in a 4-by-5 array.
    rng = np.random.default_rng(42)
    random_matrix = rng.random((4, 5))
    print('\nExercise 4 - Random 4x5 matrix:')
    print(repr(np.round(random_matrix, 2)))

    # Exercise 5: Select the second row (index 1).
    given_array = np.array([[21, 22, 23, 22, 22],
                            [20, 21, 22, 23, 24],
                            [21, 22, 23, 22, 22]])
    print('\nExercise 5 - Second row:')
    print(repr(given_array[1]))

    # Exercise 6: Reverse the elements of the 1D array.
    print('\nExercise 6 - Reversed array:')
    print(repr(numbers[::-1]))

    # Exercise 7: Create a 4-by-4 identity matrix.
    print('\nExercise 7 - Identity matrix:')
    print(repr(np.eye(4)))

    # Exercise 8: Calculate the sum and mean of 0 through 9.
    print('\nExercise 8 - Sum and average:')
    print(f'Sum: {numbers.sum()}, Average: {numbers.mean()}')

    # Exercise 9: Reshape 1 through 20 into 4 rows and 5 columns.
    matrix_4x5 = np.arange(1, 21).reshape(4, 5)
    print('\nExercise 9 - 4x5 matrix:')
    print(repr(matrix_4x5))

    # Exercise 10: Select odd numbers with boolean indexing.
    odd_numbers = numbers[numbers % 2 != 0]
    print('\nExercise 10 - Odd numbers:')
    print(repr(odd_numbers))


if __name__ == '__main__':
    main()
