"""checks for corect input of numbers

Functions:
    input_check(in_str):
        Check str for convertation to positive integer
    list_reading(my_string):
        Check string for only digits and "-" symbols being

"""

def input_check(in_str):
    """Check agrument for convertation to positive integer

    Argument:
        in_str -- number, which can be converted to positive integer.
    Return:
        Return converted positive integer if argument can be converted, 
        else return 0
    """
    if type(in_str) == int:
        return in_str
    elif in_str.isdigit() or (in_str[1:].isdigit() and in_str[0] == "-"):
        return int(in_str)
    else:
        return 0

def list_reading(my_string):
    """Check string for only digits and "-" symbols being

    Argument:
        my_string -- string which only contain digits and "-" sybols
    Return:
        list with separated numbers

    """

    out_list = []
    t_stack = []

    for i in my_string:
        if i == "-" or i.isdigit():
            t_stack.append(i)
        elif i == " " and len(t_stack) == 0:
            continue
        elif i == " " and len(t_stack) != 0:
            out_list.append(float("".join(t_stack)))
            t_stack = []
        else:
            print(f"Введен необрабатываемый символ {i}")
            return 0
    if len(t_stack) != 0:
        out_list.append(float("".join(t_stack)))
    
    return out_list