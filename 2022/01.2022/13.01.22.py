import random
def question_one():
    def correct_digits(guess, solution, mode):
        string_guess = str(guess)
        string_solution = str(solution)
        correct = []
        for i in range(4):
            if string_guess[i] == string_solution[i]:
                correct.append(True)
            else:
                correct.append(False)
        print(f"You got {correct.count(True)} digits correct")
        if mode == "easy":
            print(f"Digits {', '.join([str(x+1) for x in range(4) if correct[x]])} were correct")


    high_scores = {}
    mode = ["easy", "medium", "hard"]
    valid_mode = False
    user_seletc = ""
    while valid_mode == False:
        user_select = input("Please select a mode from easy, medium and hard : ")
        if user_select.lower() not in mode:
            print(f"{user_select} is not a valid mode. Please try again")
        else:
            valid_mode = True
            mode = user_select.lower()


    end = False
    while end == False:
        print(high_scores)
        attempts = 0
        correct = False
        if mode == "easy" or mode == "medium":
            target = random.randint(1000,9999)
        elif mode == "hard":
            target = random.randint(10000,99999)
        print(target)
        while correct == False:
            user_guess = input("Input a guess : ")
            if user_guess.isnumeric():
                user_guess = int(user_guess)
                if mode == "easy" or mode == "medium":
                    if user_guess > 999 and user_guess < 10000:
                        correct_digits(user_guess, target, mode)
                        attempts += 1
                        if user_guess == target:
                            print(f"Congratulations You got it correct with {attempts} {'guesses' if attempts > 1 else 'guess'}")
                            correct = True
                    else:
                        print("Guess is not a 4 digit number")
                elif mode == "hard":
                    if user_guess > 9999 and user_guess < 100000:
                        correct_digits(user_guess, target, mode)
                        attempts += 1
                        if user_guess == target:
                            print(f"Congratulations You got it correct with {attempts} {'guesses' if attempts > 1 else 'guess'}")
                            correct = True
                    else:
                        print("Guess is not a 5 digit number")
            else:
                print("Guess is not a number")
        name = input("Please input your name")

        high_scores[name] = [mode, attempts]
        if input("Quit? Type YES to quit") == "YES":
            end = True

def question_three():
    def validate_email(address):
        errors = []
        at_index = -1
        dot_index = -1
        if "@" in address:
            at_index = address.index("@")
        if "." in address:
            dot_index = address.index(".")
        if " " in address:
            errors.append("Email address cannot have a space")
        if at_index == -1:
            errors.append("Email address must have an @")
        if dot_index == -1:
            errors.append("Email address must have a .")
        if dot_index != -1 and at_index != -1:
            if dot_index < at_index:
                errors.append(". cannot be after @")
            else:
                if at_index == 0:
                    errors.append("Email address must have character(s) before the @")
                if dot_index == len(address) - 1:
                    errors.append("Email address must have character(s) after the .")
        return address, errors
    
    choice_valid = False
    options = ["1", "2"]
    user_choice = 0
    while choice_valid == False:
        user_choice = input("Type 1 for opening a file, Type 2 for direct input : ")
        if user_choice in options:
            choice_valid = True
        else:
            print("Invalid choice")
    if user_choice == "1":
        emails = open("emails.txt", "r")
        for email in emails:
            output = validate_email(email.strip())
            if output[1] == []:
                print(f"  Valid {email.strip()}")
            else:
                print(f"Invalid {', '.join(output[1])}")
    elif user_choice == "2":
        email = input("Please input an email to test for validity")
        output = validate_email(email)
        if output[1] == []:
            print(f"  Valid {email}")
        else:
            print(f"Invalid {email} {', '.join(output[1])}")

question_three()