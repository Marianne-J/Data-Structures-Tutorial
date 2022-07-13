class BST():
    '''Emulates a binary search tree.'''

    class _Node():
        '''Emulates a node in the BST.'''
        
        def __init__(self, value):
            '''The class constructor.'''
            self._value = value
            self._left = None
            self._right = None

    def __init__(self):
        '''The class constructor.'''
        self._root = None
    
    def insert(self, value):
        '''Inserts a value into the BST.'''
        # Start at the root
        self._insert(self._root, value)

    def _insert(self, curr_node, value):
        '''The recursive insert function.'''
        # Check if the root is empty
        if self._root is None:
            self._root = BST._Node(value)
            return
        
        # Check whether value goes on the left or the right
        if value >= curr_node._value:
            # Check if the next node is empty
            # If the node is empty, insert the value
            if curr_node._right is None:
                curr_node._right = BST._Node(value)
            
            # Otherwise, keep searching for an empty node
            else:
                self._insert(curr_node._right, value)
        
        else:
            # Check if the next node is empty
            # If the node is empty, insert the value
            if curr_node._left is None:
                curr_node._left = BST._Node(value)
            
            # Otherwise, keep searching for an empty node
            else:
                self._insert(curr_node._left, value)

    def contains(self, value):
        '''Returns whether or not a node is in the BST.'''
        # TODO complete the function
        pass

    def _contains(self, value):
        '''The recursive contains function.'''
        # TODO complete the function
        pass

    def empty(self):
        '''Returns whether or not the BST is empty.'''
        # TODO complete the function
        pass

    def height(self, node):
        '''Returns the height of the given node.'''
        # Start at the root
        return self._height(node, self._root)

    def _height(self, node, curr_node, height = None):
        '''The recursive height function.'''
        # Check if this is the first call
        if height is None:
            height = 0
        
        # Check if this is the node being searched for
        if node == curr_node._value:
            # Return the height
            return height
        
        # Otherwise, check which node to move to next
        elif node > curr_node._value:
            return self._height(node, curr_node._right, height + 1)
        
        else:
            return self._height(node, curr_node._left, height + 1)

    def size(self):
        '''Returns the size of the BST.'''
        # TODO complete the function

    def _size(self, height = None):
        '''The recursive size function.'''
        # TODO complete the function

    def __iter__(self):
        '''Traverse through the tree forwards.'''
        # Start at the root
        yield from self._traverse_forward(self._root)

    def _traverse_forward(self, node):
        '''Recursively traverses forwards through the tree and returns the nodes.'''
        # Make sure the node is not empty
        if node is not None:
            yield from self._traverse_forward(node._left)
            yield node._value
            yield from self._traverse_forward(node._right)


def main():
    bst = BST()
    
    # Example - Insert
    print('\nExample - Insert')
    print('-----------------------\n')

    bst.insert(6)
    bst.insert(8)
    bst.insert(10)
    bst.insert(7)
    bst.insert(3)
    bst.insert(5)
    bst.insert(1)

    for node in bst:
        print(node)

    print('\n-----------------------\n')


    # Example - Height
    print('\nExample - Height')
    print('-----------------------\n')

    print(bst.height(10))
    print(bst.height(3))
    print(bst.height(6))
    
    print('\n-----------------------\n')

    # -----------------------------------------------
    # -----------------------------------------------

    # Test case 1 - Contains
    print('\nTest Case 1')
    print('-----------------------\n')

    # When displayed, the results should be...
    print(bst.contains(6)) # True
    print(bst.contains(1)) # True
    print(bst.contains(13)) # False
    print(bst.contains(9)) # False
    
    print('\n-----------------------\n')


    # Test case 2 - Size
    print('\nTest Case 2')
    print('-----------------------\n')

    # When displayed, the result should be 2
    print(bst.size())
    
    print('\n-----------------------\n')


    # Test case 3 - Empty
    print('\nTest Case 3')
    print('-----------------------\n')

    bst2 = BST()

    # The results when displayed should be...
    print(bst.empty()) # False
    print(bst2.empty()) # True
    
    print('\n-----------------------\n')

if __name__ == '__main__':
    main()