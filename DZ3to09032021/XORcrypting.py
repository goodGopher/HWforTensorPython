def decryption(encryptedString,keyWord):
    print("decryption")
    
    decryptedString = []
    j = 0

    for i in range(0,len(encryptedString)):
        char = ord(encryptedString[i]) ^ ord(keyWord[j]) ^ 6
        decryptedString.append(chr(char))
       
        j+=1
        if j == len(keyWord):
            j = 0
      
    return "".join(decryptedString)

def encryption(decryptedString,keyWord):
    print("encryption")

    encryptedString = []
    j = 0

    for i in range(0,len(decryptedString)):
        ordedChar = ord(decryptedString[i]) ^ ord(keyWord[j]) ^ 6 
        charedChar = chr(ordedChar)  
        encryptedString.append(charedChar)
        
        j+=1
        if j == len(keyWord):
            j = 0
  
    return "".join(encryptedString)



print("введите не зашифрованную строку:")
unCrStr = input()
print("введите ключевое слово:")
keyWord1 = input()
print(print("Зашифрованная строка->",encryption(unCrStr,keyWord1),"<-"))

print("введите  зашифрованную строку:")
CrStr = input()
print("введите ключевое слово:")
keyWord2 = input()
print(print("Расшифрованная строка->",encryption(CrStr,keyWord2),"<-"))

