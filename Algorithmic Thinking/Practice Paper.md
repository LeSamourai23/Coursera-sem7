# Q1 (A). Explain the hierarchical and k means clustering algorithm. Analyze their efficiency.
**Ans.**
**K-mean Clustering:**
K-means clustering is a simple and widely used unsupervised machine learning algorithm that iteratively groups a collection of data points into a fixed number of clusters (k) according to their similarity. The algorithm aims to reduce the distance between each data point and its corresponding cluster center, also called the centroid. The algorithm terminates when either the centroids remain stable, or a maximum number of iterations is achieved. K-means clustering has various applications, such as data analysis, image segmentation, anomaly detection, etc.

**Hierarchical Clustering:**
Hierarchical clustering is a type of unsupervised machine learning algorithm that organizes data points into a hierarchy of clusters based on their similarity or distance. It is also called hierarchical cluster analysis or HCA. Hierarchical clustering has two variants: agglomerative and divisive.

**_Agglomerative clustering:_** _begins with each data point as a separate cluster and then combines the nearest clusters until there is only one cluster left._

**_Divisive clustering:_** _begins with all data points in a single cluster and then divides the cluster repeatedly until each data point has its own cluster._

Hierarchical clustering can be represented by a dendrogram, which is a graph that illustrates the nested arrangement of clusters and their distances. Hierarchical clustering has various uses, such as finding patterns, discovering hierarchies, or detecting outliers in data._

![[1 2EvKLztx03IB-y8oWXbMLw.webp]]

# Q1 (b). Can you use binary search on a list that is sorted in descending order? Justify. 
**Ans.**
Yes, binary search can be used on a list sorted in descending order. The algorithm's logic remains the same: compare the middle element with the target value and adjust the search direction based on the result. The sorting order does not affect the binary search's ability to efficiently find the target in a sorted list.

# Q1 (c). Differentiate between in-place sorting and out-of-place sorting algorithms. Give an example for each.
**Ans.**
**In-Place Sorting:**
- **Definition:** In-place sorting algorithms rearrange the elements of the input data structure without requiring additional memory space proportional to the input size.
- **Advantage:** Efficient in terms of memory usage.
- **Disadvantage:** May involve complex swaps, potentially affecting performance.
- Example: **Bubble Sort**

**Out-of-Place Sorting:**
- **Definition:** Out-of-place sorting algorithms create a new data structure to store the sorted elements, leaving the original input unchanged.
- **Advantage:** Preserves the integrity of the original data.
- **Disadvantage:** Requires additional memory space. 
- Example: **Merge Sort** 

# Q2 (a). Explain the method of sorting a list using merge sort algorithm. Name the algorithm design technique used in merge sort. Illustrate the same for the following set of numbers: 34, 56, 67,23, 89,25,19.
**Ans.**
### Merge Sort Algorithm:

**Design Technique: Divide and Conquer**
- **Divide:** Split the unsorted list into \(n\) sublists, each containing one element.
- **Conquer:** Recursively merge adjacent sublists until there is only one sublist remaining.

### Merge Sort Illustration:

Let's apply Merge Sort to the set of numbers: 34, 56, 67, 23, 89, 25, 19.

1. **Divide:**
   - Split the list into individual elements: [34], [56], [67], [23], [89], [25], [19].

2. **Conquer (Recursive Merge):**
   - Merge adjacent pairs of sublists in a sorted manner.
   - [34, 56], [23, 67], [25, 89], [19].
   - [23, 34, 56, 67], [19, 25, 89].

3. **Final Merge:**
   - Merge the remaining two sorted sublists into a single sorted list.
   - [19, 23, 25, 34, 56, 67, 89].

### Pseudo Code for Merge Sort:
```Text File
merge_sort(arr):
    if length(arr) > 1:
        mid = length(arr) // 2
        left_half = arr[0 to mid - 1]
        right_half = arr[mid to end]

        // Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        // Merge the sorted halves
        merge(arr, left_half, right_half)

merge(arr, left_half, right_half):
    i = j = k = 0

    // Merge elements from left_half and right_half into arr in sorted order
    while i < length(left_half) and j < length(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i = i + 1
        else:
            arr[k] = right_half[j]
            j = j + 1
        k = k + 1

    // Copy remaining elements from left_half, if any
    while i < length(left_half):
        arr[k] = left_half[i]
        i = i + 1
        k = k + 1

    // Copy remaining elements from right_half, if any
    while j < length(right_half):
        arr[k] = right_half[j]
        j = j + 1
        k = k + 1

```
### Explanation:

- The list is repeatedly divided into smaller sublists until each sublist contains only one element.
- The merging process combines sorted sublists to create larger sorted sublists.
- This recursive division and merging continue until the entire list is sorted.

**Time Complexity:**
- Merge Sort has a time complexity of \(O(n \log n)\), making it efficient for large datasets.

In summary, Merge Sort is a divide-and-conquer algorithm that efficiently sorts a list by repeatedly dividing it into smaller parts, sorting those parts, and then merging them back together.

# Q2 (b). What does it mean when we say that an algorithm X is asymptotically more efficient than Y?
**Ans.**
When we say that algorithm X is asymptotically more efficient than algorithm Y, we are comparing their growth rates as the input size increases. Specifically, X outperforms Y in handling larger inputs over time. This comparison is expressed using Big O notation, where X has a lower-order complexity than Y. Asymptotic efficiency focuses on the dominant terms of the algorithms' time or space complexities. For example, if the time complexity of X is $O(n log n)$ and Y is $O(n^2)$, X is asymptotically more efficient as n approaches infinity, meaning X will handle larger inputs more effectively than Y in the long run.

# Q2 (c). Differentiate between following: in-degree, out-degree, and degree of node. 
**Ans.**
- **In-Degree:** The number of edges directed towards a node in a directed graph.
- **Out-Degree:** The number of edges directed away from a node in a directed graph.
- **Degree of Node:** The total number of edges connected to a node, including both incoming and outgoing edges in an undirected graph. In-degree and out-degree apply specifically to directed graphs, while the degree of a node is applicable to both directed and undirected graphs.

# Q3 (a). With suitable example, explain steps of algorithmic thinking. 
**Ans.**
1. **Understanding the problem:**
    - Understand the description of the problem.
    - What are the input/output?
    - Do a few examples by hand.
    - Think about special cases.
    
2. **Formulating the Problem:**
    - Think about the data and the best way to represent them (graphs, strings, etc.)
    - What mathematical criterion corresponds to the desired output?
    
3. **Designing an Algorithm:**
    - Is the formulated problem amenable to a certain algorithm design technique (greedy, divide-and-conquer, etc.)?
    - What data structures make sense to use?
    - Is the algorithm correct?
    - Is the algorithm efficient?
    - If the problem is “too hard,” do we want an approximation algorithm, a randomized algorithm, a heuristic, ...?
    
4. **Implementing the Algorithm:**
    - Most algorithms are destined to be ultimately implemented as computer programs.
    - Programming an algorithm presents both a peril and an opportunity.
    - The peril lies in the possibility of making the transition from an algorithm to a program either incorrectly or very inefficiently.
    - Special mathematical techniques have been developed for proving program correctness, but the power of these techniques is still limited to very small programs.
    - As a practical matter, the validity of programs is still established by testing.
    - Program correctness is necessary but not sufficient: You would not want to diminish your algorithm’s power by an inefficient implementation.
    - The opportunity lies in the possibility to better understand the algorithm and even to improve it.
    
5. **Solving the Original Problem:**
    - Once the algorithm is implemented, it is run on data to solve the original problem.
    - Sometimes, it is discovered after this entire process is followed, that the solution is not satisfactory. This might require going back to step (1) and repeating the entire process.

# Q3 (b). Here is an adjacency list representation of a directed graph. Draw a picture of the directed graph that has the above adjacency list representation. Another way to represent a graph is an adjacency matrix. Draw the adjacency matrix for this graph.
![Graph](https://i.ibb.co/LQWtv1H/image.png)
**Ans.**
**Graph:**
![Answer](https://i.ibb.co/yW7fCK2/image.png)

**Adjacency Matrix:**
![Answer2](https://i.ibb.co/G9h2H3j/image.png)

# Q3 (c). What is Pseudocode? Give an example.
**Ans.**
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

# Q4 (a). A famous problem is figuring out whether an undirected graph contains an Eulerian path. Such a path contains all of the edges in the graph exactly once, but may pass through any of the vertices in the graph as many times as desired. This problem can be formulated as the Eulerian path problem by treating each of the bridges as an undirected edge in a graph, and the parts of the city as the vertices. Here is the crucial fact: A graph contains an Eulerian path if 1. It consists of just one connected component (meaning that all vertices can be reached from any other vertex), and 2. It contains no more than two vertices of odd degree. Write an algorithm to find whether Eulerian Path exist in given graph or not. If yes algorithm should return true else false.
**Ans.**
```plaintext
Algorithm: HasEulerianPathBFS

function has_eulerian_path(graph):
    // Check condition 1: One connected component using BFS
    if not isConnectedBFS(graph):
        return false
    
    oddDegreeCount = 0

    // Check condition 2: No more than two vertices of odd degree
    for vertex in graph.vertices:
        if degree(vertex) % 2 != 0:
            oddDegreeCount += 1

    return oddDegreeCount == 0 or oddDegreeCount == 2

function isConnectedBFS(graph):
    startVertex = getAnyVertex(graph)
    visited = set()
    queue = [startVertex]

    while queue:
        currentVertex = queue.pop(0)
        visited.add(currentVertex)

        for neighbor in graph.neighbors(currentVertex):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

    return len(visited) == len(graph.vertices)

// The rest of the functions (degree, getAnyVertex) remain the same.
```

In this version, the `isConnectedBFS` function uses BFS to traverse the graph and determine if it is a single connected component. The rest of the algorithm remains the same, checking the conditions for the existence of an Eulerian Path.

# Q4 (b). Explain the adjacency list representation of an unweighted graph. Write the adjacency list for the following graph: ![Question](https://i.ibb.co/qgTDPW3/image.png)
**Ans.**
The adjacency list representation is a common way to represent an unweighted graph. In this representation, each vertex of the graph is associated with a list that contains its neighboring vertices. For an undirected graph, each edge is represented twice (once for each adjacent vertex). 

0 -> [1, 4]
1 -> [0, 2, 3, 4]
2 -> [1, 3]
3 -> [1, 2, 4]
4 -> [0, 1, 3]

# Q4 (c). Write two pros and cons for adjacency matrix method of graph representation. 
**Ans.**
**Pros:**

1. **Efficient for Dense Graphs:**
    
    - In graphs with many edges (dense graphs), an adjacency matrix is often more space-efficient than an adjacency list. It allows constant-time access to check the existence of an edge.
    
2. **Ease of Edge Weight Representation:**
    
    - If the graph is weighted, an adjacency matrix simplifies the representation of edge weights. Each entry in the matrix can store the weight of the corresponding edge, making it straightforward to access and update weights.

**Cons:**

1. **Space Inefficiency for Sparse Graphs:**
    
    - In sparse graphs (graphs with few edges), an adjacency matrix can be inefficient in terms of space utilization. It stores information about all possible edges, leading to unnecessary memory consumption and increased computational complexity.
    
2. **Costly for Dynamic Graphs:**
    
    - If the graph structure changes frequently (edges are added or removed), resizing the matrix to accommodate these changes can be computationally expensive. This is especially true for dynamic graphs where the number of edges is not constant.

# Q5 (a). What is the use of asymptotic notations? Explain the meaning and significance of big O (O) and omega ($\Omega$) notations. Give an example for each. 
**Ans.**
Asymptotic notations, such as Big O, Big Omega, and Big Theta, are mathematical tools used to describe the efficiency or complexity of algorithms in computer science. They provide a concise way to express the growth rate of algorithms as input sizes approach infinity.

1. **Big O Notation (O):**
   - Represents the upper bound or worst-case scenario of an algorithm's time complexity. It describes how an algorithm's execution time grows in relation to the input size but does not provide information about the actual performance.

2. **Big Omega Notation (Ω):**
   - Represents the lower bound or best-case scenario of an algorithm's time complexity. It describes the minimum growth rate of an algorithm, indicating that the algorithm will not perform better than this under any circumstances.

Consider the Bubble Sort algorithm, which has a time complexity of $O(n^2)$ in the worst case. The Big O notation $O(n^2)$ indicates that the running time of Bubble Sort grows quadratically with the size of the input.

Consider the Merge Sort algorithm, which has a time complexity of $Ω(nlog⁡(n))$ in the best case. The Big Omega notation $Ω(nlog(n))$ indicates that the running time of Merge Sort grows at least as fast as $nlog(n)$ with the size of the input.

# Q5 (b). What do you mean by time complexity of an algorithm? What are its two components? Explain.
**Ans.**
**Time complexity** of an algorithm is a measure of the amount of time it takes for an algorithm to run as a function of the length of the input. It provides an estimate of the upper bound on the running time of an algorithm.

**Two Components of Time Complexity:**

1. **Constant Factors (Coefficient):**
    
    - These are the factors that represent the actual computational work being done by the algorithm. They include the number of basic operations (arithmetic operations, assignments, comparisons, etc.) performed by the algorithm.
        
    - Example: In an algorithm that iterates through an array of size nn, the number of comparisons or assignments within the loop contributes to the constant factors.
        
2. **Dominant Term (Order of Growth):**
    
    - The dominant term in the time complexity expression determines the overall growth rate of the running time as the input size (nn) increases. It focuses on the most significant factor that influences the running time for large inputs.
        
    - Example: In O(n2+3n+1)O(n2+3n+1), the dominant term is n2n2, indicating a quadratic growth rate.

# Q5 (c). What do you mean by a strongly connected graph? Explain with an example. 
**Ans.**
A **strongly connected graph** is a directed graph in which there exists a directed path from any vertex to any other vertex. In other words, every pair of vertices in a strongly connected graph is mutually reachable.

**Example:**

Consider the following directed graph:

```
1 → 2
↑ ↘ ↓
4 ← 3
```

In this graph:
- There is a directed path from 1 to 2 (1 → 2).
- There is a directed path from 2 to 3 (2 → 3).
- There is a directed path from 3 to 4 (3 → 4).
- There is a directed path from 4 to 1 (4 → 1).

Therefore, every vertex in this graph is reachable from every other vertex through directed paths. Hence, this directed graph is strongly connected.

If, in a directed graph, there exists a directed path from every vertex to every other vertex, and vice versa, the graph is considered strongly connected. Strong connectivity is an important property in various applications, including network analysis, communication systems, and optimization problems.