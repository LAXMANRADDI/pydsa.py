MERGE SORT (Divide & Conquer)
Merge Sort is a **divide and conquer** sorting algorithm.
Idea:
1. Divide the array into two halves
2. Recursively sort both halves
3. Merge the two sorted halves

---
Faster than bubble/selection/insertion
Time complexity **O(n log n)** (best, avg, worst)
Stable sorting algorithm
Uses extra memory
---
3. Merge Sort Flow (Visual)

Example:
```
Array: [38, 27, 43, 3, 9, 82, 10]
Split:
[38,27,43,3]       [9,82,10]
[38,27] [43,3]     [9,82] [10]
[38] [27] [43] [3] [9] [82] [10]

Merge:
[27,38] [3,43]     [9,82]
[3,27,38,43]       [9,10,82]

Final Merge:
[3,9,10,27,38,43,82]
```

4. Merge Sort Algorithm (Steps)
```
mergeSort(arr):
    if length(arr) <= 1:
        return arr
    mid = length(arr) // 2
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)
```

5. Python Code (Very Important)

Merge Function
```python
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
``` 
Merge Sort Function
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
---
6. Dry Run (Small Example)
Array: `[5, 2, 4, 1]`
```
Split → [5,2] [4,1]
Split → [5] [2] [4] [1]

Merge:
[5] & [2] → [2,5]
[4] & [1] → [1,4]

Final:
[2,5] & [1,4] → [1,2,4,5]

---
7. Time & Space Complexity
| Case    | Time       |
| ------- | ---------- |
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   | O(n log n) |
Space Complexity:
➡ O(n) (extra array used)


---
 9. Merge Sort vs Quick Sort
| Merge Sort            | Quick Sort      |
| --------------------- | --------------- |
| O(n log n) always     | Worst O(n²)     |
| Needs extra space     | In-place        |
| Stable                | Not stable      |
| Good for linked lists | Good for arrays |
--
1. **Sorting Large Data (External Sorting)**
Merge sort is used when data **does not fit in main memory (RAM)**.
Data is stored on disk
Small chunks are sorted
Merged efficiently
Used in:
* Database systems
* File systems
* Big data processing
---
2. Sorting Linked Lists
* No random access needed
* Splitting linked list is easy
* Merging is simple (pointer changes)
Quick sort is NOT good for linked lists.
---
3. **Stable Sorting Requirement**
Merge sort is a **stable algorithm**.
Used when:
* Order of equal elements must be preserved
* Sorting records with multiple keys
Example:
Sort students by **marks**, then by **roll number**.
---
4.Used in Inversion Count Problems
Merge sort helps in:
* Counting inversions in an array
* Finding how far an array is from being sorted
Common in competitive programming.
---
5. Used in Divide & Conquer Problems
Merge sort is a base for:
* Closest pair of points
* Finding median of two sorted arrays
* Range query problems
---
6. Used in Multi-core / Parallel Processing
Merge sort can be parallelized easily.
Used in:
* Multi-threaded programs
* Distributed systems
---

7. Used in Databases
* SQL `ORDER BY` (internally uses merge-based techniques)
* Sorting records during joins
---

8. Used When Worst-Case Time Must Be Guaranteed

Merge sort always gives:
O(n log n)
```
No bad cases.
Used in:
* Real-time systems
* Critical applications

Great 👍
Let’s move to the next logical topic after Merge Sort:

🚀 QUICK SORT

This is one of the most important sorting algorithms for exams, interviews, and real systems.


---

✅ 1. What is Quick Sort?

Quick Sort is also a Divide and Conquer algorithm.

Idea:

1. Choose a pivot element


2. Rearrange array so that:

Elements smaller than pivot → left

Elements greater than pivot → right



3. Recursively apply quick sort on left & right parts




---

✅ 2. Why is it called “Quick” Sort?

Very fast in practice

Uses in-place sorting (no extra array)

Average time is O(n log n)


That’s why it’s widely used.


---

✅ 3. Quick Sort Flow (Example)

Array:

[10, 7, 8, 9, 1, 5]

Choose pivot = 5

Left  : [1]
Pivot : 5
Right : [10, 7, 8, 9]

Apply quick sort again on left & right.

Final sorted array:

[1, 5, 7, 8, 9, 10]


---

✅ 4. Algorithm (Steps – Exam Ready)

QuickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        QuickSort(arr, low, p-1)
        QuickSort(arr, p+1, high)


---

✅ 5. Partition Logic (Very Important)

We place pivot at its correct position.

Lomuto Partition (simple)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


---

✅ 6. Quick Sort Code (Complete)

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr)-1)
print(arr)


---

✅ 7. Dry Run (Short)

arr = [4, 2, 6, 9, 2]
pivot = 2

After partition:
[2, 2, 4, 6, 9]

Recursive calls continue.


---

✅ 8. Time & Space Complexity

Case	Time

Best	O(n log n)
Average	O(n log n)
Worst	O(n²) (already sorted array)


Space Complexity:
➡ O(log n) (recursive stack)


---

✅ 9. Merge Sort vs Quick Sort

Merge Sort	Quick Sort

Extra space O(n)	In-place
Always O(n log n)	Worst O(n²)
Stable	Not stable
Good for linked list	Best for arrays



---

✅ 10. Applications of Quick Sort

✔ Used in C / C++ standard libraries
✔ Best for in-memory sorting
✔ Used in system-level programming
✔ Competitive coding favorite
