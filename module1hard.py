grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

GPA=[(sum(grades[0]))/(len(grades[0])),
    (sum(grades[1]))/(len(grades[1])),
     (sum(grades[2]))/(len(grades[2])),
      (sum(grades[3]))/(len(grades[3])),
    (sum(grades[4]))/(len(grades[4]))]
#sum-сумма значений(числовых) в списке, len-колличество значений в списке(длина списка)

print(GPA)
#сортировка списка в алфовитном порядке:
students_in_order=sorted(students)
print(students_in_order)
#с помощью dict- преобразую в словарь, с помощью zip-объединяю два списка
final_GPA=dict(zip(students_in_order,GPA))
print("Средний балл учеников:",final_GPA)












