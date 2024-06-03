# try:
#     a = int(input('введите первое число:'))
#     b = int(input('введите второе число:'))
#     print(a/b)
# except ZeroDivisionError:
#     print('ошибка, деление на 0')
# except ValueError:
#     print('ошибка, введена буква')

# _________________________________________________________________________________________________________________

# try:
#     with open('example.txt','r',encoding='utf-8') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('ошибка')

# def listsum(numList):
#    if len(numList) == 1:
#         return numList[0]
#    else:
#         return numList[0] + listsum(numList[1:])

# print(listsum([5,5,5,5,5,5,5,5,5,5]))

# _________________________________________________________________________________________________________________

# def count_letters(word):
#     letter_count = {}
#     for i in word:
#         if i.isalpha():
#             i  = i.lower()
#             letter_count[i] = letter_count.get(i,0) +1
#     return letter_count

# _________________________________________________________________________________________________________________

def test_calc(op,n1,n2):
    try:
        if op == '+':
            return n1+n2
        elif op == '-':
            return n1-n2
        elif op == '*':
            return n1*n2
        elif op == '/':
            if n2 == 0:
                raise ValueError('Деление на 0 нельзя')
            return n1/n2
        else:
            raise ValueError('Неверная операция')
    except ValueError as e:
        return  str(e)
print(test_calc('+',5,3)) #ожидаю увидеть 8
print(test_calc('-',5,3)) #ожидаю увидеть 2
print(test_calc('*',5,3)) #ожидаю увидеть 15
print(test_calc('/',10,0)) #ожидаю увидеть обработку
print(test_calc('-',5,3)) #ожидаю увидеть обработку неверная операция