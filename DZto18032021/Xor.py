
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
    if a in ["1","2"]:
        data = [['input_for_encryption.txt', 'outfile_for_encryption.txt'] ,
            ['r','rb'],
            ['utf-8',None],
            ['outfile_for_encryption.txt','outfile_for_decryption.txt'],
            ['wb','wb']]
        b = int(a) - 1
        with  open(data[0][b], data[1][b],encoding=data[2][b]) as readed, open(data[3][b], data[4][b]) as writed:
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
