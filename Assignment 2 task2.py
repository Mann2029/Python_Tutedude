# Task 2

#  Sum of the all the integer numbers from 1 to a given number

n = int(input("Enter a positive integer: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"The sum of all numbers from 1 to {n} is: {total}.")