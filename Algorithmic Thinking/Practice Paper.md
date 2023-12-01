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