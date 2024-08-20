# 1st Challenge
n = 5
# This is my approuch
def number_sum(n):
    total = 0
    for i in range(1, n):
        total += i
    total= total + n
    print(total)

""" This is the solution code:
def number_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
"""
#number_sum(n)

# 2nd Challenge
def find_min(nums):
    min = float("inf")
    for num in nums:
        while min > num:
            min = num
    print(min)
    return min

# 3rd Challenge
def remove_nonints(nums):
    nonints = []

    for num in nums:
        if type(num) == int:
            nonints.append(num)
    return nonints

# 4rd Challenge
num = 5
def factorial(num):
    total = 0
    if num == 0:
        return 1

    for n in range(num, 0, -1):
        total *= n
    return total

factorial(num)

""" This is the solution provided
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
"""

# 5th Challenge
def area_sum(rectangles):
    total = 0
    area = 0
    for rectangle in rectangles:
        area = rectangle['width'] * rectangle['height']
        total += area

    return total

""" This is the solution provided
def area_sum(rectangles):
    sum = 0

    for rectangle in rectangles:
        sum += rectangle['width'] * rectangle['height']
"""

# 6th Challenge

def fizzbuzz(start, end):
    for i in range(start, end):
        if i % 5 == 0 and i % 3 == 0:
            print ("fizzbuzz")
        elif i % 3 == 0:
            print ("fizz")
        elif i % 5 == 0:
            print ("buzz")
        else:
            print(i)

# Don't Touch Below This Line


def main():
    test(1, 100)
    test(5, 30)
    #test(1, 15)


def test(start, end):
    print("Starting test")
    fizzbuzz(start, end)
    print("======================")


#main()

# 7th Challenge
def divide_list(nums, divisor):
    new_list = []
    for num in nums:
        new_list.append(num / divisor)
    return new_list

# 8th Challenge
strings = ['this', 'list', 'is', 'so', 'important']

def join_strings(strings):
    joined_string = ''
    for string in strings:
        joined_string += string + ","
    joined_string = joined_string.rstrip(',')
    print(joined_string)


""" This is the solution provided
def join_strings(strings):
    joined = ""
    for s in strings:
        joined += s + ","
    if len(joined) != 0:
        joined = joined[:-1]
    return joined
"""
join_strings(strings)
