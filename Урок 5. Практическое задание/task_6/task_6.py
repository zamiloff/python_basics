"""
6) Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                     Физика:   30(л)   —   10(лаб)
                     Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
dct = {}
file = open("task_6.txt", 'r', encoding='utf-8')
for line in file:
    replaced_line = line.replace("(л)", "").replace("(пр)", "").replace("(лаб)", "").replace("—", "0").replace(":", "")
    print(replaced_line)
    subject, lec, pr, lab = replaced_line.split()
    dct[subject] = int(lec) + int(pr) + int(lab)
print(f"{dct}")