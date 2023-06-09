class Stu():
    def __init__(self):
        self.name=input("Please enter your name ")
        self.age=int(input("Please enter your age "))
        self.std=int(input("Please enter your standard "))
        self.city=input("Please enter your city ")

    def get(self):
        self.tam=int(input("Please enter your marks in Tamil subject "))
        self.eng=int(input("Please enter your marks in English subject "))
        self.mat=int(input("Please enter your marks in Maths subject "))
        self.sci=int(input("Please enter your marks in Science subject "))
        self.soc=int(input("Please enter your marks in Social subject "))

    def display(self):
        print("\nStudent Information")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Standard: {self.std}")
        print(f"City: {self.city}")
        print("Your average is", (self.tam+self.eng+self.mat+self.sci+self.soc)/5)

obj=Stu()
obj.get()
obj.display()
