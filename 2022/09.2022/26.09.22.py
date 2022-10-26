#Task 1
import requests

url = 'https://api.exchangerate.host/convert'
print(requests.get(url+f"?amount={input('Input the amount to convert: ')}&from={input('Input the currency to convert from: ')}&to={input('Input the currency to convert to: ')}&places=2").json()['result'])
# url = 'https://api.exchangerate.host/latest'
# # convert between GBP, EUR, USD, JPY

# valid_currency = ['GBP', 'EUR', 'USD', 'JPY']

# def currency_input(question):
#     valid = False
#     while not(valid):
#         currency = input(question)
#         if currency.upper() in valid_currency:
#             valid = True
#             return currency.upper()
#         else:
#             print('Invalid currency try again')

# def currency_amount_input():
#     valid = False
#     while not(valid):
#         amount = input('Input the amount of currency to convert: ')
#         try:
#             valid = True
#             return float(amount)
#         except:
#             print('Invalid input try again')

# quit = False
# while not(quit):
    
#     base_currency = currency_input('Input the base currency: ')
#     response = requests.get(url, 
#     {
#         'base': base_currency, 
#         }
#     ).json()
#     currency_amount = currency_amount_input()
#     new_currency = currency_input('Input the new currency: ')
#     print(f"{currency_amount:.2f}{base_currency} = {currency_amount * response['rates'][new_currency]:.2f}{new_currency}")
#     quit = input('Quit? Input Q to quit: ')


# Task 2

# f = open('AddBook_dataFile.csv', 'r')
# f_data = f.readlines()[1:]
# data = []
# for d in f_data:
#     data.append(d[:-1].split(','))

# surname = input('Surname: ')
# for d in data:
#     if d[0].lower() == surname.lower():
#         print(d)

# month = input('Month: ').rjust(2, '0')
# print(month)
# for d in data:
#     if d[6][3:5] == month:
#         print(d)

# # Task 3

# def calculate_ISBN(number):
#     # 1 line solution
#     if number.isnumeric() and len(number) == 10:
#         multiplied_digits = []
#         for i in range(0, 10):
#             multiplied_digits.append(int(number[i]) * (11 - i))
#         sum_products = sum(multiplied_digits)
#         check_digit = 11 - sum_products % 11
#         if check_digit < 10:
#             check_digit = str(check_digit)
#         else:
#             check_digit = 'X'
#         return number + check_digit
        
#     else:
#         return -1

# return 'invalid' if not(number.isnumeric() and len(number) == 10) else number + str(['X' if x > 10 else x for x in [11 - sum([int(b) * (11-a) for a, b in enumerate(number)]) % 11]][0])

# print(calculate_ISBN('0241034812'))