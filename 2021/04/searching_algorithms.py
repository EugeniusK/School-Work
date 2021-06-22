import random
import time
def random_array(n, limit):
    array = []
    for i in range(n):
        array.append(random.randint(0,limit))
    return array


def linear_search(attempt, n, limit):
    times = []
    for i in range(attempt):
        test_array = random_array(n, limit)
        search_element = test_array[random.randint(0, n-1)]
        start = time.time()
        for element in test_array:
            if element == search_element:
                end = time.time()
                times.append(end-start)
                break
    average_time = sum(times)/len(times)
    return f'an array with {n} elements took {average_time} on average with a sample size of {attempt}'
print(linear_search(100000, 100, 1000000))