#part 6
#Qn B
try:
    age=int(input("enter your age:"))
    age=int(age)
    if age>=18:
            print("you can vote")
except ValueError:
    print("value error please enter integer value")
