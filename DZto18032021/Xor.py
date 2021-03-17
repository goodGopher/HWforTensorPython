
def encryption(decryptedString,keyWord):

    encryptedString = bytearray()
    if type(decryptedString) == str:
        decryptedString = bytearray(decryptedString,"utf-8")
    
    keyWord = bytearray(keyWord,"utf-8")

    for i in range(len(decryptedString)):
        ordedChar = decryptedString[i] ^ keyWord[i%len(keyWord)]
        encryptedString.append(ordedChar)
        
    return encryptedString
   



def menu_grand():
    print(
    """
            MENU
    1 - Шифрование
    2 - Дешифровка
    3 - Выход
    """
    )





while True:
    menu_grand()
    a = input()
    if a == "1":
        with open('input_for_encryption.txt', 'r', encoding='utf-8') as readed,open('outfile_for_encryption.txt', 'wb') as writed:
            print("Введите ключ:",end="")
            key = input()
            if key :
                writed.write(encryption(readed.read(),key))
 
            else:
                print("Введите ключ")
                continue
    elif a == "2":
        with open('outfile_for_encryption.txt', 'rb') as readed,open('outfile_for_decryption.txt', 'wb') as writed:
            print("Введите ключ:",end="")
            key = input()
            if key :
                writed.write(encryption(readed.read(),key))
            else:
                print("Введите ключ")
                continue
 

    elif a == "3":
        print("Выход из программы")
        exit()
    else:
        print("Вы ввели что-то не то")
