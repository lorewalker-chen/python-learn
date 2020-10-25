number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
#利用运算符%求余
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
