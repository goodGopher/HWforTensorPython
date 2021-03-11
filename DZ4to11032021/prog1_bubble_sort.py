#Реализовать алгоритм сортировки списка/массива пузырьковым методом
import random 
 

def list_reading(my_string):#чтение
    out_list = []
    t_stack = []


    for i in my_string:
        if i == "-" or i.isdigit():
            t_stack.append(i)
        elif i == " " and len(t_stack) == 0:
            continue
        elif i == " " and len(t_stack) != 0:
            out_list.append(float("".join(t_stack)))
            t_stack = []
        else:
            print(f"Введен необрабатываемый символ {i}")
            return 0
    if len(t_stack) != 0:
        out_list.append(float("".join(t_stack)))
    
    return out_list


def bubble_sort(my_list):
    for i in range(0,len(my_list)-1):
        for j in range(0,len(my_list)-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
        
    

def menu():
    print(
    """
    1 - Ввести список с клавиатуры через пробел
    2 - Сгенерировать случайно 
    3 - Выйти

    """)
print (int(-3) > int(-7))

answer = 1
while answer:
    my_list = []
    menu()
    answer = input()
    if answer == "3":
        exit()
    elif answer == "2":
        for i in range(0,5):
            my_list.append(random.randint(0,1000))
        print(f"случайный список : {my_list}")
        bubble_sort(my_list)
        print(f"отсортированный список :{my_list} ")
        answer = [1]
        continue

    elif answer == "1":
        print(f"введите список")
        my_list = input()
        my_list = list_reading(my_list)
        if  my_list:
            print(f"введенный список :{my_list}")
            bubble_sort(my_list)
            print(f"отсортированный список :{my_list}")
        answer = [1]
        continue
    else:
        print("Введено неверное значение")
        answer = [1]
        continue
    
    


