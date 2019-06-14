import sys
from cs50 import get_string

# get key from user
if len(sys.argv) != 2:
    print("Usage: python caesar.py k")
    sys.exit(1)

# get plain text from user
k = int(sys.argv[1])
plaintext = get_string("plaintext: ")

#print "ciphertext: "
print("ciphertext: ", end="")

# encrypt the plain text
for c in plaintext:
    if not c.isalpha():
        print(c, end="")
        continue

    ascii_offset = 65 if c.isupper() else 97
    p = ord(c) - ascii_offset
    c = (p + k) % 26

    print(chr(c + ascii_offset), end="")

print()