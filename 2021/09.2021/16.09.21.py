import random

def question_one():
    ans = random.sample(list(range(0,15)), k=15)
    print(ans)

def question_two():
    ans = []
    for i in range(3):
        ans.append([0]*9)
    for i in range(9):
        chosen = random.sample(list(range(i*10, i*10+9)), k=3)
        for j in range(3):
            ans[j][i] = chosen[j]
    for row in ans:
        print(row)

def question_three():
    ans = []
    for i in range(3):
        ans.append([0])
    number_count = 15
    while number_count != 0:
        if number_count <= 3:
            column_count = random.randint(1,number_count)
        else:
            column_count = random.randint(1,3)
        column_map = [0]*(3-column_count)
        column = random.sample(list(range(0,15)), k=column_count)
        final_column = column_map
        while len(final_column) != 3:
            final_column.insert(random.randint(0,len(final_column)), column.pop(0))
        for i in range(0,3):
            ans[i].append(final_column[i])
        number_count -= column_count
    for row in ans:
        print(row)

question_one()
question_two()
question_three()