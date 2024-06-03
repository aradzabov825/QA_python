text = """""
There are many variants , but most of them do not always have acceptable modifications, for example, humorous inserts or words that do not even remotely resemble Latin. If you need Lorem Ipsum for a serious project, you probably don't want some joke hidden in the middle of a paragraph. Also, all other well-known Lorem Ipsum generators use the same text, which they simply repeat until they reach the desired volume.
"""""


#разбиваю текст на слова
words = text.split()


#создаю 2 пустых списка для хранения слов и их частоты
uniq_words = []
words_count = []


#подсчитывает частоту встречаемости каждого слова
for word in words:
    #убирает знаки препинания
    word = word.strip(',.').lower()


    #если слово уже есть в списке, увеличиваю его счетчик
    if word in uniq_words:
        index = uniq_words.index(word)
        words_count[index] += 1
    #если слово встречается впервые, добавляем в список
    else:
        uniq_words.append(word)
        words_count.append(1)
#найти наиболее часто встречающееся слово
max_count = max(words_count)
most_common_word = uniq_words[words_count.index(max_count)]


#вывод
print(f'Наиболее часто встречающеся слово: {most_common_word} встречается {max_count} раз')



