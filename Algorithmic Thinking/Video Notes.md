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
![[Pasted image 20231201132226.png]]

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


