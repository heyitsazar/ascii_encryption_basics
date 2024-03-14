# ASCII Encryption and Decryption

This Python script performs encryption and decryption of ASCII messages using a transposition cipher. It takes an original message and a key as inputs, encrypts the message, and then decrypts it back using the same key. The encryption process involves converting characters to ASCII values, then to binary, and rearranging them based on the given key. Decryption reverses this process.

## How to Use

1. Clone the repository or download the Python script.
2. Run the script in a Python environment.
3. Follow the prompts to enter the original message and the encryption key.
4. The script will display the original message, the encrypted message, and the decrypted message.

## Key Validation

The script checks the validity of the encryption key according to the following criteria:
- The key must be exactly 8 characters long.
- The key must not contain duplicate digits.
- The key must not contain the digit '0' (zero).
- Each digit in the key must be between 1 and 8 inclusive.

## Encryption Process

1. Convert characters in the original message to ASCII values.
2. Convert ASCII values to binary representation.
3. Rearrange binary digits based on the encryption key using a transposition method.
4. Display the encrypted message.

## Decryption Process

1. Generate the decryption key from the encryption key.
2. Rearrange binary digits of the encrypted message using the decryption key.
3. Convert binary values back to ASCII.
4. Display the decrypted message.

## Note

- This implementation may have bugs that need fixing. Use with caution.
- This method is not considered reliable for encrypting sensitive information and should only be used for educational purposes or with non-sensitive data.

## Example

```
Enter original message: Hello
Enter the key: 21436587

Original key: 21436587
Decryption key: [2, 1, 4, 3, 6, 5, 8, 7]
Original message: ['H', 'e', 'l', 'l', 'o']
Encrypted message: ['\x84', '\x9a', '\x9c', '\x9c', '\x9f']
Decrypted message: ['H', 'e', 'l', 'l', 'o']
```
