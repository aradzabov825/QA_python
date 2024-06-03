# # spisok = [1,2,567,4,5,-345,7,8,9,10]

# # def max_num(spisok):
# #     if not spisok:
# #         return None
# #     return(max(spisok))

# # print(max_num(spisok))

# # ПРИМЕР

# # list1 = [3, 2, 8, 5, 10, 6]
# # max_number = max(list1)
# # print("Наибольшее число:", max_number)

# # ПРИМЕР

# # list1 = ["Виктор", "Артем", "Роман"]
# # max_string = max(list1, key=len)
# # print("Самая длинная строка:", max_string)

# # ПРИМЕР

# # def large(arr): 
# #     max_ = arr[0]
# #     for ele in arr:
# #         if ele > max_:
# #            max_ = ele
# #     return max_ 
# # list1 = [1,4,5,2,6]
# # result = large(list1)
# # print(result)  # вернется 6



# # ПРИМЕР 

# # from functools import reduce
# # list1 = [-1, 3, 7, 99, 0]
# # print(reduce(max, list1)) 


# # ПРИМЕР

# # import heapq
# # list1 = [-1, 3, 7, 99, 0]
# # print(heapq.nlargest(1, list1))

# # ПРИМЕР

# # list1=[1,4,22,41,5,2]
# # sorted-_list = sorted(list1)
# # result = sorted_list[-1]
# # print(result)  # -> 41

# # ПРИМЕР

# # def find_max(arr, max_=None):
# #     if max_ is None:
# #         max_ = arr.pop()
# #     current = arr.pop()
# #     if current > max_:
# #         max_ = current
# #     if arr:
# #         return find_max(arr, max_)
# #     return max_

# # list1=[1,2,3,4,2]
# # result = find_max(list1)
# # print(result)  # -> 4


# # КАЛЬКУЛЯТОР


# # num1 = float(input("Введите первое число: "))
# # operator = input("Выбирете действие (+, -, *, /): ")
# # num2 = float(input("Введите второе число: "))



# # if operator == "+":
# #     result = num1 + num2
# #     print('вы выбрали сложение:')
# # elif operator == "-":
# #     result = num1 - num2
# #     print('вы выбрали вычитание:')
# # elif operator == "*":
# #     result = num1 * num2
# #     print('вы выбрали умножение:')
# # elif operator == "/":
# #     print('вы выбрали деление:')
# #     if num2 == 0:
# #         print("Ошибка: деление на ноль!")
# #         exit()
# #     result = num1 / num2  
# # else:
# #     print("Ошибка: неверный оператор!")
# #     exit()
# # print("Результат:", result)


# print ('Приветствуем вас в калькуляторе Python')
# q1 = int (input('Введите число 1: '))
# q2 = int (input('Введите число 2: '))

# v = int (input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n'))

# if v == 1:
#     r = q1 + q2
#     p = 'сложения'
#     t = p
# if v == 2:
#     r = q1 - q2
#     l = 'вычитания'
#     t = l
# if v == 3:
#     r = float(q1 / q2)
#     m = 'деления'
#     t = m
# if v == 4:
#     r = q1 * q2
#     n = 'умножения'
#     t = n
# print ('Результат',t,' = ',r)

# # калькулятор 2

# def add(x,y):
#     return x+y
# def subtract(x,y):
#     return x-y
# def multiply(x,y):
#     return x*y
# def divide(x,y):
#     if y == 0:
#         return None
#     return x/y



# import math

# print('Калькулятор')

# f = int(input('Выберите функцию \nСложение -- 1\nВычитание -- 2\nУмножение -- 3\nДеление -- 4\nВозведение в квадрат -- 5\nВычисление квадратного корня -- 6\nВычисление синуса -- 7\nВычисление косинуса -- 8\n'))

# if f == 1:
# ch1 = int(input('Введите первое число: '))
# ch2 = int(input('Введите второе число: '))
# r = ch1 + ch2
# elif f == 2:
# ch1 = int(input('Введите первое число: '))
# ch2 = int(input('Введите второе число: '))
# r = ch1 - ch2
# elif f == 3:
# ch1 = int(input('Введите первое число: '))
# ch2 = int(input('Введите второе число: '))
# r = ch1 * ch2
# elif f == 4:
# ch1 = int(input('Введите первое число: '))
# ch2 = int(input('Введите второе число: '))
# r = float(ch1 / ch2)
# elif f == 5:
# ch = int(input('Введите число: '))
# r = ch * ch

# elif f == 6:
# ch = int(input('Введите число: '))
# sqrt = ch ** (0.5)
# r = sqrt

# elif f == 7:
# ch = int(input('Введите число: '))
# r = math.sin(ch)

# elif f == 8:
# ch = int(input('Введите число: '))
# r = math.cos(ch)

# print('Ответ:', r)



# import math
# def calculator():
# try:
# print('\nВітаємо у кулькуляторі')
# print('\n1 - Додавання \n2 - Віднімання \n3 - Множення \n4 - Ділення \n5 - Степінь числа(друге число - степінь) \n6 - Квадратний корінь числа \n7 - Знайти синус \n8 - Знайти косинус \n9 - Знайти тангенс')
# o1=float(input('\nВиберіть дію зі списку вище: '))
# def value1():
# global v1
# global v2
# v1 = float(input('\nВведіть перше число: '))
# v2 = float(input('\nВведіть друге число: '))
# def value2():
# global v3
# v3 = float(input('\nВведіть число:'))
# if o1 <= 5:
# value1()
# if o1 == 1:
# r = v1 + v2
# print('Ваш результат:',r)
# elif o1 == 2:
# r = v1 - v2
# print('Ваш результат:',r)
# elif o1 == 3:
# r = v1 * v2
# print('Ваш результат:',r)
# elif o1 == 4:
# r = v1 / v2
# print('Ваш результат:',r)
# elif o1 == 5:
# r =pow(v1,v2)
# print('Ваш результат:',r)
# if o1 >= 6:
# value2()
# if o1 == 6:
# r = math.sqrt(v3)
# print('Ваш результат:',r)
# elif o1 == 7:
# r = math.sin(v3)
# print('Ваш результат:',r)
# elif o1 == 8:
# r = math.cos(v3)
# print('Ваш результат:',r)
# elif o1 == 9:
# r = math.tan(v3)
# print('Ваш результат:',r)
# ask = input('Ви бажаєте продовжити?(Так/Ні): ')
# if ask == 'Так' or ask == 'так':
# calculator()
# else:
# print('На все добре!')
# except:
# print('Сталась помилка. Спробуйте ще раз :(')
# calculator()




# def is_valid(num_str):
#     try:
#         int(num_str)
#         return True
#     except ValueError:
#         return False
   




# def calc():
#     while True:
#         n1 = input('Введите число:')
#         n2 = input('Введите число:')
#         # пример валидации всех проверок
#         if not (n1.isnumeric() or (n1.startswith('-') and n1[1:].isnumeric())):
#             print('ошибка введи число')
#             continue
#         if not (n2.isnumeric() or (n2.startswith('-') and n2[1:].isnumeric())):
#             print('ошибка введи число')
#             continue
#         # if not is_valid(n1) or not is_valid(n2):
#         #     print('ошибка введи число')
#         #     continue
#         n1 = int(n1)
#         n2 = int(n2)


#         operator = input('+-/*')


#         if operator == "+":
#             result = add(n1,n2)
#         elif operator == "-":
#             result = subtract(n1,n2)
#         elif operator == "*":
#             result = multiply(n1,n2)
#         elif operator == "/":
#             result = divide(n1,n2)
#             if result is None:
#                 print('Ошибка деления на 0')
#                 continue
#         else:
#             print("неверная операция")
#             continue
#         print(result)


# calc()




# def taxi_cost(distance):
#     return(round((base + add * distance) + 2))
    
# base = 5
# add = 1
# distance = int(input("Введите расстояние: "))
# print('Стоимость поездки: ', taxi_cost(distance))

# password = input('Введите пароль: ')

# is_numeric = False
# is_upper = False
# is_lower = False
# is_spec = False
# is_isdigit = True

# for a in password:
#     if a.isnumeric():
#         is_numeric = True
#     elif a.islower():
#         is_lower = True
#     elif a.isupper():
#         is_upper = True
#     elif a in "@#%&?":
#         is_spec = True
#     elif a.isdigit():
#         is_isdigit = True

# if len(password) >= 8 and is_numeric and is_upper and is_lower and is_spec and is_isdigit:
#     print('Пароль: Надежный')
# else:
#     print('Пароль слишком простой')


# num = float(input('введите число:'))
# sqrt = num ** (0.5)
# print("Квадратный корень из числа " +str(num)+" это " +str(sqrt))