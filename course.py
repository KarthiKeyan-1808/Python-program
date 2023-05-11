#choosing a course

#declearing
dict1={"course":"c++", "course1":"php", "course2":"java", "course3":"python"}
dict2={"c++":10000,"php":12000,"java":14000,"python":16000}

#intro
print("Hi, wellcome to VK Academy. How can i help you?")
cus=input("")# I would like to learn a programming language
print("Sure i will guide you, which cource you want to study")

#checking the availablity and discount if yes
for i in dict1.values():
        cus=input("")#Enterig the specific course
        if cus =="c++":
                print("Fine, we do teach",cus)
                if "c++" in cus:
                        cus=input("") #What is the cost?
                        print("For c++ it's",dict2.get("c++"))
                        cus=input("") #Do you have any "discounts"? 
                        if "discount" in cus:
                                print("Yes, we do 10% discount for c++, you have to pay", int(dict2.get("c++")-(dict2.get("c++")*10/100)),"only")
                                cus=input("")# Fine, i will join c++
                                print("Thank you for choosing c++")
        if cus =="php":
                print("Fine, we do teach",cus)
                if "php" in cus:
                        cus=input("")
                        print("For php it's",dict2.get("php"))
                        cus=input("")
                        if "discount" in cus:
                                print("Yes, we do 12% discount for php, you have to pay", int(dict2.get("php")-(dict2.get("php")*12/100)),"only")
                                cus=input("")
                                print("Thank you for choosing php")
        if cus =="java":
                print("Fine, we do teach",cus)
                if "java" in cus:
                        cus=input("")
                        print("For java it's",dict2.get("java"))
                        cus=input("")
                        if "discount" in cus:
                                print("Yes, we do 14% discount for java, you have to pay", int(dict2.get("java")-(dict2.get("java")*14/100)),"only")
                                cus=input("")
                                print("Thank you for choosing java")
        if cus =="python":
                print("Fine, we do teach",cus)
                if "python" in cus:
                        cus=input("")
                        print("For python it's",dict2.get("python"))
                        cus=input("")
                        if "discount" in cus:
                                print("Yes, we do 16% discount for python, you have to pay", int(dict2.get("python")-(dict2.get("python")*12/100)),"only")
                                cus=input("")
                                print("Thank you for choosing python")
        else:
                print("Sorry, we are currently not operating",cus,"but we do have other courses")
                break
        
#other course details
cus=input("")
for i in dict1:
        print(dict1[i])
print("These are the computer language studies that we are currently operating")

#cost
cus=input("")
for i,j in dict2.items():
        print("for",i,j)
print("What would you like to learn")

#choosing and offer
cus=input("")
if "c++" in cus:
        print("You have to pay",int(dict2.get("c++")-(dict2.get("c++")*10/100)),"for c++, included the discount of 10%")
        cus=input("")# Fine, i will join c++
        print("Thank you for choosing c++")
if "php" in cus:
        print("You have to pay",int(dict2.get("php")-(dict2.get("php")*12/100)),"for php, included the discount of 12%")
        cus=input("")# Fine, i will join php
        print("Thank you for choosing php")
if "java" in cus:
        print("You have to pay",int(dict2.get("java")-(dict2.get("java")*14/100))," for java, included the discount of 14%")
        cus=input("")# Fine, i will join java
        print("Thank you for choosing java")
if "python" in cus:
        print("You have to pay",int(dict2.get("python")-(dict2.get("python")*16/100))," for python, included the discount of 16%")
        cus=input("")# Fine, i will join python
        print("Thank you for choosing python")
