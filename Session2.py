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