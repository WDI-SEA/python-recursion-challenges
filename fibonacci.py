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

def fib(n):
  # case where number is 0
  if n < 0:
    return 0
  # case where number is the first fibanaccis
  if n == 1 or n == 2:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)

print("it should return 55:", fib(10))
print("it should return 2:", fib(3))
print("it shoucld return 832040:", fib(30))