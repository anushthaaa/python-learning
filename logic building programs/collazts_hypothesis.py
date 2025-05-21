# Write a program which reads one natural number and 
# executes the above steps as long as c0 remains different from 1. 
# We also want you to count the steps needed to achieve the goal.
# Your code should output all the intermediate values of c0, too.

c0 = int(input("Enter a natural number: "))
count = 0

if c0 > 0:
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 // 2
        elif c0 % 2 != 0:
            c0 = 3 * c0 + 1
        print(c0)
        count += 1

print("No. of steps: ", count)
