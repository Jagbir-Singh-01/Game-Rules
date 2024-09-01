## Assignment Objectives

In this assignment we will:

*  draw diagrams of your implementation in order to gain a better insight as to how this is accomplished.
*  implement a sorted linked list
*  implement array based data structures
*  implement a recursive function


## Part A: Drawings (5 marks), Due May 31. No late submissions accepted for part A

In your repository you will find two pdf file containing some diagrams.  Decide if you will implement your part B with or without the use of sentinel nodes and use the diagram file that matches your decision for Part A.

Read through the specs part B, C and D to get an idea of the functionalities asked for in Part A.

Modify each of the lists in the drawings to show the result of the operation indicated in the diagram

* Be clear about what is changing and how.  
* The diagrams do not need to be neat.. but they need to be understandable so clearly scribbling over a link that no longer exsists is perfectly acceptable.  The idea is to think through what you need to change to based on a written specification.
* You can modify the diagrams electronically using something like paint on windows, or preview on macs.  You can also use other diagramming software 
* Alternatively you can print out the pdf and then hand draw on the printed diagrams. If you choose this method you must:
     * take a picture of each drawing and put them into word document in same order as original
     * convert that document to a pdf (print to a pdf) and name the pdf file the same as the original file.
     * Upload the file to your github repo.
     * A bunch of individual images will not be graded, it needs to be in **one** pdf file.


## Part B: Implement a Sorted Doubly Linked list (10 marks)

The class declarations have been created in the a1_partb.py starter file.  You are responsible to write all the listed functions.

* You are allowed to add data members and helper functions to both Node and DoublyLInked classes.
* You are not allowed to remove/change the interfaces of the listed functions
* Only the listed functions will be called directly by the tester, thus any helper functions you add must be called from those listed below

### Node

The Node class is declared within SortedList.  It stores:
* a piece of data
* a reference to the next Node in the SortedList (None if Node is last node)
* a reference to the previous Node in the SortedList (None if Node is first node)
    
When a Node is initialized, it is passed a data value.  Optionally it is also passed a reference to the next node and a reference to the previous node (in that order).  If the data values are not passed in, they are defaulted to None.

The Node function has the following member functions:

---

```python
def get_data(self)
```
function returns data stored in node

---

```python
def get_next(self)
```
function returns reference to next node in SortedList

---

```python
def get_previous(self)
```
function returns reference to previous node in SortedList

---

### SortedList

A SortedList is a sorted doubly linked list. 


A sorted linked list is a linked list where values stay sorted from smallest to biggest with the smallest node at the front of the list and the largest node at the back.

When the SortedList is first created it is empty.

The SortedList has the following member functions

```python
def get_front(self)
```
This function returns a reference to the first data node in the list.  If list is empty, function returns None

---

```python
def get_back(self)
```
This function returns a reference to the last data node in the list.  If list is empty, function returns None

---

```python  

def is_empty(self)
```
This function returns True if the list is empty, False otherwise

---


```python
def __len__(self)
```
This function returns the number of values stored in the list

---

```python
def insert(self,data)
```
this function inserts data into the list such that the list stays sorted. You may assume that the data being added can be compared using comparison operators.  Function returns reference to newly added node.

---

```python
def erase(self, node)
```
This function removes the node referred to by the node argument.   This function returns nothing. If node is None, function does not alter list and will raise the ValueError with this statement:

```python
  raise ValueError('Cannot erase node referred to by None')
```

---

```python
def search(self, data)
```
This function returns a reference to the node containing data if it exists within the list, None if no node contains data





## Part C - Stack, Queue, Deque(10 marks)

Implementation of the three classes are done in a1_partc.py

These three classes must use a python list based (not linked list based) implementation. NOTE, you can use a python list only.. no other python collection is allowed.

You are allowed to use **most** of the functions available for a python list in your solution.  However the following functions are prohibited (you cannot use them in your solution, or your solution will be subject to deductions or possibly resubmissions):

* append()
* pop()
* insert() 


Furthermore, the functions you are asked to write will have a runtime requirement.  Using a python function that causes the function to exceed the required run time will result in a reduced grade.

This reference may be useful in determining whether or not you can make use of a certain function:

https://wiki.python.org/moin/TimeComplexity#list

In functions that add an item to the data structure (enqueue and other push functions) , there is a possibility that the underlying list will require a resizing operation.  You do not need to count this resizing operation when considering the runtime.

When resizing a data structure, always double the current capacity.  The reason for this is because it can be proved that if we were to double our capacity on resize when list is full, the cost of the resize operation can be amortized over the cost of all insertions allowing for the run time to be O(1) on average.  If we were to do increase the capacity by some other method, by adding some constant amount to our capacity for example, the run time will not be O(1) average.  This type of analysis is called an amortized analysis which is beyond the scope of this course.  Thus, it is good enough to simply know that you should resize by doubling the current capacity.


### Stack class


The Stack class implements a FILO data structure.  This class must be implemented using a python list (not a linked list) based solution.


```python
def __init__(self, cap):
```
This function initializes the Stack class data members. It is passed a value representing it's capacity, with a default capacity of 10 if no capacity is passed in.

---


```python
def capacity(self):
```
This function returns capacity.  

Runtime requirement for this function is O(1)

---


``` python
def push(self, data):
```
This function adds data to the "top" of the Stack.  function does not return anything.  When this operation causes the number of items stored to exceed the current capacity, a resizing operation will need to take place.  Resizing always doubles the current capacity of the array.


Runtime requirement for this function is O(1) when no resizing occurs, O(n) when resizing occurs




---

``` python
def pop(self):
```
This function removes the newest value from the Stack (the value at the "top" of the Stack).  function returns value removed.  

If the function is called on an empty Stack, raise the IndexError with this statement

```python
raise IndexError('pop() used on empty stack')
```


Runtime requirement for this function is O(1)

---

``` python
def get_top(self):
```
This function returns the the newest value (value at "top") from the Stack without removing it.  Function returns None if stack is empty 

Runtime requirement for this function is O(1)

---

``` python

  def is_empty(self):
```
This function returns True if Stack is empty, False otherwise.  

Runtime requirement for this function is O(1)


---

``` python

  def __len__(self):
```
This function returns the number of values in the Stack.  

Runtime requirement for this function is O(1)





### Queue class:

The Queue class implements a FIFO data structure.  This class must be implemented using a python list (not a linked list) based solution.


```python
def __init__(self, cap):
```
This function initializes the Queue class data members. It is passed a value representing it's capacity, with a default capacity of 10 if no capacity is passed in.

---

```python
def capacity(self):
```
This function returns capacity.

Runtime requirement for this function is O(1)

---

``` python
def enqueue(self, data):
```
This function adds data to the "back" of the Queue.  function does not return anything.  When this operation causes the number of items stored to exceed the current capacity, a resizing operation will need to take place.  Resizing always doubles the current capacity of the array.


Runtime requirement for this function is O(1) when no resizing occurs, O(n) when resizing occurs

---

``` python
def dequeue(self):
```
This function removes the oldest value from the Queue (the value at the "front" of the Queue).  Function returns value removed.  

If the function is called on an empty Queue, raise the IndexError with this statement

---

```python
raise IndexError('dequeue() used on empty queue')
```


Runtime requirement for this function is O(1)

---

``` python
def get_front(self):
```
This function returns the the oldest value (value at "front") from the Queue without removing it. Function returns None if Queue is empty.

Runtime requirement for this function is O(1)

---

``` python

def is_empty(self):
```
This function returns True if Queue is empty, False otherwise.  Runtime requirement for this function is O(1)

---

``` python

def __len__(self):
```
This function returns the number of values in the Queue.  Runtime requirement for this function is O(1)



### Deque class 


A Deque is a double ended queue.  This class allows you to add/remove items from front or the back of the data structure.  This class must be implemented using a python list (not a linked list) based solution.  

```python

def __init__(self, cap):
```
This function initializes the Deque class data members. It is passed a value representing it's capacity, with a default capacity of 10 if no capacity is passed in.


```python
def capacity(self):
```
This function returns capacity

Runtime requirement for this function is O(1)

---

``` python
def push_front(self, data):
```
This function adds data to the "front" of the Deque.  Function does not return anything.  When this operation causes the number of items stored to exceed the current capcity, a resizing operation will need to take place.  Resizing always doubles the current capcity of the array.


Runtime requirement for this function is O(1) when no resizing occurs, O(n) when resizing occurs

---

``` python
def pop_front(self):
```
This function removes the  value from the "front" of the Deque. Function returns value removed.  


If the function is called on an empty Deque, raise the IndexError with this statement


```python
raise IndexError('pop_front() used on empty deque')
```

Runtime requirement for this function is O(1)

---

``` python
def push_back(self):
```
This function adds data to the "back" of the Deque.  Function does not return anything.  When this operation causes the number of items stored to exceed the current capcity, a resizing operation will need to take place.  Resizing always doubles the current capcity of the array.


Runtime requirement for this function is O(1) when no resizing occurs, O(n) when resizing occurs

---
``` python
def pop_back(self):
```
This function removes the  value from the "back" of the Deque. Function returns value removed.  

If the function is called on an empty Deque, raise the IndexError with this statement


```python
  raise IndexError('pop_back() used on empty deque')
```


Runtime requirement for this function is O(1)

---

``` python
  def get_front(self):
```
This function returns the value from the "front" of the Deque without removing it.  Runtime requirement for this function is O(1)

---

``` python
  def get_back(self):
```
This function returns the value from the "back" of the Deque without removing it.  Runtime requirement for this function is O(1)

---

``` python

def is_empty(self):
```
This function returns True if Deque is empty, False otherwise.  Runtime requirement for this function is O(1)

---

``` python
def __len__(self):
```
This function returns the number of values in the Deque.  Runtime requirement for this function is O(1)

---


``` python
def __getitem__(self, k):
```
This function returns the k'th value from the "front" of the Deque without removing it.  For example, if k == 0, this function would return the item at front of the Deque.  if k == 1, function would return the second item from the of the front item of the Deque.  


If k is out of range, raise the IndexError exception using the statement:

```python
raise IndexError('Index out of range')
```

Runtime requirement for this function is O(1)

---


## Part D - Overflow (10 marks):

Implementation of these function are done in a1_partd.py


### get_overflow_list() function

```python
def get_overflow_list(grid):
```

This function is passed a grid (2D array) of numbers and returns a list of 2 valued tuples (see below). You may assume the grid is rectangular (no need to test if each row has same length as the other rows).  Each cell within the grid has a number of "neighbours".  The neighbours are cells that are beside a cell either vertically or horizontally.  Thus:

* cells in the corners of the grid have exactly two neighbours
* other cells at edge of grid have exactly 3 neighbours
* cells that are not on the outside have exactly 4 neighbours

Each cell is defined by a row and column, indexed from 0.  Thus, the top left corner is row 0, column 0, and the bottom right corner is indexed (number of rows-1, number of columns-1)

The ascii picture below shows the number of neighbours each cell contains on a 4 X 5 grid:

```
|-----|-----|-----|-----|-----|
|  2  |  3  |  3  |  3  |  2  |
|-----|-----|-----|-----|-----| 
|  3  |  4  |  4  |  4  |  3  |
|-----|-----|-----|-----|-----| 
|  3  |  4  |  4  |  4  |  3  |
|-----|-----|-----|-----|-----| 
|  2  |  3  |  3  |  3  |  2  |
|-----|-----|-----|-----|-----| 

```

The number of neighbours contained within a cell define when a cell will overflow.

The grid of numbers passed to this function can be positive, negative or zero.  The absolute value of these numbers represent the number of items within each cell.

This function returns a list of tuples (row,col) indicating all the cells that will overflow.  A cell will overflow if a cell has as at least as many items as neighbours.  If there are no cells that will overflow, function returns None

The original grid must not be modified by this function


#### Example 1

For example, given the following grid:

```
|-----|-----|-----|-----|-----|
|  2  |  0  |  0  |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  | -3  |  0  |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  0  |  -2 |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  3  |
|-----|-----|-----|-----|-----| 

```

Given the above grid, the function would return the following list

[(0,0), (3,4)].  This is because both the top left and bottom right cells contain cells that are greater than or equal to the number of neighbours


#### Example 2

For example, given the following grid:

```
|-----|-----|-----|-----|-----|
|  -2 |  0  |  2  |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  | -4  |  0  |  -5 |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  0  |  -2 |  0  |  1  |
|-----|-----|-----|-----|-----| 
|  -2 |  0  |  0  |  0  |  1  |
|-----|-----|-----|-----|-----| 

```

Given the above grid, the function would return the following list

[(0,0), (1,1), (1,3), (3,0)].  the two corner cells with -2, as well as the cells with -4 and -5 have all reached or exceeded the capacity for their cells, so their locations are part of the result list.

---

### overflow() function


```python
def overflow(grid, a_queue):
```

**This function is written recursively.  An iterative solution will not be accepted and subject to resubmission with penalty**

This function is passed a grid of numbers and an instance of the Queue data structure from part C.  The absolute value of the numbers within each cell represent the number of items within a cell.  This function will perform an overflow operation on the **grid** (described in detail below) making it the result of the overflow process, adding intermediate results to **a_queue** and returning the number of grids added to **a_queue**

A grid is "overflowing" if the following conditions are both true:

a) the grid contains one or more cells that are overflowing
b) the signs of all non-zero cells are not all the same.  In otherwords, if the signs are the same, then the grid is not overflowing.

If the grid is overflowing, a new grid is created based on the following rules and added to the queue:

- you may assume that all overflowing cells will have the same sign (either all positive or all negative)
- any cell that is overflowing becomes empty (assigned 0)
- every neighbour of an overflowing cell gets one extra item
- every neighbour of an overflowing cell takes on the same sign as the overflowing cell (ie overflowing cell "takes over" its neighbours if they were not the same sign)
- all overflowing cells overflow at the same time to form the next grid


this process continues until either:
1. the grid does not contain any overflowing cells.
2. the grid contains cells with all the same signs regardless of the number of overflowing cells.

This function returns number of grids added to the queue.  Note, this is not necessarily the same as the number length of the queue as the queue does not have to be initially empty.

#### Example 1:

Suppose you are given the following:

```
|-----|-----|-----|-----|-----|
|  -2 |  2  |  -3 |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  | -4  |  0  |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  0  |  3  |  0  |  1  |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  1  |
|-----|-----|-----|-----|-----| 

cells with -2, -3, and -4 are all overflowing
```


All overflows happen at the same time resulting in the following:

```
|-----|-----|-----|-----|-----|
|  0  |  -5 |  0  |  -1 |  0  |
|-----|-----|-----|-----|-----| 
|  -2 |  0  |  -2 |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  -1 |  3  |  0  |  1  |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  1  |
|-----|-----|-----|-----|-----| 

All 3 of the overflowing cells become empty and spread.

Cell [0,1] with the -5 became -5 because it had 3 overflowing neighbours that added 1 item to that cell, it became negative because the overflowing neighbours were negative

Cell [1,0] and [1,2] -2 because it had 2 overflowing neighbours

Cell [2,1] and [0,3] became -1 because it had 1 overflowing neighbour

This grid is added to the queue

but.. not done as cell [0,1] is will overflow
```


after it overflows we get:


```
|-----|-----|-----|-----|-----|
|  -1 |  0  |  -1 |  -1 |  0  |
|-----|-----|-----|-----|-----| 
|  -2 |  -1 |  -2 |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  -1 |  3  |  0  |  1  |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  1  |
|-----|-----|-----|-----|-----| 

overflowing cell become empty and spread.


Cell [0,0] [0,2] and [1,1] became -1 because it had 1 overflowing neighbour


This grid is added to the queue


```
Above grid is done, no cells are at overflow.
function returns 2


#### Example 2:

When 2 side by side cells are set to overflow, they both overflow at the same time.  This means that they both become empty (0) and both gain one from their overflowing neighbour:

```

|-----|-----|-----|-----|-----|
|  -1 |  0  |  -1 |  -1 |  0  |
|-----|-----|-----|-----|-----| 
|  -1 |  4  |  4  |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  -1 |  3  |  0  |  1  |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  1  |
|-----|-----|-----|-----|-----| 

both cells with 4 are set to overflow

```
result:

```
|-----|-----|-----|-----|-----|
|  -1 |  1  |  2  |  -1 |  0  |
|-----|-----|-----|-----|-----| 
|  2  |  1  |  1  |  1  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  2  |  4  |  0  |  1  |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  1  |
|-----|-----|-----|-----|-----| 


The two cells with 4 became 0 at the same time, then each of them gained 1 from their neighbour that use to have 4
```
But we are not done as there is another cell with 4, so we will have to overflow that cell



```
|-----|-----|-----|-----|-----|
|  -1 |  1  |  2  |  -1 |  0  |
|-----|-----|-----|-----|-----| 
|  2  |  1  |  2  |  1  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  3  |  0  |  1  |  1  |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  1  |  0  |  1  |
|-----|-----|-----|-----|-----| 


The cell with 4 becomes 0 and each of it's neighbour gains 1 item

```

### Example 3:


Suppose you are given the following:

```
|-----|-----|-----|-----|-----|
|  -2 |  -2 |  -3 |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  | -4  |  0  |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  0  |  -3 |  0  |  -1 |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  -1 |
|-----|-----|-----|-----|-----| 

Here, there are overflowing cells, but all non-zero cells are the same sign.  Thus, this grid is not in an overflowing state.  Function does nothing and returns 0


```



### Example 4:

Suppose you are given the following:

```
|-----|-----|-----|-----|-----|
|  -1 |  -2 |  -2 |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  | -3  |  0  |  0  |  0  |
|-----|-----|-----|-----|-----| 
|  0  |  0  |  3  |  0  |  -1 |
|-----|-----|-----|-----|-----| 
|  -1 |  0  |  0  |  0  |  -1 |
|-----|-----|-----|-----|-----| 

Here, there are no overflowing cells. Thus, this grid is not in an overflowing state.  Function does nothing and returns 0

```

