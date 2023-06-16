Here's an example Python program that uses a while loop to add, view and remove names:

```python
names = []
while True:
    print("Enter 1 to add name")
    print("Enter 2 to view names")
    print("Enter 3 to remove name")
    print("Enter 4 to exit")
    choice = int(input())
    if choice == 1:
        name = input("Enter name: ")
        names.append(name)
    elif choice == 2:
        print("Names:")
        for name in names:
            print(name)
    elif choice == 3:
        name = input("Enter name: ")
        if name in names:
            names.remove(name)
        else:
            print("Name not found")
    elif choice == 4:
        break
    else:
        print("Invalid choice")

```

This program uses an infinite loop (`while True`) and a series of if-elif statements to perform different actions based on the user's input. The user can add a name to the list, view all the names in the list, remove a name from the list, or exit the program.

I hope this helps! Let me know if you have any other questions.

Source: Conversation with Bing, 16/06/2023
(1) How to remove list elements in a for loop in Python?. https://stackoverflow.com/questions/10665591/how-to-remove-list-elements-in-a-for-loop-in-python.
(2) python - creating a list of user input names using loop - Stack Overflow. https://stackoverflow.com/questions/36754307/creating-a-list-of-user-input-names-using-loop.
(3) 18 Python while Loop Examples and Exercises | Pythonista Planet. https://pythonistaplanet.com/python-while-loop-examples/.
(4) Python while Loop (With Examples) - Programiz. https://www.programiz.com/python-programming/while-loop.
