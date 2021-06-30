myNumbers = [10,20,30,40,50,60,70,80,90,100]
total = 0
for theNumber in myNumbers:
    total = total + theNumber
    if theNumber % 2 == 0:
        print('Even')
    else:
        print('Odd')
print(total)