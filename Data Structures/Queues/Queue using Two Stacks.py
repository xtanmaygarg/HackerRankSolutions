class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        return self.first[0]
        
    def pop(self):
        self.first.pop(0)
        
    def put(self, value):
        self.first.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = input().split()
    if values[0] == '1':
        queue.put(int(values[1]))
    elif values[0] == '2':
        queue.pop()
    else:
        print(queue.peek())
