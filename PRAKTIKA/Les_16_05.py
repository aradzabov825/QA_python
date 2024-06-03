# import re

# regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\[A-Z|a-z]{2,7}\b')

# def check(email):
    
#     if re.match(regex, email):
#        print("Норм")
#     else:
#         print("Не норм")

# print(check(input('Введите Email ')))

# # ____________________________________________________________________________________________


# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\[A-Z|a-z]{2,7}\b'
# или pattern r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# # ____________________________________________________________________________________________

# БЕЗ РЕГУЛЯРНЫХ ВЫРАЖЕНИЙ

# def check_emails(email):

#     #проверка на наличие собаки
#     if '@' not in email:
#         return False
#     #делим адрес по символу собаки
#     parts = email.split('@')

#     #проверку н наличие логина и домена
#     if len(parts) != 2:
#         return False
   
#     login,domain = parts[0],parts[1]

#     #проверка длины логина
#     if len(login) < 4:
#         return False


#     #проверка формата логина
#     if not login or not login.replace('.','').isalnum():
#         return False
   
#     #проверка формы домена
#     domain_par = domain.split('.')
#     if len(domain_par) <2 or any(not part.isalnum() for part in domain_par):
#         return False
#     return True


# print(check_emails('example@email.com')) # True
# print(check_emails('invalid.email@domain'))  #False
# print(check_emails('another.example@sub.domain.com'))  #True
# print(check_emails('invalid_enother?@domain.name')) # false
# print(check_emails('we@domain.name')) # false


#__________________________________________________________________________________________

# import re


# def check_emails(mail):
#     #создаю паттерн для проверки формата адреса email
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


#     if not re.match(pattern,mail):
#         return False
   
#     parts = mail.split('@')


#     if len(parts[0])<4:
#         return False
   
#     return True


   
# print(check_emails('example@email.com')) # True
# print(check_emails('invalid.email@domain'))  #False
# print(check_emails('another.example@sub.domain.com'))  #True
# print(check_emails('invalid_enother?@domain.name')) # false
# print(check_emails('we@domain.name')) # false


# __________________________________________________________________________________________

# a = [1,2,3,4,5,4,3,4,34]
# b = [3,5,1,8,8,9,9]


# for num in set(a):
#     print(f'Число {num} {"" if a.count(num) == 1 else "НЕ"} уникальное в списке')
# for num in set(b):
#     print(f'Число {num} {"" if b.count(num) == 1 else "НЕ"} уникальное в списке')


# ________________________________________________________________________________

# def is_uniq(lst):
#     #пройтись по всем элементам списка
#     for i in range(len(lst)):
#         #сравнить текущий элемент с остальными элементами списка
#         for j in range(i+1,len(lst)):
#             if lst[i] == lst[j]:
#                 return False
#     return True

# print(is_uniq([1,2,3,4,5]))
# print(is_uniq([1,2,3,4,5,1]))

# ______________________________________________________________________

# def is_uniq(lst):
   
#     uniq_set = set(lst)

#     return len(uniq_set) == len(lst)

# print(is_uniq([1,2,3,4,5]))
# print(is_uniq([1,2,3,4,5,1]))



# ________________________________________________________________________________________

user_database = {
    "user1@example.com": {'name':'User', 'password': 'Qwe12343r'},
    "user2@example.com": {'name':'Vasya', 'password': 'Qwe12343r'},
    "user3@example.com": {'name':'Petya', 'password': 'Qwe12343r'},
    "user4@example.com": {'name':'Sereja', 'password': 'Qwe12343r'}},

import re 
def reg_user():
    while True:
        # проверка ввода имени
        name = input('Введи имя ')
        if not re.match(r'[A-Za-z-]', name):
            print('Недопустимое имя ')
            continue
        # проверка почты
        email = input('Введи почту ')
        if not re.match(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            print('Недопустимая почта ')
            continue
        
        if not re.match(r'[a-zA-Z-]',name):
            print('Недопустимое имя')
            continue

        if len(name) <2:
            print('короткий имя')
            continue
        password = input('Введи пароль ')
        if len(password) < 8:
            print('короткий')
            continue
        if not any(char.isupper() for char in password):
            print('должен иметь хоть 1 заглавную')
            continue
        if not any(char.islower() for char in password):
            print('должен быть хотя бы 1 мелкий буква')
            continue
        if not any(char.isdigit() & char in '!@#$%^&*()-_=+[{]};;\",<>/>`~' for char in password):
            print('Цифру вбей хоть 1')
            continue
        user_database[email] = {'name': name, 'password': password}
        print('новый чувак создан')
        view_database = input('смотрим базу? y/n')
        if view_database.lower() == 'y':
            print(user_database)
            break
reg_user()
