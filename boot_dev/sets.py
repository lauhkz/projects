new_set = {}

#print(type(new_set))

# Prints: 'Dict'

"""
 Remove duplicates
 Complete the remove_duplicates function. It accepts a list of strings and remove any duplicate values.
 It should utilize and return a set, not a list!
 /it can be write in a single line/
"""

lst = ['basketball', 'football', 'soccer', 'baseball', 'basketball']

def no_duplicates(lst):
    #return set(lst)
    print(set(lst))

#no_duplicates(lst)

"""
  Complete the count_vowels function. It should take a string and return a count of the number of vowels within the
  given string, and a set of its unique vowels.
"""

text = "Building a job-ready portfolio of coding projects does not happen overnight."

def count_vowels(text):
    total = 0
    unique_vowels = set()

    for letter in text:
        print(letter)
        if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U"):
            unique_vowels.add(letter)
            total += 1

    print(unique_vowels)

#count_vowels(text)

first_ids = [1, 1, 1, 2, 2, 2, 3]
second_ids = [1, 2]

# first is my solution
def find_missing_ids(first_ids, second_ids):
    unique_ids = set()

    for id in first_ids:
        if id not in second_ids:
            unique_ids.add(id)

    list_ids = list(unique_ids)

    return list_ids

# shorter and easier solution

def find_missing_ids_shorter(first_ids, second_ids):
    s1 = set(first_ids)
    s2 = set(second_ids)
    return list(s1 - s2)

# Returns 3
