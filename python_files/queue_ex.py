# Create an empty queue
queue = []


# Add Mary, Joseph, Eric, and Sue to the queue.
queue.append('Mary')
queue.append('Joseph')
queue.append('Eric')
queue.append('Sue')

# Display all of the items in the queue
for item in queue:
    print(item)


# Display the size (length) of the queue
print(len(queue))


# Remove Mary from the queue
queue.pop(0) # The pop() method removes the last item by default, so we need to
             # tell it to remove the item at the first index

# Display the queue
for item in queue:
    print(queue)


# Create a variable to store the result
empty = False

# Check if the queue is empty
if len(queue) == 0:
    empty = True
else:
    empty = False

# Display the result
print(empty)

# Alternative method
if queue == []:
    empty = True
else:
    empty = False

print(empty)