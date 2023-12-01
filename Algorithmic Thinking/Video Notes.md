# Week 1 
## 1. Pseudo-Code
Pseudo-code is a high-level description of a computer program or algorithm that uses a mixture of natural language and informal programming language-like constructs. It's not meant to be executed on a computer but serves as a helpful way to outline the logic of a solution before actual coding begins. Pseudo-code provides a bridge between human understanding and the eventual implementation in a specific programming language.

Here's a simple example of pseudo-code for a basic algorithm:

```plaintext
Algorithm: Find Maximum Number

Input: List of numbers

Procedure:
1. Set max_num to negative infinity (a very small number).
2. For each number in the list:
    a. If the current number is greater than max_num:
        i. Set max_num to the current number.
3. Output max_num as the maximum number in the list.
```

This pseudo-code describes an algorithm to find the maximum number in a list. It outlines the steps without using the syntax of a specific programming language, making it easy for anyone familiar with programming concepts to understand.

Here's a breakdown of the pseudo-code:

- **Algorithm Name:** Find Maximum Number
- **Input:** A list of numbers
- **Procedure:**
  1. Initialize `max_num` to negative infinity.
  2. Iterate through each number in the list.
     - If the current number is greater than `max_num`, update `max_num`.
  3. Output `max_num` as the maximum number in the list.

This pseudo-code is clear and concise, focusing on the logic rather than the syntax. Once the pseudo-code is well-defined, it can be translated into a specific programming language like Python, Java, or C++ to create a functional and executable program.

## 2. Graphs and Representation

Graphs are mathematical structures that consist of a set of vertices (or nodes) and a set of edges connecting these vertices. Graphs can be categorized into two main types: directed graphs (digraphs) and undirected graphs.

### Undirected Graphs:

In an undirected graph, edges have no direction. If there is an edge between vertices A and B, it implies that there is a connection from A to B and from B to A. Undirected graphs are symmetric.

**Notation:**
- Denoted by \( G = (V, E) \), where:
  - \( V \) is the set of vertices.
  - \( E \) is the set of edges, where each edge is an unordered pair of vertices.

**Example:**
```
Graph G:
Vertices: {A, B, C, D}
Edges: {(A, B), (B, C), (C, D), (D, A)}
```

### Directed Graphs (Digraphs):

In a directed graph, edges have a direction. If there is a directed edge from vertex A to vertex B, it doesn't necessarily mean there is an edge from B to A. Directed graphs can represent asymmetric relationships.

**Notation:**
- Denoted by \( G = (V, E) \), where:
  - \( V \) is the set of vertices.
  - \( E \) is the set of edges, where each edge is an ordered pair of vertices.

**Example:**
```
Directed Graph G:
Vertices: {A, B, C, D}
Edges: {(A, B), (B, C), (C, D), (D, A)}
```

In the directed graph example, the edge (A, B) indicates a directed edge from A to B.

### Notations:

#### 1. Adjacency Matrix:
   - For an undirected graph, the adjacency matrix is symmetric.
   - For a directed graph, it might not be symmetric.

**Undirected Graph Example:**
```
    A B C D
  +---------
A | 0 1 0 1
B | 1 0 1 0
C | 0 1 0 1
D | 1 0 1 0
```

**Directed Graph Example:**
```
    A B C D
  +---------
A | 0 1 0 1
B | 0 0 1 0
C | 0 0 0 1
D | 1 0 0 0
```

#### 2. Adjacency List:
   - Represents each vertex and its neighbors.

**Undirected Graph Example:**
```
A: B D
B: A C
C: B D
D: A C
```

**Directed Graph Example:**
```
A: B D
B: C
C: D
D: A
```

Both notations are widely used and have their own advantages depending on the specific use case and the nature of the graph. The choice between directed and undirected graphs and their respective notations depends on the relationships being modeled in a particular application or problem.

## 3. Paths and Distances
In graph theory, paths and distances are essential concepts that help analyze and understand the connectivity and relationships within a graph.

### Paths:

A path in a graph is a sequence of vertices where each adjacent pair is connected by an edge. It represents a route or a way to traverse from one vertex to another. The length of a path is the number of edges it contains.

- **Simple Path:** A path in which no vertex is repeated.

- **Cycle:** A path that starts and ends at the same vertex, without repeating any edge except the starting and ending vertex.

**Example:**
Consider the graph with vertices {A, B, C, D} and edges {(A, B), (B, C), (C, D)}.

- Path from A to D: A -> B -> C -> D
- Simple path from A to D: A -> B -> C -> D
- Cycle: None in this example.

### Distances:

The distance between two vertices in a graph is the length of the shortest path between them. It is a measure of how "far" apart two vertices are in terms of the number of edges or weights along the path.

- **Shortest Path:** The path with the minimum possible length between two vertices.

- **Distance Matrix:** A matrix representing the shortest distances between all pairs of vertices in a graph.

**Example:**
Consider the graph with vertices {A, B, C, D} and edges {(A, B), (B, C), (C, D)}.

- Shortest path from A to D: A -> B -> C -> D
- Distance matrix:
  ```
      A  B  C  D
    +------------
  A | 0  1  2  3
  B | 1  0  1  2
  C | 2  1  0  1
  D | 3  2  1  0
  ```

In the distance matrix, the entry at the ith row and jth column represents the shortest distance between vertex i and vertex j. For example, the entry at (A, D) is 3, indicating that the shortest path from A to D has a length of 3.

## 4.  Brute Force 
Brute force algorithms exhaustively consider all possible solutions without optimization. While conceptually simple, they are computationally expensive for large problems. These methods, suitable for small instances, systematically enumerate solutions, lacking scalability and efficiency. Despite limitations, brute force algorithms find use in education and as verification tools for more optimized approaches.

**Taxonomy of the problems in Brute Force:**
* Group 1: [We can do much better than brute force]
	Bipartiteness, connectivity, shortest paths, and distance
* Group 2: [We can’t do much better than brute force]
	Clique, traveling salesman
* Group 3: [Even brute force doesn’t work; there is no algorithm]
	Post correspondence problem

## 5. Algorithmic Efficiency
* When presented with a set of correct algorithms for a certain problem,
it is natural to choose the most efficient one(s) out of these algorithms.
* (In some cases, we may opt for an algorithm X that’s a bit slower than
algorithm Y, but that is much, much easier to implement than Y.)
* Efficiency:
 Time: how fast an algorithm runs
 Space: how much extra space the algorithm requires
 There’s often a trade-off between the two.
* We often investigate the algorithm’s complexity (or, efficiency) in
terms of some parameter n that indicates the algorithm’s input size
* For example, for an algorithm that sorts a list of numbers, the input’s
size is the number of elements in the list.
* For some algorithms, more than one parameter may be needed to
indicates the size of their inputs.
* For the algorithm IsBipartite, the input size is given by the number
of nodes if the graph is represented as an adjacency matrix,
whereas the input size is given by the number of nodes and
number of edges if the graph is represented by an adjacency list.

## 6. Brute Force distance between graphs
[![Jz23b7s.md.png](https://iili.io/Jz23b7s.md.png)](https://freeimage.host/i/Jz23b7s)
## 7. Degree Distribution of Graphs
Degree distribution in a graph refers to the distribution of degrees (number of edges incident to a node) across all nodes. There are three types of degree distribution: in-degree, out-degree, and in-out degree distribution.

### Example Graph:

Consider the directed graph with four nodes (A, B, C, D) and the following edges:

- (A, B), (A, C), (B, C), (C, A), (D, A)

### In-Degree Distribution:

In-degree is the number of incoming edges to a node.

- In-degree of A: 2 (incoming edges from C and D)
- In-degree of B: 1 (incoming edge from A)
- In-degree of C: 2 (incoming edges from A and B)
- In-degree of D: 1 (incoming edge from A)

**In-Degree Distribution:**
```
In-Degree   Number of Nodes
--------------------------
   0            0
   1            2 (B, D)
   2            2 (A, C)
```

### Out-Degree Distribution:

Out-degree is the number of outgoing edges from a node.

- Out-degree of A: 2 (outgoing edges to B and C)
- Out-degree of B: 1 (outgoing edge to C)
- Out-degree of C: 1 (outgoing edge to A)
- Out-degree of D: 0 (no outgoing edges)

**Out-Degree Distribution:**
```
Out-Degree   Number of Nodes
---------------------------
   0            1 (D)
   1            2 (B, C)
   2            1 (A)
```

### In-Out Degree Distribution:

In-out degree is the sum of in-degree and out-degree for a node.

- In-out degree of A: 4 (in-degree 2 + out-degree 2)
- In-out degree of B: 2 (in-degree 1 + out-degree 1)
- In-out degree of C: 3 (in-degree 2 + out-degree 1)
- In-out degree of D: 1 (in-degree 1 + out-degree 0)

**In-Out Degree Distribution:**
```
In-Out Degree   Number of Nodes
-------------------------------
      0                0
      1                1 (D)
      2                1 (B)
      3                1 (C)
      4                1 (A)
```

Understanding these degree distributions provides insights into the connectivity patterns and overall structure of the directed graph.

# Week 2
## 1. Order of Growth
* When analyzing the complexity, or efficiency, of algorithms, we pay special attention to the order of growth of the number of steps of an algorithm on large input sizes.
* The complexity analysis framework ignores multiplicative constants and concentrates on the order of growth of the number of steps to within a constant multiple for large-size inputs.
![Order of Growth](https://www.cs.odu.edu/~toida/nerzic/content/function/growth_files/summary.gif?w=144)

## 2. Asymptotics
Asymptotic notations, such as Big O, Big Omega, and Big Theta, are mathematical tools used to describe the efficiency or complexity of algorithms in computer science. They provide a concise way to express the growth rate of algorithms as input sizes approach infinity.

1. **Big O Notation (O):**
   - Represents the upper bound or worst-case scenario of an algorithm's time complexity. It describes how an algorithm's execution time grows in relation to the input size but does not provide information about the actual performance.

2. **Big Omega Notation (Ω):**
   - Represents the lower bound or best-case scenario of an algorithm's time complexity. It describes the minimum growth rate of an algorithm, indicating that the algorithm will not perform better than this under any circumstances.

3. **Big Theta Notation (Θ):**
   - Represents both the upper and lower bounds, providing a tight bound on an algorithm's time complexity. It characterizes the average-case performance of an algorithm and provides a more precise estimation of its behavior.

Asymptotic notations are crucial for comparing and analyzing algorithms independently of machine-specific details. They simplify discussions about efficiency, aiding in algorithm selection and design based on the expected input size and performance requirements. For example, an algorithm with O(n^2) time complexity is less efficient than one with O(n log n) when handling large datasets.

**Theorem**: If T1(n)=O(f1(n)) and T2(n)=O(f2(n)) then T1(n)+T2(n)=O(max{f1(n),f2(n)}).
 Examples:
* n + n^2 = O(n^2)
* log n + n = O(n)
* 1 + n + n^2 + 106*n^3 + 2*n^4 = O(n4)

## 3. Breadth First Search and Graph Exploration
Graph exploration can be done:
* deterministically: using, for example, breadth-first search (BFS) or depth-first search (DFS)
* nondeterminstically: using random walks.

Breadth-First Search (BFS) is a fundamental algorithm for traversing or searching tree or graph data structures. It explores all the vertices of a graph in breadth-first order, visiting all the neighbors of a vertex before moving on to their neighbors.

### Key Characteristics:

1. **Queue-based Approach:**
   - BFS employs a queue data structure to keep track of vertices to be visited. The vertices are visited in the order they are enqueued.

2. **Level Order Traversal:**
   - BFS explores vertices level by level, starting from the source vertex. It systematically visits all vertices at the current level before moving to the next level.

3. **Shortest Path:**
   - When BFS is applied to unweighted graphs, it guarantees finding the shortest path from the source vertex to all other vertices.

4. **Connected Components:**
   - BFS can be used to find connected components in an undirected graph.

### Algorithm Steps:

1. Enqueue the source vertex into the queue and mark it as visited.
2. While the queue is not empty:
   - Dequeue a vertex and process it.
   - Enqueue all unvisited neighbors of the processed vertex.
   - Mark the neighbors as visited.

### Example:

Consider the graph with vertices {A, B, C, D, E} and edges {(A, B), (A, C), (B, D), (C, D), (D, E)}.

**BFS from A:**
```
Visited Order: A -> B -> C -> D -> E
```

### Applications:

1. **Shortest Path Finding:**
   - BFS can find the shortest path in an unweighted graph.

2. **Connected Components:**
   - Identifying connected components in an undirected graph.

3. **Web Crawling:**
   - Crawling web pages where links represent edges, exploring websites level by level.

4. **Puzzle Solving:**
   - Solving puzzles like the sliding tile puzzle using BFS to find the shortest sequence of moves.

## 4. Pseudo-code and Efficiency of BFS
**Pseudo-code for BFS:**

```plaintext
BFS(Graph G, Vertex source):
    queue = new Queue()
    visited = new Set()
    
    queue.enqueue(source)
    visited.add(source)

    while queue is not empty:
        current_vertex = queue.dequeue()
        process(current_vertex)  // Process or print the current vertex
        
        for neighbor in G.adjacent_vertices(current_vertex):
            if neighbor not in visited:
                queue.enqueue(neighbor)
                visited.add(neighbor)
```

This pseudo-code outlines the basic steps of BFS. It uses a queue to keep track of vertices to be visited and a set to keep track of visited vertices. The process function represents any action you want to take when visiting a vertex, such as printing its value.

**Efficiency of BFS:**

- **Time Complexity:** In the worst case, where all vertices and edges are explored, the time complexity is O(V + E), where V is the number of vertices and E is the number of edges. This is because each vertex and edge is visited once.

- **Space Complexity:** The space complexity is O(V) due to the queue and visited set. In the worst case, all vertices may be enqueued, and the visited set may store all vertices.

BFS is efficient for exploring and traversing graphs, especially when the goal is to visit all vertices reachable from the source in a systematic order. Its time and space complexity make it suitable for applications such as shortest path finding in unweighted graphs and exploring connected components.

# Week 3
## Algorithmic Thinking
1. **Understanding the problem:**
	✤ Understand the description of the problem.
	✤ What are the input/output?
	✤ Do a few examples by hand.
	✤ Think about special cases.

2.  **Formulating the Problem:**
	✤ Think about the data and the best way to represent them (graphs, strings, etc.)
	✤ What mathematical criterion corresponds to the desired output?

3.  **Designing an Algorithm:**
	✤ Is the formulated problem amenable to a certain algorithm design technique (greedy, divide-and-conquer, etc.)?
	✤ What data structures make sense to use?
	✤ Is the algorithm correct?
	✤ Is the algorithm efficient?
	✤ If the problem is “too hard,” do we want an approximation algorithm, a randomized algorithm, a heuristic, ...?

4. **Implementing the Algorithm:**
	✤ Most algorithms are destined to be ultimately implemented as computer programs.
	✤ Programming an algorithm presents both a peril and an opportunity.
	✤ The peril lies in the possibility of making the transition from an algorithm to a program either incorrectly or very inefficiently.
	✤ Special mathematical techniques have been developed for proving program correctness, but the power of these techniques is still limited to very small programs.
	✤ As a practical matter, the validity of programs is still established by testing.
	✤ Program correctness is necessary but not sufficient: You would not want to diminish your algorithm’s power by an inefficient implementation.
	✤ The opportunity lies in the possibility to better understand the algorithm and even to improve it.

5. **Solving the Original Problem:**
	✤ Once the algorithm is implemented, it is run on data to solve the original problem.
	✤ Sometimes, it is discovered after this entire process is followed, that
	the solution is not satisfactory. This might require going back to step
	(1) and repeating the entire process.

## 2. Merge Sort
Merge Sort is a divide-and-conquer sorting algorithm that divides the input array into two halves, recursively sorts each half, and then merges the sorted halves to produce a sorted array. It is known for its stability and guaranteed time complexity of O(n log n).

### Merge Sort Pseudocode:

```plaintext
Algorithm: Merge Sort

merge_sort(arr):
    if length of arr <= 1:
        return arr  // Already sorted
    
    // Divide the array into two halves
    middle = length of arr / 2
    left_half = merge_sort(arr[0 to middle-1])
    right_half = merge_sort(arr[middle to end])
    
    // Merge the sorted halves
    merged_array = merge(left_half, right_half)
    return merged_array

merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    // Compare elements from left and right arrays
    while left_index < length of left and right_index < length of right:
        if left[left_index] <= right[right_index]:
            append left[left_index] to merged
            left_index++
        else:
            append right[right_index] to merged
            right_index++
    
    // Add remaining elements (if any) from left and right arrays
    append remaining elements from left[left_index to end] to merged
    append remaining elements from right[right_index to end] to merged
    
    return merged
```

### Explanation:

1. The `merge_sort` function recursively divides the input array into two halves until the base case is reached (when the array has one or zero elements).

2. The `merge` function takes two sorted arrays (`left` and `right`) and merges them into a single sorted array. It compares elements from both arrays and appends the smaller element to the `merged` array.

3. The merging process continues until one of the arrays is exhausted. Any remaining elements in the non-empty array are appended to the `merged` array.

4. The merged array is then returned.

### Example:

Let's consider an example with the array `[38, 27, 43, 3, 9, 82, 10]`.

```plaintext
merge_sort([38, 27, 43, 3, 9, 82, 10])

// Divide
merge_sort([38, 27, 43]) + merge_sort([3, 9, 82, 10])

// Divide further
merge_sort([38]) + merge_sort([27, 43]) + merge_sort([3]) + merge_sort([9, 82, 10])

// Merge
[38] + merge([27], [43]) + [3] + merge([9], [82, 10])

// Final Merge
merge([38], merge([27, 43], [3]), merge([9], [10, 82]))
```

The final merged array will be the sorted version of the input array `[38, 27, 43, 3, 9, 82, 10]`.

## 3. Recurrence of Merge Sort
The recurrence relation for Merge Sort describes the time complexity of the algorithm in terms of the time complexity of its subproblems. Merge Sort uses a divide-and-conquer approach, dividing the array into two halves, recursively sorting each half, and then merging them. The recurrence relation helps express the time complexity as a function of the size of the input.

### Recurrence Relation for Merge Sort:

Let \( T(n) \) represent the time complexity of Merge Sort on an input array of size \( n \). The recurrence relation is given by:

$[ T(n) = 2T\left(\frac{n}{2}\right) + O(n)]$

- $( T(n) )$: Time taken to sort an array of size \( n \).
- $( 2T\left(\frac{n}{2}\right) )$: Time taken to sort two subarrays of size \( \frac{n}{2} \) each.
- $( O(n) )$: Time taken for the merging step, where each element is compared and placed in the correct order.

### Recurrence Tree:

The recurrence relation can be visualized as a recurrence tree, where each level represents a recursive call, and the nodes at each level represent the time complexity of sorting a subarray of a specific size. At each level, the work done is \( O(n) \) for merging.

For example, for an array of size \( n \):

- Level 0: \( n \) (initial array)
- Level 1: $( \frac{n}{2} + \frac{n}{2} )$ (two subarrays of size $( \frac{n}{2} )$ each)
- Level 2: $( \frac{n}{4} + \frac{n}{4} + \frac{n}{4} + \frac{n}{4} )$ (four subarrays of size $( \frac{n}{4} )$ each)
- ...

The total work done is the sum of work at each level, which can be expressed as a geometric series.

### Time Complexity:

The solution to the recurrence relation is \( T(n) = O(n \log n) \), indicating that Merge Sort has a time complexity of \( O(n \log n) \). This makes it an efficient sorting algorithm, particularly for large datasets, as it guarantees a consistent time complexity regardless of the input arrangement.

## 4. Master Theorem and MergeSort Efficiency
The **Master Theorem** is a mathematical tool for analyzing the time complexity of divide-and-conquer algorithms, particularly those with specific recurrence relations. It provides a method for determining time complexity based on the structure of recursive algorithms.

The recurrence relation for the time complexity of **Merge Sort** is given by:

$[ T(n) = 2T\left(\frac{n}{2}\right) + O(n) ]$

Here:
- \( a = 2 \) (two recursive calls),
- \( b = 2 \) (input size is halved in each recursive call),
- $( f(n) = O(n) )$ (work done for merging).

### Master Theorem Cases:

1. **Case 1:** If $( f(n) )$ is $( O(n^c) )$, where $( c < \log_b a )$, then the time complexity is $( \Theta(n^{\log_b a}) )$.

2. **Case 2:** If $( f(n) )$ is $( \Theta(n^{\log_b a} \log^k n) )$, where $( k \geq 0 )$, then the time complexity is $( \Theta(n^{\log_b a} \log^{k+1} n) )$.

3. **Case 3:** If $( f(n) )$ is $( \Omega(n^c) )$, where $( c > \log_b a )$, and $( af\left(\frac{n}{b}\right) \leq kf(n) )$ for some $( k < 1 )$ and sufficiently large $( n )$, then the time complexity is $( \Theta(f(n)) )$.

### Merge Sort Analysis:

In the case of Merge Sort, $( a = 2 )$, $( b = 2 )$, and $( f(n) = O(n) )$. The recurrence relation falls into **Case 1** because $( \log_b a = \log_2 2 = 1 )$, and $( c = 0 )$. Thus, the time complexity of Merge Sort is $( \Theta(n^{\log_b a}) = \Theta(n^1) = \Theta(n) )$.

In summary, the Master Theorem confirms that the time complexity of Merge Sort is $( \Theta(n \log n) )$, making it an efficient algorithm for sorting large datasets.

## 5. Linear and Binary Search
### Binary Search:

**Algorithm:**
Binary Search is an efficient algorithm for finding a specific value in a sorted array.

```plaintext
Algorithm: Binary Search

binary_search(arr, target):
    low = 0
    high = length of arr - 1
    
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == target:
            return mid  // Target found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  // Target not found
```

**Time Complexity:**
- Best Case: O(1) (when the target is found in the middle on the first try)
- Worst Case: O(log n) (when repeatedly dividing the array in half)
- Average Case: O(log n)

**Space Complexity:**
- O(1) (constant space, as only a few variables are used)

### Linear Search:

**Algorithm:**
Linear Search is a simple algorithm that sequentially checks each element in a list until a match is found.

```plaintext
Algorithm: Linear Search

linear_search(arr, target):
    for i from 0 to length of arr - 1:
        if arr[i] == target:
            return i  // Target found
    
    return -1  // Target not found
```

**Time Complexity:**
- Best Case: O(1) (when the target is the first element)
- Worst Case: O(n) (when the target is at the end or not present)
- Average Case: O(n)

**Space Complexity:**
- O(1) (constant space, as only a few variables are used)

### Comparison:
* **Binary Search:**
  - Requires a sorted array.
  - Efficient for large datasets.
  - Divide-and-conquer approach.

- **Linear Search:**
  - Works on both sorted and unsorted arrays.
  - Simple and straightforward.
  - Sequential approach.

In summary, Binary Search is more efficient for searching in sorted arrays, with a time complexity of O(log n), while Linear Search is suitable for smaller datasets or unsorted arrays, with a time complexity of O(n). The choice depends on the nature of the data and the search requirements.

# Week 4
## 1. RNA Secondary Structure Problem
The RNA Secondary Structure Problem is a computational biology problem that involves predicting the secondary structure of a given RNA (ribonucleic acid) sequence. The secondary structure refers to the spatial arrangement of base pairs within the RNA molecule, including the formation of helices, loops, and other structures.

RNA is composed of nucleotides, and the four types of RNA nucleotides are adenine (A), cytosine (C), guanine (G), and uracil (U). The secondary structure is determined by the complementary base pairing between adenine and uracil (A-U) and between guanine and cytosine (G-C).

### Problem Statement:
Given an RNA sequence, the RNA Secondary Structure Problem involves predicting how the nucleotides will pair with each other to form stable secondary structures. The goal is to identify the base pairs and the resulting helices and loops in the secondary structure.

### Imagine a String of Letters:
Think of a long string made up of only four letters: A, U, G, and C. Each letter represents a building block in a special molecule called RNA.

### Base Pairing Rules:
Now, there are some rules for how these letters can stick together:

- A pairs with U.
- G pairs with C.

So, if you have the sequence AU, it means that A and U are stuck together. Similarly, GC means G and C are paired up.

### Building Structures:
RNA molecules can fold and form structures like helices (twists) and loops. The challenge is to figure out how these letters pair up to create the most stable structure, following the pairing rules.

### Computational Problem:
The RNA Secondary Structure Problem in computational biology is about using computer algorithms to predict how these letters in the RNA sequence will pair up to form the most stable and meaningful structures.

### Dynamic Programming:
Dynamic programming algorithms, such as the Nussinov algorithm and the Zuker algorithm, are commonly used for predicting RNA secondary structures. These algorithms aim to find the optimal pairing of nucleotides by considering the stability of the secondary structure.

## 2. Closest Pair Problem

The Closest Pair Problem is a computational problem that involves finding the two points in a set of points in a two-dimensional space that are closest to each other. The "closeness" is typically measured as the Euclidean distance between points.

### Problem Statement:

Given a set of points \( P \) in a 2D plane, the goal is to find the pair of points \( (p_i, p_j) \) where \( p_i \) and \( p_j \) are distinct points in \( P \), and the Euclidean distance between them is minimized.

### Brute Force Approach:

One straightforward approach is to compute the distance between every pair of points and find the minimum distance. However, this has a time complexity of \( O(n^2) \), where \( n \) is the number of points, making it inefficient for large datasets.

### Efficient Divide and Conquer Approach:

The Divide and Conquer approach provides a more efficient solution with a time complexity of \( O(n \log n) \).

**Algorithm: Closest Pair (Divide and Conquer)**

**Imagine a Maze:**
Think of a big maze filled with many twists and turns. Your goal is to find the two people in the maze who are closest to each other.

**Divide:**
Instead of trying to find the closest pair directly in the entire maze, you decide to make the problem simpler. You divide the maze into smaller sections. Each section is like a mini-maze.

**Conquer:**
Now, you focus on each mini-maze separately. You apply the same strategy to each mini-maze: find the two closest people within that smaller space. It's easier to handle a small maze than the entire big maze.

**Combine:**
After finding the closest pairs in each mini-maze, you look at the borders between these mini-mazes. Why? Because the closest pair might involve one person from one mini-maze and another from a neighboring mini-maze.

This Divide and Conquer algorithm recursively divides the set of points, solves the closest pair problem in each half, and then merges the solutions efficiently. The middle strip ensures that pairs with one point on each side of the division line are considered.

## Data Clustering

### K-Means Clustering:

**Note:**
K-Means is a partitioning-based clustering algorithm that groups data points into K clusters. It aims to minimize the sum of squared distances between data points and the centroid of their assigned cluster.

**Algorithm Steps:**
1. Randomly initialize K centroids (representative points for clusters).
2. Assign each data point to the nearest centroid, forming K clusters.
3. Recalculate the centroids as the mean of data points in each cluster.
4. Repeat steps 2-3 until convergence or a predetermined number of iterations.

**Example:**
Consider customer data for online shopping. K-Means clustering could be used to group customers based on their purchase behavior, such as frequency, recency, and monetary value. This helps identify customer segments for targeted marketing.

### Hierarchical Clustering:

**Note:**
Hierarchical Clustering builds a tree-like hierarchy of clusters, either from the bottom-up (agglomerative) or top-down (divisive). It captures relationships between data points at different levels of granularity.

**Algorithm Steps (Agglomerative):**
1. Treat each data point as a single cluster.
2. Merge the closest clusters iteratively until only one cluster remains.
3. Build a dendrogram (tree structure) to represent the merging process.

**Example:**
In biology, hierarchical clustering can be applied to gene expression data. The algorithm helps identify groups of genes with similar expression patterns, allowing researchers to explore relationships and potential functional connections.

### Examples of Applications:

1. **K-Means:**
   - **E-commerce:** Segmenting customers for personalized marketing.
   - **Image Compression:** Reducing image size while preserving essential features.

2. **Hierarchical Clustering:**
   - **Biology:** Understanding genetic relationships and evolutionary trees.
   - **Market Research:** Grouping products or services based on similarity for strategic planning.

### Considerations:

1. **K-Means:**
   - Sensitive to initial centroids (may converge to local minima).
   - Assumes spherical clusters of similar sizes.

2. **Hierarchical Clustering:**
   - No need to specify the number of clusters beforehand.
   - Dendrogram visualization helps in understanding hierarchy.

In practice, the choice between these algorithms depends on the nature of the data and the goals of the analysis. K-Means is suitable for well-defined, compact clusters, while hierarchical clustering is versatile and captures hierarchical relationships within the data.

## 5. Dynamic Programming
To set about developing an algorithm based on dynamic programming, one needs a collection of subproblems derived from the original problem that satisfies a few basic properties:!
* The solution to the original problem can be easily computed from the
	solutions to the subproblems (for example, the original problem may
	actually be one of the subproblems).!
* There is a natural ordering on subproblems from “smallest” to “largest,”
	together with an easy-to-compute recurrence that allows one to determine the solution to a subproblem from the solutions to some number of smaller subproblems.

![DP](https://i.ibb.co/LtBwW1k/image.png[/img)

**[READ THIS!](https://storage.googleapis.com/codeskulptor-alg/pdf/DynamicProgramming.pdf)**
