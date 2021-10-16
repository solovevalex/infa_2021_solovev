print('введите свое ФИО: ')
fio_str = input()
fio_list = fio_str.split(' ')
var_list = ['f', 'i', 'o']
dict_values = {}
for i in range(len(fio_list)):
    dict_values.setdefault(var_list[i], fio_list[i])
print(dict_values)

familia = dict_values['f']
imia = dict_values['i']
otchestvo = dict_values['o']

print(f'{familia} {imia} {otchestvo}')