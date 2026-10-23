"""
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
numbers.sort()
print("Sorted numbers:", numbers)
key=int(input("Enter a number to search for: "))
result = binary_search(numbers, key)
if result != -1:
    print(f"element{key}found at {result}")
else:
    print(f"element not found") 
"""
def binary_search(file_path, target):
    with open(file_path, 'r') as file:
        words = file.read().split()
        words.sort()  # Ensure the list is sorted for binary search
        left = 0
        right = len(words) - 1
        steps=0
        print(f"Searching for '{target}' in the file{file_path}")
        print(f"sorted words: {words}")
        while left <= right:
            mid = (left + right) // 2
            steps+=1
            print(f"Step {steps}:range({words[left:right+1]})")
            if words[mid] == target:
                print(f"'{target}' found at index {mid} after {steps} steps.")
                return mid
            elif words[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            print(f"'{target}' not found after {steps} steps.")
            return -1
file_path = '/home/caleb/orv.txt'  # Replace with your file path
target = str(input("Enter a word to search for: "))
result = binary_search(file_path, target)   