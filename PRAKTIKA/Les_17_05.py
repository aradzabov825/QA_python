# import requests

# def check_website(url):
#     try:
#         resp = requests.get(url)
#         if resp.status_code == 200:
#             return True
#         else:
#             return False
#     except:
#         return False

# print(check_website('https://easysmarthub.ru'))
# print(check_website('https://easysmarthub.ru/contact'))
# print(check_website('https://easysmarthub.ru/1'))
# print(check_website('https://easysmarthub.ru/mega'))


# _________________________________________________________________________________________________________________


# import string
# import random
# def generate_password(length):
#     char = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(char) for _ in range(length))
#     return password
# password_length = int(input("Введите желаемую длину пароля: "))
# generated_password = generate_password(password_length)
# print("Ваш сгенерированный пароль:", generated_password)


# или второй вариант

# import string
# import random
# def generate_password(length):
#     char = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(char) for _ in range(length))
#     if password_length < 8:
#         print('Пароль короткий ')
#     else:
#         return password
# password_length = int(input("Введите желаемую длину пароля: "))
# generated_password = generate_password(password_length)
# print("Ваш сгенерированный пароль:", generated_password)

# _________________________________________________________________________________________________________________


# import random
# num = input('login ')
# dictionaries = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789', '!&?-+()^$#@']

# password = [random.choice(d) for d in dictionaries] + random.choices(''.join(dictionaries), k=random.randint(20, 32) - 4)
# random.shuffle(password)
# password = ''.join(password)

# print('Ваш логин', num, 'Ваш пароль', password)


# _________________________________________________________________________________________________________________


# import random
# num = input('login ')
# pas = ''
# for x in range(8,32): #Количество символов (8-32)
#     pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) #Символы, из которых будет составлен пароль
# print('Hello, ', num, 'your password is: ', pas)


# _________________________________________________________________________________________________________________


# a = int(input())

# suma = 0

# while a > 0:
#     digit = a % 10
#     suma = suma + digit
#     a = a // 10
# print("Сумма:", suma)


# ___________________________________________________________________________________________________________________


# suma = 0
# mult = 1

# while n > 0:
#     digit = n % 10
#     if digit != 0:
#         suma += digit
#         mult *= digit
#     n = n // 10

# print("Сумма:", suma)
# print("Произведение:", mult)


# ___________________________________________________________________________________________________________________


# from random import choice
 
# with open('example.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
# if lines:
#     print(choice(lines).strip())


# ___________________________________________________________________________________________________________________


# import random

# with open("example.txt", 'r', encoding='utf-8') as inp:
#     lines = inp.readlines()

# random_line = random.choice(lines).strip()
# print(random_line)


# ___________________________________________________________________________________________________________________


# import pyjokes
# print(pyjokes.get_joke())


# ___________________________________________________________________________________________________________________


# import random

# joke_templates = [
#     'Почему %s катится вниз?',
#     'Потому что %s смеятся над ним!',
#     'Кто %s в книгах?',
#     'Кто %s?',
#     'Что сказал %s ему когда они встретились ?'
# ]
# joke_elements = [
#     'слон','заяц','бетмен','крокодил','чебурашка','студент','препод',
#     'водитель','улитка'
# ]

# joke_template = random.choice(joke_templates)

# joke = joke_template % random.choice(joke_elements)
# print(joke)


# ___________________________________________________________________________________________________________________