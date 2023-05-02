sen=input("Please enter the word ")
count=0
for i in range(len(sen)):
    if ((sen[i]=="a") or (sen[i]=="e") or (sen[i]=="i") or
        (sen[i]=="o") or (sen[i]=="u") or (sen[i]=="A") or
        (sen[i]=="E") or (sen[i]=="I") or
        (sen[i]=="O") or (sen[i]=="U")):
        count+=1
print("Number of vowels in the sentence is: ", count)

sen=input("Please enter the word ")
list1=sen.split(" ")
print(list1[::-1])
