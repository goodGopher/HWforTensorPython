#Удалить из списка элементы, значения которых уже встречались в предыдущих элементах
def list_reading(my_list):
    element = input()
    i = 0
    while element :
        my_list.append(element)
        i+=1
        element = input()

print("Введите список через Enter:")
main_list = []
list_reading(main_list)
print(f"начальный список {main_list}")

rand_list = list(set(main_list))
main_list.reverse()
for i in rand_list:
    while main_list.count(i) > 1:
        main_list.remove(i)
main_list.reverse()

print(f"обработанный список {main_list}")
