class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

n1=Node('eggs')
n2=Node('ham')
n3=Node('spam')

n1.next=n2
n2.next=n3
current = n1
# while current:
#     print(current.data)
#     current=current.next

def iter(self):
    current = self.head
    while current:
        val=current.data
        current=current.next
        yield val

# for word in words.iter():
#     print(word)

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def append(self,data):
        node = Node(data)
        if self.head is None:
            self.head=node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next = node

words=SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

current = words.head
while current:
    print(current.data)
    current=current.next