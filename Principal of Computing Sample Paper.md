## Q1 (a). Describe the different types of invariants with the help of example.
**Ans.** 
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

## Q1 (b). What is inheritance? Write the output of the code with explanations.
**Ans.**
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

## Q1 (c). What are the uses of recurrence?
**Ans.**
Recurrence in Python, often associated with recursion, has various uses in programming. Here are some common applications:

1. **Solving Problems with Divisible Subproblems:**
   - Many problems can be naturally divided into smaller subproblems that are similar to the original problem. Recurrence is used to express the solution to the overall problem in terms of solutions to its subproblems. Dynamic programming often utilizes recurrence to solve problems efficiently.

2. **Mathematical Calculations:**
   - Recurrence is commonly used in mathematics to define sequences or functions recursively. For example, the Fibonacci sequence is defined using recurrence: \( F(n) = F(n-1) + F(n-2) \).

3. **Tree and Graph Traversals:**
   - Recursive algorithms are often employed for tree and graph traversals. For example, depth-first search (DFS) and breadth-first search (BFS) can be implemented using recurrence to explore and process nodes.

4. **Binary Tree Operations:**
   - Recursive approaches are commonly used for binary tree operations such as traversal (inorder, preorder, postorder), searching, insertion, and deletion.


## Q2  (a). Describe the method of creating generator in python with an example.
**Ans.**
Generators are a way of programmatically producing a sequence of values in Python. In some ways, generators are like lists. Lists are a sequence of values and I can iterate over them, however the list exists in its entirety at once. And you can do other things besides iterate over them.
Generators, on the other hand, do not, they, produce the entire sequence at once. Rather, they produce the sequence as you iterate over them. So, they're only producing one value at a time. This can be significantly more efficient, especially when you're producing large sequences of values.
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
        yield num     #Function is not over, unlike in return
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

## Q2 (b). Explain with example, the built- in functions in python that can be used along with lambda function.
**Ans.**
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

## Q2 (c). Write the code in python to read a file from network.
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

## Q3 (a). Define the rooted binary tree and describe its components with a neat diagram. Describe its structural properties also.
### Ans.
Basic definition and display
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

## Q3 (b). What are the different applications of binary tree?
**Ans.**
Tic-Tac-Toe Game Tree

The following image shows a portion of the game tree for Tic-Tac-Toe:

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/UiqAC-rnEeWOVQ68c1xy2w_cd21ff0555a4988cfffd764e826f1d7f_assets_ttt_tree.png?expiry=1701302400000&hmac=Ufu0RqsLOb2I3Ee_SyR-zYNi8jQ5XugiuVauQmXS6sU)

In the tree, each node represents a board position, and the children of each node represent possible moves from that board position. Therefore, this tree illustrates all possible ways that a game could be played out if you start from the board position at the root node.
It uses Minimax strategy.
Minimax is a decision-making algorithm commonly used in two-player, zero-sum games. It aims to find the optimal move for the maximizing player while assuming that both players play optimally. The algorithm explores the game tree, assigning scores to each possible move based on the outcome of the game. The maximizing player seeks to maximize their score, while the minimizing player aims to minimize the score. The algorithm recursively evaluates moves until reaching leaf nodes, where scores are assigned. Alternating between maximizing and minimizing players, Minimax determines the best move for the maximizing player, assuming optimal play by both players.

## Q3 (c). Differentiate between return and yield statement used in a function.
The `return` statement is used in a function to immediately send a value back to the caller and terminate the function's execution. Once a `return` statement is encountered, the function exits, and any subsequent code is not executed.

On the other hand, the `yield` statement is used in a function to produce a sequence of values for iteration, allowing the function to be paused and resumed. When a function contains a `yield` statement, it becomes a generator. Each time the generator is iterated, it produces the next value in the sequence until there are no more values to yield.

In short, `return` sends a value back and ends the function, while `yield` produces a sequence of values, allowing the function to be paused and resumed during iteration.

## Q4 (a). Write a program in python to solve the problem of determining the count of binary numbers of length n using recurrence.
**Ans.**
```python
def count_binary_numbers(n):
    # Base cases
    if n == 1:
        return 2  # '0' and '1'
    if n == 2:
        return 3  # '00', '01', '10'

    # Recurrence relation: F(n) = F(n-1) + F(n-2)
    return count_binary_numbers(n-1) + count_binary_numbers(n-2)

# Example usage
n = 4
result = count_binary_numbers(n)
print(f"The count of binary numbers of length {n} without consecutive 1s is: {result}")
```

## Q4 (b). Explain the three types of tree traversal in binary trees with example? 
**Ans.**
Tree traversal refers to the process of visiting and processing each node in a tree data structure. In binary trees, where each node has at most two children (left and right), there are three main types of tree traversal: inorder, preorder, and postorder.

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

## Q4 (c). How can the breadth first search technique be implemented using a grid? 
**Ans.**
The `bfs` function takes a grid, start and end points as input and returns the length of the shortest path using BFS. The grid contains 0 for open cells and 1 for obstacles. The algorithm explores the grid level by level until the destination is reached or determined to be unreachable. Adjust the grid, start, and end points according to your specific use case.
## Q5 (a). Which types of problems can be solved using recursion? Explain the two parts of recursive function. Write a recursive function in python to check whether the given string strings “Malayalam” and “Kannada” is palindrome or not.
**Ans.**
Recursion is a powerful technique that can be applied to solve various types of problems. Here are some types of problems that can be effectively solved using recursion:

1. **Divide and Conquer Problems:**
   - Problems that can be broken down into smaller, simpler subproblems. Recursive solutions can then be applied to solve these subproblems, and their results combined to solve the original problem.

2. **Search and Traverse Problems:**
   - Tree and graph traversal problems, where exploring nodes or paths involves repeated patterns that can be naturally expressed using recursion.

3. **Backtracking Problems:**
   - Problems that involve exploring possibilities and undoing choices if they lead to dead ends. Backtracking algorithms often use recursion to explore different paths.

4. **Dynamic Programming Problems:**
   - Problems that exhibit overlapping subproblems and optimal substructure. Recursive solutions combined with memoization can be applied to efficiently solve such problems.

5. **Mathematical Calculations:**
   - Problems involving mathematical calculations, sequences, and series often have recursive solutions.

### Parts of a Recursive Function:

A recursive function typically consists of two parts:

1. **Base Case:**
   - The base case defines the simplest scenario where the function does not make a recursive call and directly returns a result.
   - It prevents the recursion from continuing indefinitely and provides a termination condition.

2. **Recursive Case:**
   - The recursive case defines the general logic of the function, including one or more recursive calls to solve smaller instances of the problem.
   - It breaks down a complex problem into simpler subproblems and leverages the results of recursive calls.

### Recursive Function to Check Palindrome:

Here's a recursive function in Python to check whether a given string is a palindrome or not:

```python
def is_palindrome(s):
    # Base case: an empty string or a string with one character is a palindrome
    if len(s) <= 1:
        return True

    # Recursive case: check if the first and last characters are the same
    # and recursively check the substring between them
    return s[0] == s[-1] and is_palindrome(s[1:-1])

# Example usage
string1 = "Malayalam"
string2 = "Kannada"

result1 = is_palindrome(string1.lower())
result2 = is_palindrome(string2.lower())

print(f"{string1} is a palindrome: {result1}")
print(f"{string2} is a palindrome: {result2}")
```

In this example, the `is_palindrome` function uses recursion to check whether a given string is a palindrome. The base case handles strings with one or zero characters, while the recursive case compares the first and last characters and recursively checks the substring between them. The strings are converted to lowercase for case-insensitive palindrome checks.

## Q5 (b). Differentiate lambda functions from a normal def defined functions with the help of example.
**Ans.**
```python
# Normal Function
def even(val):
    if val % 2:
        return False
    else:
        return True
    
newdata3 = filter(even, data)
print newdata3

# Lambda Function
data4 = filter(lambda val: val % 2 == 0, data)
print data4
```

## Q5 (c). Which data structure can be used to implement the recursive function and why?
Recursive functions are more naturally associated with the call stack, where each function call creates a new frame on the stack. The Last In, First Out (LIFO) property of the call stack is well-suited for managing the flow of recursive function calls.