"""Script that guessing random numbers on base of binary search
"""
import numpy as np
from typing import Callable

MIN_NUMBER = 1
MAX_NUMBER = 100

def guess_binary(number:int=1) -> int:
    """Script tries to guess number on base minimum and maximum number
    and information lesser or greater guessed number to input number.

    Args:
        number (int, optional): input number

    Returns:
        int: number of attempts
    """
    left_limit = MIN_NUMBER
    right_limit = MAX_NUMBER
    attempts = 0
    while True:
        attempts += 1
        predicted_number = int((left_limit+right_limit) / 2)
        if predicted_number > number:
            right_limit = predicted_number
            # When is difference between limits equal to 1
            # limit need to be corrected
            if right_limit-left_limit == 1:
                right_limit -= 1
        elif predicted_number < number:
            left_limit = predicted_number
            # When is difference between limits equal to 1
            # limit need to be corrected
            if right_limit-left_limit == 1:
                right_limit += 1
        else:
            break

    return attempts


def average_attempts(guess_func: Callable[[int], int]) -> int:
    """Script generates array of random 1000 numbers and runs guess
    function to count attempts for each random number.

    Args:
        guess_func (Callable[[int], int]): guess function

    Returns:
        int: average number of attempts
    """
    np.random.seed(1)   #Comment this line to test with different numbers
    random_array = np.random.randint(MIN_NUMBER, MAX_NUMBER+1, size=(1000))

    attempts_list = []
    for number in random_array:
        attempts_list.append(guess_func(number))

    average_attempts = int(np.mean(attempts_list))
    return average_attempts


if __name__ == '__main__':
    avg_attempts = average_attempts(guess_binary)
    print(f'On average, your algorithm guesses in {avg_attempts} attempts')