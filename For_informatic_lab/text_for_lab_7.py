name = 'acc'
S = 9
# открыть файл на чтение и дозапись, так как нужно не просто добавить игрока в рейтинг, но и обозначить его положение.
fail_records = open('records.txt', 'a+', encoding='utf-8')
# просто добавляю результаты игрока в конец файла
fail_records.write(f'{name} : {S}\n')
fail_records.close()
# переношу данные файла в список
fail_records = open('records.txt', 'a+', encoding='utf-8')
fail_records.seek(0)
results = []
for line in fail_records:
    results.append(line)

# нужно удалить перенос строки
# каждый элемент моего списка - строка, состоящая из имени и результата через " : ". хочу из этого сделать словарь.
results_real = []
for result in results:
    result = result.replace('\n', '')
    result = result.split(' : ')
    results_real.append(result)
# отсортирую результаты списка
result_sort = sorted(results_real, key=lambda x: int(x[1]), reverse=True)
fail_records.close()
# Занесу данные списка в файл
fail_records = open('records.txt', 'w')

for line in result_sort:
    result_for_write = f'{line[0]} : {line[1]}\n'
    fail_records.write(result_for_write)
fail_records.close()
