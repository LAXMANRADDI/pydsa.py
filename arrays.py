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
