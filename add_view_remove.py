names = []
while True:
    print("Enter 1 to add name")
    print("Enter 2 to view names")
    print("Enter 3 to remove name")
    print("Enter 4 to exit")

    choice=int(input("Please enter your choice "))

    def add():
        count=int(input("How many names you would like to enter "))
        for i in range(count):
            name=input("Please enter the name: ")
            names.append(name)

    def view():
        print("Names:")
        for i in names:
            print(i)

    def remove():
            name=input("Please enter the name to remove: ")
            if name in names:
              names.remove(name)
            else:
                print("Name not found")

    def exit():
        print("Thanks!")

    def invalid():
        print("Please enter a valid choice")


    if choice==1:
        add()
    if choice==2:
        view()
    if choice==3:
        remove()
    if choice==4:
        exit()
        break
    if choice!=1 or 2 or 3 or 4:
        invalid()
