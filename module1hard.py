grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
new = {} #создаем пустой словарь
names = list(students) #преобразовываем словарь в лист
names.sort() #сортируем в элементы листа в алфавитном порядке

gradesAverage = [] #создаем пустой список для средних оценок
#вычисляем среднее для каждого элемента списка и добавляем его в список
for e in grades:
    average = sum(e) / len(e)
    gradesAverage.append(average)
#добавляем пары ключ:значение в пустой словарь
for e in names:
    for el in gradesAverage:
        if names.index(e) == gradesAverage.index(el):
            new[e] = el
print(new)
