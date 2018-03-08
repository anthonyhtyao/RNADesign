import unittest
from anytree import LevelOrderIter, findall_by_attr, findall
from collections import Counter
from models.tree import Tree
import utils.structure as stc

class AuxFunctionTest(unittest.TestCase):
    """
    Tests for auxiliar funcitions about RNA secondary structure
    """
    
    def setUp(self):
        self.structure = '..(((...(((...((((...))))..((((...(((.....)))...)))).....)))...)))...'
    
    def test_is_parentized(self):
        self.assertTrue(stc.is_parenthesized(self.structure))

    def test_bracket_to_index(self):
        """
        Test auxiliar function, bracket_to_index
        """
        true = [-1,-1,65,64,63,-1,-1,-1,59,58,57,-1,-1,-1,24,23,22,21,-1,-1,-1,17,16,15,14,-1,-1,51,
                50,49,48,-1,-1,-1,44,43,42,-1,-1,-1,-1,-1,36,35,34,-1,-1,-1,30,29,28,27,-1,-1,-1,-1,
                -1,10,9,8,-1,-1,-1,4,3,2,-1,-1,-1]
        index = stc.bracket_to_index(self.structure)
        self.assertEqual(index,true)

class TreeTest(unittest.TestCase):
    """
    Tests for tree presentation (models.tree.Tree)
    """

    def setUp(self):
        self.structure = '(((.((...))((...)))))'
        self.tree = Tree.from_bracket(self.structure)

    def test_tree_construction(self):
        """
        Test if tree constructor returns same amount of nodes as expected.
        """
        true_count = Counter({'R':1,'H':2,'M':1,'S':4})
        nodes_count = Counter(map(lambda node:node.label, LevelOrderIter(self.tree.root)))
        self.assertEqual(true_count, nodes_count)

    def test_ends_with_H(self):
        """
        If the construction is correct, leaves of the secondary structure can only be hairpin loops
        and a hairpin loop can only be a leaf (no offspring)..
        """
        hairpins = set(findall_by_attr(self.tree.root,'H',name='label'))
        leaves = set(findall(self.tree.root,filter_=lambda node: node.is_leaf))
        self.assertSetEqual(hairpins, leaves)

if __name__ == '__main__':
    unittest.main()
