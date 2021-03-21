"""Errors and rigt(?) versions of code"""

#SyntaxError invalid syntax
# С ошибкой
a = True
if a
    print "not funny error"
# Исправлнный
a = True
if a :
    print ("not funny error")
#----------------------------
# TypeError
# С ошибкой
a1 = 4
a2 = a1 + "5"
# Исправленный
a1 = 4
a2 = "3"
a3 = str(a1) + a2
#----------------------------
#NameError
# С ошибкой
name1 = "John"
name2 = "Janny"
print(name1,name2,name3)
# Исправлнный
name1 = "John"
name2 = "Janny"
name3 = "Иван"
print(name1,name2,name3)
#----------------------------
#UnboundLocalError
# С ошибкой
yourDogSize = 33
if myDogSize > yourDogSize :
    print(myDogSize)
myDogSize = 34
# Исправлнный
myDogSize = 34
yourDogSize = 33
if myDogSize > yourDogSize :
    print(myDogSize)
#----------------------------
#IndentationError
# С ошибкой
n1 = 2
n2 = 3
if (n2 > n1) :
print(n2)
# Исправлнный
n1 = 2
n2 = 3
if (n2 > n1) :
    print(n2)
#----------------------------
#TabError
# С ошибкой
m = 1
if (m < 10):
	m = 10
        print(m)
# Исправлнный
m = 1
if (m < 10):
	m = 10
	print(m)
