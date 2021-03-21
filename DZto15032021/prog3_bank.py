"""Simulates  simple bank deposit 

Functions:
    dig_check(dig):
        Check number for possibility to convert to float and for number > 0.
    dig_int_check(dig):
        Check number for possibility to convert to int and for number > 0.
    bank_stonks(begin_summ,percent,validity):
        Calculate result summ which you will have on your deposit.
    menu():
        Show user's actions.
    main():
        Allows to enter begin summ, percent, validity and to see result summ which you will have on your deposit.       

"""

def dig_check(dig):
    """Check number for possibility to convert to float and for number is positive.

    Arguments:
        dig -- number, can be str-type.
    Return:
        Return 1 if number can be convert to float and number is positive,
        else return 0.

    """
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
    """Check number for possibility to convert to int and for number is positive.

    Arguments:
        dig -- number, can be str-type.
    Return:
        Return 1 if number can be convert to int and number is positive,
        else return 0.

    """
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
    """Calculate result summ which you will have on your deposit.
    
    Arguments:
        begin_summ -- number (type: float), begin summ on your deposit.
        percent -- number (type: float), percent, which will using for increase your deposit summ.
        validity -- number(type: int), number of mounths during which deposit will exist. 
    """
    if percent > 100 or percent <= 0 :
        raise ValueError
    summ = 0.0
    for i in range(validity):
        summ = summ + begin_summ 
        summ = summ * (1 + percent / 100)
    
    return summ


def menu():
    """Show user's actions."""
    print(
    """
                    МЕНЮ
    1 - расчет полученной через банк прибыли
    2 - выход
    """
    )


def main():
    """Allows to enter begin summ, percent, validity and to see result summ which you will have on your deposit."""
    while True:
        menu()
        a = input()
        if a == "1":
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


if __name__ == "__main__":
    main()