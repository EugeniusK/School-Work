import random

number_questions = 2
f = open('quiz.txt', 'r')

questions = f.read().split('\n')

selected_questions = random.sample(questions, number_questions)
for q in selected_questions:
    data = q.split(',')
    print('11',data[0])
    
    input_valid = False
    while input_valid == False:
        choice = input(f'Please select {" or ".join([str(chr(65+b[0])) + ":" + b[1] for b in enumerate(data[1:-1])])}')
        if choice.upper() in [chr(65+n) for n in range(0,number_questions+1)]:
            input_valid = True
        else:
            print('Invalid answer')
    if choice == data[-1].strip():
        print('Congratulations! You got it correct')
    else:
        print('FAIL!!!')
f.close()
