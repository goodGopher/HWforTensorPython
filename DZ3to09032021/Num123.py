#Определить, является ли введенное число простым
#Нахождение наибольшего общего делителя
#Нахождение наименьшего общего кратного

def NOD(x,y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


def NOK(x,y):
    return x * y / NOD(x,y)

def IsSimple(x):
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

#FORMAT
def menu():
    print("\tВыберите действие:")
    print("""
    1 - НОД двух чисел\n
    2 - НОК двух чисел\n
    3 - Проверка числа на простоту\n
    4 - Выход из программы
    """)
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
            print(NOK(int(a1),(int(a2))))
        else:
            print("Вы ввели некорректные значения")
            continue
    elif answer == '3':
        print("Введите число:", end = " ")
        a1 = input()
        if a1.isdigit() :
            if(IsSimple(int(a1))):
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
        
        