"""Checking text for correct parentheses arrangement.

Functions:
    text_check(text):
        Check text for correct parentheses arrangement.
    main():
        Allows to enter text and check him for correct parentheses arrangement.

"""

def text_check(text):
    """Check text for correct parentheses arrangement.
    
    Argument:
        text -- text (type: str).
    Return:
        0 if parentheses arrangement is incorrect.
    If parentheses arrangement is correct prints "все скобки расставлены корректно",
    else return 0.

    """
    left_list = []
    right_list = []
    for i in range(0,len(text)):
        if text[i] == "{" or text[i] == "(" or text[i] == "[" :
            left_list.append(text[i])
        if text[i] == "}" or text[i] == ")" or text[i] == "]" :
            if len(left_list) == 0:
                print("скобки расставлены некорректно\n")
                return 0
            res = left_list.pop()+text[i]
            if res != "{}" and res != "()" and res != "[]":
                print("скобки расставлены некорректно\n")
                return 0
    if len(left_list) != 0 :
        print("скобки расставлены некорректно\n")
        return 0
    print("все скобки расставлены корректно\n")


def main():
    """Allows to enter text and check him for correct parentheses arrangement."""
    print("Для выхода введите пустую строку.\nВведите текст:")
    text = input()
    while text:
        text_check(text)
        print("Для выхода введите пустую строку.\nВведите текст:")
        text = input()


if __name__ == "__main__":
    main()


