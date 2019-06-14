from cs50 import get_float

change = 0

# get the change owed from user
while True:
    change = get_float("Change owed: ")

    if change > 0:
        break

change = change * 100

# coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢)
q = 25
d = 10
n = 5
p = 1

quarters = int(change // 25)
dimes = int((change % 25) // 10)
nickels = int(((change % 25) % 10) // 5)
pennies = int(((change % 25) % 10) % 5)

print(f"{quarters + dimes + nickels + pennies}")