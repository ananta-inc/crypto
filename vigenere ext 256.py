# Python code to implement
# Vigenere Cipher

def identifyType():
    tipe = input ('''
Pilih jenis teks:
a. Masukan keyboard
b. File
Pilihan: ''')
    if tipe == 'a':
         string = input("Masukkan teks yang ingin dienkripsi: ")
    elif tipe == 'b':
         string = openText()
    
    return string

# Reading string from txt file
def openText ():
    with open("file.txt") as f:
        content = f.read()
        string = list(content)
            
        return(string)
    f.close()
 
# This function generates the
# key in a cyclic manner until
# it's length isn't equal to
# the length of original text
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(string[i % len(key)])
    return("" . join(key))
     
# This function returns the
# encrypted text generated
# with the help of the key
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 256
        x += ord(' ')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
     
# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 256) % 256
        x += ord(' ')
        orig_text.append(chr(x))
    return("" . join(orig_text))
     
# Driver code
if __name__ == "__main__":
    string = identifyType()
        
    keyword = input ("Masukkan teks kunci: ")
    key = generateKey(string, keyword)
    cipher_text = cipherText(string,key)
    print("Ciphertext :", cipher_text)
    print("Plaintext :",
           originalText(cipher_text, key))
    print("Kunci extended: ", key)
 