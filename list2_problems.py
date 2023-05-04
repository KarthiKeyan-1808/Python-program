#count_evens
tup=()
lis1=list(tup)
count=0
lis=int(input("Please enter the range "))
for i in range(lis):
    user=int(input("Please enter the value "))
    lis1.append(user)
for i in lis1:
        if i %2==0:
                count+=1
print("The even number in the entered velue is",count)



#big_diff
tup=()
lis1=list(tup)
lis=int(input("Please enter the range "))
for i in range(lis):
    user=int(input("Please enter the value "))
    lis1.append(user)
max1=lis1[0]                
for i in lis1:
        if i>max1:
                max1=i
##print(max1)
min1=lis1[0]
for i in lis1:
        if i<min1:
                min1=i
##print(min1)
print(max1-min1)


#centered_average
tup=()
lis1=list(tup)
lis=int(input("Please enter the range "))
for i in range(lis):
    user=int(input("Please enter the value "))
    lis1.append(user)
max1=lis1[0]                
for i in lis1:
        if i>max1:
                max1=i
##print(max1)
lis1.remove(max1)
min1=lis1[0]
for i in lis1:
        if i<min1:
                min1=i
##print(min1)
if min1 and min1 in lis1 or min1 in lis1:
                min2=min(lis1)
lis1.remove(min2)
add=sum(lis1)//len(lis1)
print(add)



#sum13
tup=()
lis1=list(tup)
count=0
lis=int(input("Please enter the range "))
for i in range(lis):
    user=int(input("Please enter the value "))
    lis1.append(user)
for i in range (len(lis1)):
        if lis1[i]==13:
                break
        count+=lis1[i]
print(count)


#has22
tup=()
lis1=list(tup)
count=0
lis=int(input("Please enter the range "))
for i in range(lis):
    user=int(input("Please enter the value "))
    lis1.append(user)
for i in range (len(lis1)-1):
        if lis1[i]==2 and lis1[i+1]==2:
                count+=1
if count>0:
        print(True)
else:
        print(False)
