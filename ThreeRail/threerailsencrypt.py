
import sys
#the fucntion encrypts a text by adding every 3rd character to strings 1,2,3 in order #
def encrypt(plainText):
    string1 = ''
    string2 = ''
    string3 = ''
    cipherText = ''
# the for loops finds all the values that are 3rd values (divisible by 3) and adds them to the coresponding string depending on the remainder #
    for i in range(len(plainText)):
        if i % 3 == 0:
            string1 = string1 + plainText[i]
        elif i % 3 == 1:
            string2 = string2 + plainText[i]
        elif i % 3 == 2:
            string3 = string3 + plainText[i]
            
    cipherText = cipherText + string1 + string2 + string3

    return cipherText
# the main fucntions applies the encrypt function to the text inside one file and outputs (writes) the result intot another file #
def main():
    in_File = sys.argv[1]
    to_encrypt = open(in_File, 'r')
    encrypted = open("encrypted.txt", 'w')

    for i in to_encrypt:
        i = i.strip('\n')
        encryptedMsg = encrypt(i)
        encrypted.write(encryptedMsg + '\n')

    to_encrypt.close()
    encrypted.close()

main()
