
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for exercise and 2 for food "))
        if c==1:
            value = input("Type here ")
            with open ("Harry-ex.txt","a") as op:
                op.write(str([str(gettime())]) + value + "\n")
            print("sucesfully written ")
        elif c==2:
            value = input("Type here ")
            with open ("Harry-food.txt","a") as op:
                op.write(str([str(gettime())]) +value +"\n")
            print("Succesfully written")
    elif k==2:
        c=int(input("Enter 1 for exercise and 2 for food "))
        if c==1:
            value = input("Type here ")
            with open ("Carry-ex.txt","a") as op:
                op.write(str([str(gettime())]) + value + "\n")
            print("sucesfully written ")
        elif c==2:
            value = input("Type here ")
            with open ("Carry-food.txt","a") as op:
                op.write(str([str(gettime())]) +value +"\n")
            print("Succesfully written")
    elif k==3:
        c=int(input("Enter 1 for exercise and 2 for food "))
        if c==1:
            value = input("Type here ")
            with open ("Hammad-ex.txt","a") as op:
                op.write(str([str(gettime())]) + value + "\n")
            print("sucesfully written ")
        elif c==2:
            value = input("Type here ")
            with open ("Hammad-food.txt","a") as op:
                op.write(str([str(gettime())]) +value +"\n")
            print("Succesfully written")
    else:
        print("Invalid input")
def retrieve(k):
    if k==1:
        c= int(input("Enter 1 for exercise and 2 for food "))
        if c==1:
            with open ("Harry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open ("Harry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k==2:
        c= int(input("Enter 1 for exercise and 2 for food "))
        if c==1:
            with open ("Carry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open ("Carry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k==3:
        c= int(input("Enter 1 for exercise and 2 for food "))
        if c==1:
            with open ("Hammad-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open ("Hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Invalid input")
while(True):
    print("Health management system")
    a = int(input("Enter 1 for lock the value and 2 for retrieve the value 3 for exit "))
    if a== 1:
        b=int(input("Enter 1 for Harry and 2 for Carry and 3 for Hammad "))
        take(b)
    elif a==3:
        break
    else:
        b= int(input("Enter 1 for Harry and 2 for Carry and 3 for Hammad "))
        retrieve(b)