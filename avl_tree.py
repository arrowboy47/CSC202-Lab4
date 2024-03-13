from typing import Union
from dataclasses import dataclass

@dataclass
class AVLNode:
    value: int
    left: Union[None, 'AVLNode']
    right: Union[None, 'AVLNode']
    height: int

class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value: int):
        pass

    def isAVL(self):
        pass

    def _isAVL(self, node: Union[None, AVLNode]):
        pass

    def balanceFactor(self, node: AVLNode):
        pass

    def rotateRight(self, node: AVLNode):
        pass
    
    def rotateLeft(self, node: AVLNode):
        pass

    def deleteNode(self, value: int):
        pass