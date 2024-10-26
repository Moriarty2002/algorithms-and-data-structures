from random import randint as ri

priority_list = []

class Node:
    def __init__(self, key: int) -> None:
        
        priority = ri(1, 100)
        while priority in priority_list:
            priority = ri(1, 100)
        priority_list.append(priority)
        
        self.key = key
        self.priority = priority
        
        self.parent: Node = None
        self.l_child: Node = None
        self.r_child: Node = None
    
    # to keep the code clean, I will not create getter / setter


class Treap:
    
    def __init__(self) -> None:
        self.root = None
    
    def print_treap(self, node: Node = None, level: int = 0):
        if node is None:
            node = self.root  # Start from the root if no node is given

        # Base case: if the node is None, return (stop recursion)
        if node is None:
            return

        # Print right child first (visualizes on the right side)
        if node.r_child is not None:
            self.print_treap(node.r_child, level + 1)
        
        # Print the current node with indentation based on level
        print(' ' * 8 * level + f"-> (Key: {node.key}, Priority: {node.priority})")

        # Print left child next (visualizes on the left side)
        if node.l_child is not None:
            self.print_treap(node.l_child, level + 1)
    
    
    def bst_insert(self, node: Node):        
        pointer_current: Node = self.root
        pointer_next: Node = self.root
        
        while pointer_next is not None:
            pointer_current = pointer_next
            
            if node.key < pointer_current.key:
                pointer_next = pointer_current.l_child
            else:
                pointer_next = pointer_current.r_child
        
        node.parent = pointer_current
        if node.key < pointer_current.key:
            pointer_current.l_child = node
        else:
            pointer_current.r_child = node

    def min_heapify(self, node: Node):
        
        if node.parent is None:
            self.root = node
            return
    
        if node.parent.priority < node.priority:
            return
        
        # start rotations
        
        parent = node.parent
        grandparent = parent.parent
        
        if node.parent.l_child is not None and node.parent.l_child is node:     # right rotation
            
            parent.l_child = node.r_child
            parent.parent = node

            if node.r_child:
                node.r_child.parent = parent
            
            node.r_child = parent
            node.r_child.parent = node
        
        else:                                                                   # left rotation
            parent.r_child = node.l_child
            
            if node.l_child:
                node.l_child.parent = parent
            
            node.l_child = parent
            node.l_child.parent = node
        
        
        node.parent = grandparent
        if grandparent is not None:
            if grandparent.l_child is parent:
                grandparent.l_child = node
            else:
                grandparent.r_child = node
        else: # if the parent was the root
            self.root = node
        
        return self.min_heapify(node)
    
    """
    Two main steps:
        1. Make a classic insertion into a binary tree using the key
        2. Min-heapify the three using the priority
    """
    def treap_insert(self, key) -> None:
        
        node = Node(key)
        
        if self.root is None:
            self.root = node
            return
        
        self.bst_insert(node)
        self.min_heapify(node)
        
        print("\n**** STATUS ****") # check step by step after the insertion
        self.print_treap()
        return
        

if __name__ == "__main__":
    
    treap = Treap()
    
    for key in [50, 30, 70, 20, 40, 60, 80]:
        treap.treap_insert(key)
    
    # Print the treap to check correctness
    print("\n**** FINAL ****")
    treap.print_treap()
    
