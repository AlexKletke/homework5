# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def compression_algorithm(string_standart):
    string = ''
    count = 1
    element = string_standart[0]
    for i in range(1, len(string_standart)):
        if string_standart[i] == element:
            count += 1
        else:
            string = string + str(count) + element
            element = string_standart[i]
            count = 1
    return string

def recovery_algorithm(compressed_string):
    string_standart = ''
    elements = ''
    for i in range(len(compressed_string)):
        if compressed_string[i].isdigit():
            elements += compressed_string[i]
        else:
            string_standart += compressed_string[i] * int(elements)
        elements = ''
    print(string_standart)
    return string_standart

with open('standart.txt', 'w') as data:
    data.write('fffllltttjjjvvvkkkk')
with open('standart.txt', 'r') as data:
    string_standart = data.readline()
with open('standart.txt', 'r') as file:
    string_standart = file.read()
with open('compression.txt', 'w') as file:
    compressed_string = compression_algorithm(string_standart)
    file.write(compressed_string)
print('Восстановленная строка: ' + string_standart)
print('Сжатая строка: ' + compression_algorithm(string_standart))