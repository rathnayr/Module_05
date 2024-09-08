Numbers= []

while True:
    User_Input= input("Enter a number: ")
    if User_Input == "":
        break
    try:
        number = float(User_Input)
        Numbers.append(number)
    except ValueError:
        print("Please enter a valid number")
        continue
    Numbers.sort(reverse=True)
    Five_Greatest_Numbers= Numbers[0:5]
    print("The five greatest numbers in the descending order is :", Five_Greatest_Numbers)
