def happyNumber():
    happyNumbers = []
    i = 1
    while len(happyNumbers) != 8:
        happy_number_test = i
        previous_results = []
        while happy_number_test != 1:
            happy_number_test = sum([int(x)**2 for x in str(happy_number_test)])
            previous_results.append(happy_number_test)
            if previous_results.count(happy_number_test) > 1:
                break
        if happy_number_test == 1:
            happyNumbers.append(i)
        i += 1
    return happyNumbers


def numberNames(n):
    ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    tens_exceptions = {10: 'ten', 11: 'eleven', 12: 'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
    tens = {20: 'twenty', 30: 'thirty', 40:'fourty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
    greater_powers_ten = {100: 'hundred', 1000: 'thousand', 1000000: 'million'}

    name = []
    if n in ones.keys():
        return ones[n]
    elif n in tens_exceptions.keys():
        return tens_exceptions[n]
    elif n in tens.keys():
        return tens[n]
    elif n in greater_powers_ten.keys():
        return greater_powers_ten[n]
    for k in list(greater_powers_ten.keys())[::-1]:
    
        if n > k and n < k * 1000:
            return k, n // k
    
    return name

print(numberNames(150))