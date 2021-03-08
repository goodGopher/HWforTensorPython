#частота использования символов в тексте
from typing import Counter


print("Введите текст:")
#добавить проверку на ввод?
text = input()

listOfLetters = sorted(text)
j = 0
Counter = 1
for i in range(0,len(listOfLetters)):
    if len(listOfLetters) - i > 1:
        if listOfLetters[i] == listOfLetters[i+1]:
            Counter+=1
        else:
            print("частота использования символа ",listOfLetters[i]," в тексе :",Counter)
            Counter = 1
    else:
        print("частота использования символа ",listOfLetters[i]," в тексе :",Counter)
    
    





