Recursion is used in linked lists, trees, backtracking, DP, quicksort, mergesort, etc.

function calling itself until a stopping condition.
ex:
def fun():
    fun() #This will run forever →  infinite recursion.

amd Every recursive function must have:
Base Case → stopping condition
Recursive Case → function calling itself


Example: Print numbers 1 to n
Code:
def print_nums(n):
    if n == 0:
        return
    print_nums(n-1)
    print(n)

Dry-run for n = 3:
print_nums(3)
→ print_nums(2)
    → print_nums(1)
        → print_nums(0) stops
        → print 1
    → print 2


Factorial using Recursion
n! = n × (n-1)!

Code:
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

Dry-run factorial(4)
4 * factorial(3)
    3 * factorial(2)
        2 * factorial(1)
            1 * factorial(0)