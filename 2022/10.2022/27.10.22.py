# Task 1
ten_array = [0 for x in range(10)]
print(ten_array)

# Task 2
ascending_ten_array = list(range(1,10+1))
print(ascending_ten_array)

# Task 3
increment_ascending_ten_array = list(range(1,10+1))
user_input = int(input('Number: '))
while user_input != 0:
    increment_ascending_ten_array[user_input - 1] += 1
    print(increment_ascending_ten_array)
    user_input = int(input('Number: '))

# Task 4
five_five_array = [[0] * 5 for x in range(5)]
print(five_five_array)

# Task 5
increment_five_five_array = [[0] * 5 for x in range(5)]
user_input = int(input('Number: '))
while user_input != 0:
    tmp = user_input
    user_input = int(input('Number: '))
    if user_input != 0:
        increment_five_five_array[tmp - 1][user_input - 1] = increment_five_five_array[tmp - 1][user_input - 1] + 1
    else:
        break
    print(increment_five_five_array)
    user_input = int(input('Number: '))

# Task 6
f = open('lorem.txt','r')
content = f.read()
f.close()
print(content)

# Task 7
f = open('lorem.txt', 'r')
content = f.read()
f.close()
g = open('copy of lorem.txt', 'w')
g.write(content)
g.close()