# AI-PROGRAMS
Greedy Best-First Search (GBFS) algorithm,
What is this code used for?

The code searches for a target node in a graph by always choosing the node with the lowest heuristic value (the node that appears closest to the goal).

It is commonly used in:

AI pathfinding
Route planning
Robot navigation
Game AI
State-space search problems
Example Graph

Your graph looks like this:

        A(10)
       /     \
    B(8)    C(5)
    /  \      \
 D(6) E(4)   F(0)

The numbers in parentheses are the heuristic values.

Step-by-Step Execution
Initial State

Priority Queue:

(A,10)

Visited:

A
Step 1

Remove node with the smallest heuristic.

A

Not the target.

Add its neighbors.

B(8)
C(5)

Priority Queue becomes

C(5)
B(8)
Step 2

Remove

C(5)

Not target.

Add

F(0)

Priority Queue

F(0)
B(8)
Step 3

Remove

F(0)

This is the target.

Search stops.

Output
Path found by Best-First Search: ['A', 'C', 'F'] with target heuristic: 0
How the Main Function Works
Function Definition
def best_first_Search(graph, start, target, heuristics):

Parameters:

graph → Stores the graph as an adjacency list.
start → Starting node.
target → Goal node.
heuristics → Estimated distance from each node to the goal.
Visited Set
visited = set()

Keeps track of visited nodes to avoid revisiting them.

Priority Queue
pq = PriorityQueue()

Stores nodes ordered by their heuristic value.

Add Starting Node
pq.put((heuristics[start], start, [start]))

Stores:

(10, 'A', ['A'])

where:

10 → heuristic
'A' → current node
['A'] → path so far
Loop Until Queue is Empty
while not pq.empty():

Keeps searching until the target is found or there are no more nodes.

Remove Best Node
h, node, path = pq.get()

Removes the node with the smallest heuristic value.

Check Goal
if node == target:
    return path, h

If the current node is the goal, return the path and heuristic.

Explore Neighbors
for neighbor in graph.get(node, []):

Checks each neighboring node.

If Not Visited
if neighbor not in visited:

Prevents revisiting the same node.

Add to Queue
pq.put((heuristics[neighbor], neighbor, path + [neighbor]))

Stores the neighbor along with the updated path.

Time Complexity

If:

V = Number of vertices
E = Number of edges

Then the time complexity is approximately:

O((V + E) log V)

because inserting and removing items from the priority queue takes O(log V) time.

Advantages
Faster than uninformed searches in many cases.
Uses heuristic information to guide the search.
Often reaches the goal quickly when the heuristic is good.
Simple to implement.
Disadvantages
Does not guarantee the shortest path.
A poor heuristic can lead to inefficient searches.
Can get stuck exploring a path that looks promising but isn't optimal.
Real-Life Example

Imagine you're using a GPS to reach a destination. Instead of calculating the total travel cost, the system always chooses the road that appears closest to the destination in a straight line (the heuristic). This can get you to the destination quickly, but not necessarily by the shortest or fastest route. That's the basic idea behind Greedy Best-First Search.
