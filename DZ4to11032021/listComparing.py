#Даны два списка. Определите, совпадают ли множества их элементов.
def list_reading(my_list):
    element = input()
    i = 0
    while element :
        my_list.append(element)
        i+=1
        element = input()

l1 = []
l2 = []

print(
"""
Введите элементы двух сравниваемых множеств элементов списков.
Для того, чтобы произвести ввод элемента списка, нажмите Enter.
Для того, чтобы закончить ввод списка не вводите значение и нажмите Enter.

"""
)
print("Введите первый список:")
list_reading(l1)
print("Введите второй список:")
list_reading(l2)

l3 = set(l1)
l4 = set(l2)

if l3 == l4:
    print("Совпадают")
else:
    print("не совпадают")
