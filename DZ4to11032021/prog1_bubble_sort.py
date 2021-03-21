"""Realize bubble sorting.

Functions:
    list_reading(my_str):
        Check string for errors: symbols which are not digits or "-".
    bubble_sort(my_list):
        Sorting of lsit by bubble method.
    menu():
        Print information about actions in a module.
    main():
        Start working with unsorted list and sort him.

"""

import random 

import checks
 
def bubble_sort(my_list):
    """Sorting of lsit by bubble method.

    Argument:
        my_list -- list with integer numbers.
    Return:
        Nothing return, but makes my_list sorted.
    
    """
    for i in range(0,len(my_list)-1):
        for j in range(0,len(my_list)-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
        
    
def menu():
    """Print information about actions in a module."""
    print(
    """
    1 - Ввести список с клавиатуры через пробел
    2 - Сгенерировать случайно 
    3 - Выйти

    """)


def main():
    """Start working with unsorted list to sort him."""
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
            my_list = checks.list_reading(my_list)
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


if __name__ == "__main__":
    main()

    
    


