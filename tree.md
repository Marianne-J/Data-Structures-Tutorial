# Tree

## Introduction

A tree is a data structure with nodes that are connected by pointers. It is similar to a linked list, but a single node on a tree can be connected to more than one node as opposed to just one. There are a variety of different kinds of trees. This tutorial will cover a binary search tree (BST) and a balanced binary search tree (balanced BST), two commonly used trees.

## Characteristics

A binary search tree has a root that is connected to at most two nodes. Each additional node is connected to at most three nodes (its parent node and two child nodes). The nodes of the tree that are only connected to a parent node are called leaves. The root can be any data value. Every additional value that is added is compared with the already existing nodes. If the value is greater than the root, then it is moved right. Otherwise, it is moved left. The value is then compared to the node it was moved to (if it exists) in the same fashion. The value is moved through the tree until an empty node is found. A balanced BST has about the same depth on both sides of the tree (as depicted below).

![Balanced BST](images\ex_img9.png)

Here are some common BST methods.

Operation | Description | Parameters | Returns
--------- | ----------- | ---------- | -------
**insert()** | Adds a value into the tree. | **value**: the value to add to the tree. | None
**remove()** | Removes a value from the tree. | **value**: the value to remove from the tree. | None
**contains()** | Checks if a value is in the tree. | **value**: the value to look for. | A boolean value. True if the value is in the tree, False if it is not.
**height()** | Returns the height of a specific node. | **node**: the node to calculate the height of. | An integer representing the height of the node.
**size()** | Returns the size of the tree. | None | An integer representing the number of values in the tree.
**empty()** | Checks if the tree is empty or not. | None | A boolean value. This value is True if the tree is empty, and False if it is not.

## Applications

Trees can be used in data compression, which allows for large amounts of data to be transferred without requiring a large amount of space. If you have done family history, then your family tree is also a type of tree (with you being the root and your earliest recorded ancestors being the leaves). Both of these examples use a type of binary tree. Because there are many different kinds of trees, they can be used  for all sorts of different situations. A tree could have at most three connections per node instead of two, greater values could go on the left instead of the right, etc.

## Recursion

Recursion can be an integral part of a tree. Recursion is a programming technique where a function calls itself. A function that uses recursion is known as a recursive function. A recursive function must follow to rules: a recursive call must be performed on a smaller problem, and there must be a base case. If the problem does not get smaller each time a recursive function is called, then the program will run until a RecursionError exception is raised.

When a function is called, it is put in a stack. This stack is used to keep track of the functions that have been called. Once that stack fills up, an exception is raised and the program crashes.

A base case is simply the result that a recursive function should end on. If there is no base case, then the function will continue to make recursive calls forever. It is important to note that the function does not automatically return a result to the main program. It returns the result to the function that called it (in this case, itself). Keep this in mind when you are designing a recursive function.

Here is an example of a recursive function that displays a range of numbers in Python.

```python
def display_range(start, end):
    # This is the base case
    if start == end:
        print(start)
        return
    
    # If the base case is not met, the function makes a recursive call
    else:
        print(start)
        # Make sure the problem gets smaller!
        display_range(start - 1, end)

display_range(5, 2)
```
Output:
```
5
4
3
2
```

In trees, recursion is typically used to navigate through the tree.

## Example

Let's try creating a BST class in Python. I will only be completing part of it for this example; the rest you will complete in the "try it yourself" activity. I opted to exclude the remove function for both this example and the practice code as that is a bit more complicated.

```python
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
```

```python
def main():
    bst = BST()
```

### Insert

We need to be able to add values to our binary search tree. For that we will need two functions, one to make the first call, and one to make recursive calls.

```python
    def insert(self, value):
        '''Inserts a value into the BST.'''
        pass

    def _insert(self, curr_node, value):
        '''The recursive insert function.'''
        pass
```

The insert function simply needs to call the _insert function for the first time using the root.

```python
    def insert(self, value):
        '''Inserts a value into the BST.'''
        # Start at the root
        self._insert(self._root, value)
```

The _insert function is where most of the work will actually be done. The first thing the function should check for is whether or not the root is empty. If the root is empty, then it inserts the value there.

```python
    def _insert(self, curr_node, value):
            '''The recursive insert function.'''
            # Check if the root is empty
            if self._root is None:
                self._root = BST._Node(value)
                return
```

If the root is not empty, then the function needs to compare the value to the value of the root. If the value is greater than the root, it should move to the left. If it is less than the root, it should move to the right.

```python
    def _insert(self, curr_node, value):
            '''The recursive insert function.'''
            # Check if the root is empty
            if self._root is None:
                self._root = BST._Node(value)
                return
            
            # Check whether value goes on the left or the right
            if value >= curr_node._value:
                pass
            
            else:
                pass
```

Once the function knows which direction to move, it should check whether the next node is empty. If it is, then it should insert the value there. This is the base case. If the node is not empty, then it should make a recursive call and keep searching. Not that the recursive call uses the next node instead of the current node.

```python
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
```

We can then use this function to insert values into a bst.

```python
    # Example - Insert
    bst.insert(6)
    bst.insert(8)
    bst.insert(10)
    bst.insert(7)
    bst.insert(3)
    bst.insert(5)
    bst.insert(1)
```

### Height

In order to find the height of a specific node, we once again need a recursive function. The height function will make the first call using the root. Notice that since we need to return a value this time, we use return.

```python
    def height(self, node):
        '''Returns the height of the given node.'''
        # Start at the root
        return self._height(node, self._root)

    def _height(self, node, curr_node, height = None):
        '''The recursive height function.'''
        pass
```

If this is the first call to the recursive function, the height memory value should be set to 0. Next, the function needs to check if the current node is the one the user is searching for. If it is not, it should compare the value of the node to the value of the current node to determine where to go next.

```python
    def _height(self, node, curr_node, height = None):
        '''The recursive height function.'''
        # Check if this is the first call
        if height is None:
            height = 0
        
        # Check if this is the node being searched for
        if node == curr_node._value:
            pass
        
        # Otherwise, check which node to move to next
        elif node > curr_node._value:
            pass

        else:
            pass
```

If the current node is the one being searched for, then the function should return the height. This is the base case. If not, then it should make a recursive call with the next node and return the result. Notice that the height is increased by one for the recursive call.

```python
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
```

We can then use this function to find the height of nodes we have inserted into the tree.

```python
    # Example - Height
    print('\nExample - Height')
    print('-----------------------\n')

    print(bst.height(10))
    print(bst.height(3))
    print(bst.height(6))
    
    print('\n-----------------------\n')
```

```
Example - Height
-----------------------

2
1
0

-----------------------
```

### Traverse Forward

In order to iterate through the BST, we need to add an \_\_iter\_\_ function, as well as a function to make recursive calls.

```python
    def __iter__(self):
        '''Traverse through the tree forwards.'''
        pass

    def _traverse_forward(self, node):
        '''Recursively traverses forwards through the tree and returns the nodes.'''
        pass
```

The \_\_iter\_\_ function will make the first call to the \_traverse\_forward function.

```python
    def __iter__(self):
        '''Traverse through the tree forwards.'''
        # Start at the root
        yield from self._traverse_forward(self._root)
```

The \_traverse\_forward function will then use recursive calls to move through the tree and return the node values until it reaches the empty nodes at the end of the tree.

```python
    def _traverse_forward(self, node):
        '''Recursively traverses forwards through the tree and returns the nodes.'''
        # Make sure the node is not empty
        if node is not None:
            yield from self._traverse_forward(node._left)
            yield node._value
            yield from self._traverse_forward(node._right)
```

We can then iterate through the BST using a for loop.

```python
    # Example - Traverse forward
    print('\nExample - Traverse forward')
    print('-----------------------\n')

    for node in bst:
        print(node)
    
    print('\n-----------------------\n')
```

```
Example - Traverse forward
-----------------------

1
3
5
6
7
8
10

-----------------------
```

## Try it Yourself

Using [this](python_files\tree.py) Python script, try finishing the BST class so that it satisfies the test cases. The example code is also included in this file. Use it to help you complete the remaining functions. If you need to add functions or parameters, you may do so.