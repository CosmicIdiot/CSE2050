import itertools 

class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    
    # START HERE
    #adds operation or int to the nodes left
    def add_left(self,node):
        self.left=node

    #adds operation or int to the nodes right
    def add_right(self,node): 
        self.right=node

    #evaluates / dose the math that you want dome for that particular node
    def evaluate(self):
        #checks if node is a operation
        if self.value in self.OPERATORS:#if yes 
            #set the left and right nodes for calculation
            x = self.left.evaluate()
            y = self.right.evaluate()

            '''calculate the left and right, depending on what your operation (node is)
            return the product one completed'''
            if self.value=='+':
                return (x + y)

            if self.value=='-':
                return (x - y)

            if self.value=='*':
                return (x * y)

            if self.value=='/':
                return (x / y)
        else:#if no
            return self.CARD_VAL_DICT[self.value]#return the valuse of the card 

#prints out the representation for the tree with using in order
    def __repr__(self): 
        str= ""#set a empty string

    #if there is a left to the node
        if self.left:
            item=self.left.__repr__()#recursivly call to get the left most node
            str="("+str+item#add the new node to the string with (

        str=str+self.value #add root value to string

    #if there is a right to the node
        if self.right:
            item=self.right.__repr__()#recursivly call to get the right most node
            str=str+item+")"#add the new node to the string with )
            
        return str

"""create a set with all the possible trees"""
def create_trees(cards): 
    operators = '+-*/'#def the operation that will be used
    trees = set()#create the tree set 
    for ops in itertools.permutations(operators,3):#loop through each possible order of operations
        for cds in itertools.permutations(cards, 4):#loop through each possible order of cards
            # first shape
            str1=''#create empty string
            str1=str1+cds[0]#add card 1 to string
            str1=str1+cds[1]#add card 2 to string
            str1=str1+ops[0]#add ops 1 to string
            str1=str1+cds[2]#add card 3 to string
            str1=str1+cds[3]#add card 4 to string
            str1=str1+ops[1]#add ops 2 to string
            str1=str1+ops[2]#add ops 3 to string
            trees.add(str1)#add the string to the possible trees set

            """doc string for shape 1 apply to the rest of the shapes"""
            # 2 shape
            str2=''
            str2=str2+cds[0]
            str2=str2+cds[1]
            str2=str2+ops[0]
            str2=str2+cds[2]
            str2=str2+ops[1]
            str2=str2+cds[3]
            str2=str2+ops[2]
            trees.add(str2)

            # 3 shape

            str3=''
            str3=str3+cds[0]
            str3=str3+cds[1]
            str3=str3+cds[2]
            str3=str3+ops[0]
            str3=str3+ops[1]
            str3=str3+cds[3]
            str3=str3+ops[2]
            trees.add(str3)

            # 4 shape
            str4=''
            str4=str4+cds[0]
            str4=str4+cds[1]
            str4=str4+cds[2]
            str4=str4+ops[0]
            str4=str4+cds[3]
            str4=str4+ops[1]
            str4=str4+ops[2]
            trees.add(str4)

            # 5 shape
            str5=''
            str5=str5+cds[0]
            str5=str5+cds[1]
            str5=str5+cds[2]
            str5=str5+cds[3]
            str5=str5+ops[0]
            str5=str5+ops[1]
            str5=str5+ops[2]
            trees.add(str5)

    return trees#return the set of all possible trees

'''find which trees give you 24 and returns a set with all the valid solutions.'''
def find_solutions(cards): 
    list_trees=create_trees(cards)#get the set with all possible trees 
    valid_trees=set()#create a set for all the valid trees
    for trees in list_trees:#for every tree in the possible tree
        revtree=trees[::-1]#reveres the post ordered tree repesentation
        root=make_tree(revtree)#call the function that creates our tree for us
        try:#try to:
            if root.evaluate()==24:#check if the function evaluates to 24
                valid_trees.add(repr(root))#if yes add that trees string representation to the valid trees set
        except:#if the tree evaluation is not possible
            pass#skip it and go to the next one
    return valid_trees#return all the valid trees as a set

'''function that makes all the trees'''
def make_tree(str):
    str=str#def the str repr of the tree
    opr = {'+', '-', '*', '/'}#set the operations possible
    root=BETNode(str[0])#set the root node (dosent change)
    root.add_right(str[1])#set the root right node (dosent change)

    if str[2] in opr:
        root.add_right(str[2])
    else:
        root.add_left(str[2])

    return root



cards='1234'
trees=find_solutions(cards)
print(trees)

#3840