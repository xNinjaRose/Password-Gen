import sys

with open("passgen.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

f.close()

print (content)

while True:
    choiceA = input("Would you want to access a random password: (Y/N) ")
    if choiceA == "Y" or choiceA == "y":
        print ("Enter your 4 Digit pin: ")
        a = input("Enter First Value: ")
        b = input("Enter Second Value: ")
        c = input("Enter Third Value: ")
        d = input("Enter Fourth value: ")
        try: 
            print (content[int(a)] + content[int(b)] + content[int(c)] + content[int(d)]) 
        except IndexError:
            print ("Values can only be from 0 through 9! Please try again")
    elif choiceA == "N" or choiceA == "n":
        print("Shutting down......")
        sys.exit()
