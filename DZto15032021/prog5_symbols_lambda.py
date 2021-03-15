f = lambda text,letter: 1 if len(text) == 1 and text == letter else  0 if len(text) == 1 else f(text[0],i)+f(text[1:],i)#sorry... 
""" 1 if len(text) == 1 and text == letter  #возвращаем 1 если символ в тексте совпадает с подсчитываемым
else  
    0 if len(text) == 1                     #возвращаем 0 если не совпадает
else 
    f(text[0],i)+f(text[1:],i)"""           #отделяем первый символ от строки и обрабатываем его (левое слагаемое попадает в первые два условия)
                                            #рассматриваем остальную строку без первого символа, обработка начнется со второго (правое слагаемое)
text = input()
t1 = set(text)
for i in t1:
    print(f"Частота вхождения символа {i}  равна {f(text,i)}")