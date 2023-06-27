# Develop a Python program that calculates the first N values in the Fibonacci sequence, stores 
# the values in a list, and then outputs the list to the IDLE shell.  The Fibonacci numbers are 
# defined by the linear recurrence equation: 
# 𝐹𝑛 =𝐹𝑛−1 +𝐹𝑛−2
#
# User inputs a positive, real integer value ‘N’.  Make sure your code checks that N is 
# greater than 0 and if not, continues to prompt the user until a positive integer is entered for N. 
N = int(input("Please enter a positive integer: "))
while N <= 0:
    N = int(input("Please enter a positive integer: "))
# Compute the first N terms in the Fibonacci sequence using the general convention that 
# the initial Fibonacci term will be 0 followed by 1.  
F = 0
FibonacciList = []
for i in range(N):
    F = FibonacciList[0+i] + FibonacciList[1+i]
    FibonacciList.append(F)
# Store the terms in a list as they are computed. 
# Output the list of Fibonacci numbers to the IDLE shell.
print("The first", N, "Fibonacci numbers are: ", FibonacciList)