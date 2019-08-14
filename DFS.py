
# Depth First Search 
# Find the order of the values in the tress traversing through the left child of the node and to the right child


# Time complexity O( v + e) 
# Space complexity O(v) 

# [v : the vertex or the node, e: edges for each node]

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
		array.append(self.name)
		
		for child in self.children:
			child.depthFirstSearch(array)
		
		return array
		


