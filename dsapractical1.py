"""def linear_search(arr,target):
    for index in range(len(arr)):
        if arr[index]==target:
            return index
    return -1
number=[4,5,3,7,2.8]
print(number)
key=int(input("enter the key element"))
result=linear_search(number,key)
if result !=-1:
    print(f"element{key}found at {result}")
else:
    print(f"element not found")

def linear_seacrh(booklist,book):
    book=book.lower()
    for index in range(len(booklist)):
        if booklist[index].lower()==book:
            return index
    return -1
books=["demian","wuthering heights","odyssey"]
print(books)
target=(input("enter your book"))
result=linear_seacrh(books,target)
if result != -1:
    print(f"{target}found at {result}")
else:
    print(f"{target}not found")    
""" 
import random
def linear_search(winning_list,your_number):
    for index in range(len(winning_list)):
        if winning_list[index] == your_number:
            return True
    return False
winning_numbers = random.sample(range(1000, 9999), 10)
print("Winning numbers:", winning_numbers)
your_number = int(input("Enter your 4-digit number: "))
if linear_search(winning_numbers, your_number):
    print("Congratulations! You have won!")
else:
    print("Sorry, better luck next time.")
    