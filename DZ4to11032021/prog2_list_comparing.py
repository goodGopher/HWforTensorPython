"""Compare quantitys of two lists.

Functions:
    list_reading(my_list):
        Allows to read list from keyboard.
    main():
        Compare quantitys of two lists.

"""

import checks

def main():
    """Compare quantitys of two lists.

    Allows to enter from keyboard two lists
    and then, compare quantitys of their elements.

    """
    l1 = [1]
    l2 = [1]
    while l1 and l2:
        print(
    """
    Введите элементы двух сравниваемых множеств элементов списков.
    Для того, чтобы произвести ввод элемента списка, нажмите Enter.
    Для того, чтобы закончить ввод списка не вводите значение и нажмите Enter.
    Для выхода не вводите ничего в оба списка.
    """
    )
        l1 = []
        l2 = []
        print("Введите первый список:")
        checks.list_reading(l1)
        print("Введите второй список:")
        checks.list_reading(l2)
        l3 = set(l1)
        l4 = set(l2)
        if l3 == l4:
            if l3 and l4:
                print("Совпадают")
            else:
                print("Выход из программы")
        else:
            print("не совпадают")


if __name__ == "__main__":
    main()
