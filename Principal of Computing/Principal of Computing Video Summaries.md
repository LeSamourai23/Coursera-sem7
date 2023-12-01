# Week 1
## 1. Generators
Generators in Python are a powerful and memory-efficient way to create iterators. Unlike regular functions that return a single value, generators produce a sequence of values lazily, meaning they generate values on-the-fly as requested, rather than computing and storing all values at once. This leads to efficient memory usage, especially when dealing with large datasets.

Key characteristics of generators:

1. **Yield Statement:**
   - Generators use the `yield` statement instead of `return`. When a generator function is called, it returns an iterator, and the function's state is saved. The next time `next()` is called on the iterator, the function resumes execution from where it left off.

2. **Lazy Evaluation:**
   - Values are generated one at a time and are not stored in memory. This is especially beneficial for large datasets or infinite sequences.

3. **Memory Efficiency:**
   - Generators are memory-efficient because they do not store the entire sequence in memory. Each value is generated and consumed independently.

4. **Iteration Protocol:**
   - Generators follow the Python iteration protocol, making them compatible with constructs like `for` loops and other iterable operations.

5. **Infinite Sequences:**
   - Generators can represent infinite sequences. Since values are generated on demand, it's possible to create generators that produce an endless stream of values.

Here's a simple example of a generator function that yields a sequence of square numbers:

```python
"""
Generator examples.
"""

# A list comprehension
print "max in list:", max([num * 2 - 3 for num in range(7)])

# A generator expression
print "max in gen:", max(num * 2 - 3 for num in range(7))

# A generator function
def genfunc(limit):
    num = 0
    while num < limit:
        yield num
        num = num + 1

print genfunc(7)
        
# Iteration using a generator function
print "Iterate over generator:"
for number in genfunc(7):
    print number
    
# Pass to functions expecting a sequence
print "max in gen func:", max(genfunc(4))

# Use return to end generator
def genfunc2(endfunc):
    num = 0
    while True:
        if endfunc(num):
            return
        yield num
        num = num + 1
        
def endfn(num):
    if num == 7:
        return True
    return False

print "Iterate over second generator:"
for number in genfunc2(endfn):
    print number
```

In this example, `square_numbers` is a generator function that yields the square of each number up to `n`. The generator is used in a `for` loop, and each value is generated and printed lazily. This is more memory-efficient compared to creating a list of squares, especially for large values of `n`.

## 2. Stacks and Queues
**Stacks:**

A stack is a data structure that follows the Last In, First Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. Think of it as a stack of plates where you can only take the top plate off.

- **Operations:**
  - `push`: Adds an element to the top of the stack.
  - `pop`: Removes the element from the top of the stack.
  - `peek` or `top`: Returns the element at the top of the stack without removing it.
  - `isEmpty`: Checks if the stack is empty.

- **Use Cases:**
  - Function call management (call stack in programming).
  - Undo mechanisms in applications.
  - Expression evaluation (postfix, prefix notations).

**Queues:**

A queue is a data structure that follows the First In, First Out (FIFO) principle. This means that the first element added to the queue is the first one to be removed. Think of it as a line of people waiting for a bus where the person who arrived first is the first to board.

- **Operations:**
  - `enqueue`: Adds an element to the back of the queue.
  - `dequeue`: Removes the element from the front of the queue.
  - `front`: Returns the element at the front of the queue without removing it.
  - `isEmpty`: Checks if the queue is empty.

- **Use Cases:**
  - Task scheduling in operating systems.
  - Print job management.
  - Breadth-First Search (BFS) algorithm in graph traversal.

**Comparison:**

- Stacks and queues are both linear data structures with constrained access patterns.
- Stacks are suitable for scenarios where the order of processing is last in, first out, while queues are used when the order of processing is first in, first out.
- Both can be implemented using arrays or linked lists, and variations like double-ended queues (dequeues) can combine features of both.

**A simple queue class**
```python
"""
Queue class
"""

class Queue:
    """
    A simple implementation of a FIFO queue.
    """

    def __init__(self):
        """ 
        Initialize the queue.
        """
        self._items = []

    def __len__(self):
        """
        Return the number of items in the queue.
        """
        return len(self._items)
    
    def __iter__(self):
        """
        Create an iterator for the queue.
        """
        for item in self._items:
            yield item

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        return str(self._items)

    def enqueue(self, item):
        """
        Add item to the queue.
        """        
        self._items.append(item)

    def dequeue(self):
        """
        Remove and return the least recently inserted item.
        """
        return self._items.pop(0)

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._items = []
        

```

## 3. Inheritance
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (subclass or derived class) to inherit attributes and behaviors (methods) from an existing class (base class or parent class). The subclass can then extend or override these inherited characteristics and may also introduce its own unique features.
```python
class Base:
	def hello(self):
		print "Good Morning"
	def message(self, msg):
		print msg

class Sub(Base):
	def message(self, msg):
		print "sub:", msg

baseobj = Base()
baseobj.hello()
baseobj.message("How are you")

obj = Sub()
obj.hello()
obj.message("Have a good day?")
```

## 4. BFS on Grids
Breadth First Search takes a grid, start and end points as input and returns the length of the shortest path using BFS. The grid contains 0 for open cells and 1 for obstacles. The algorithm explores the grid level by level until the destination is reached or determined to be unreachable. Adjust the grid, start, and end points according to your specific use case.

Take an example of forest fire spreading, The way we implement this is we have an underlying grid that actually stores the yellow cells. The orange cells on the boundary of the fire are actually stored in a cube. On each step, every time we click the step button, we dequeue an element off the queue, we check to see for its four neighbors. Which of those neighbours are not yellow? They haven't been burned. Those that are unburned, we add to the queue. And then when we're done, we basically take this cell and turn it yellow.
That simple algorithm allows to kind of visit all the cells in the grid in a very nice, kind of outwardly growing manner.

## 5. Growth Rate Functions

**Techniques for comparing growth rates**
In practice, comparing the growth rates of the functions that we will encounter in this class is relatively easy. Here are some simple rules that you should remember:

- Two polynomial functions **f(n)** and **g(n)** grow at the same rate if they have the same degree. Lower degree terms in these functions have no effect on the relative growth rates.
    
- If the degree of a polynomial function **f(n)** is higher than the degree of **g(n)**, **f(n)** grows faster than **g(n)**. Conversely, if the degree of **f(n)** is lower, **f(n)** grows slower than **g(n)**.
    
- The function **log⁡(n)** grows faster than the constant function 11 and slower than the linear function **n**. The function **nlog⁡(n)** grows faster than **n** and slower than **n^2**.
    
- Any exponential function **α^n** with **α>1** grows faster than any polynomial function. The factorial function **n!** grows faster than **α^n** and, consequently, faster than any polynomial function.

**Example**
```python
"""
Example comparisons of growth rates
"""

import simpleplot

def f(n):
    """
    A test function
    """
    return 0.1 * n ** 3 + 20 * n

def g(n):
    """
    A test function
    """
    return n ** 3
    #return 20 * n ** 2
    #return .1 * n ** 4

def make_plot(fun1, fun2, plot_length):
    """
    Create a plot relating the growth of fun1 vs. fun2
    """
    answer = []
    for index in range(10, plot_length):
        answer.append([index, fun1(index) / float(fun2(index))])
    simpleplot.plot_lines("Growth rate comparison", 300, 300, "n", "f(n)/g(n)", [answer])
    
# create an example plot    
make_plot(f, g, 100)
```

![[6qCx1ey6EeWo2w5fYwEDxw_c4597cdaec1c09aa71628f6edd77a239_poc_growth_plot1.png]]
![[8IhhVuy6EeWTZAooSlqjlw_28a84a5808529b14f9f5504efa29917f_poc_growth_plot2.png]]
![[9pchrey6EeW27Q44dKtmBQ_96aba8675b0e8f5505e0a1478256c7de_poc_growth_plot3.png]]

## 6. Grid Representation
```python
cells = [ [... for col in range(grid_width)] for row in range(grid_height)]
```

## 7. Breadth-First Search in Code
```python
while boundary is not empty:

    current_cell  ←  dequeue boundary

    for all neighbors neighbor_cell of current_cell:

        if neighbor_cell is not in visited:

            add neighbor_cell to visited

            enqueue neighbor_cell onto boundary
```

# Week 2

## 1. Recursion
Recursion is a programming technique where a function calls itself. It requires a base case for termination and a recursive case to solve smaller instances. Example:

```python
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

result = factorial(5)  # Returns 120
```

## 2. Binary Search
Binary search is a divide-and-conquer algorithm used to efficiently find a target element in a sorted collection. It repeatedly divides the search space in half, eliminating half of the remaining elements in each step. The algorithm compares the target element with the middle element, narrowing down the search until the target is found or the search space becomes empty.

Example Code in Python:

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  # Target found
        elif mid_val < target:
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half

    return -1  # Target not found

# Example usage
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 7

result = binary_search(sorted_array, target_element)
print(f"Index of {target_element} is {result}")
```

In this example, `binary_search` takes a sorted array and a target element as input, and it returns the index of the target element in the array. If the target is not found, it returns -1. The algorithm efficiently reduces the search space, making it particularly useful for large datasets.

## 3. Reading Files from the web
```python
# Reading files from the network

import urllib2
import codeskulptor

FILENAME = "examples_files_dracula.txt"

url = codeskulptor.file2url(FILENAME)
netfile = urllib2.urlopen(url)

#data = netfile.read()
#print data
#print type(data)

#for line in netfile.readlines():
#    print line
```

## 4. Recurrence Relation
![[Pasted image 20231129162114.png]]

# Week 3
## 1. Lambda Functions
Lambda functions in Python are anonymous, one-line functions created using the `lambda` keyword. They are often used for short, simple operations and can be passed as arguments.
```python
# Anonymous functions - Lambda

def double(val):
    return 2 * val

def square(val):
    return val ** 2

data = [1, 3, 6, 9, 18]

newdata2 = map(square, data)
print newdata2

data3 = map(lambda x: x ** 2, data)
print data3

def even(val):
    if val % 2:
        return False
    else:
        return True
    
newdata3 = filter(even, data)
print newdata3

data4 = filter(lambda val: val % 2 == 0, data)
print data4
```

## 2. Trees
Formally, a rooted [tree](http://en.wikipedia.org/wiki/Tree_(data_structure)) is a collection of nodes and edges that can be organized recursively as follows. The tree has a _root_ node with an associated value and a list of references to a collection of _subtrees_. The root nodes of these subtrees are the _children_ of the root node for the original tree while the root node is the _parent_of the children. Each node in the tree should have exactly one parent with the exception of the root which has no parent. This last condition ensures that the tree is hierarchical since each subtree of the root is then guaranteed to be disjoint from the other subtrees.
![[CJYiqOrnEeWOVQ68c1xy2w_6be08d9fcc9608d3572c1340e2269112_poc_tree_diagram.png]]
Certainly! Let's consider a simple binary tree to illustrate these concepts. 

Suppose we have the following binary tree:

```
       A
      / \
     B   C
    / \
   D   E
```

Structural Property:

1. **Number of Nodes:**
   - The root node is A, which has two children (B and C).
   - B has two children (D and E).
   - So, the total number of nodes is 5 (A, B, C, D, E).

2. **Number of Leaves:**
   - The leaves are the nodes without any children (D, E, C).
   - So, the total number of leaves is 3.

3. **Height of the Tree:**
   - The longest path from the root (A) to a leaf is A -> B -> E. So, the height is 2.

Now, let's apply the recursive definitions:

1. **Number of Nodes (in Python-like pseudocode):**
   ```python
   def num_nodes(node):
       if node is a leaf:
           return 1
       else:
           return 1 + num_nodes(left_subtree) + num_nodes(right_subtree)
   ```

   Applying this to the tree:
   ```python
   num_nodes(A) = 1 + num_nodes(B) + num_nodes(C)
                = 1 + (1 + num_nodes(D) + num_nodes(E)) + 1
                = 5
   ```

2. **Number of Leaves (in Python-like pseudocode):**
   ```python
   def num_leaves(node):
       if node is a leaf:
           return 1
       else:
           return num_leaves(left_subtree) + num_leaves(right_subtree)
   ```

   Applying this to the tree:
   ```python
   num_leaves(A) = num_leaves(B) + num_leaves(C)
                 = num_leaves(D) + num_leaves(E) + 1
                 = 3
   ```

3. **Height of the Tree (in Python-like pseudocode):**
   ```python
   def tree_height(node):
       if node is a leaf:
           return 0
       else:
           return 1 + max(tree_height(left_subtree), tree_height(right_subtree))
   ```

   Applying this to the tree:
   ```python
   tree_height(A) = 1 + max(tree_height(B), tree_height(C))
                 = 1 + max(1 + max(tree_height(D), tree_height(E)), 0)
                 = 2
   ```

These recursive functions capture the essence of the definitions provided earlier. You can use similar recursive logic in actual code to compute these properties for a given tree.

**Tree Traversal**
1. Inorder Traversal:
In inorder traversal, the left subtree is visited first, followed by the root node, and then the right subtree. It yields nodes in non-decreasing order for a binary search tree.

Example Binary Tree:
```
        1
       / \
      2   3
     / \
    4   5
```

Inorder Traversal (Result): `4 2 5 1 3`

2. Preorder Traversal:
In preorder traversal, the root node is visited first, followed by the left subtree, and then the right subtree.

Example Binary Tree:
```
        1
       / \
      2   3
     / \
    4   5
```

Preorder Traversal (Result): `1 2 4 5 3`

3. Postorder Traversal:
In Postorder traversal, the left subtree is visited first, followed by the right subtree, and then the root node.

Example Binary Tree:
```
        1
       / \
      2   3
     / \
    4   5
```

Postorder Traversal (Result): `4 5 2 3 1`

Explanation:

- Inorder Traversal:
  - Left -> Root -> Right
  - Used to get elements of BST in ascending order.

- Preorder Traversal:
  - Root -> Left -> Right
  - Used to create a copy of the tree.

- Postorder Traversal:
  - Left -> Right -> Root
  - Used to delete the tree or nodes.

## 3. Minimax
### Tic-Tac-Toe Game Tree
The following image shows a portion of the game tree for Tic-Tac-Toe:
![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/UiqAC-rnEeWOVQ68c1xy2w_cd21ff0555a4988cfffd764e826f1d7f_assets_ttt_tree.png?expiry=1701388800000&hmac=V9dyeJkCApTSERDu-sPvRLdnL_4MTcxa3JEYHl-CrbE)

In the tree, each node represents a board position, and the children of each node represent possible moves from that board position. Therefore, this tree illustrates all possible ways that a game could be played out if you start from the board position at the root node.

The Minimax algorithm applied to a game tree. Boards are scored based on outcomes, with +1 for X win, -1 for O win, and 0 for a draw. Minimax assumes players make optimal moves, maximizing for X and minimizing for O. The algorithm recursively evaluates possible moves, selecting the best ones. A sophisticated scoring function could handle larger game trees efficiently by limiting the search depth. Minimax helps make optimal decisions in turn-based games by considering the best and worst-case scenarios for both players.

# Week 4

## 1. Assertions
Assertions in Python are statements that assert a certain condition to be true. They are often used for debugging and testing purposes. In Python, the `assert` statement is used to check if a given condition evaluates to `True`. If the condition is `False`, an `AssertionError` is raised, indicating a bug or an unexpected condition.

Example in Python:

```python
def divide(a, b):
    assert b != 0, "Division by zero is not allowed"
    return a / b

result = divide(6, 2)  # Returns 3.0
result = divide(5, 0)  # Raises AssertionError: Division by zero is not allowed
```

In this example, the `assert` statement checks whether the divisor `b` is not equal to zero. If the condition is violated, the program raises an `AssertionError` with the specified message. Assertions are typically used during development to catch logical errors early. It's important to note that assertions can be disabled globally with the `-O` (optimize) command line switch or the `PYTHONOPTIMIZE` environment variable in a production environment.

## 2. Invariants
In programming, an invariant is a condition that remains true throughout the execution of a program or a specific portion of code. Invariants are crucial for ensuring the correctness of algorithms and data structures. They act as consistency checks, helping maintain a predictable state in the system.

For example, in a sorting algorithm, an invariant might be that the array remains sorted after each iteration. In a class representing a stack, an invariant could be that the elements are added and removed in a Last In, First Out (LIFO) order.

1. Loop Invariants: 
```python
def iterative_factorial(num):
    answer = 1
    index = 0

    assert answer == math.factorial(index)

    while index < num:
        index += 1
        answer *= index
        assert answer == math.factorial(index)
        
    return answer
```

2. Invariants for recursive functions:
```python
def recursive_factorial(num):
    if num == 0:
        answer = 1
        assert answer == math.factorial(num)
        
        return answer

    else:
        rec_part = recursive_factorial(num - 1)
        answer = num * rec_part
        assert answer == math.factorial(num)

        return answer
```

3. Class Invariants
```python
def boundary_invariant(self):
	for cell in self.fire_boundary():
		if self.is_empty(cell[0], cell[1]):
		  print "Cell " + str(cell) + " in fire boundary is empty."
		return False
	return True
```

## 3. Modeling
Modeling in Python involves creating abstract representations of real-world systems or processes using code. This can include mathematical models, simulations, or machine learning models, depending on the context. Python provides various libraries and frameworks for modeling, such as NumPy for numerical computing, SimPy for discrete-event simulation, and scikit-learn for machine learning.

Modeling in Python allows developers and researchers to:

1. **Solve Complex Problems:** Python's versatility enables the modeling of intricate systems, making it suitable for scientific research, engineering, and data analysis.

2. **Experimentation:** Python's ease of use and extensive libraries make it conducive for prototyping and experimenting with different models quickly.

3. **Visualization:** Python's data visualization libraries like Matplotlib and Seaborn facilitate the graphical representation of model outputs, aiding in better understanding and interpretation.

4. **Integration:** Python models can be seamlessly integrated into larger applications, workflows, or systems, promoting interoperability and reusability.

Whether simulating physical phenomena, predicting outcomes based on data, or analyzing complex systems, Python provides a flexible and powerful environment for modeling diverse scenarios.