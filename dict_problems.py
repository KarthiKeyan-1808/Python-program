##Student mark
student={}
length=int(input("Please enter the length"))
for i in range (length):
    name=input("Please enter the name")
    mark=int(input("Please enter the mark"))
    if mark>35:
        student[name]=mark
print(student)


##Two list to dictionary
dict1={}
l1=[1,3,7]
l2=[10,2,8]
for i in range(len(l1)):
    keys=l1[i]
    dict1[keys]=l2[i]
print(dict1)


##Counting numbers
dict1={}
list1=[1,1,1,2,2,3,7,3,3,8,7]
count=0
for i in range(len(list1)):
        keys=list1[i]
        count=list1.count(list1[i])
        dict1[keys]=count
print(dict1)


##vovels
user=input("Please enter the word")
dict1={}
count=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
for i in range(len(user)):
        key="a"
        if user[i]==key:
                count+=1
        dict1[key]=count
        key="A"
        if user[i]==key:
                count1+=1
        dict1[key]=count1
        key="e"
        if user[i]==key:
                count2+=1
        dict1[key]=count2
        key="E"
        if user[i]==key:
                count3+=1
        dict1[key]=count3
        key="i"
        if user[i]==key:
                count4+=1
        dict1[key]=count4
        key="I"
        if user[i]==key:
                count5+=1
        dict1[key]=count5
        key="o"
        if user[i]==key:
                count6+=1
        dict1[key]=count6
        key="O"
        if user[i]==key:
                count7+=1
        dict1[key]=count7
        key="u"
        if user[i]==key:
                count8+=1
        dict1[key]=count8
        key="U"
        if user[i]==key:
                count9+=1
        dict1[key]=count9
print(dict1)
