import sys 
import random as rnd 


passSegment = []
upper = []
lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbol = ["!","@","#","$","%","&","*","?"]
numerical = ["0","1","2","3","4","5","6","7","8","9"]

#Converts lower case to upper case and places it in the list
for i in lower:
    count = 0
    upper += i.upper()
    count +=1

#Creates empty string for each segment
pass0 = ""
pass1 = ""
pass2 = ""
pass3 = ""
pass4 = ""
pass5 = ""
pass6 = ""
pass7 = ""
pass8 = ""
pass9 = ""
passSegment = []

#Function to generate a new set of password segments
def Generate(passVar,passSegment):
    #Randomize 4 values between upper and lower case
    for e in range(0,3):
        test = rnd.choice(upper+lower)
        passVar += test
    #Randomize random symbol and add it at the end of PassVar
    test = rnd.choice(symbol)
    passVar += test
    #Randomize random number to add at end of passvar
    test = rnd.choice(numerical)
    passVar += test 
    #Make passVar a list, shuffle it, then join it back into a string
    l = list(passVar)
    rnd.shuffle(l)
    passVar = "".join(l)
    #Append the new passvar into a passsegment list
    passSegment.append(passVar)
    return passVar, passSegment

def Write(passSegment):
    f = open('passgen.txt','w')
    for element in passSegment:
        f.write(element)
        f.write('\n')
    f.close()


Generate(pass0,passSegment)
Generate(pass1,passSegment)
Generate(pass2,passSegment)
Generate(pass3,passSegment)
Generate(pass4,passSegment)
Generate(pass5,passSegment)
Generate(pass6,passSegment)
Generate(pass7,passSegment)
Generate(pass8,passSegment)
Generate(pass9,passSegment)

Write(passSegment)

print(passSegment)

