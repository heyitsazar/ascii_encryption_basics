# ASCII Encryption

This Python script allows users to encrypt a message using a simple ASCII encryption technique. It prompts the user to input an original message and a key. The key is used to encrypt the message.

## Usage

1. Run the script.
2. Enter the original message when prompted.
3. Enter a key of exactly 8 characters when prompted.

## Key Validation

The script checks the validity of the key before proceeding with encryption. The key must meet the following criteria:

- The length of the key must be exactly 8 characters.
- The key must not contain duplicate digits.
- The key must not contain the digit '0' (zero).
- Each digit in the key must be between '1' and '8'.

If any of these conditions are not met, the script will display an appropriate error message and terminate.

## Encryption Process

1. The original message is converted into ASCII values.
2. Each ASCII value is converted into an 8-bit binary representation.
3. If the length of the original message is not divisible by 8, spaces are added to the end of the message.
4. Transposition encryption is performed based on the provided key:
   - The binary bits of each character are rearranged according to the positions specified by the key.
5. The encrypted message is converted back to ASCII values.
6. Both the original and encrypted messages are displayed.

## Example

### Input
```python
Enter original message: Hello
Enter the key: 12345678
```

### Output
```python
Original message: ['H', 'e', 'l', 'l', 'o']
Encrypted message: ['\x02', '\x08', '\x16', '\x16', '\x1e']
```

## Notes

- This encryption method is basic and not suitable for secure communications.
- The key serves as a permutation sequence to rearrange the bits of the ASCII representation of the message. 
