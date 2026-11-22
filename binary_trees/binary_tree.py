class TreeNode:
    def __init__(self,val:int):
        self.val = val
        self.left = None
        self.right = None
    

root = TreeNode(13)
root.left = TreeNode(8)
root.right = TreeNode(18)
root.left.left = TreeNode(5)
root.left.right = TreeNode(10)
root.right.left = TreeNode(15)
root.right.right = TreeNode(21)
"""
      13
  8       18
5  10   15   21  
"""

d2vals = {}

def tprint(root: TreeNode, d2vals, depth):
    print(f'tprint called for {root.val} with depth = {depth}')
    if depth not in d2vals:
        d2vals[depth] = []
    d2vals[depth].append(root.val)
    if root.left is not None:
        tprint(root.left, d2vals, depth+1)
    if root.right is not None:
        tprint(root.right, d2vals, depth+1)


tprint(root,d2vals,0)

print(f'd2vals = {d2vals}')