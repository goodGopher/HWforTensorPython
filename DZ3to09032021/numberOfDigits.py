#Частота использования цифр в диапазоне чисел

print("Введите границы диапазона:")
print("Введите первое число: ",end = "")
x1 = input()
print("Введите второе число: ",end = "")
x2 = input()

if x1.isdigit() and x2.isdigit() :
    x1 = int(x1)
    x2 = int(x2)
    if x1 > x2 :
        x1, x2 = x2, x1

for digit in range(0,10):
    Summ = 0
    for i in range(x1,x2+1):
        x = i
       
        while x != 0:
            last = x % 10
            x = x // 10

            if last == digit:
                Summ+=1
    print(f"Для цифры {digit} частота использования {Summ}")
    Summ = 0

