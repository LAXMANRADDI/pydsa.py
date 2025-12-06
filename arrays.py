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
|
|        /
|      /
|    /
|  /
|/_______________  n →
```
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


Example 1: Linear Search
Q: Find element = 30 in arr = [10, 20, 30, 40, 50]
Dry Run:
i=0 → arr[0]=10  ≠30  
i=1 → arr[1]=20  ≠30  
i=2 → arr[2]=30  ✓ found

Code:
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

print(linear_search([10,20,30,40], 30))


Example 2: Binary Search
Q: Search 40 in [10, 20, 30, 40, 50, 60]
Dry Run:
low=0, high=5  
mid=2 → arr[2]=30 < 40 → search right
low=3, high=5  
mid=4 → arr[4]=50 > 40 → search left
low=3, high=3  
mid=3 → arr[3]=40 → FOUND
Code:
def binary_search(arr, x):
    low, high = 0, len(arr)-1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


Example 3: First Occurrence of x
arr = [1,2,2,2,3,4], x=2
Dry Run:
mid=2 → arr[2]=2 → ans=2 → move left
mid=0 → arr[0]=1 → move right
mid=1 → arr[1]=2 → ans=1 → move left
END → 1

Code:
def first_occ(arr, x):
    low, high = 0, len(arr)-1
    ans = -1
    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] == x:
            ans = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return ans


Example 4: Count Occurrences
arr = [2,2,2,3,4], x=2
first=0, last=2 → count = 3
count = last_occ(arr,x) - first_occ(arr,x) + 1

 Example 5: Find Peak Element
arr = [1, 3, 20, 4, 1]
Peak = 20
Binary Search-based.

 SORTING 
 Example 1: Bubble Sort
Sort:
arr = [5, 1, 4, 2]
Dry Run:
Pass 1: [1,4,2,5]
Pass 2: [1,2,4,5]
Pass 3: [1,2,4,5]

Code:
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

Example 2: Selection Sort
arr = [64, 25, 12, 22, 11]
Dry Run:
Pick min: 11 → swap with 64
Pick min: 12
Pick min: 22
...
Sorted = [11,12,22,25,64]

Code:
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_i=i
        for j in range(i+1,n):
            if arr[j] < arr[min_i]:
                min_i=j
        arr[i],arr[min_i]=arr[min_i],arr[i]
    return arr

 Example 3: Insertion Sort
arr = [5, 2, 4, 6, 1]
Dry Run:
2 inserts before 5 → [2,5,4,6,1]
4 inserts between 2 and 5 → [2,4,5,6,1]
1 goes to start → [1,2,4,5,6]

Code:
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

Example 4: Merge Sort
arr = [38,27,43,3,9,82,10]
Merge sort splits:

[38,27,43,3]  |  [9,82,10]
[38,27] [43,3] | [9,82] [10]
...
Final sorted = [3,9,10,27,38,43,82]

Code:
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i=j=0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

Example 5: Quick Sort
arr = [10, 7, 8, 9, 1, 5]
pivot = 5
→ small: [1]
→ big: [10,7,8,9]

Code:
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
