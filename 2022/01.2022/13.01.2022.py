import random

def correct_digits(guess, solution):
    string_guess = str(guess)
    string_solution = str(solution)
    correct = []
    for i in range(4):
        if string_guess[i] == string_solution[i]:
            correct.append(True)
        else:
            correct.append(False)