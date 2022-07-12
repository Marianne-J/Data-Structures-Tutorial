# Queues

## Introduction

Queues are a data structure used to not only keep track of a set of data, but the order in which each individual element of that data was added to the set. They are incredibly useful in a variety of situations in programming and in real-life.

## Characteristics

Queues are very similar to stacks. The difference is that while stacks function on a last in, first out (LIFO) basis, queues function on a first in, first out (FIFO) basis. This means that the first item added to a queue is also the first item to leave that queue. Here are some common queue methods.

Operation | Description | Parameters | Returns
--------- | ----------- | ---------- | -------
**enqueue()** | Adds a value to the back of the queue. | **value**: the value to add to the queue. | None
**dequeue()** | Removes a value from the front of the queue. | None | None
**size()** | Returns the number of items in the queue. | None | The number of items in the queue as an integer.
**empty()** | Checks if the queue is empty or not. | None | A boolean value. This value is True if the queue is empty, and False if it is not.

## Real Life Comparison

A good example of a queue in real life are lines for a cash register, ticket booth, ride, etc. The first person to arrive stands at the front of the line.

![First person arrives](images\ex_img1.png)

The next person to arrive stands behind the first person, the next person stands behind that person, and so on. 

![Second person arrives](images\ex_img2.png)
![Third person arrives](images\ex_img3.png)
![Filled line](images\ex_img4.png)

The first person in line will be served first.

![First person served](images\ex_img5.png)
![First person leaves](images\ex_img6.png)

Once they have been served, the next person will be served. This pattern will continue until the line is empty (or the service is closed.)

![Next person served](images\ex_img7.png)
![Next person leaves](images\ex_img8.png)

## Python Lists

In Python, Lists are a stack. However, they can also be used to create a queue. The append() method functions the same as the enqueue() method of a queue and the len() function can be used to get the size of a List, like the size() method. The len() function can also be used in conjunction with an if-statement to emulate the empty() method and the pop() method can be used to emulate the dequeue method.

## Example

Lets create a queue for a cash register line. We will be using a list to do this.

```python
# Create an empty queue
queue = []
```

When someone joins the line, we need to add them to the back of the queue. This can be done using the append() method. Say Mary, Joseph, Eric, and Sue join the line for the cash register.

```python
# Add Mary, Joseph, Eric, and Sue to the queue.
queue.append('Mary')
queue.append('Joseph')
queue.append('Eric')
queue.append('Sue')
```

If we display the queue, it will look like this:

```python
# Display all of the items in the queue
for item in queue:
    print(item)
```
```
Mary
Joseph
Eric
Sue
```

As you can see, Mary is currently at the end of the line. If we wanted to see how long the line currently is, we would use the len() function.

```python
# Display the size (length) of the queue
print(len(queue))
```
```
4
```

Once Mary has paid for her items, she will leave the line. Subsequently, she needs to be removed from the queue. We can use the pop() method to do this.

```python
# Remove Mary from the queue
queue.pop(0) # The pop() method removes the last item by default, so we need to
             # tell it to remove the item at the first index

# Display the queue
for item in queue:
    print(queue)
```
```
Joseph
Eric
Sue
```

To check if the line is empty, we need to use the len() function again. Since the queue is not empty, the result we should get is False.

```python
# Create a variable to store the result
empty = False

# Check if the queue is empty
if len(queue) == 0:
    empty = True
else:
    empty = False

# Display the result
print(empty)
```
```
False
```

Alternatively, since we are using a List, we can check if the queue is empty by seeing if it is an empty list.

```python
# Check if the queue is empty
if queue == []:
    empty = True
else:
    empty = False
```

## Try it Yourself

Using [this](python_files\queue_tiy.py) Python script, try finishing the Queue class and implementing it to satisfy the test cases.


You may find the example code [here](python_files\queue_ex.py).