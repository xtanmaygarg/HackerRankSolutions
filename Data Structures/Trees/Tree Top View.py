class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def setLevel(root, level):
    if root == None:
        return
    root.level = level
    setLevel(root.left, level + 1)
    setLevel(root.right, level + 1)

def preOrder(root, horizontalHeight):
    if horizontalHeight not in hashLevel:
        hashTable[horizontalHeight] = root.info
        hashLevel[horizontalHeight] = root.level
    else:
        if hashLevel[horizontalHeight] > root.level:
            hashTable[horizontalHeight] = root.info
            hashLevel[horizontalHeight] = root.level
    if root.left != None:
        preOrder(root.left, horizontalHeight - 1)
    if root.right != None:
        preOrder(root.right, horizontalHeight + 1)

hashTable = dict()
hashLevel = dict()
def topView(root):
    setLevel(root, 0)
    preOrder(root, 0)
    Keys = list(hashTable.keys())
    Keys.sort()
    for key in Keys:
        print(hashTable[key], end = " ")


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
