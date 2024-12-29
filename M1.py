# Средний балл
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # список оценок уч-ся поимённый
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # множество имён уч-ся неупорядоченно
# Средний балл списка
grades_middle = []
# i - это список
for i in grades:
    grades_middle.append(sum(i) / len(i))
    continue
sorted_students = sorted(students)
result = dict(zip(sorted_students, grades_middle))
print(result)