# Set

## Introduction

A set is a data structure similar to a stack or a queue. However, unlike a stack or a queue, the order of the data in a set does not matter. As a result, operations can performed on the set in O(1) time (the fastest possible performance in Big O notation).

## Characteristics

Sets use hashing in order to determine whether a value is part of a data set, add a value to the set, or remove a value from the set. They also do not allow duplicates, which helps increase the performance of operations on a set. Hashing uses the value of the data to determine which index it should be stored at. Here are some common set methods.

Operation | Description | Parameters | Returns
--------- | ----------- | ---------- | -------
**add()** | Adds a value to the set. | **value**: the value to add to the set. | None
**remove()** | Removes the specified value from the set. | **value**: the value to remove from the set. | None
**size()** | Returns the number of items in the set. | None | The number of items in the set as an integer.
**member()** | Checks if the specified value is in the set. | **value**: the value to check for. | A boolean value. This value is True if the value is in the set, and False if it is not.

## Applications

Some uses of sets include finding unique values in a data set, performing union or intersection operations on sets of data, etc. If you have ever worked with a database, then you will have also used intersections or unions. An intersection takes the data from two different data sets and filters for the values they share in common. A union joins two data sets together, ignoring any duplicate values.

## Python Dictionaries

In Python, sets are represented by curly braces.
```python
my_set = {1, 2, 3, 4, 5} 
```
As such, they can easily be confused with Python dictionaries, which also use curly braces (dictionaries are actually made using the set data structure).
```python
my_dict = {'first':1, 'second':2, 'third':3}
```
When initializing an empty set you use `set()` instead of empty curly brackets, as empty curly brackets initialize an empty dictionary.
```python
# Empty set
my_set = set()

# Empty dictionary
my_dict = {}
``` 

## Example

Let's practice using set operations to manipulate data. I will be using two sets containing the names of people who have been to another country and the names of people who enjoy travelling, respectively, for this example.

```python
# Create the sets
been_out_of_country = {'Henry', 'Frank', 'Ashley', 'Sam', 'Rebecca'}
enjoys_travelling = {'Frank', 'Joseph', 'Eliza', 'Sam', 'George'}
```

Let's say we want to know who has been out of country *or* enjoys travelling. To find this information, we would perform a union on the two sets.

```python
# Perform the union
# The "OR" operator is used for this
been_ooc_or_et = been_out_of_country | enjoys_travelling
print(been_ooc_or_et)
```

If we run this code, we find that Ashley, Frank, Eliza, Joseph, Sam, Henry, and Rebecca have either been out of country or enjoy travelling. Notice that each person only appears once in the set, even if they were in both sets.

```
{'Ashley', 'George', 'Frank', 'Eliza', 'Joseph', 'Sam', 'Henry', 'Rebecca'}
```

If we wanted to know who has been out of country *and* enjoys travelling, we would perform an intersection on the two sets.

```python
# Perform the intersection
# The "AND" operator is used for this
been_ooc_and_et = been_out_of_country & enjoys_travelling
print(been_ooc_and_et)
```

If we run this code, we find that only Sam and Frank have been out of country and enjoy travelling. Notice that they are the only people in both sets.

```
{'Sam', 'Frank'}
```

Because the sets in this example are so small, it is easy to tell who has been out of country and who enjoys travelling without having to search for an individual name. However, for much larger sets of data, this would not be the case. If we wanted to see if someone is in one of the sets (or their union or intersection), we would use the "in" operator in Python.

Let's check if Joseph has been out of country.

```python
# Is "Joseph" in the out of country set?
print('Joseph' in been_out_of_country)
```

Since Joseph is in the set, the program will display "True." However, if we checked to see if Joseph enjoys travelling, the program would return "False", as Joseph is not in the enjoys travelling set.

```python
# Is "Joseph" in the enjoys travelling set?
print('Joseph' in enjoys_travelling)
```

## Try it Yourself
Using [this](python_files\set_tiy.py) Python script, write code to find and display the information requested in each of the cases.


You may find the example code [here](python_files\set_ex.py).