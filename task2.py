def get_count_char(str_):
    count_char_dict = {}
    for words in str_.lower():
        if words.isalpha():
            if words in count_char_dict:
                count_char_dict[words] += 1
            else:
                count_char_dict[words] = 1
    return count_char_dict

def new_char(count_char_dict):
    i = 0
    new_dict = {}
    for char in count_char_dict:
        i += count_char_dict.get(char)
    for char in count_char_dict:
        new_dict[char] = round((count_char_dict.get(char)/i)*100, 2)
    check = 0
    for char in new_dict:
        check += new_dict.get(char)
    return new_dict
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
