# Multiply all the elements in a list
def multiply_list(l):
    if l[0] == l[-1]:
        return 1
    return l[0] * multiply_list(l[1:])

list = [1,2,3,4]
print multiply_list(list)

# Return the factorial of n
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
    #n - 1! = n-1 * n-2!

# Count the number of elements in the list l


def count(l):
    if l == []:
        return 0
    return len(l[0]) + count(l[1:])



# Sum all of the elements in a list
def sum_list(l):
    if l[0] == l[-1]:
        return 1
    n + sum_list(l[1:])

# Reverse a list without slicing or loops
def reverse(l):
    pass

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    pass

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    

# Determines if a string is a palindrome
def palindrome(some_string):
    return False

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    return (0, 0)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    return

list = [1,2,3,4]
print count(list)  
