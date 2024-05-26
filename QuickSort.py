#Internet source / insperation: https://www.programiz.com/dsa/quick-sort

#To sort a[left...right] into ascending order:
#1. If left < right:
#1.1. Partition a[left...right] such that
#a[left...p–1] are all less than or equal to a[p], and
#a[p+1...right] are all greater than or equal to a[p].
#1.2. Sort a[left...p–1] into ascending order.
#1.3. Sort a[p+1...right] into ascending order.
#2. Terminate.

# Test Vars: a = [4,3,4,5,2,3,4,6,8,9,10]  # O(1)

# Test Vars: 
a = ["fox", "cow", "pig", "cat", "rat", "lion", "tiger", "goat", "dog"]  # O(1)
# Test Vars: a = [23, 56, 7, 44, 768, 90, 107, 22, 45, 66, 99, 1, 12]  # O(1)

arr = a  # O(1)

def quick_sort(arr):  # O(n log n)
    if len(arr) <= 1:  # O(1)
        return arr  # O(1)

    pivot = arr[len(arr) // 2]  # O(1) - Choosing a pivot element
    left = [x for x in arr if x < pivot]  # O(n) - Elements smaller than the pivot
    middle = [x for x in arr if x == pivot]  # O(n) - Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # O(n) - Elements greater than the pivot

    return quick_sort(left) + middle + quick_sort(right)  # T(n) = 2T(n/2) + O(n)

print(quick_sort(arr))  # O(n log n)