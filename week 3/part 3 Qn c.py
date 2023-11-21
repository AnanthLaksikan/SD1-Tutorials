cost=int(input("enter the cost of the meal:"))
satisfaction_level=int(input("enter your satisfaction level \n Totally satisfied=1 \n satisfied=2 \n dissatisfied=3:"))
if satisfaction_level=="1":
    bill=cost+(cost*0.20)
    print(f"you choose totally satisfacton level thank you your feed back you have to pay {bill} come again")
elif satisfaction_level==2:
    bill=cost+(cost*0.15)
    print(f"you choose satisfied level thank you your feed back you have {bill} come again")
else:
    bill=cost+(cost*0.10)
    print(f"you choose dissatisfied level thank you your feedback you have to pay {bill} come again")
    
