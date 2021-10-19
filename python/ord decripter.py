# extra credit
a = input("enter the code or letter you want to see the (ord) value for here ")

if a.isdigit():
    a = int(a)
    print("the letter you entered has a (code) of ", chr(a))
else:
    print("the number you entered has a (ord) value of ", ord(a))
input("press enter to end ")
