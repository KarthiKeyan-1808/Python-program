#hello_name
a=input("Please enter the name ")
print("Hello ",a,"!")

#make_abba
a=input("Please enter the name ")
b=input("Please enter the name ")
print(a+b+b+a)

#make_tags
a=input("Please enter the name ")
b=input("Please enter the name ")
print("<",a,">",b,"</",a,">")

#make_out_word
a=input("Please enter the name ")
b=input("Please enter the name ")
print(a[:2]+b+a[2:])

#extra_end
a=input("Please enter the name ")
print(a[-2:]+a[-2:]+a[-2:])

#first_two
a=input("Please enter the name ")
print(a[:2])

#first_half
a=input("Please enter the name ")
b=len(a)
c=b/2
print(a[0:int(c)])

#without_end
a=input("Please enter the name ")
print(a[1:-1])

#combo_string
a=input("Please enter the name ")
b=input("Please enter the name ")
c=len(a)
d=len(b)
if c>d:
    print(b+a+b)
else:
    print(a+b+a)

#non_start
a=input("Please enter the name ")
b=input("Please enter the name ")
print(a[1:]+b[1:])

#left2
a=input("Please enter the name ")
print(a[2:]+a[:2])
