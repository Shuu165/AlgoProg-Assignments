#Its 3 am rn
#Tried to be a bit ambitious and i wanna die

class BinusMaya:
    def __init__(self):
        self.lectures = MyLectures
        self.classes = MyClasses
        self.schedules = MySchedules
    
    def addlec(self):
        name = input("Enter Lecturer Name: ")
        subject = input("Enter Subject: ")
        lecID = input("Enter LecturerID: ")

        for lec in self.lectures:
            if lec["subject"] == subject:
                print(f"A Lecturer has been assigned to this {subject}!")
                return
            
        new_lec = [{"name": name, "subject": subject, "lecID": lecID}]
        self.lectures.append(new_lec)

    def remlec(self): 
        lecID = input("Enter LecturerID to Remove: ")

        for lec in self.lectures:
            if lec["lecID"] == lecID:
                self.lectures.remove(lec)
            return

    def addcla(self):
        cla = input("Enter a Class: ")

        if cla in self.classes:
            print(f"Input denied: Class code {cla} already exists.")
        else:
            self.classes.append(cla)

    def remcla(self):
        cla = input("Enter class code to remove: ")

        if cla in self.classes:
            self.classes.remove(cla)
        else:
            print(f"Class code {cla} not found.")
    
    def sche(self):
        cla = input("Enter Class: ")
        time = input("Enter Time: ")
        subject = input("Enter Subject: ")

        for lec in self.lectures:
            if lec["subject"] == subject:
                schedule = (time, cla, subject, lec["name"])
                self.schedules.append(schedule)
                return
        print(f"No one teaching {subject} at the moment.")

MyLectures = [{"name": "Michael", "subject": "Algorithm Programming", "lecID": "007"}, {"name": "James", "subject": "Chemistry", "lecID": "0309"}, {"name": "Bradley", "subject": "Cooking", "lecID": "0106"}]
MyClasses = ["L1AC", "L1BC", "L1CC"]
MySchedules = []


Site = BinusMaya()

while True:

        print()
        print("Welcome to BinusMaya!")
        print("Your Current Lecturers: ", MyLectures)
        print("Classes Available: ", MyClasses)
        print("Your Schedule Today: ", MySchedules)
        print()

        x = input("What would you like to see? (Lectures, Classes, Schedule, Exit): ")

        if x == "Lectures":
            y = input("What would you like to do? (Add/Remove): ")
            if y == "Add":
                Site.addlec()
            elif y == "Remove":
                Site.remlec()

        elif x == "Classes":
            z = input("What would you like to do? (Add/Remove): ")
            if z == "Add":
                Site.addcla()
            elif y == "Remove":
                Site.remcla()
        
        elif x == "Schedule":
            Site.sche()

        elif x == "Exit":
            print("Thank You for using BinusMaya!")
            break