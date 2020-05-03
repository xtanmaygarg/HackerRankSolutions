import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        L = 1
        i = 0
        Queue = [root]
        while(i < L):
            Current = Queue[i]
            print(Current.data, end = " ")
            if Current.left and Current.right:
                Queue.append(Current.left)
                Queue.append(Current.right)
                L += 2
            elif Current.left:
                Queue.append(Current.left)
                L += 1
            elif Current.right:
                Queue.append(Current.right)
                L += 1
            else:
                pass
            i += 1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
