from pprint import pprint

def custom_write(file_name, strings):
    strings_position = {}
    num_string = 0
    file = open(file_name, 'w')

    for i in strings:
        file.write(i + '\n')
        num_string += 1
        byte_string = file.tell()
        strings_position[(num_string, byte_string)] = i

    file.close()

    return strings_position














info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)