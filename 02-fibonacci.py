'''
The Fibonacci Sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.

Read more about it:

https://www.mathsisfun.com/numbers/fibonacci-sequence.html

Write a recursive function called fib that accepts a number N greater than zero and returns the Nth fibonacci number

Examples:

input: 10
output: 55

input: 3
output: 2

input: 30
output: 832040
'''

def fibbonacci(n):
    #base case is n == 1 or2
    if n == 1 or n == 2:
        return 1
    else:
        return fibbonacci(n - 1) + fibbonacci(n - 2)
    
print(fibbonacci(30))