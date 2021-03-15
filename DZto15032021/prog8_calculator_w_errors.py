def prim_read(prim):#проверки и правильное чтение чисел
    out_list = []
    t_stack = []


    for i in prim:
        if i in ["+","-","*","/","^","(",")"]:
            if len(t_stack) != 0:
                out_list.append("".join(t_stack))
                t_stack = []
            out_list.append(i)
        elif i.isdigit() :
            t_stack.append(i)
        elif i == " " and len(t_stack) == 0:
            continue
        elif i == " " and len(t_stack) != 0:
            out_list.append("".join(t_stack))
            t_stack = []
        else:
            print(f"Введен необрабатываемый символ {i}")
            raise TypeError
    if len(t_stack) != 0:
        out_list.append("".join(t_stack))
    return out_list


def prim_to_RPN(input_str):#Преобразование к обратной польской записи
    if prim_read(input_str):
        prim = prim_read(input_str)
    else:
       return 0
    operations_priority = {#приоритеты операций
        "(":0,
        "+":1,
        "-":1,
        "*":2,
        "/":2,
        "^":3
    }
    
    output_str = []
    stack = []
    for i in prim:
       
        if i.isdigit() :
            output_str.append(i)
        elif i == "(" or i == "^" :
           stack.append(i) 
        elif i in ["+","-","*","/"]:#бинарные операции
            while len(stack)!= 0 and operations_priority[stack[len(stack)-1]] >= operations_priority[i] :
                output_str.append(stack.pop())
            stack.append(i)
        elif i == ")":
            symbol = stack.pop()
            while symbol != "(":
                output_str.append(symbol)
                if len(stack) == 0:
                    
                    raise ValueError
                else:
                    symbol = stack.pop()
    stack.reverse()
    for i in stack:
        if i in ["+","-","*","/","^"]:
            output_str.append(i)
        else:

            raise ValueError

    return output_str
    
def calculating(RPN_str):#Вычисление примера на основе ОПЗ 
    RPN_str = prim_to_RPN(RPN_str)
   

    stack = []

    for i in RPN_str:
        x1 = 0
        x2 = 0
        if i.isdigit():
            stack.append(i)
            #стек на пустоту
        elif i in ["+","-","*","/","^"]:
            x1 = float(stack.pop())
            x2 = float(stack.pop())
            if i == "+":
                stack.append(x1+x2)
            elif i == "-": 
                stack.append(x2-x1)
            elif i == "*":
                stack.append(x1*x2)
            elif i == "/":
                stack.append(x2/x1)
            elif i == "^":
                stack.append(x2**x1)
    return stack.pop()
        
def menu():
    print("Для выхода введите пустую стоку.")
    print("Введите пример:", end = " ")
    





menu()
primer = input()
while primer :
    try:
        print(f"Ответ: {calculating(primer)}")
    except ValueError:
        print("Не согласованы скобки")
    except TypeError:
        print("Введен необрабатываемый символ")
    except OverflowError:
        print("получилось слишком большое значение для отображения...")
    except ZeroDivisionError:
        print("Нельзя делить на 0")
    except IndexError:
        print("Не верная форма ввода примера")
    finally:
        menu()
        primer = input()
print("Выход из программы")