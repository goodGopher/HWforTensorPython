
import math
f = lambda x: math.factorial(x)
       

def input_check(in_str):
    if type(in_str) == int:
        return in_str
    elif in_str.isdigit() or (in_str[1:].isdigit() and in_str[0] == "-"):
       # in_str = int(in_str)
        return int(in_str)
    else:
        return 0

def menu():
    print("Для выхода введите \"выход\" ")
    print("Введите целое положительное число:",end = " ")



while True :
    try:
        menu()
        a = input()

        if a == "выход":
            print("Выход из программы")
            exit()
        res = input_check(a)
        print(f" res = {res}")
        if (res == 0 and a == "0") or res:
            print(f"{res}! = {f(res)}")
        elif res < 0 :
            raise ValueError
        else:
            raise TypeError
    except TypeError :
        print("Введено не целое положительное число")
    except ValueError:
      print("Введено отрицательное число")
    except Exception:
       print("Введено слишком большое число") 