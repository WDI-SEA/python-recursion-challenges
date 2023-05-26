'''
Write a recursive function called reverse that accepts a string and returns a reversed string.

Examples:

input: "computer"
output: "retupmoc"

input: "ab"
output: "ba"

input: "abcdefghijklmnopqrstuvwxyz"
output: "zyxwvutsrqponmlkjihgfedcba"
'''

def reverse(string):
    if len(string) <= 1:
        return string
    else:
        print(string)
        return reverse(string[1:]) + string[0]
    
print(reverse("hello world"))