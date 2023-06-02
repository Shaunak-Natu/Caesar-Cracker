# What is Caesar Cipher?

The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to his allies. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it with a shift of three (A becoming D when encrypting, and D becoming A when decrypting) to protect messages of military significance. While Caesar's was the first recorded use of this scheme, other substitution ciphers are known to have been used earlier.

Here is an example of how the Caesar cipher works:

Plaintext: HELLO
Ciphertext: IFMMP

To encrypt the message, we start by assigning each letter of the alphabet a number, starting with A = 0 and Z = 25. Then, we shift each letter in the plaintext by the specified number of positions. In this case, we are using a shift of 3, so A becomes D, B becomes E, and so on. The ciphertext is then created by reading off the numbers corresponding to the encrypted letters.

To decrypt the message, we simply reverse the process. We start by assigning each letter of the alphabet a number, starting with A = 0 and Z = 25. Then, we subtract the specified number of positions from each letter in the ciphertext. In this case, we are using a shift of 3, so D becomes A, E becomes B, and so on. The plaintext is then created by reading off the letters corresponding to the decrypted numbers.

## Cracking Caesar Cipher: -

The Caesar cipher is a very simple cipher, and it can be easily broken by a skilled cryptanalyst. Here, I have used a brute-forcing approach. You enter the encrypted message, and the app generates all 25 possible plain text combinations.

## GUI: -
![image](https://github.com/Shaunak-Natu/Caesar-Cracker/assets/78775456/f488279c-9785-43d3-9196-a60db21d3f0d)



