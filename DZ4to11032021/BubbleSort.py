#Реализовать алгоритм сортировки списка/массива пузырьковым методом
import random 
def out_data(data):
    for i in range(0,len(data)):
        print(f"{data[i]:.0f}", end = " ")
    print()

my_list = []
for i in range(0,20):
    my_list.append(random.random()*1000)
print(f"список :")
out_data(my_list)

for i in range(0,len(my_list)-1):
    for j in range(0,len(my_list)-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j],my_list[j+1] = my_list[j+1],my_list[j]

if sorted(my_list) != my_list:
    print("ERROR")

print(f"отсортированный список :")
out_data(my_list)