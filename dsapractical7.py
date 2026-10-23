'''from collections import deque
import queue
q = deque()
q.append('A')
q.append('B')
q.append('C')
print(q)
item = q.popleft()
print("Removed item:", item)
print("Queue after removal:", q)
'''
capacity=5
queue=[None]*capacity
front=-1
rear=-1
def enqueue(item):
    global front, rear
    if (rear+1)%capacity==front:
        print("Queue is full")
    else:
        if front==-1:
            front=0
        rear=(rear+1)%capacity
        queue[rear]=item
        print("Enqueued:", item)
def dequeue():
    global front, rear
    if front==-1:
        print("Queue is empty")
    else:
        removed_item=queue[front]
        if front==rear:
            front=-1
        else:
            front=(front+1)%capacity
        print("Dequeued:", removed_item)
def display():
    if front==-1:
        print("Queue is empty")
    else:
        print("Queue elements:")
        i=front
        while True:
            print(queue[i], end=" ")
            if i==rear:
                break
            i=(i+1)%capacity
        print()
enqueue(10)
enqueue(20)
enqueue(30)
display()
dequeue()
display()
enqueue(40)
enqueue(50)
enqueue(60)
display()