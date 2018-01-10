import sys
import cs50

if len(sys.argv)!=2:
    print("usage: vigenere.py k, where k is a string.")
    sys.exit(1)
for c in sys.argv[1]:
    if c.isalpha() == False:
        print("the key must be alphabetical characters only.")
        sys.exit(2)

key = sys.argv[1]

print("plaintext: ", end="")
text = cs50.get_string()

print("ciphertext: ", end="")

j=0
m=len(key)

for c in text:
    if key[j].isupper():
        if ord(c) >= 65 and ord(c) <= 90:
            print(chr(((ord(c)-65+ord(key[j])-65)%26)+65), end="")
        elif ord(c) >= 97 and ord(c) <= 122:
            print(chr(((ord(c)-97+ ord(key[j])-65)%26)+97), end="")
        else:
            print(c, end="")
    else:
        if ord(c) >= 65 and ord(c) <= 90:
            print(chr(((ord(c)-65+ord(key[j])-97)%26)+65), end="")
        elif ord(c) >= 97 and ord(c) <= 122:
            print(chr(((ord(c)-97+ ord(key[j])-97)%26)+97), end="")
        else: 
            print(c, end="")
        
    if c.isalpha():
        j = (j+1)% m
    
print("")

sys.exit(0)