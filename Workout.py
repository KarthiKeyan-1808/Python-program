#Single inheritance

class Stu():

    def __init__(self,name,age,m1,m2):

        self.name=name

        self.age=age

        self.m1=m1

        self.m2=m2      

class Stu1(Stu):

    def __init__(self,name,age,m1,m2,m3,m4):

        super().__init__(name,age,m1,m2)

        self.m3=m3

        self.m4=m4 

    def display(self):

        print("Student Information")

        print("Name is = ",self.name)

        print("Age is = ",self.age)

        print("Mark1 = ",self.m1)

        print("Mark2 = ",self.m2)

        print("Mark3 = ",self.m3)

        print("Mark4 = ",self.m4)

    def average(self):

        print("Average is = ",(self.m1+self.m2+self.m3+self.m4)/4)

        

obj=Stu1("clement",10,20,30,40,50)

obj.display()

obj.average()

#Multi-Level inheritance

class Stu():

    def __init__(self,name,age):

        self.name=name

        self.age=age

class Stu1(Stu):

    def __init__(self,name,age,m1,m2):

        super().__init__(name,age)

        self.m1=m1

        self.m2=m2    

class Stu2(Stu1):

    def __init__(self,name,age,m1,m2,m3,m4):

        super().__init__(name,age,m1,m2)

        self.m3=m3

        self.m4=m4 

    def display(self):

        print("Student Information")

        print("Name is = ",self.name)

        print("Age is = ",self.age)

        print("Mark1 = ",self.m1)

        print("Mark2 = ",self.m2)

        print("Mark3 = ",self.m3)

        print("Mark4 = ",self.m4)

    def average(self):

        print("Average is = ",(self.m1+self.m2+self.m3+self.m4)/4)       

obj=Stu2("clement",20,51,52,53,54)

obj.display()

obj.average()

#Multiple inheritance

class Stu():

    def __init__(self,name,age):

        self.name=name

        self.age=age

class Stu1():

    def __init__(self,name,age,m1,m2):

        self.m1=m1

        self.m2=m2    

class Stu2(Stu,Stu1):

    def __init__(self,name,age,m1,m2,m3,m4):

        Stu1.__init__(self,name,age,m1,m2)

        Stu.__init__(self,name,age)

        self.m3=m3

        self.m4=m4 

    def display(self):

        print("Student Information")

        print("Name is = ",self.name)

        print("Age is = ",self.age)

        print("Mark1 = ",self.m1)

        print("Mark2 = ",self.m2)

        print("Mark3 = ",self.m3)

        print("Mark4 = ",self.m4)

    def average(self):

        print("Average is = ",(self.m1+self.m2+self.m3+self.m4)/4)       

obj=Stu2("clement",20,51,52,53,54)

obj.display()

obj.average()

##Hierarchical Inheritance

class Stu():

    def __init__(self,name,age,m1,m2,m3,m4):

        self.name=name

        self.age=age

        self.m1=m1

        self.m2=m2

        self.m3=m3

        self.m4=m4 

class Stu1(Stu):

    def __init__(self,name,age,m1,m2,m3,m4):

        super().__init__(name,age,m1,m2,m3,m4)

    def display(self):

        print("Student Information")

        print("Name is = ",self.name)

        print("Age is = ",self.age)

        print("Mark1 = ",self.m1)

        print("Mark2 = ",self.m2)

        print("Mark3 = ",self.m3)

        print("Mark4 = ",self.m4)

class Stu2(Stu):

    def __init__(self,name,age,m1,m2,m3,m4):

        super().__init__(name,age,m1,m2,m3,m4)

    def display(self):

        print("Student Information")

        print("Name is = ",self.name)

        print("Age is = ",self.age)

        print("Mark1 = ",self.m1)

        print("Mark2 = ",self.m2)

        print("Mark3 = ",self.m3)

        print("Mark4 = ",self.m4)       

obj=Stu2("clement",20,51,52,53,54)

obj1=Stu1("raj",20,10,20,30,40)

obj.display()

obj1.display()

#Hybrid Inheritance inheritance

class Stu1():

    def __init__(self,name,age,m1,m2):

        self.name=name

        self.age=age

        self.m1=m1

        self.m2=m2  

class Stu2(Stu1):

    def __init__(self,name,age,m1,m2,m3,m4):

        super().__init__(name,age,m1,m2)

        self.m3=m3

        self.m4=m4 

class Stu3():

    def __init__(self):

        print("Student Information")

class Stu4(Stu2,Stu3):

    def __init__(self,name,age,m1,m2,m3,m4):

        Stu2.__init__(self,name,age,m1,m2,m3,m4)

        Stu3.__init__(self)

    def display(self):

        print("Name is = ",self.name)

        print("Age is = ",self.age)

        print("Mark1 = ",self.m1)

        print("Mark2 = ",self.m2)

        print("Mark3 = ",self.m3)

        print("Mark4 = ",self.m4)

        print("Average is = ",(self.m1+self.m2+self.m3+self.m4)/4)

obj=Stu4("clement",10,20,30,40,50)

obj.display()
