#part6
#Qn 1
try:
    n=input("give me a number over 100:")
    n=int(n)
    if n<=100:
        print(n,"is a not over 100")
except ValueError:
    print("please enter integer value")
