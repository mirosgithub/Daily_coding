"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""

# Solution
# It was a huge challenge since I have very little knowledge on linked lists (never heard of XOR linked list before!)
# As Python does not support pointers, I simulated it using Python's object id
# My attempt: missing the functionality of adding nodes to the pointers dictionary, incomplete error handling for index out of bounds in get() method
class Node:
    def __init__(self, value):
        self.value = value
        self.both = 0
        
pointers = {}

def get_pointer(object):
    if object is None:
        return 0
    
    return id(object)

def dereference_pointer(pointer):
    if pointer == 0:
        return None
    
    return pointers.get(pointer)

class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add(self, element):
        node = Node(element)
        
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        
        self.tail.both = self.tail.both ^ get_pointer(node)
        node.both = get_pointer(self.tail)
        self.tail = node
        
    def get(self, index):
        if index < 0:
            return None
        
        prev_pt = 0
        current_node = self.head
        
        for i in range(index):
            next_pt = current_node.both ^ prev_pt
            next_node = dereference_pointer(next_pt)
            
            prev_pt = get_pointer(current_node)
            current_node = next_node
            
        return current_node
    
# Improved Solution:
class XORLinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add(self, element):
        node = Node(element)
        pointers.update({get_pointer(node): node})
        
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        
        self.tail.both = self.tail.both ^ get_pointer(node)
        node.both = get_pointer(self.tail)
        self.tail = node
        
    def get(self, index):
        if index < 0:
            return None
        
        prev_pt = 0
        current_node = self.head
        
        for i in range(index):
            if current_node is self.tail:
                return None
            
            next_pt = current_node.both ^ prev_pt
            next_node = dereference_pointer(next_pt)
            
            prev_pt = get_pointer(current_node)
            current_node = next_node
            
        return current_node
    
# Tests
# Create a new XOR linked list
xor_list = XORLinkedList2()

# Test 1: Empty list
print("Test 1: Empty list")
print(f"Get index 0: {xor_list.get(0)}")  # None

# Test 2: Add single element
print("\nTest 2: Add single element")
xor_list.add("A")
node = xor_list.get(0)
print(f"Get index 0: {node.value if node else None}")  # "A"
print(f"Head value: {xor_list.head.value}")  # "A"
print(f"Tail value: {xor_list.tail.value}")  # "A"

# Test 3: Add multiple elements
print("\nTest 3: Add multiple elements")
xor_list.add("B")
xor_list.add("C")
xor_list.add("D")

node0 = xor_list.get(0)
node1 = xor_list.get(1)
node2 = xor_list.get(2)
node3 = xor_list.get(3)

print(f"Get index 0: {node0.value if node0 else None}")  # "A"
print(f"Get index 1: {node1.value if node1 else None}")  # "B"
print(f"Get index 2: {node2.value if node2 else None}")  # "C" 
print(f"Get index 3: {node3.value if node3 else None}")  # "D"

# Test 4: Negative index
print("\nTest 4: Negative index")
node = xor_list.get(-1)
print(f"Get index -1: {node.value if node else None}")  # None

# Test 5: Out of bounds index
print("\nTest 5: Out of bounds index")
node = xor_list.get(10)
print(f"Get index 10: {node.value if node else None}")  # None

# Test 6: Clear and rebuild list
print("\nTest 6: Clear and rebuild list")
xor_list = XORLinkedList2()  # Create new empty list
xor_list.add(100)
xor_list.add(200)
node0 = xor_list.get(0)
node1 = xor_list.get(1)
print(f"Get index 0: {node0.value if node0 else None}")  # 100
print(f"Get index 1: {node1.value if node1 else None}")  # 200

# Test 7: Verify correct traversal with object identity
print("\nTest 7: Verify object identity during traversal")
xor_list = XORLinkedList2()
xor_list.add("First")
xor_list.add("Second") 
xor_list.add("Third")

# Get objects at each position
first = xor_list.get(0)
second = xor_list.get(1)
third = xor_list.get(2)

# Verify head and tail
print(f"Head is first node: {xor_list.head is first}")  # True
print(f"Tail is third node: {xor_list.tail is third}")  # True

# Print values to verify
print(f"First: {first.value}")   # "First"
print(f"Second: {second.value}") # "Second"
print(f"Third: {third.value}")   # "Third"

# Test 8: Verify XOR operations are working correctly
print("\nTest 8: Verify XOR operations")
xor_list = XORLinkedList2()
xor_list.add("X")
xor_list.add("Y")

# Get nodes
x_node = xor_list.get(0)
y_node = xor_list.get(1)

# The tail (y_node) should have its both field equal to the pointer to x_node
print(f"Y.both == pointer(X): {y_node.both == get_pointer(x_node)}")  # True

# Add a third node
xor_list.add("Z")
z_node = xor_list.get(2)

# Now y_node.both pointer(X) ^ pointer(Z)
expected_both = get_pointer(x_node) ^ get_pointer(z_node)
print(f"Y.both == pointer(X) ^ pointer(Z): {y_node.both == expected_both}")  # True