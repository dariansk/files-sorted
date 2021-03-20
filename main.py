def convert_file_to_list(file):
    with open(file, 'r', encoding='utf-8') as f:
        text_list = f.readlines()
        return text_list


# сортируем файлы и записываем их в результирующий файл
# спасибо гуглу за подсказку, как сортировать словарь по значениям
def write_to_sorted_file():
    files = {'1.txt': convert_file_to_list('1.txt'), '2.txt': convert_file_to_list('2.txt'),
             '3.txt': convert_file_to_list('3.txt')}
    sorted_list = sorted(files.items(), key= lambda value: len(value[1]))
    files_sorted_dict = {item[0]:item[1] for item in sorted_list}
    with open('file_sorted.txt', 'w', encoding='utf-8') as file:
        for item in list((files_sorted_dict.keys())):
            file.write(f'{item}\n')
            file.write(str(len(files_sorted_dict.setdefault(item))) + '\n')
            for str_dict in files_sorted_dict[item]:
                file.write(str_dict)
            file.write('\n')


write_to_sorted_file()
