import unittest
import models.tree
import utils.structure as stc

def fun(x):
    return x + 1

class TreeTest(unittest.TestCase):
    
    def setUp(self):
        self.structure = '(((.((...))((...)))))'
    
    def test_is_parentized(self):
        self.assertTrue(stc.is_parenthesized(self.structure))

if __name__ == '__main__':
    unittest.main()
