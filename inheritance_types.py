#Single inheritance

class Stu():
    def __init__(self,name,age,dpt):
        self.name=name
        self.age=age
        self.dpt=dpt 

class Stu1(Stu):
    def __init__(self,name,age,dpt,mark1,mark2):
        super().__init__(name,age,dpt)
        self.mark1=mark1
        self.mark2=mark2
    def display(self):
        print("Student Information")
        print(f"Name is: {self.name}")
        print(f"Age is: {self.age}")
        print(f"Mark1: {self.mark1}")
        print(f"Mark2: {self.mark2}")
    def average(self):
        print("Average is = ",(self.mark1+self.mark2)/2)

obj=Stu1("Karthi",28,"Mat",80,85)
obj.display()
obj.average()



#multiple inheritance

class Stu():
    def __init__(self,name,age,dpt):
        self.name=name
        self.age=age
        self.dpt=dpt 

class Stu1():
    def __init__(self,mark1,mark2):
        self.mark1=mark1
        self.mark2=mark2

class Avg(Stu,Stu1):
    def __init__(self,name,age,dpt,mark1,mark2,avg):
        Stu.__init__(self,name,age,dpt)
        Stu1.__init__(self,mark1,mark2)
        self.avg=avg
    def display(self):
        print("Student Information")
        print(f"Name is: {self.name}")
        print(f"Age is: {self.age}")
        print(f"Mark1: {self.mark1}")
        print(f"Mark2: {self.mark2}")
    def average(self):
        print("Average is = ",(self.mark1+self.mark2)/2)

obj=Avg("Karthi",28,"Mat",80,85,"avg")
obj.display()
obj.average()



#multilevel inheritance

class Stu():
    def __init__(self,name,age,dpt):
        self.name=name
        self.age=age
        self.dpt=dpt 

class Stu1(Stu):
    def __init__(self,name,age,dpt,mark1,mark2):
        super().__init__(name,age,dpt)
        self.mark1=mark1
        self.mark2=mark2

class Avg(Stu1):
    def __init__(self,name,age,dpt,mark1,mark2,avg):
        super().__init__(name,age,dpt,mark1,mark2)
        self.avg=avg
    def display(self):
        print("Student Information")
        print(f"Name is: {self.name}")
        print(f"Age is: {self.age}")
        print(f"Mark1: {self.mark1}")
        print(f"Mark2: {self.mark2}")
    def average(self):
        print("Average is = ",(self.mark1+self.mark2)/2)

obj=Avg("Karthi",28,"Mat",80,85,"avg")
obj.display()
obj.average()



#hierarchical inheritance

class Stu():
    def __init__(self,name,age,dpt,mark1,mark2):
        self.name=name
        self.age=age
        self.dpt=dpt
        self.mark1=mark1
        self.mark2=mark2

class Stu1(Stu):
    def __init__(self,name,age,dpt,mark1,mark2):
        super().__init__(name,age,dpt,mark1,mark2)
    def display(self):
        print(f"Student info: \nName: {self.name}\nAge: {self.age}\nDpt: {self.dpt}\nMark: {self.mark1}\nMark2: {self.mark2}")
    def average(self):
        print("Average is = ",(self.mark1+self.mark2)/2)

class Stu2(Stu):
    def __init__(self,name,age,dpt,mark1,mark2):
        super().__init__(name,age,dpt,mark1,mark2)
    def display(self):
        print(f"Student info: \nName: {self.name}\nAge: {self.age}\nDpt: {self.dpt}\nMark: {self.mark1}\nMark2: {self.mark2}")
    def average(self):
        print("Average is = ",(self.mark1+self.mark2)/2)

obj=Stu1("Karthi",28,"Mat",80,85)
obj.display()
obj.average()
obj=Stu2("Vinoth",29,"Mat",65,74)
obj.display()
obj.average()



#hybrid inheritance

class Stu():
    def __init__(self,name,age,dpt):
        self.name=name
        self.age=age
        self.dpt=dpt

class Stu1(Stu):
    def __init__(self, name, age,dpt, mark1,mark2):
        super().__init__(name, age,dpt)
        self.mark1=mark1
        self.mark2=mark2

class Info():
    def __init__(self):
        print("Student Information")

class Stu2(Stu1,Info):
    def __init__(self, name, age,dpt,mark1,mark2):
        Stu1.__init__(self,name,age,dpt,mark1,mark2)
        Info.__init__(self)
    def display(self):
        print(f"Student info: \nName: {self.name}\nAge: {self.age}\nDpt: {self.dpt}\nMark: {self.mark1}\nMark2: {self.mark2}")
    def average(self):
        print("Average is = ",(self.mark1+self.mark2)/2)

obj=Stu2("Karthi",28,"Mat",80,85)
obj.display()
obj.average()