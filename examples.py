# Multiply all the elements in a list
def multiply_list(l):
    if l[0] == l[-1]:
        return 1
    return l[0] * multiply_list(l[1:])

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
    if l == []:
        return l
    return reverse(l[1:]) + [l[0]]

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if l[0] == i:
        return i
    if l == []:
        return none
    # give the function the new list and the item to find again    
    return find(l[1:],i)

# Determines if a string is a palindrome
def palindrome(some_string):    
    if len(some_string) <= 1:
        return some_string
    
    some_string[0] == some_string[-1]


# Given the width and height of a sheet of paper, and the number of times 
# to fold it, return the final dimensions of the sheet as a tuple. 
# Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return (width, height)

    # for each fold, need to divide the width by 2
    # height stays the same
    # need to count down the folds
    return fold_paper(width / 2.0, height, folds - 1)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    print n
    if n == target:
        return n
    return count_up(target, n+1)
    
#count_up(5,0)

#list = [1,2,3,4]
#print fibonacci(4)  

