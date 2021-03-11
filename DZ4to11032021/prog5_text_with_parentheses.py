#Водится текст, 
#содержащий различные скобки, необходимо определить,
#все ли скобки расставлены корректно 
   
def text_check2(text):
    left_list = []
    right_list = []
    for i in range(0,len(text)):
        if text[i] == "{" or text[i] == "(" or text[i] == "[" :
            left_list.append(text[i])
        if text[i] == "}" or text[i] == ")" or text[i] == "]" :
            if len(left_list) == 0:
                print("скобки расставлены некорректно\n")
                return 
            res = left_list.pop()+text[i]
            if res != "{}" and res != "()" and res != "[]":
                print("скобки расставлены некорректно\n")
                return 
    if len(left_list) != 0 :
        print("скобки расставлены некорректно\n")
        return
    print("все скобки расставлены корректно\n")


print("Для выхода введите пустую строку.\nВведите текст:")
text = input()
while text:
    text_check2(text)
    print("Для выхода введите пустую строку.\nВведите текст:")
    text = input()


