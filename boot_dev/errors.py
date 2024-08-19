#while True:
    # try:
    #     x = int(input("Please enter a number: "))
    #     break
    # except ValueError:
    #     print("Ops! That's not a valid number. Try again...")

try:
    raise Exception("zero division")
except ZeroDivisionError as e:
    print("zero")

# The program will "crash" with the ZeroDivisionError exception uncaughted

try:
    raise Exception("zero division")
except ZeroDivisionError as e:
    print("zero")
except Exception as e:
    print("other")

# This will print 'other'

try:
        10/0
except ZeroDivisionError:
        print("0 division")
except Exception as e:
        print(e)

try:
        nums = [0, 1]
        print(nums[2])
except IndexError:
        print("index error")
except Exception as e:
        print(e)
