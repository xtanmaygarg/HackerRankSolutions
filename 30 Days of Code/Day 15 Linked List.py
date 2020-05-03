class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self, head, data):
        if head:
            Current = head
            New = Node(data)
            while(Current.next):
                Current = Current.next
            Current.next = New
            return head


        else:
            head = Node(data)
            return head

mylist= Solution()
