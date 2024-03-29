# first input
original_message = input("Enter original message: ")
key = input("Enter the key: ")

# checks the key, if key length is not 8 or there's a digit which is duplicate or if the key contains 0 or there's a digit which is bigger than 8: it will return False
def checkKey():
    def checkDuplicate():
        for i in range(0, len(key)): 
            for j in range(i+1, len(key)):
                if(key[i] == key[j]):
                    return True;
    if len(key) != 8:
        print("Your key length is not 8 character long")
        return False
    elif checkDuplicate():
        print("Your key contains duplicate digit")
        return False
    elif '0' in str(key):
        print("Your key contains 0 (Zero)")
    else:
        for digit in key:
            if (int(digit)>8):
                print("There's a digit which is bigger than 8")
                return False
    return True

# a function to convert decimal to binary without b in the representation
def decimalToBinary(digit):
    return bin(digit).replace("b", "")

if checkKey() == True:
    # it converts the characters to ascii values and adding them into a list
    ascii_message = list(original_message.encode('ascii'))

    # from ascii values to binary and putting them into a list
    binary_message = []
    for value in ascii_message:
        binary_message.append(decimalToBinary(value))

    # checks if the length of the word is modulo 8, if not it adds spaces to the end of the word. we'll use it later    
    while len(original_message) % 8 != 0:
        original_message += " "

    # transposition (encryption)
    # creating a list with 0 values in order to change them later according to our key
    secret_message = ['00000000' for binary_element in binary_message]
    decrypted_message = ['00000000' for binary_element in binary_message]
    
    # this loop is for changing every character of our secret_message list, but since [] is immutable we're making it mutable inside this loop
    for i, binary_letter in enumerate(binary_message):
        secret_message[i] = list(secret_message[i])
        for j, binary_value in enumerate(binary_letter):
            secret_message[i][int(key[j])-1]=binary_message[i][j]

    # decryption
    # generating the decryption key
    decryption_key = [key.index(str(i)) + 1 for i in range(1, len(key) + 1)]

    # decrypting the message with the same way that we encrypt
    print(decryption_key)
    for i, binary_letter in enumerate(secret_message):
        decrypted_message[i] = list(decrypted_message[i])
        for j, binary_value in enumerate(binary_letter):
            decrypted_message[i][int(decryption_key[j])-1]=secret_message[i][j]

    # and here we're making sure that the values that we converted to be mutable stick together
    secret_message = [''.join(secret_message[i]) for i in range(len(secret_message))]
    decrypted_message = [''.join(decrypted_message[i]) for i in range(len(decrypted_message))]

    ascii = [chr(int(binary, 2)) for binary in binary_message]
    secret_ascii = [chr(int(binary, 2)) for binary in secret_message]
    decrypted_ascii = [chr(int(binary, 2)) for binary in decrypted_message]

    print("Original key: " + str(key))
    print("Decryption key: " + str(decryption_key))
    print("Original message: " + str(ascii))
    print("Encrypted message: " + str(secret_ascii))
    print("Decrypted message: " + str(decrypted_ascii))
