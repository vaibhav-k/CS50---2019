from cs50 import get_int

while True:
    # get height of pyramid from user
    h = get_int("Height:")

    if h <= 8 and h >= 1:
        break

for i in range(h):

    # print spaces
    for j in range(h - i - 1):
        print(" ", end = "")

    # print hashes
    for k in range(i + 1):
        print("#", end = "")

    # print new line
    print()