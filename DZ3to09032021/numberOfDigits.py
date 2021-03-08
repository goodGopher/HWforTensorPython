#Частота использования цифр в диапазоне чисел
#Добавить форматирование к программам
print("Введите границы диапазона:")
#добавить проверку на ввод
x1 = int(input())
x2 = int(input())

for digit in range(0,10):
    Summ = 0
    for i in range(x1,x2+1):
        x = i
       
        while x != 0:
            last = x % 10
            x = x // 10

            if last == digit:
                Summ+=1
    print("Для цифры ",digit," частота использования ", Summ)
    Summ = 0

