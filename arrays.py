TIME COMPLXITY :
Time Complexity = How fast an algorithm grows as input size **n** increases.
It does NOT measure seconds.
It measures **growth rate**.

---
Big-O describes the **maximum** time taken as n becomes very large.

Common complexities:
 Big-O           Name         Fast?                  
 **O(1)**        Constant      Fastest              
 **O(log n)**    Logarithmic  Very fast              
 **O(n)**        Linear       Normal
 **O(n log n)**  Log-linear  Slower                 
 **O(n²)**       Quadratic   Slow                   
 **O(2ⁿ)**      Exponential  Very slow              
 **O(n!)**       Factorial     Impossible for big n 

---

Time grows directly with size.


for x in arr:
    print(x)
Diagram:


|
|      /
|     /
|    /
|___/_________  n →



Nested loops.

```python
for i in arr:
    for j in arr:
        print(i, j)
```

Diagram:

```
|
|        /
|      /
|    /
|  /
|/_______________  n →
```

---

Divide input into 2 each time.
Example: **Binary Search**.


while low <= high:
    mid = (low + high) // 2


Diagram:


|
|   __
|  /
| /
|/______________  n →






Most sorting algorithms (MergeSort, QuickSort average).
```
merge_sort(arr)


📈 Diagram:

```
|
|     /_
|    / /
|   / /
|__/ /__________ n →
```

---


Operation              Time               

 Access array element  **O(1)**           
 Linear Search          **O(n)**          
 Binary Search          **O(log n)**       
 Nested loops           **O(n²)**          
 Merge Sort             **O(n log n)**     
 Append in Python list  **O(1) amortized** 
 Insert in middle        *O(n)**           

AAAAAAAAAAAARRRRRRRRRRRRRRRRRRRRRRRRRRRAAAAAAAAAAAAAAAAAAAAYYYYYYYYYYYYYSSSSSSSSSSSSSSSSS  :

Array :An array is a continuous block of memory holding elements of the same type.
i.e
Index:   0   1   2   3   4
Value:  10  20  30  40  50
In low-level languages (C/C++), arrays have fixed size.
In Python, arrays are implemented using lists (dynamic arrays).

1]Creating Arrays (Lists) in Python
arr = [10, 20, 30, 40]
print(arr) # [10, 20 , 30 , 40]

2] Access
print(arr[0])   # 10
print(arr[2])   # 30

2.2] Update
arr[1] = 200
print(arr)   # [10, 200, 30, 40]

2.3] Insert
At end → append()
arr.append(50)
At specific index → insert()
arr.insert(2, 999)

2.4] Delete
delete by index
del arr[3]
delete by value
arr.remove(30)
delete last
arr.pop()

 3]. Array Traversal
Going through each element.
arr = [10,20,30,40]
for x in arr:
    print(x)

4].  Linear Search (O(n))
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(linear_search([10,20,30,40], 30))  # 2


SEARCHING TECHNIQUES:

1. Linear Search (O(n))

Check every element until you find the target.
i.e
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

Example:

linear_search([10, 20, 30, 40], 30)
# Output: 2


---
2. Binary Search (O(log n)) — Very Important
 Works only on a SORTED array
Divide the array into half every step.

Diagram:

[10 20 30 40 50 60]
  L     M       R
---
Binary Search Code (Iterative)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
