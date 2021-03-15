def input_check(in_str):
    if type(in_str) == int:
        return in_str
    elif in_str.isdigit() or (in_str[1:].isdigit() and in_str[0] == "-"):
       # in_str = int(in_str)
        return int(in_str)
    else:
        return 0

def factorial(input_str):
    a = input_check(input_str)
    if a or input_str == "0":
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
    print("Для выхода введите \"выход\" ")
    print("Введите целое положительное число:",end = " ")



while True :#sorry
    try:
        menu()
        a = input()
        
        if a == "выход":
            print("Выход из программы")
            exit()
        print(f"{a}! = {factorial(a)}") 
    except TypeError :
        print("Введено не целое положительное число")
    except ValueError:
      print("Введено отрицательное число")
    except RecursionError:
       print("Введено слишком большое число") 
    

