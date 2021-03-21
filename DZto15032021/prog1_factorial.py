"""Calculating factorial.

Functions:
    input_check(in_str):
        Сheck in_str for integer type
    factorial(input_int):
        Сalculate factorial 
    menu():
        Show user's actions.
    main():
        Allows to enter number and to see his factorial.

"""

import checks

def factorial(input_int):
    """Calculate factorial"""
    a = checks.input_check(input_int)
    if a or input_int == "0":
        if a < 0 :
            raise ValueError
        elif a == 0:
            return 1
        elif a == 1 or a == 2:
            return a
        else:
            return factorial(a-1)*a
    else:
        raise TypeError


def menu():
    """Show user's actions."""
    print("Для выхода введите \"выход\" ")
    print("Введите целое положительное число:",end = " ")


def main():
    """Allows to enter number and to see his factorial."""
    while True:
        try:
            menu()
            a = input()
            if a == "выход":
                print("Выход из программы")
                exit()
            print(f"{a}! = {factorial(a)}")
        except TypeError:
            print("Введено не целое положительное число")
        except ValueError:
          print("Введено отрицательное число")
        except RecursionError:
           print("Введено слишком большое число")


if __name__ == "__main__":
    main()
    

