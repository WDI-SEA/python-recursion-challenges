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

def str_reverse(s):
    str = ""
    for letter in s:
        str = letter + str
    return str

s = 'Hello World'
print(str_reverse(s))