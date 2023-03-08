#Name: Loc Nguyen 
#Date: 03/04/2023
#Objective: Implement Vigenere Cipher with 2 keyboard input: plaintext and key

def vignereEncrypt (key, plaintext):
    plaintext=plaintext.lower()
    key=key.lower()
    plaintext=plaintext.replace(' ','')
    keyLength=len(key)
    cipherText=''
    for i in range(len(plaintext)):
        letter = plaintext[i]
        k = key[i % keyLength]
        cipherText = cipherText + chr(((ord(letter) - 97) + (ord(k)-97)) % 26 + 97)
    print("Encrypted text is:",cipherText)
    return cipherText

def main():
    key=input("Please enter the encryption key: ")
    plaintext=input("Please enter the plaintext: ")
    vignereEncrypt(key,plaintext)

main()
