from avl_tree import *
import unittest



# some basic test functions for AVL trees
class TestAVL(unittest.TestCase):
    def test_00_init(self):
        test_tree = AVLTree()
        self.assertEqual(test_tree.get_size(), 0)
        self.assertEqual(test_tree.get_height(), -1)
        self.assertTrue(test_tree.is_empty())

    def test_01_insert(self):
        test_tree = AVLTree()
        test_tree.insert(5)
        self.assertEqual(test_tree.get_size(), 1)
        self.assertEqual(test_tree.get_height(), 0)
        self.assertEqual(test_tree.get_balance(), 0)
        self.assertEqual(test_tree.in_order_list(), [5])

    def test_02_insert(self):
        test_tree = AVLTree()
        test_tree.insert(5)
        test_tree.insert(4)
        self.assertEqual(test_tree.get_size(), 2)
        self.assertEqual(test_tree.get_height(), 1)
        self.assertEqual(test_tree.get_balance(), 0)
        self.assertEqual(test_tree.in_order_list(), [4, 5])

    def test_03_insert(self):
        test_tree = AVLTree()
        test_tree.insert(5)
        test_tree.insert(4)
        test_tree.insert(3)
        self.assertEqual(test_tree.get_size(), 3)
        self.assertEqual(test_tree.get_height(), 1)
        self.assertEqual(test_tree.get_balance(), 0)
        self.assertEqual(test_tree.in_order_list(), [3, 4, 5])

    def test_04_insert(self):
        test_tree = AVLTree()
        test_tree.insert(5)
        test_tree.insert(4)
        test_tree.insert(3)
        test_tree.insert(2)
        self.assertEqual(test_tree.get_size(), 4)
        self.assertEqual(test_tree.get_height(), 2)
        self.assertEqual(test_tree.get_balance(), 0)
        self.assertEqual(test_tree.in_order_list(), [2, 3, 4, 5])

    def test_05_insert(self):
        test_tree = AVLTree()
        test_tree.insert(5)
        test_tree.insert(4)
        test_tree.insert(3)
        test_tree.insert(2)
        test_tree.insert(1)
        self.assertEqual(test_tree.get_size(), 5)
        self.assertEqual(test_tree.get_height(), 2)
        self.assertEqual(test_tree.get_balance(), 0)
        self.assertEqual(test_tree.in_order_list(), [1, 2, 3, 4, 5])

    def test_06_insert(self):
        test_tree = AVLTree()
        test_tree.insert
    
if __name__ == '__main__':
    unittest.main()
    
