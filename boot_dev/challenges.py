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
number_sum(n)

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
