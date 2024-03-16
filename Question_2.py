#Task 1
x = input("Input variable x: ")
y = input("Input variable y: ")
z = input("Input variable z: ")

largest_number = 0

if x > y:
    largest_number = x
elif y > z:
    largest_number = y
else:
    largest_number = z

print(f"The largest number is {largest_number}")

#Task 2
smallest_number = 0

if x < y:
    smallest_number = x
elif y < z:
    smallest_number = y
else:
    smallest_number = z

print(f"The smallest number is {smallest_number}")

#Task 3
if x == y == z:
    print("All numbers are equal")

if x == y:
    print(f"Variables x and y are equal to each other, both being: {x}")

if y == z:
    print(f"Variables y and z are equal to each other, both being: {z}")

if x == z:
    print(f"Variables x and z are equal to each other, both being: {x}")


#For some reason if any number greater than 100 is put in as a variable and the other variables are single/double digits, the largest and smallest numbers flip. Would love some feedback on why that is. Thanks :)