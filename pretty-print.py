'''
Write a function called pretty_print that accepts a complex dictionary and prints out all of it's keys and all of its values. 
The dictionary can have dictionaries nested inside of it.

HOW TO:

Make the function accept two parameters: pretty_print(dictionary, indent).
* dictionary is the dictionary that's currently being iterated over.
* indent is a string representing the current level of indentation.

Whenever you make a recursive call increase the level of indentation by adding two spaces to indent:

It's useful to know how to detect if an object is an instance of a specific class in Python. 
Use the isinstance method to see if a value is an instance of a certain class.

Examples:

dicts:
o1 = {"a": 1, "b": 2}
o2 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero"}, "d": 4}

pretty_print(o1, "")
a: 1
b: 2

pretty_print(o2, "")
a: 1
b: 2
c:
  name: Bruce Wayne
  occupation: Hero
d: 4
'''

# use these for testing
o1 = {"a": 1, "b": 2}
o2 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero"}, "d": 4}
o3 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero", "friends": {"spiderman": {"name": "Peter Parker"}, "superman": {"name": "Clark Kent"}}}, "d": 4}

def pretty_print(dictionary, indent="  "):
  # iterate through every key in the dictionary
  for key in dictionary:
    # get the value associated with the key
    val = dictionary[key]
    # check the type of the key to see if it's another dict
    if isinstance(val, dict):
      print(f"{indent}{key}:")
      pretty_print(dictionary[key], indent + indent)
    else:
      # it's the val isn't a dict then just print out they key and val
      print(f"{indent}{key}: {val}")

pretty_print(o1)
pretty_print(o2)
pretty_print(o3)