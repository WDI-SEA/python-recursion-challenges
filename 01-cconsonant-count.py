'''
Write a function that given a string, counts total number of consonants in it. 
A consonant is a English alphabet character that is not vowel (a, e, i, o and u). 
Examples of constants are b, c, d, f, g, ..
input will never have spaces or non letter characters

Examples: 

Input: 'snakes'
Output: 4

Input: 'SpamAndEggs'
Output: 8
'''

def consonant_count_iterative(string):
    current_count = 0
    vowels = "aeiouAEIOU"
    for char in string:
        if char not in vowels:
            current_count += 1
    
    return current_count

def consonant_count_recursive(string, current_count = 0):
    # base case -- string is empty
    if len(string) == 0:
        return current_count
    # logic 
    if string[0] not in "aeiouAEIOU":
        current_count += 1

    print(f"{string}, {current_count}")

    return consonant_count_recursive(string[1:], current_count) 

print(consonant_count_recursive("snakes"))
print(consonant_count_recursive("SpamAndEggs"))

# [index to start slicing at : index to stop slicing at : step for each slice]
string = "spam.jpeg"

print(string[len(string) - 4:])