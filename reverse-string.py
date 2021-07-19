'''
Write a recursive function called reverse that accepts a string and returns a reversed string.

Examples:

input: "computer"
output: "retupmoc"

input: "ab"
output: "ba"

input: "abcdefghijklmnopqrstuvwxyz"
output: "zyxwvutsrqponmlkjihgfedcba"

input: reverse("computer")
output: "computer"
'''

def reverse(string):
  # base case
  if len(string) == 0:
    return ""
  # slice the last char and put it on the front
  return string[-1] + reverse(string[:-1])

print('it should be "retupmoc"', reverse("computer"))
print('it should be "zyxwvutsrqponmlkjihgfedcba"', reverse("abcdefghijklmnopqrstuvwxyz"))