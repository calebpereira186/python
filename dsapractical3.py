"""def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("original array:", arr)
insertion_sort(arr)
print("insertion sort:", arr)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("original array:", arr)
bubble_sort(arr)
print("bubble sort:", arr)
"""
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
arr=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("original array:", arr)
merge_sort(arr)
print("merge sort:", arr)