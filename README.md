# Cipher-Encoder-Decoder

A python application with the use of encrypting and decrypting messages with the following 2 cipher types
- Substitution
- Transposition

## Application features
- The ability to encode and decode file messages with the respective chosen cipher
- Choosing your own custom cipher key ( 26 letter shuffled alphabet in the case of the substitution cipher)

## Running the application
Drop all the files contained in the zip file into a python compiler. Next launch the application based on
"current file" in the config and select either "substitution.py" or "transposition.py". If upon running it, it displays
the "Awaiting commands..." message that means it runs properly, and you can move on to using commands in the terminal.

Available commands:
```python
-k  # used to set the key for the ciphers (for substitution a 26 letter shuffled alphabet must be inputted)
-e  # starts the encryption process
-d  # starts the decryption process
-f  # read the initial input file
-o  # write the output file
```

Both ciphers have been tested in the tests directory. Here is the process for both of them:

### Substitution cipher
```python
python substitution.py -k zyxwvutsrqponmlkjihgfedcba
# set the key

python substitution.py -e -f tests\substitution\input.txt -o tests\substitution\encrypt.txt
# enter encryption mode, read the file input.txt and write the encrypted message in encrypt.txt

python transposition.py -d -f tests\transposition\encrypt.txt -o tests\transposition\decrypt.txt
# enter decryption mode, read the file encrypt.txt and write the decrypted message in decrypt.txt 
```
### Transposition cipher
```python
python transposition.py -k FMI
# start with setting the cipher key
```
Resulting transposition grid:
```bash
F M I
1 3 2
t h i
s   i
s   a
n o t
h e r
  t e
s t
s e n
t e n
c e 
```
```python
python transposition.py -e -f tests\transposition\input.txt -o tests\transposition\encrypt.txt
# enters encryption mode and reads the sentence present in "input.txt" and encrypts it in "encrypt.txt"

python transposition.py -d -f tests\transposition\encrypt.txt -o tests\transposition\decrypt.txt
# enters decryption mode and reads the encrypted message in "encrypt.txt" and returns it to plain text in "decrypt.txt"
```

