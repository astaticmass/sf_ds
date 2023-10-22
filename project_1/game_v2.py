import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guessing the number

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Number of attempts
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # hidden number
        if number == predict_number:
            break # exiting the loop when hidden number and generated number matched
    return(count)

def score_game(random_predict) -> int:
    """Avarege number of attempts for 1000 repeats of our script

    Args:
        random_predict ([type]): Guessing function

    Returns:
        int: avarage number of  attempts
    """

    count_ls = [] # list for saving number of attempts
    np.random.seed(1) # fixing seed for recreating the situation for future uses
    random_array = np.random.randint(1, 101, size=(1000)) # generating list of random numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # calculating avarage number of attempts

    print(f'Your script guesses the number on avarage for {score} attempts')
    return(score)

if __name__ == '__main__':
    # RUN
    score_game(random_predict)