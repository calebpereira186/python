"""
def create_set():
    return {10, 20, 30, 40, 50}
def len_set(s):
    return len(s)
def contains(s, element):
    return element in s
def add_element(s, element):
    s.add(element)
    return s
def remove_element(s, element):
    s.remove(element)
    return s
def equals(s1, s2):
    return s1 == s2
def is_subset(s1, s2):
    return s1.issubset(s2)
def union(s1, s2):
    return s1.union(s2)
def intersection(s1, s2):
    return s1.intersection(s2)
def difference(s1, s2):
    return s1.difference(s2)
a=create_set()
b={30, 40, 50, 60, 70}
print("Set A:", a)
print("Set B:", b)
print("Length of Set A:", len_set(a))
print("Does Set A contain 20?", contains(a, 20))
print("Adding 60 to Set A:", add_element(a, 60))
print("Removing 10 from Set A:", remove_element(a, 10))
print("Are Set A and Set B equal?", equals(a, b))
print("Is Set A a subset of Set B?", is_subset(a, b))
print("Union of Set A and Set B:", union(a, b))
print("Intersection of Set A and Set B:", intersection(a, b))
print("Difference of Set A and Set B:", difference(a, b))
"""
import csv
def create(s):
    return s
def symmetric_difference(s1, s2):
    return s1.symmetric_difference(s2)
def length(s):
    return len(s)
def contains(s, element):
    return element in s
def add(s, element):
    s.add(element)
    return s
def remove(s, element):
    s.remove(element)
    return s   
def equals(s1, s2):
    return s1 == s2
def is_subset(s1, s2):
    return s1.issubset(s2)
def union(s1, s2):
    return s1.union(s2)
def intersection(s1, s2):
    return s1.intersection(s2)
def difference(s1, s2):
    return s1.difference(s2) 
def display_set(s, name):
    print(f"{name}:", s)
set1=set()
set2=set()
with open('sets.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        set1.add(int(row["set1"]))
        set2.add(int(row["set2"]))
display_set(set1, "Set 1")
display_set(set2, "Set 2")
add(set1, 100)
remove(set2, 20)
display_set(set1, "Set 1 after adding 100")
display_set(set2, "Set 2 after removing 20")    
print("intersection of Set 1 and Set 2:", intersection(set1, set2))
print("union of Set 1 and Set 2:", union(set1, set2))
print("difference of Set 1 and Set 2:", difference(set1, set2))
print("symmetric difference of Set 1 and Set 2:", symmetric_difference(set1, set2))
