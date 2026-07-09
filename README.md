Below is a GitHub-friendly **README.md** that explains your program in a clear and professional way.

# Best-First Search (Greedy Best-First Search) in Python

## Overview

This project implements the **Greedy Best-First Search (GBFS)** algorithm using Python. Best-First Search is an **informed search algorithm** used in Artificial Intelligence (AI) to find a path from a starting node to a target node by selecting the node with the **lowest heuristic value**.

Unlike Breadth-First Search (BFS) or Depth-First Search (DFS), Greedy Best-First Search uses heuristic information to guide the search toward the goal.

---

# Objective

The objective of this program is to:

* Find a path from a start node to a target node.
* Use heuristic values to guide the search.
* Demonstrate how Greedy Best-First Search works on a graph.

---

# Algorithm Used

**Greedy Best-First Search (GBFS)**

The algorithm always expands the node with the **smallest heuristic value**, assuming it is closest to the goal.

---

# Technologies Used

* Python 3
* `queue.PriorityQueue` module

---

# Project Structure

```
best_first_search.py
README.md
```

---

# Graph Used

```
        A(10)
       /     \
    B(8)    C(5)
    /  \      \
 D(6) E(4)   F(0)
```

The numbers in parentheses represent the heuristic values.

---

# Input

### Graph

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
```

### Heuristic Values

```python
heuristics = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 6,
    'E': 4,
    'F': 0
}
```

### Start Node

```
A
```

### Target Node

```
F
```

---

# Working of the Algorithm

### Step 1

Insert the start node into the priority queue.

```
Priority Queue:
A(10)
```

---

### Step 2

Remove the node with the lowest heuristic value.

Current Node:

```
A
```

Add its neighbors:

```
B(8)
C(5)
```

Priority Queue:

```
C(5)
B(8)
```

---

### Step 3

Remove the node with the smallest heuristic.

Current Node:

```
C
```

Add its neighbor:

```
F(0)
```

Priority Queue:

```
F(0)
B(8)
```

---

### Step 4

Remove:

```
F
```

Since **F** is the target node, the search stops.

---

# Output

```
Path found by Best-First Search: ['A', 'C', 'F'] with target heuristic: 0
```

---

# Code Explanation

## Function Definition

```python
best_first_Search(graph, start, target, heuristics)
```

### Parameters

| Parameter  | Description                                   |
| ---------- | --------------------------------------------- |
| graph      | Graph represented as an adjacency list        |
| start      | Starting node                                 |
| target     | Goal node                                     |
| heuristics | Estimated distance from each node to the goal |

---

## Visited Set

```python
visited = set()
```

Stores the nodes that have already been visited to prevent revisiting them.

---

## Priority Queue

```python
pq = PriorityQueue()
```

Maintains the nodes in ascending order of heuristic value.

---

## Insert Start Node

```python
pq.put((heuristics[start], start, [start]))
```

Stores:

* Heuristic value
* Current node
* Path followed so far

---

## Search Loop

```python
while not pq.empty():
```

The algorithm continues until:

* The target node is found, or
* No nodes remain to be explored.

---

## Remove Best Node

```python
h, node, path = pq.get()
```

Removes the node with the lowest heuristic value.

---

## Goal Test

```python
if node == target:
    return path, h
```

If the current node is the target, the algorithm returns the path and terminates.

---

## Explore Neighboring Nodes

```python
for neighbor in graph.get(node, []):
```

Visits all neighboring nodes.

---

## Check if Already Visited

```python
if neighbor not in visited:
```

Ensures that each node is processed only once.

---

## Add Neighbor to Priority Queue

```python
pq.put((heuristics[neighbor], neighbor, path + [neighbor]))
```

Adds the neighboring node along with the updated path.

---

# Time Complexity

| Operation                 | Complexity       |
| ------------------------- | ---------------- |
| Priority Queue Operations | O(log V)         |
| Overall Algorithm         | O((V + E) log V) |

Where:

* **V** = Number of vertices
* **E** = Number of edges

---

# Space Complexity

```
O(V)
```

Space is used for:

* Visited set
* Priority queue
* Path storage

---

# Advantages

* Simple and easy to implement.
* Uses heuristic information to guide the search.
* Often reaches the goal quickly.
* Efficient when a good heuristic is available.

---

# Limitations

* Does **not** guarantee the shortest path.
* Performance depends on the quality of the heuristic.
* May explore a suboptimal path if the heuristic is misleading.

---

# Applications

* Artificial Intelligence
* Robot Navigation
* GPS Route Planning
* Game Pathfinding
* State Space Search
* Decision-Making Systems

---

# Sample Execution

```
Start Node : A
Goal Node  : F

Visited Order:
A
C
F

Path:
A → C → F
```

---

# Conclusion

This project demonstrates the implementation of the **Greedy Best-First Search** algorithm using Python. The algorithm uses heuristic values to prioritize nodes that appear closest to the goal, making it an efficient choice for many AI search problems. However, because it relies solely on heuristic estimates, it does not always produce the shortest or optimal path.

You can save this as **`README.md`** in your GitHub repository. GitHub will automatically render the headings, tables, code blocks, and diagrams in a clean, professional format.
