"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
        
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Solution
# This was my first time working with binary trees
# So I looked up binary tree and preorder traversal algorithm before implementing it
def serialize(root):
    vals = []
    
    def preorder(node):
        if node is None:
            vals.append("None")
            return
        
        vals.append(str(node.val))
        
        preorder(node.left)
        
        preorder(node.right)
    
    preorder(root)
    
    return ",".join(vals)

def deserialize(s):
    vals = s.split(",")
    i = [0]
    
    def reverse_preorder():
        val = vals[i[0]]
        i[0] += 1
        
        if val == "None":
            return None
        
        node = Node(val)
        
        node.left = reverse_preorder()
        
        node.right = reverse_preorder()
        
        return node
    
    return reverse_preorder()

# Test  
node = Node('root', Node('left', Node('left.left')), Node('right'))

serialized = serialize(node)
deserialized = deserialize(serialized)

print(f"Root value: {deserialized.val}")
print(f"Left value: {deserialized.left.left.val}")
print(f"Right value: {deserialized.right.val}")