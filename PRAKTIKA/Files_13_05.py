with open('example.txt','r',encoding='utf-8') as file:
    #первая задача
    print(file.read())


#__________________вторая задача первый способ через цикл for
# lines = file.readlines() #читаем все строки из файла в список


#     for i in range(1,len(lines),2):
#         print(lines[i])
#         print(lines[1::2])






# _________________через метод интервала enumerate()


#         for i, line in enumerate(file, start=1):
#               if i % 2 == 0:
#                    print(line)




#___________________третья задача


# search_word = 'Рэдрик'
# found_lines = []
   
# for line in file:
#         if search_word in line:
#             found_lines.append(line)


# if found_lines:
#         print(search_word)
#         for found_line in found_lines:
#             print(found_line)
