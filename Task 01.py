import random
num_of_rolls=int(input("Enter the number of rolls: "))
total_sum=0
for i in range(num_of_rolls):
    Random_Number= random.randint(1,6)
    total_sum+=Random_Number
print("The sum of all numbers is: ",total_sum)


