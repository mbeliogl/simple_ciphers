
import sys


# using caesar cipher to encrypy a string 
def caesarEncrypt(plainText, numShift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    key = []
    cipherText = ''
    plainText = plainText.lower()
    
# the for loop ensures we are looping around 
    for i in range(len(alphabet)):
        if i + numShift >= 27:
            key.append(alphabet[i + numShift - 27])
        else:
            key.append(alphabet[i+numShift])

# shifting each character n spaces 
    for i in range(len(plainText)):
        cipherText = cipherText + key[alphabet.find(plainText[i])]

    return cipherText

# decrypting the string by reversing the caesarEncrypt() method
def caesarDecrypt(cipherText, numberShift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    key = []
    plainText = ''

    for i in range(len(alphabet)):
        if i + numberShift >= 27:
            key.append(alphabet[i + numberShift - 27])
        else:
            key.append(alphabet[i + numberShift])

    for i in range(len(cipherText)):
        plainText = plainText + alphabet[key.index(cipherText[i])]

    return plainText

# breaking using brute force approach 
def caesarBreak(cipherText):
    guess = 1
    for i in range(27):
        print('Guess ' + str(guess) + ': ' +  caesarDecrypt(cipherText, i))
        guess = guess + 1


# driver     
def main():

    task_list = ['encrypt', 'decrypt', 'break']
    task = input(f"Please choose the task type {task_list} : ")

    if task == task_list[0]:
        msg = input("Enter the string to encrypt: ")
        key = int(input("Enter the key (how many letters to shift): "))
        key = key % 27

        encrypted_msg = caesarEncrypt(msg, key)
        print(f"Your encrypted message: {encrypted_msg}")


    if task == task_list[1]:
        msg = input("Enter the string to decrypt: ")
        key = int(input("Enter the key (how many letters to shift): "))
        key = key % 27
        decrypted_msg = caesarDecrypt(msg, key)
        print(f"\nYour encrypted message: {decrypted_msg}")


    if task == task_list[2]:
        msg = input("Enter the string break: ")
        caesarBreak(msg)

main()

