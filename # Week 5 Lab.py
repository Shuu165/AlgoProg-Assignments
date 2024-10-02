# Week 5 Lab
#Circle Class (1)
class Circle:
   def __init__(self, radius, color, pi):
      self.radius = radius
      self.color = color
      self.pi = pi

   def getColor (self):
      return self.color
   
   def getCircum (self):
      return self.radius * 2 * self.pi
   
Circular = Circle(10, "Blue", 3.14)
print(Circular.getColor())
print(Circular.getCircum())


#Player Class (2)
class Player:
   def __init__(self, key, value, health, money, status):
      self.key = key
      self.value = int(value)
      self.health = health
      self.money = money
      self.status = status

   def add(self):
      MyInventory[self.key] = self.value

   def addagain(self):
      MyInventory[self.key] += self.value

   def pop(self):
      MyInventory.pop(self.key)

   def healthdecrease(self):
       self.health -= 1

   def addmoney(self):
       if "Gold Coin" in MyInventory:
           self.money += MyInventory["Gold Coin"]
           MyInventory.pop("Gold Coin")
       else: 
           print("You're Broke")

MyInventory = {}
MyWallet = {}
player = Player("Default", 0, 10, 0, "Healthy")

while True:

    print()
    print(f"Your Health: {player.health}")
    print(f"Your Money: {player.money}")
    print("Your Inventory: ", MyInventory)
    print()

    if player.status == "Poisoned":
        player.healthdecrease()
        print("You are Poisoned! Remove it from your Inventory!")

    if player.health <= 0:
        print("You have DIED!")
        break 

    x = input("Would you like to Add or Remove?")

    if x == "add":
        print("Adding Poison could be Interesting hihi")
        key = input("What would you like to Add?")
        value = int(input("How many?"))
        if key in MyInventory:
            player.key = key 
            player.value = value 
            player.addagain()
        else:
            player.key = key 
            player.value = value 
            player.add()

    elif x == "remove": 
        key = input("What item would you like to remove? : ")
        if key in MyInventory: 
            player.key = key
            player.pop()
        if key == "Poison":
                player.status = "Healthy"
                print("You have removed poison from your inventory!")
        else:
            print(f"{key} is not found in inventory.")

    if "Poison" in MyInventory and MyInventory["Poison"] > 0:
        player.status = "Poisoned"
    else:
        player.status = "Healthy"

    if "Gold Coin" in MyInventory:
        player.addmoney()

#Bank Class (3)
class Bank:
    def __init__(self, account, balance=0.0): #balance=0.0 using float since money isnt always as a whole number
        self.__account = account
        self.__balance = balance # since its a bank, people's accounts and balance should be privated :) (Encapsulation)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount # adds newly input value to old value
            print(f"Deposited {amount}. New balance is {self.__balance}.") # and sum it up
        else:
            print("Weird Amount Naur >:(")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance: # makes it so a valid amount is > 0
            self.__balance -= amount # subtracts new value from old value
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("You're definately Broke..")

    def check(self):
        print(f"{self.__account}'s balance is {self.__balance}.") # just to check up on how bad im broke :)

account = input("Enter the account holder's name: ") #input name :)
initial_balance = float(input(f"Enter {account}'s initial balance: ")) #float cuz same reason to line 104, yay not broke :D

acc = Bank(account, initial_balance) # new acc created :D

while True:

    print()
    print("Welcome to Binus Bank!")
    print("Account: ", account)
    print("Balance: ", initial_balance) # check up 1

    l = input("What would you like to do? (Deposit, Withdraw, Check): ")
    if l == "Deposit":
        amount = float(input("Enter the amount to deposit: "))
        acc.deposit(amount)
    
    elif l == "Withdraw":
        amount = float(input("Enter the amount to withdraw: "))
        acc.withdraw(amount)

    elif l == "Check":
        acc.check()

    elif l == "Exit":
        print("Thanks for Visiting!")
        break