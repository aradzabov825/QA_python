str1 = input("Введите фразу 1")
str2 = input("Введите фразу 2")

def anagrams(str1, str2):
    return sorted (str1) == sorted (str2)
if anagrams(str1, str2):
    result = True
else:
    result = False
print(result)