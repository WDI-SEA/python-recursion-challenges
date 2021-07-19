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

def count_cosonants(string: str, num: int = 0) -> int:
  # base case -- all letters have been sliced off
  if len(string) == 0:
    return num
  # list of vowels in both upper and lower case
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  # check if next letter is 
  if string[0] not in vowels:
    num = num + 1 
  # cut off first letter in string sicne we checked it 
  string = string[1:]
  # recursively invoke
  return count_cosonants(string, num)

print('it should be 4:', count_cosonants('snakes'))
print('it should be 8:', count_cosonants('SpamAndEggs'))