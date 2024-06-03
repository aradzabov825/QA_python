# import re

# x = [1,2,3,4,5,6,7,8,9]

# for i in x:
#     if i % 3 == 0:
#         print(i)

# # ______________________________________________________________________________________________________________________

# contacts = [
#     {
#         "name": "Карина",
#         "phone": "+79818769751"
#     },
#     {
#         "name": "Артем",
#         "phone": "+79321658569"
#     },
#     {
#         "name": "Сергей",
#         "phone": "+79216549636"
#     },
# ]
 
# FORMAT_STR = '{:<15} {:>12}'
 
 
# def list(contacts):
#     print(FORMAT_STR.format('Name', 'Phone'))
#     for contact in contacts:
#         print(FORMAT_STR.format(
#             contact['name'],
#             contact['phone']
#         ))
 
 
 
# def find(contacts):
#     print("Введите имя контакта:")
#     name = input("> ")
 
#     for contact in contacts:
#         if contact['name'] == name:
#             print(FORMAT_STR.format(
#                 contact['name'],
#                 contact['phone']
#             ))
#             break
#     else: 
#         print("Контакт не найден")
 
# def delete(contacts):
#     print("Введите контакт: ")
#     name = input('> ')
#     for contact in contacts:
#         if contact['name'] == name:
#             print("Вы хотите удалить контакт %s (yes/no)?: " % name )
#             name_del = input('> ')
#             if name_del == 'yes':
#                contacts.remove(contact)
#                print("Вы удалили контакт %s " % name)
 
 
 
# def add(contacts):
#     print("Введите имя контакта:")
#     name = input("> ")
#     print("Введите телефон контакта:")
#     phone = input("> ")
#     new_contact = {
#         'name': name,
#         'phone': phone
#     }
#     contacts.append(new_contact)
    
#     print('Контакт сохранён')

# print("Добро пожаловать в телефонную книгу.")
# print("""Введите команду:
# * list - чтобы посмотреть список контактов.
# * find - найти контакт по имени
# * add  - добавить контакт
# * del  - удаление контакта
# * exit - выход""")
 
# while True:
#     print("\nВведите команду: ")
#     command = input('> ')
#     if command == 'list':
#         list(contacts)
#     elif command == 'find':
#         find(contacts)
#     elif command == 'add':
#         add(contacts)
#     elif command == 'del':
#         delete(contacts)
#     elif command == 'exit':
#         break
#     else:
#         print("Неизвестная команда")

# # _______________________________________________________________________________________________________________________

# import math

# print('Калькулятор')

# f = int(input('Выберите функцию \nСложение -- 1\nВычитание -- 2\nУмножение -- 3\nДеление -- 4\n'))

# if f == 1:
#     ch1 = int(input('Введите первое число: '))
#     ch2 = int(input('Введите второе число: '))
#     r = ch1 + ch2
# elif f == 2:
#     ch1 = int(input('Введите первое число: '))
#     ch2 = int(input('Введите второе число: '))
#     r = ch1 - ch2
# elif f == 3:
#     ch1 = int(input('Введите первое число: '))
#     ch2 = int(input('Введите второе число: '))
#     r = ch1 * ch2
# elif f == 4:
#     ch1 = int(input('Введите первое число: '))
#     ch2 = int(input('Введите второе число: '))
#     r = float(ch1 / ch2)
# print('Ответ:', r)

# # _______________________________________________________________________________________________________________________

# with open('example.txt','r',encoding='utf-8') as file:
#     search_word = (input('какое слово найти? '))
#     found_lines = []
   
#     for line in file:
#         if search_word in line:
#             found_lines.append(line)


#     if found_lines:
#         print(search_word)
#         for found_line in found_lines:
#             print(found_line)
#     print(file.read())

# # _____________зацикленный алгоритм

# with open('example.txt','r',encoding='utf-8') as file:
#     while True:
#         search_word = (input('какое слово найти? '))
#         found_lines = []
        
#         for line in file:
#             if search_word in line:
#                 found_lines.append(line)
                
#             if found_lines:
#                 print(search_word)
#                 break
               
#         for found_line in found_lines:
#             print(found_line)
#             break
#         file.read()

# # _______________________________________________________________________________________________________________________

# dct = {'Вопрос 1': {
#             'Вопрос': 'сколько будет 3 в третьей степени ', 
#             'Ответ': {1: '27', 2: '28', 3: '29'}, 
#             'Правильный ответ': 1},
    
#        'Вопрос 2': {
#            'Вопрос': 'Где в феврале 1945 года прошла встреча Сталина, Рузвельта и Черчилля? ', 
#            'Ответ': {1: 'Ялта', 2: 'Ленинград', 3: 'Ленинград'}, 
#            'Правильный ответ': 1},
    
#        'Вопрос 3': {
#            'Вопрос': 'Где в феврале 1945 года прошла встреча Сталина, Рузвельта и Черчилля? ', 
#            'Ответ': {1: 'Ялта', 2: 'Ленинград', 3: 'Ленинград'}, 
#            'Правильный ответ': 1}
#        } 
# score = 0
# print(dct.items())
# for key, values in dct.items():
 
#     question = key, values['Вопрос']
#     answer_options = values['Ответ']
#     answer_correct = values['Правильный ответ']
#     print('\n', *question)
#     print('Варианты ответов: ', answer_options)
#     answer_user = int(input('Выберите вариант ответа: '))
    
#     if answer_user not in answer_options.keys():
#         print("Ошибка ввода")
#     else:
#         if answer_user == answer_correct:
#             score += 1
#             print('Ответ верный. Ваш счёт:', score)
#         else:
#             print("Ответ не верный, попробуйте ещё")


# a = [1,2,3]  # список с аргументами
# for i in a:
#     print(i)