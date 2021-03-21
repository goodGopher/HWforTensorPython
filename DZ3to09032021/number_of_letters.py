"""Print frequency of using symbols in text."""

def number_of_letters():
    """Print frequency of using symbols in text."""
    print("Введите текст:")
    text = input()
    listOfLetters = sorted(text)
    j = 0
    Counter = 1
    for i in range(0,len(listOfLetters)):
        if len(listOfLetters) - i > 1:
            if listOfLetters[i] == listOfLetters[i+1]:
                Counter+=1
            else:
                print(f"частота использования символа {listOfLetters[i]} в тексте :{Counter}")
                Counter = 1
        else:
            print(f"частота использования символа {listOfLetters[i]} в тексте : {Counter}")


if __name__ == "__main__":
    number_of_letters()
    
    





