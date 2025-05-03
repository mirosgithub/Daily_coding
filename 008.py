"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """

# Solution
# My attempt: incomplete None child handling, not considering the node itself
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def count_unival(root):
    count = [0]
    
    def traverse(node):
        if node.left is None and node.right is None:
            count[0] += 1
            print(f"both nodes None, add 1 to count")
            return 
        
        if node.left:
            traverse(node.left)
            
        if node.right:
            traverse(node.right)
            
        if node.left.value == node.right.value:
            print(f"equal child nodes, add 1 to count")
            count[0] += 1
            
    traverse(root)
    return count[0]

# Correct Solution:
def count_unival2(root):
    count = [0]
    
    def check_unival(node):
        if node is None:
            return True, None
        
        uni_left, left_val = check_unival(node.left)
        uni_right, right_val = check_unival(node.right)
        
        if uni_left and uni_right:
            if node.left is not None and left_val != node.value:
                return False, node.value
            
            if node.right is not None and right_val != node.value:
                return False, node.value
            
            count[0] += 1
            return True, node.value
        
        return False, node.value
    
    check_unival(root)
    return count[0]
        
        
        
# Tests
tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
print(count_unival2(tree))