import numpy as np

number = np.random.randint(1, 101) # generating hidden number

count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100: "))

    if predict_number > number:
        print("Number have to be lesser!")

    elif predict_number < number:
        print("Number have to be greater!")

    else:
        print(f"You guessed th number! This number = {number}, for {count} attempts")
        break # end of game, exit from loop
