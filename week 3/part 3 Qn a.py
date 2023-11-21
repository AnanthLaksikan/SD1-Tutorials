f=int(input("enter the fahrenheit value:"))
c=int(input("enter the celcius value:"))
user_option=int(input("enter your option 1 or 2:"))
if user_option==1:
    print("you choose celcius to ferenheit value")
    ferenheit=(c*1.8)+32
    print(f"ferhenheit value is{ferenheit}")
elif user_option==2:
    print("you choose ferenheit to celcius value")
    celcius=(f-32)/1.8
    print(f"celcius value is{celcius}")
else:
    print("invalid option entered")
