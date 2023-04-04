#To find even or odd number

num=int(input("Please enter the number "))
if(num%2==0):
    print("The entered number is even number")
else:
    print("The entered number is odd number")

### To find positive or negative value

num=int(input("Please enter the number "))
if(num>0):
    print("The entered number is positive number")
else:
    print("The entered number is negative number")

#To find the greatest number of two numbers

num=int(input("Please enter the number "))
num1=int(input("Please enter the number "))
if(num>num1):
    print(num,"is the greatest number")
else:
    print(num1,"is the greatest number")

#Attendence

work=int(input("Please enter the number of working days "))
present=int(input("Please enter the number of present days "))
present=(present/work)*100
if (present>=75):
    print("Attendence =",present)
    print("The student is eligible to attend the exam")
else:
    print("Attendence =",present)
    print("The student is not eligible to attend the exam")
