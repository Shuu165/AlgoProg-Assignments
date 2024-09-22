#Assignment

x = int(input("Enter Number 1:"))
y = int(input("Enter Number 2:"))
z = input("Enter Operator:")

if z == "+":
    Total = x + y
elif z == "-":
    Total = x - y
elif z == "*":
    Total = x * y
elif z == ":":
    Total = x / y
print(Total)

#Session 2 Assignment Morse Code Translator 

MyDict = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    " " : " "
}
sean = list(str.upper(input("WRITE SENTENCE")))
for i in sean:
    print(MyDict[i], end = " ")