
# students = input('Введите имена студентов: ').split()
# grades = input('Введите оценки студентов: ').split()
 
# print({students[i]: int(grades[i]) for i in range(len(students))})


# ___________________________________________________________________________________________________________________

# students = [
#     {'name': "Alice", 'grades':[5,3,4,4]},
#     {'name': "Bill", 'grades':[2,2,3]},
#     {'name': "Bob", 'grades':[4,4,4,5]},
#     {'name': "David", 'grades':[]}
#     ]

# def filter_students(st):
#     #создал пустой список который будет использоваться для хранения студентов с баллом выше 4
#     filtred_students  = []
#     #начало цикла for который будет перебирать каждый элемент(каждого студента) из списка students
#     for i in st:
#         #извлекаю список оценок текущего студента(i) - это словарь, и обращение i['grades'] позволяет мне обратится по ключу grades
#         grades = i['grades']
#         #считаю средний балл для текущего студента
#         if grades:
#             average_grade = sum(grades) / len(grades)
#         else:
#             average_grade = 0
           
#         if average_grade > 4:
#             filtred_students.append(i['name'])
#     return filtred_students


# print(filter_students(students))

# ___________________________________________________________________________________________________________________

import os
 
def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ").replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    # text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words
 
 
def get_words_dict(words):
    words_dict = dict()
 
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict
 

def main():
    filename = input("Введите путь к файлу: ")
    if not os.path.exists(filename):
        print("Указанный файл не существует")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)

        # print(f"Кол-во символов: {len()}")
        print(f"Кол-во слов: {len(words)}")
        print(f"Кол-во уника-льных слов: {len(words_dict)}")
        print("Все использованные слова:")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])
 
if __name__ == "__main__":
    main()

# ___________________________________________________________________________________________________________________

# logs = [
#     '192.168.0.1 /home',
#     '192.168.0.1 /about',
#     '192.168.0.2 /home',
#     '192.168.0.1 /home',
#     '192.168.0.2 /contact',
#     '192.168.0.1 /about',
# ]

# def analyze_logs(logs):

#     ip_dict = {}

#     for log in logs:
#         ip,url = log.split()
#         print(ip,url)
#         if ip not in ip_dict:
#             ip_dict[ip] = set()
#             print(ip_dict)

#         ip_dict[ip].add(url)

#     uniq = {ip:len(url) for ip, url in ip_dict.items()}
#     return uniq

# print(analyze_logs(logs))

# ___________________________________________________________________________________________________________________

# import re

# number = input('Введите номер телефона: ')
# result = re.match(r'^(\+7|)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', number)
# print(bool(result))

# _______________________________________________

# def valid_num(num):
#     if len(num) != 12 or num[0] != "+":
#         return False
   
#     for i in num[1:]:
#         if not i.isdigit():
#             return False
#     return True


# print(valid_num('+79956247294'))
# print(valid_num('79956247294'))
# print(valid_num('+7995624'))
# print(valid_num('+asdjsadhsua'))

# ________________________________________________

# import re


# def valid_num(num):


#     phone_pattern = r'^\+\d{11}$'


#     if re.match(phone_pattern, num):
#         return True
#     else:
#         return False
   
# print(valid_num('+79956247294'))
# print(valid_num('79956247294'))
# print(valid_num('+7995624'))
# print(valid_num('+asdjsadhsua'))

# _________________________________________________


# import re

# regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\[A-Z|a-z]{2,7}\b')

# def check(email):
    
#     if re.match(regex, email):
#        print("Норм")
#     else:
#         print("Не норм")

# print(check(input('Введите Email ')))


# ________________________________________________________________________________________________________


# password=input('Введите пароль:')
# digits='1234567890'
# upper_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# lower_letters='abcdefghijklmnopqrstuvwxyz'
# symbols='!@#$%^&*()-+'
# message="Слабый пароль.Рекомендации:"
# acceptable=upper_letters+lower_letters+symbols
# cond1=(len(password))>11
# cond2=all(char in password for char in symbols)
# cond3=all(char in password for char in upper_letters)
# cond4=all(char in password for char in digits)
# cond5=all(char in set(password) for char in set(acceptable))
# rules=[cond1,cond2,cond3,cond4,cond5]
# p=set(password)
# a=set(acceptable)
# result=[]

# for x in p:
#     result.append(x in a)
# if all(result) is False:
#     print('Ошибка. Запрещенный спецсимвол')
# elif all(result) is True:
#     if cond1 is False:
#         message+=' увеличить число символов -'+" "+str(12-len(password))+','      
#     if cond2 is False:
#         message+=' '+'добавить 1 спецсимвол,'
#     if cond3 is False:
#         message+=' '+'добавить 1 заглавную букву,'
#     if cond4 is False:
#         message+=' '+'добавить 1 цифру,'
#         print(message[:(len(message)-1)])
# else:
#     if all(rules) is True:
#         print('Сильный пароль')


# ________________________________________________________________________________________________________

# def pas_val(pw):
#     if len(pw) < 8:
#         return False
#     h_d = any(char.isdigit() for char in pw)


#     h_l = any(char.isalpha() for char in pw)


#     h_plus  = pw.startswith('+') or pw.endswith('+')


#     return h_d and h_l and h_plus


# print(pas_val('+Password13'))
# print(pas_val('Password13+'))
# print(pas_val('Password13'))
# print(pas_val('+asdasdasada'))
# print(pas_val('+12312321321'))

# ________________________________________________________________________________________________________


