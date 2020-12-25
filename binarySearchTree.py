# Importing necessary modules
import random

# Defining a class for the tree nodes
class node:

    # The constructor for the node class
    # The value of each node is initialized to None
    def __init__(self, value = None):

        # Allows the constructor to initialize the value of the node if a value is passed
        self.value = value

        # Initializes the left child to be a null pointer
        self.leftChild = None

        # Initiializes the right child to be a null pointer
        self.rightChild = None

# Defining the binary search tree (BST) class
class binarySearchTree:

    # Constructor for the BST class
    def __init__(self):

        # Initializes the root as a null pointer
        self.root = None

    # Function to add a node to the BST
    def insert(self, valueParam):

        # Checks to see if the tree is empty
        if self.root == None:

            # Sets the root to be a new node with the specified value
            self.root = node(valueParam)

        # If the root already exists
        else:

            # Calls a recursive helper function to insert nodes further down the tree
            self.helpInsert(valueParam, self.root)

    # Function to help the insertion function
    def helpInsert(self, valueParam, currNode):

        # If the specified value is less than the value of the current node being evaluated
        if valueParam < currNode.value:

            # If the current node doesn't have a left child
            if currNode.leftChild == None:

                # Sets the left child of the current node to be a new node with the specified value
                currNode.leftChild = node(valueParam)

            # If the current node does have a left child
            else:

                # Recursively calls the insert helper function on the left child
                self.helpInsert(valueParam, currNode.leftChild)

        # If the specified value is greater than the value of the current node being evaluated
        elif valueParam > currNode.value:

            # If the current node doesn't have a right child
            if currNode.rightChild == None:

                # Sets the right child of the current node to be a new node with the specified value
                currNode.rightChild = node(valueParam)

            # If the current node does have a right child
            else:

                # Recursively calls the insert helper function on the right child
                self.helpInsert(valueParam, currNode.rightChild)

        '''
        # If the speicifed value equals the value of the current node being evaluated
        else:

            # Indicates that the value is already in the tree 
            print("The value " + str(valueParam) + " is already in the tree.")
        '''

    # Function to display the nodes in the tree
    def printTreeInOrder(self):

        # Checks if the tree actually has a root
        if self.root != None:

            # Calls a helper function to display the tree nodes
            self.helpPrintTree(self.root)

    # Function to recursively traverse the tree and display all of the nodes "in order"
    def helpPrintTree(self, currNode):

        # If the current node is not a null pointer
        if currNode != None:

            # Recursively calls the function on the left child node
            self.helpPrintTree(currNode.leftChild)

            # Prints the value of the current node
            print(str(currNode.value))

            # Recursively calls the function on the right child node
            self.helpPrintTree(currNode.rightChild)

    # Function to return the height of the tree
    def findHeight(self):

        # Checks if the root exists
        if self.root != None:

            # Returns the output of the helper function
            return self.helpFindHeight(self.root, 0)

        # If the root doesn't exist
        else:

            # Returns 0 to indicate that the tree has a height of 0
            return 0

    # Recursive helper function to find the height of the tree
    def helpFindHeight(self, currNode, maxHeightFound):

        # Checks if the current node is a null pointer
        if currNode == None:

            # Returns the greatest height that has been currently found
            return maxHeightFound

        # Stores the maximum height found in the left subtree
        heightOfLeftSubTree = self.helpFindHeight(currNode.leftChild, maxHeightFound + 1)

        # Stores the maximum height found in the right subtree
        heightOfRightSubTree = self.helpFindHeight(currNode.rightChild, maxHeightFound + 1)

        # Returns the larger height of either subtree
        return max(heightOfLeftSubTree, heightOfRightSubTree)

    # Function to search the tree for a specified value (Binary search)
    def search(self, value):

        # Checks if the tree is empty
        if self.root == None:

            # Returns false to indicate that the node is not in the
            return False

        # If the tree is not empty
        else:

            # Returns the output of the helper function 
            return self.helpSearch(value, self.root)

    # Recursive function to traverse the tree for a specified node
    def helpSearch(self, valueParam, currNode):

        # Checks to see if the current node has the specified value
        if currNode.value == valueParam:

            # Returns true to indicate that the node was found
            return True

        # Checks if:
        # the specified value is less than the value of the current node
        # the current node has a left child
        elif  valueParam < currNode.value and currNode.leftChild != None:

            # Recursively calls the search helper function on the left child
            return self.helpSearch(valueParam, currNode.leftChild)

        # Checks if:
        # the specified value is greater than the value of the current node
        # the current node has a right child
        elif valueParam > currNode.value and currNode.rightChild != None:

            # Recursively calls the search helper function on the right child
            return self.helpSearch(valueParam, currNode.rightChild)

        # If none of the other conditions can be satisfied
        else:

            # Returns false to indicate that the value is not in the tree
            return False

# Function to randomly populate a BST
def populateBST(tree):

    # For loop to run 50000 times
    # Uses '_' since the loop control variable is not used in the loop
    for _ in range(50000):

        # Uses the randint function from the random module to generate a random number between 0 and 1000
        currValue = random.randint(0, 1000)

        # Inserts the current value into the tree
        tree.insert(currValue)

    # returns the tree
    return tree


# Instantiates a BST
myTree = binarySearchTree()

# Inserts nodes into the tree
myTree.insert(5)
myTree.insert(1)
myTree.insert(3)
myTree.insert(2)
myTree.insert(7)
myTree.insert(10)
myTree.insert(0)
myTree.insert(20)

# Outputs the nodes of the tree in order
myTree.printTreeInOrder()

# Displays the heught of the tree
print("The height of the tree is: " + str(myTree.findHeight()))

# Variables to be searched for
value1 = 10
value2 = 30

# Searches the tree for the values and notes if they are found
print("Is " + str(value1) + " in the tree? " + str(myTree.search(value1)))
print("Is " + str(value2) + " in the tree? " + str(myTree.search(value2)))

'''
# Can be used to see that many elements can be stored in a relatively small # of tree levels
# 50,000 elements can be stored in ~20 tree levels
myTree = populateBST(myTree)
print("The height of the tree is: " + str(myTree.findHeight()))
'''

