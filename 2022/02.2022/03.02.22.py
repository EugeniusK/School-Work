import random
def checksum_creditcard(test_number):
    if len(str(test_number)) != 16:
        return False
    digits = []
    for i in range(0,15):
        digits.append(int(str(test_number)[i]))

    doubled_digits = []
    for digit in digits:
        doubled = digit * 2
        doubled_digits.append(doubled)

    combined_two_digits = []
    for digit in doubled_digits:
        if len(str(digit)) == 1:
            combined_two_digits.append(digit)
        else:
            sum_digits = int(str(digit)[0]) + int(str(digit)[1])
            combined_two_digits.append(sum_digits)
    if (sum(combined_two_digits) + int(str(test_number))) % 10 == 0:
        return True
    else:
        return False

print(checksum_creditcard(1234567812345678))
    
def arithmetic_test():
    points = 0
    name = input('What is your name? ')
    class_options = ['1','2','3']
    user_class = input('Which class are you in? Choose from 1, 2, 3')
    while user_class not in class_options:
        print('Invalid class')
        user_class = input('Which class are you in? Choose from 1, 2, 3')
    for i in range(10):
        a = random.randint(1,100)
        b = random.randint(1,100)
        operation = random.choice(['+', '-', '*', '/'])
        solution = round(eval(f'{a} {operation} {b}'),1)
        guess = input(f'What is {a} {operation} {b}? (Answer to 1dp id necessary) ')
        while not(guess.isnumeric()):
            print('Input is not a number. ')
            guess = input(f'What is {a} {operation} {b}? (Answer to 1dp if necessary)')
        guess = float(guess)
        if guess - solution == 0:
            print('Yay your are correct')
            points += 1
    print(f'You got {points} out of 10')
    output = open('results.txt', 'a')
    output.write(name + '\n')
    output.write(user_class + '\n')
    output.write(str(points) + '\n')
    output.write('\n')
    output.close()
    output = open('results.txt', 'r')
    file = output.readlines()

    results = []
    name_list = []
    for i in range(int(len(file) // 4)):
        student_data = file[4*i:4*i+3]
        cleaned_student_data = []
        for data in student_data:
            cleaned_student_data.append(data[:-1])
        if cleaned_student_data[0] + cleaned_student_data[1] not in name_list:
            results.append([cleaned_student_data[0], cleaned_student_data[1], [int(cleaned_student_data[2])]])
            name_list.append(cleaned_student_data[0] + cleaned_student_data[1])
        else:
            name_index = name_list.index(cleaned_student_data[0] + cleaned_student_data[1])
            points = results[name_index][2]
            points.append(int(cleaned_student_data[2]))
            if len(points) > 3:
                points.pop(0)
            points.sort(reverse=True)
            results[name_index][2] = points
    sorted_name_list = sorted(name_list)
    for name in sorted_name_list:
        name_data = results[name_list.index(name)]
        str_points = []
        for point in name_data[2]:
            str_points.append(str(point))
        print(f'{name_data[0]} in class {name_data[1]} has gotten {"/10, ".join(str_points)}/10 recently in this quiz')
    output.close()
arithmetic_test()