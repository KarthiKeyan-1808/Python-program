##Sum of the numbers in the given list
a=[5,7,4,9]
sum1=0
for i in a:
    sum1+=i
print(sum1)

##Find the maximim and minimum value in the given list
a=[113,52,133,99,125]
b=0
c=0
for i in range(len(a)):
    for j in range(1,len(a)-1):
        if a[j]>a[j+1]:
            b=a[j]
        else:
            c=a[j+1]
if b>c:
    print("The maximum number is ",b)
else:
    print("The maximum number is ",c)
