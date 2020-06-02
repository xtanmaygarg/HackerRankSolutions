""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def helper(root, minVal, maxVal):
    if root == None:
        return True
    #print(root.data, minVal, maxVal)
    Num = root.data
    if Num > minVal and Num < maxVal:
        Left = helper(root.left, minVal, Num)
        Right = helper(root.right, Num, maxVal)
        return Left and Right
    else:
        return False

def check_binary_search_tree_(root):
    minVal = -10
    maxVal = 10e15
    return helper(root, minVal, maxVal)
