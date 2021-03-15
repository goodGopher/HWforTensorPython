def dig_check(dig):
    try:
        if dig :
            dig = float(dig)
        else:
            return 0 
    except ValueError :
        print(f"{dig} - недопустимый формат ввода")
        return 0
    if dig <= 0:
        return 0
    return 1

def dig_int_check(dig):
    try:
        if dig :
            dig = int(dig)
        else:
            return 0 
    except ValueError :
        print(f"{dig} - недопустимый формат ввода для времени действия вклада")
        print("оно может быть только целым положительным числом месяцев")
        return 0
    if dig <= 0:
        return 0
    return 1

def bank_stonks(begin_summ,percent,validity):
    if percent > 100 or percent <= 0 :
        raise ValueError
    #validity в месяцах
    #Проверки аргументов
    summ = 0.0
    for i in range(validity):
        summ = summ + begin_summ 
        summ = summ * (1 + percent / 100)
    
    return summ

def menu():
    print(
    """
                    МЕНЮ
    1 - расчет полученной через банк прибыли
    2 - выход
    """
    )

print(bank_stonks(4,50,2))

while True :
    menu()
    a = input()
    if a == "1" :
        try:
            print("Введите начальную сумму вклада:", end = "")
            begin_summ = input()

            print("Введите начисляемый процент:", end = "")
            percent = input()
            print("Введите срок действия вклада в месяцах:", end = "")
            validity = input()

            if dig_check(begin_summ) and dig_check(percent) and dig_int_check(validity):
                print(f"Итоговая сумма: {bank_stonks(float(begin_summ),float(percent),int(validity))}")
            else:
                print("Введено неверное значение")
        except ValueError:
            print("Одно из значений введено в несоответствии с форматом")
            continue
    elif a == "2":
        print("Выход из программы")
        exit()
    else:
        print("Вы ввели не обрабатываемое значение")