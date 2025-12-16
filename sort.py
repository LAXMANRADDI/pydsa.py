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


