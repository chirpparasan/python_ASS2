#TASK 1
num=int(input("Enter the number: "))
if num%2==0:
    print("it is an even number.")
else:
    print("it is an odd number.")
    #TASK 2
    # Program to calculate the sum of numbers from 1 to 50

    total_sum = 0

    for num in range(1, 51):
        total_sum += num  # Add each number to the total sum

    # Display the final sum
    print("The sum of numbers from 1 to 50 is:", total_sum)
