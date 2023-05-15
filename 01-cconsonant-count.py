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

# def count_check(string):
#     vowels = ["a", "e", "i", "o", "u"]

#     if string == "":
#         return 0
#     if


def const_count(str):
        vowel = 'aeiouAEIOU'
        if str == '':
            return 0
        if str[0].casefold() not in vowel:
            return 1 + const_count(str[1:])
        else:
            return const_count(str[1:])

print(const_count('SpamAndEggs'))

# def consonant_count(str):
#     cons = 0
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for char  in str:
#         if(char not in vowels):
#             cons += 1
#         else: 
#             cons = cons
#     return cons

# print(consonant_count('airplane'))