def create_node(data):
    return {'data': data, 'next': None}
def add_node(head, data):
    new_node = create_node(data)
    if head is None:
        return new_node
    current = head
    while current['next'] is not None:
        current = current['next']
    current['next'] = new_node
    return head
def delete_node(head,key,):
    current = head
    previous = None
    if current is not None and current['data'] == key:
        head = current['next']
        current = None
        return head
    while current is not None and current['data'] != key:
        previous = current
        current = current['next']
    if current is None:
        return head
    previous['next'] = current['next']
    current = None
    return head
def display_list(head):
    current = head
    while current is not None:
        print(current['data'], end=' ')
        current = current['next']
    print()
head = None
head = add_node(head, 1)
head = add_node(head, 2)
head = add_node(head, 3)
print("Original list:")
display_list(head)
head = delete_node(head, 2)
print("List after deleting node with data 2:")
display_list(head)  
