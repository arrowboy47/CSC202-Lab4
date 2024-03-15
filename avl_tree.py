from typing import Union
from dataclasses import dataclass

@dataclass
class AVLNode:
    value: int
    left: Union[None, 'AVLNode']
    right: Union[None, 'AVLNode']
    height: int = 0 # root node has height 0
    balance: int = 0 # balance factor = height(left) - height(right)

@dataclass
class AVLTree:
    root: Union[None, AVLNode] = None

    # extra goofy methods needed for testing
    def in_order_list(self):
        return self._in_order_list(self.root)
    
    def _in_order_list(self, node: Union[None, AVLNode]) -> list:
        if not node:
            return []
        return self._in_order_list(node.left) + [node.value] + self._in_order_list(node.right)
    
    def is_empty(self):
        if not self.root:
            return True
        return False
    
    def insert(self, value: int):
        self.root = self.insert_recurse(value, self.root)
    
    def insert_recurse(self, value, root: Union[None, AVLNode] = None) -> AVLNode:
        if not root:
            print(f"node: {value} being interested")
            return AVLNode(value, None, None)

        # value is inserted in BST fashion
        if value < root.value:
            root.left = self.insert_recurse(value, root.left)
            print(f"parent: {root.value}, left: {root.left.value}")
        elif value > root.value:
            root.right = self.insert_recurse(value, root.right)
            print(f"parent: {root.value}, right: {root.right.value}")
        else:
            raise ValueError(f"Value {value} already exists in the tree")

        # update the height of ancestors of the inserted node
        # going to update height from root, rather than parents of inserted node
        root.height = 1 + max(self.get_height_node(root.left), self.get_height_node(root.right))
        print(f"node: {root.value}, height: {root.height}")

        # Update the balance factor of the current node
        root.balance = self.get_height_node(root.left) - self.get_height_node(root.right)
        print(f"node: {root.value}, balance: {root.balance}")

        # balance the tree if necessary
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # value corresponds to the value of the node that was just inserted: 3rd node in chain

        # Case 1 - left left: 
        if root.balance > 1 and value < root.left.value:
            print(f"rotating right at node {root.value}")
            return self.rotateRight(root)

        # Case 2 - right right 
        if root.balance < -1 and value > root.right.value:
            print(f"rotating left at node {root.value}")
            return self.rotateLeft(root)

        # Case 3 - left right 
        if root.balance > 1 and value > root.left.value:
            print(f"rotating left right at node {root.value}")
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        # Case 4 - right left 
        if root.balance < -1 and value < root.right.value:
            print(f"rotating right left at node {root.value}")
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root  # Return the updated root

    # returns the height of the tree
    # returns the level of the deepest node: 0- just root, 1- first level, 2- second level, etc.
    def get_height(self):
        return self._get_height(self.root)
    
    def _get_height(self, node: Union[None, AVLNode]) -> int:
        if not node:
            return -1
        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)
        return 1 + max(left_height, right_height)
        
    
    # returns the height of the node 
    def get_height_node(self, node: Union[None, AVLNode]) -> int:
        if not node:
            return -1
        return node.height

    def get_size(self):
        return self._get_size(self.root)
    
    def _get_size(self, node: AVLNode):
        if not node:
            return 0
        return 1 + self._get_size(node.left) + self._get_size(node.right)
    

    # conditions for AVL tree:
    # 1. The left and right subtrees' heights differ by at most 1
    # 2. it is a binary search tree
        
    # traverse the tree and check if each nodes balance factor is within -1 and 1
    def isAVL(self):
        return self._isAVL(self.root)
        
    def _isAVL(self, node: Union[None, AVLNode]) -> bool:
        # base case
        if not node:
            return True
        # performing pre-order traversal: OLR
        if node.balance < -1 or node.balance > 1:
            raise ValueError(f"Node {node.value} is not balanced")
        return self._isAVL(node.left) and self._isAVL(node.right)
    

    def get_balance(self, node: Union[AVLNode, None] = None):
        if not node:
            node = self.root
        if not node:
            return 0
        return self.get_height_node(node.left) - self.get_height_node(node.right)

    def rotateRight(self, node: AVLNode):
        y = node.left
        t = y.right

        # Perform rotation
        y.right = node
        node.left = t

        # Update heights
        node.height = 1 + max(self.get_height_node(node.left), self.get_height_node(node.right))
        y.height = 1 + max(self.get_height_node(y.left), self.get_height_node(y.right))

        # Return the new root
        return y

    
    def rotateLeft(self, node: AVLNode):
        y = node.right
        t = y.left

        # Perform rotation
        y.left = node
        node.right = t

        # Update heights
        node.height = 1 + max(self.get_height_node(node.left), self.get_height_node(node.right))
        y.height = 1 + max(self.get_height_node(y.left), self.get_height_node(y.right))

        # Return the new root
        return y

    def deleteNode(self, value: int):
        pass

    def rotateRight(self, node: AVLNode):
        y = node.left
        t = y.right

        # Perform rotation
        y.right = node
        node.left = t

        # Update heights
        node.height = 1 + max(self.get_height_node(node.left), self.get_height_node(node.right))
        y.height = 1 + max(self.get_height_node(y.left), self.get_height_node(y.right))

        # Update balance factors
        node.balance = self.get_balance(node)
        y.balance = self.get_balance(y)

        # Return the new root
        return y

    
    def rotateLeft(self, node: AVLNode):
        y = node.right
        t = y.left

        # Perform rotation
        y.left = node
        node.right = t

        # Update heights
        node.height = 1 + max(self.get_height_node(node.left), self.get_height_node(node.right))
        y.height = 1 + max(self.get_height_node(y.left), self.get_height_node(y.right))

        # Update balance factors
        node.balance = self.get_balance(node)
        y.balance = self.get_balance(y)

        # Return the new root
        return y

    def deleteNode(self, value: int):
        # check if the tree is empty
        if not self.root:
            return self.root
        
        # perform the standard BST delete
        self.root = self.delete_recurse(self.root, value)


    def delete_recurse(self, root: AVLNode, value: int):
        # base case
        if not root:
            return root
        
        # If the value to be deleted is smaller than the root's value,
        # then it lies in the left subtree
        if value < root.value:
            root.left = self.delete_recurse(root.left, value)
        
        # If the value to be deleted is greater than the root's value,
        # then it lies in the right subtree
        elif value > root.value:
            root.right = self.delete_recurse(root.right, value)
        
        # if the value is the same as the root's value, then this is the node to be deleted
        else:
            # node with only one child or no child
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            
            # node with two children: get the inorder successor (smallest in the right subtree)
            temp = self.min_value_node(root.right)
            # copy the inorder successor's content to this node
            root.value = temp.value
            # delete the inorder successor
            root.right = self.delete_recurse(root.right, temp.value)
        
        # if the tree had only one node then return
        if not root:
            return root
        
        # update the height of the current node
        root.height = 1 + max(self.get_height_node(root.left), self.get_height_node(root.right))
        
        # get the balance factor of this node (to check whether this node became unbalanced)
        balance = self.get_balance(root)
        
        # if this node becomes unbalanced, then there are 4 cases
        # Case 1 - left left
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotateRight(root)
        
        # Case 2 - right right
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotateLeft(root)
        
        # Case 3 - left right
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        
        # Case 4 - right left
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right
            return self.rotateLeft(root)
        
        return root
    

        

            
