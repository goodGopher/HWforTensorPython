"""Calculating factorial.

Functions:
    input_check(in_str):
        Сheck in_str for integer type.
    menu():
        Show user's actions.
    main():
        Allows to enter number and to see his factorial.
"""

import checks

def menu():
    """Show user's actions."""
    print("Для выхода введите \"выход\" ")
    print("Введите целое положительное число:",end = " ")


def main():
    """Allows to enter number and to see his factorial."""
    f = lambda x: 1 if x==0 or x == 1 else x*f(x-1)
    while True:
        try:
            menu()
            a = input()
            if a == "выход":
                print("Выход из программы")
                exit()
            res = checks.input_check(a)
            print(f" res = {res}")
            if (res == 0 and a == "0") or res:
                print(f"{res}! = {f(res)}")
            elif res < 0:
                raise ValueError
            else:
                raise TypeError
        except TypeError:
            print("Введено не целое положительное число")
        except ValueError:
          print("Введено отрицательное число")
        except Exception:
           print("Введено слишком большое число")


if __name__ == "__main__":
    main()