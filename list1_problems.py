#first_last6
list1=[]
range1=int(input("Please enter the list range "))
for i in range (range1):
        user_input=int(input("Please enter the values "))
        list1.append(user_input)
print(list1)
if list1[0]==6 or list1[-1]==6:
        print("True")
else:
        print("False")


#same_first_last
list1=[]
range1=int(input("Please enter the list range "))
for i in range (range1):
        user_input=int(input("Please enter the values "))
        list1.append(user_input)
print(list1)
if list1[0]==list1[-1]:
        print("True")
else:
        print("False")


#common_end
list1=[]
range1=int(input("Please enter the list range "))
for i in range (range1):
        user_input=int(input("Please enter the values "))
        list1.append(user_input)
print(list1)
list2=[]
range2=int(input("Please enter the list range "))
for i in range (range2):
        user_input1=int(input("Please enter the values "))
        list2.append(user_input1)
print(list2)
if list1[0]==list2[0] or list1[-1]==list2[-1]:
        print("True")
else:
        print("False")


#sum3
list1=[]
for i in range (3):
        user_input=int(input("Please enter the values "))
        list1.append(user_input)
print(list1[0]+list1[1]+list1[2])


#rotate3
list1=[]
for i in range (3):
        user_input=int(input("Please enter the values "))
        list1.append(user_input)
list1=list1[1:]+[list1[0]]
print(list1)


#reverse3
list1=[]
for i in range (3):
        user_input=int(input("Please enter the values "))
        list1.append(user_input)
list1.reverse()
print(list1)


#max_end3
list1=[]
for i in range (3):
        user_input=int(input("Please enter the values "))
        list1.append(user_input)
print([list1[0]]*3)
print([list1[2]]*3)
list1=max(list1)
print([list1]*3)


##sum2
list1=[]
range1=int(input("Please enter the list range "))
for i in range (range1):
        user_input=int(input("Please enter the values "))
        list1.append(user_input)
if len(list1)>=2:
        print(list1[0]+list1[1])
elif len(list1)==1:
        print(list1[0])
else:
        print(range1)


##middle_way
list1=[]
for i in range (3):
        user_input=int(input("Please enter the values for first list "))
        list1.append(user_input)
print()
list2=[]
for i in range (3):
        user_input1=int(input("Please enter the values for second list "))
        list2.append(user_input1)
print()
print("The middle element of the two list is ",[list1[1]]+[list2[1]] )


##make_ends
list1=[]
range1=int(input("Please enter the list range "))
for i in range (range1):
        user_input=int(input("Please enter the values "))
        list1.append(user_input)
if list1.count(3) or list1.count(2) in list1:
        print("True")
else:
        print("False")
