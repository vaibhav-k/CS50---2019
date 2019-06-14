from cs50 import get_string
from sys import argv


def main():
    #check if user typed in valid input
    if(len(argv) != 2 ):
        print("Usage: python bleep.py dictionary")
        return 1

    # get inout string to be censores from user
    msg = get_string("What message would you like to censor?\n")
    msg = msg.split()

    # censor the inout string

    # open list of banned words
    bw = open(argv[1], 'r')
    bw = bw.read()

    # split banned words from dictionary
    bww = bw.split()

    # replace banned words in user input by stars
    bwmsg = []
    for i in msg:
        i = i.lower()
        for w in bww:
            if i == w:
                bwmsg.append('*' * len(w))
            else:
                bwmsg.append(i)

    #print(msg)
    seperator = ' '
    print(seperator.join(bwmsg))


if __name__ == "__main__":
    main()
