print("welcome to tip  calculator:")
num_1=int(input("enter the number 1"))
num_2=int(input("enter the number 2"))
ari_operator=input("enter the arithmatic operator you want:")
if ari_operator=="+":
    addition=num_1+num_2
    print(num_1 "+" num_2 "=" ,addition)
elif ari_operator=="-":
    substraction=num_1-num_2
    print(num_1 "-" num_2 "=", substraction)
elif ari_operator=="*":
    multiplication=num_1*num_2
    print(num_1 "*" num_2 "=", multiplication)
elif ari_operator=="/":
    devision=num_1/num_2
    print(num_1 "/" num_2 "=", dervision)
else:
    print("syntax error")

    
    
