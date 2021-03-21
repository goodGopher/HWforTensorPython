"""Calculating LCM,GCF and check number for simplicity.

Functions:
    is_simple(x):
        Check a number for simplicity.
    NOD(x,y):
        Finding the greatest common factor.
    NOK(x,y):
        Finding the least common multiple.
    menu():
        Print menu with actions.
    main():
        Starts script, which can use GCF(x,y),LCM(x,y),is_simple(x) fumctions.

"""

def NOD(x,y):
    """Return the greatest common factor.

    Arguments:
        x,y -- integer.
    Return:
        integer

    """
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


def LCM(x,y):
    """Return the least common multiple.
    
    Arguments:
        x,y -- integer.
    Return:
        integer

    """
    return x * y / NOD(x,y)


def is_simple(x):
    """Check number for simplicity.
    
    Arguments:
        x -- integer
    Return:
        1 or 0

    """
    check = 1
    
    if x == 2:
        return 1
    elif x == 4:
        return 0
    else:
        for i in range(2, x//2+1):
            if x % i == 0:
                check = 0
                break
        if check  :
            return 1
        else:
            return 0


def menu():
    """Print menu with actions."""
    print("\tВыберите действие:")
    print("""
    1 - НОД двух чисел\n
    2 - НОК двух чисел\n
    3 - Проверка числа на простоту\n
    4 - Выход из программы
    """)


def main():
    """Allows to choose: NOD(), NOK() or is_simple()."""
    menu()
    answer = input()

    while answer != '4':
        if answer == '1':
            print("Введите первое число:", end = " ")
            a1 = input()
            print("Введите второе число:", end = " ")
            a2 = input()
            if (a1.isdigit() and a2.isdigit()):
                print(NOD(int(a1),(int(a2))))
            else:
                print("Вы ввели некорректные значения")
                continue
        elif answer == '2':
            print("Введите первое число:", end = " ")
            a1 = input()
            print("Введите второе число:", end = " ")
            a2 = input()
            if (a1.isdigit() and a2.isdigit()):
                print(LCM(int(a1),(int(a2))))
            else:
                print("Вы ввели некорректные значения")
                continue
        elif answer == '3':
            print("Введите число:", end = " ")
            a1 = input()
            if a1.isdigit() :
                if(is_simple(int(a1))):
                    print("Число простое")
                else:
                    print("Число не простое")
            else:
                print("Вы ввели некорректные значения")
                continue
        else :
            print("Вы ввели некорректное значение")
        menu()
        answer = input()


if __name__ == "__main__":
    main()