import unittest
from BET import BETNode, create_trees, find_solutions


class TestBETNode(unittest.TestCase):
    def test_repr(self):
        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4
           
        """
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))
        expected_str = '(A*(2-(3+4)))'
        self.assertEqual(repr(root), expected_str)

    # TODO: Add test cases below. Repr is provided for you.

    """tests the code can evaluate 2 diffent types of trees"""    
    def test_evaluate_tree1(self): 
        root = BETNode('*')#set the top node(root)
        root.add_left(BETNode('A'))#set the left node from the root
        root.add_right(BETNode('-'))#set the right node from the root
        root.right.add_left(BETNode('2'))#set the left node from the right node
        root.right.add_right(BETNode('+'))#set the right node from the right node
        root.right.right.add_left(BETNode('3'))#set the left node from the right, right node
        root.right.right.add_right(BETNode('4'))#set the right node from the right, right node
        self.assertEqual(root.evaluate(), -5)#checks if it has been evaluated properly

    def test_evaluate_tree2(self): 
        root = BETNode('*')#set the top node(root)
        root.add_left(BETNode('+'))#set the left node from the root
        root.add_right(BETNode('Q'))#set the right node from the root
        root.left.add_left(BETNode('-'))#set the left node from the left node
        root.left.add_right(BETNode('A'))#set the right node from the left node
        root.left.left.add_left(BETNode('3'))#set the left node from the left, left node
        root.left.left.add_right(BETNode('2'))#set the right node from the left, left node
        self.assertEqual(root.evaluate(),24)#checks if it has been evaluated properly
        #print(repr(root))
        #r=root.evaluate()
        #print(r)

"""tests the code outputs a set with a certain length of possible trees"""
class TestCreateTrees(unittest.TestCase):
    def test_hand1(self): 
        cards="A123" #def the cards to use for the game
        trees=create_trees(cards)#get the set with all possible trees
        self.assertEqual(len(trees),2880)#check the amount of trees is the amount required
        
    def test_hand2(self): 
        cards="A1QK"#def the cards to use for the game
        trees=create_trees(cards)#get the set with all possible trees
        self.assertEqual(len(trees),2880)#check the amount of trees is the amount required

        
"""tests the code outputs a set with a certain length of valid trees"""
class TestFindSolutions(unittest.TestCase):
    def test0sols(self): 
        cards="A123"#def the cards to use for the game
        valid_trees=find_solutions(cards)#get the set with all valid trees
        self.assertEqual(len(valid_trees),0)#check the amount of trees is the amount required (zero)

    def test_A23Q(self): 
        cards='A23Q'#def the cards to use for the game
        valid_trees=find_solutions(cards)#get the set with all valid trees
        self.assertEqual(len(valid_trees),33)#check the amount of trees is the amount required (33)

        
unittest.main()