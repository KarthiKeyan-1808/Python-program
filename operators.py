a=int(input("Please enter the value of A "))
b=int(input("Please enter the value of B "))
c=input("Please enter the oprtator to perform ")
if(c=="+" or c=="-" or c=="/" or c=="*" or c=="%" or c=="//" or c=="**"):
    if(c=="+"):
        print("\nThe addition of A and B is ",(a+b))
    elif(c=="-"):
        print("\nThe subtraction of A and B is ",(a-b))
    elif(c=="/"):
        print("\nThe divison of A and B is ",(a/b))
    elif(c=="*"):
        print("\nThe multiplication of A and B is ",(a*b))
    elif(c=="%"):
        print("\nThe modulus of A and B is ",(a%b))
    elif(c=="//"):
        print("\nThe floor divition of A and B is ",(a//b))
    elif(c=="**"):
        print("\nThe exponent of A and B is ",(a**b))
else:
    print("\nPlease enter a valid operator")
