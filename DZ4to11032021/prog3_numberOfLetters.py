#частота использования символов в тексте



print("Введите текст:")

text = input()
letter_dict = {}
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
    
    





