"""Calculate number of words or sentenses and frequency of letters using in text.

Functions:
    text_letters_num(text):
        Calculate frequency of letters using in text.
    text_words(text):
        Calculate number of words in text.
    text_sentenses(text):
        Calculate number of sentenses in text.
    menu():
        Show user's actions.
    main():
        Allows to enter text and to see his number of words,sentenses and frequency of letters using.

"""

def text_letters_num(text):
    """Calculate frequency of letters using in text.
    
    Arguments:
        text -- text (type: str).
    Return:
        frequency of letters using in text
    """
    letter_dict = {}
    j = 0
    Counter = 1
    for i in text:
        if letter_dict.get(i) == None:
            letter_dict[i] = 1
        else:
            letter_dict[i] += 1  

    sort_keys_list = sorted(list(letter_dict.keys()))
    sort_letter_dict = {}
    for i in sort_keys_list:    
        sort_letter_dict[i] = letter_dict[i] 
    return sort_letter_dict


def text_words(text):
    """Calculate number of words in text.
    
    Arguments:
        text -- text (type: str).
    Return:
        number of words in text

    """
    out_list = []
    t_stack = []
    controler = " ,.[]{}();:!?"

    for i in text:
        
        if i in controler:
            if len(t_stack) != 0:
                out_list.append("".join(t_stack))
                t_stack = []
            else:
                continue
        else:
            t_stack.append(i)
        
    if len(t_stack) != 0:
        out_list.append("".join(t_stack))
    return len(out_list)


def text_sentenсes(text):
    """Calculate number of sentenses in text.
    
    Arguments:
        text -- text (type: str).
    Return:
        number of sentenses in text

    """
    out_list = []
    t_stack = []
    last3=[]

    for i in text:

        if len(t_stack) == 0 and i == " ":
            continue
        elif i in [".","!","?"]:
            if len(t_stack) != 0:
                out_list.append("".join(t_stack))
                t_stack = []
            else:
                continue
        else:
            t_stack.append(i)
    return len(out_list)


def menu():
    """Show user's actions."""
    print(
    """
    1 - ввести текст с клавиатуры
    2 - выйти из программы
    """
    )


def main():
    """Allows to enter text and shows number of words,sentenses and frequency of letters using."""
    while True:
        menu()
        a = input()
        if a == "1":
            print("Введите текст:")
            t = input()
            wor = text_words(t)
            wor_end = ""
            if wor%10 in [2,3,4]:
                wor_end = "а"
            elif wor%10 == 1:
                wor_end = "о"
            print(f"В тексте {wor} слов{wor_end}")
            sen = text_sentenсes(t)
            end = "й"
            if sen%10 in [2,3,4]:
                end = "я"
            elif sen%10 == 1:
                end = "е"
            print(f"В тексте {sen} предложени{end}")
            letters_inf = text_letters_num(t)
            for i in letters_inf:
                print(f"Для символа {i} частота вхождения  {letters_inf[i]}")
        elif a == "2":
            print("выход из программы")
            exit()
        else:
            print("Вы ввели что-то не то")


if __name__ == "__main__":
    main()
