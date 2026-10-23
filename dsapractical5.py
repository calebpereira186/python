stack=[]    
def push(item):
    stack.append(item)
    print(f"Pushed {item} onto the stack.")
def pop():
    if len(stack) == 0:
        print("Stack is empty. Cannot pop.")
        return None
    else:
        item = stack.pop()
        print(f"Popped {item} from the stack.")
def peek():
    if len(stack) == 0:
        print("Stack is empty. Cannot peek.")
        return None
    else:
        item = stack[-1]
        print(f"Top item in the stack is {item}.")
def is_empty():
    return len(stack) == 0
def display():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Stack contents:", stack)
push(10)
push(20)
push(30)
display()
peek()
pop()
display()
