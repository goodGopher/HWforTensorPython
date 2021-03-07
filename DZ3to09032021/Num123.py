#Определить, является ли введенное число простым
#Нахождение наибольшего общего делителя
#Нахождение наименьшего общего кратного

def NOD(x,y):
    print("Nod")
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


def NOK(x,y):
    print("NOK")
    return x * y / NOD(x,y)

def IsSimple(x):
    print("Is num simple?")
    check = 1
    
    if x == 2:
        return 1
    elif x == 4:
        return 0
    else:
        for i in range(2, x//2+1):
            if x % i == 0:
                check = 0
                break
        if check  :
            return 1
        else:
            return 0
        

print(NOD(32,24))
print(NOK(32,24))
IsSimple(4)
print(101//2)

for m in range(1,160):
    print(m,IsSimple(m))
