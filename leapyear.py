year=int(input("Please enter the year"))
if(year>3):
    if(year%4==0):
        print("This is a leap year")
    else:
        print("This is not a leap year")
else:
    print("Please enter a valid year")
