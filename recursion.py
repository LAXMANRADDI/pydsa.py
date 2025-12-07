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

Fibonacci Recursion
fib(n) = fib(n-1) + fib(n-2)

Code:
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

Time complexity: O(2ⁿ) → VERY SLOW


--
 Sum of digits using recursion

Question:
Input: 1234
Output: 1+2+3+4 = 10

Code:
def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)


---
 Reverse a String using Recursion

def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]


---
Tower of Hanoi (Most Famous)

Moves n disks from A → C using B.
Moves required = 2ⁿ – 1
def hanoi(n, src, aux, dest):
    if n == 1:
        print(f"Move disk 1 from {src} to {dest}")
        return 
    hanoi(n-1, src, dest, aux)
    print(f"Move disk {n} from {src} to {dest}")
    hanoi(n-1, aux, src, dest)