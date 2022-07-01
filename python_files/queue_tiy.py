class Queue():
    '''Emulates a queue data structure.'''

    def __init__(self):
        '''The class constructor.'''
        self._queue = []
    
    # TODO add enqueue, dequeue, size, and empty functions to the Queue class

    def __iter__(self):
        '''Iterate through the queue.'''
        for item in self._queue:
            yield item
    
    def __str__(self):
        '''Returns a string representation of the queue.'''
        return 'Queue' + str(self._queue)


def main():
    queue = Queue()
    
    # Test case 1
    print('\nTest Case 1')
    print('-----------------------\n')

    # TODO Add five people to the queue

    print(queue) # The five people you added should all be displayed
    
    print('\n-----------------------\n')

    # Test case 2
    print('\nTest Case 2')
    print('-----------------------\n')

    # TODO dequeue the first person from the queue

    print(queue) # There should only be four people, and the first person you added
                 # should be gone
    
    print('\n-----------------------\n')

    # Test case 3
    print('\nTest Case 3')
    print('-----------------------\n')

    # TODO use the size() method get the size of the queue and display it

    # The size should be 4.
    
    print('\n-----------------------\n')

    # Test case 4
    print('\nTest Case 4')
    print('-----------------------\n')

    # TODO use the empty() method on the queue and display the result.
    #      Then remove all of the remaining people from the list and use
    #      the empty() method again. Display the result again.

    # The first result should be False, the second should be True
    
    print('\n-----------------------\n')


if __name__ == '__main__':
    main()