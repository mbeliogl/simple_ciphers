
import sys


def decrypt(cipherText):
    plainText = ''

    lengthOfString1 = len(cipherText) // 3
    lengthOfString2 = len(cipherText) // 3
    lengthOfString3 = len(cipherText) // 3

    string1value = 0
    string2value = 0
    string3value = 0

    if len(cipherText) % 3 == 1:
        lengthOfString1 = lengthOfString1 + 1
    if len(cipherText) % 3 == 2:
        lengthOfString1 = lengthOfString1 + 1
        lengthOfString2 = lengthOfString2 + 1

# dividing into 3 parts 
    rail1 = cipherText[:lengthOfString1]
    rail2 = cipherText[lengthOfString1:lengthOfString1 + lengthOfString2]
    rail3 = cipherText[lengthOfString1 + lengthOfString2:lengthOfString1 + lengthOfString2 + lengthOfString3]

# adding the characters into appropriate strings 
    for i in range(len(cipherText)):
        if i % 3 == 0:
            plainText = plainText + rail1[string1value]
            string1value = string1value + 1
        if i % 3 == 1:
            plainText = plainText + rail2[string2value]
            string2value = string2value + 1
        if i % 3 == 2:
            plainText = plainText + rail3[string3value]
            string3value = string3value + 1

    return plainText 



# driver
def main():
    in_File = sys.argv[1]

    to_decrypt = open(in_File, 'r')
    decrypted = open("decrypted.txt", 'w')

    for i in to_decrypt:
        i = i.strip('\n')
        plainText = decrypt(i)

        decrypted.write(plainText + '\n')

    to_decrypt.close()
    decrypted.close()

main()
