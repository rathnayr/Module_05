import math
Number= int(input("Enter an integer to check that is a prime number: "))
def is_prime(number):
    if number <= 1:
        return False
    for i in range (2,int(math.sqrt(number))+1):
        if number % i == 0:
            return False

    return True

if is_prime(Number):
    print(f"{Number} is a prime number")
else:
    print(f"{Number} is not a prime number")

