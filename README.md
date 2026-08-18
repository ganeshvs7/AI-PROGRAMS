# AI & Machine Learning Laboratory

A collection of **Artificial Intelligence and Machine Learning laboratory programs implemented in Python**. The repository covers fundamental search algorithms, knowledge representation, concept learning, classification, neural networks, and clustering.

## 📚 Programs & Algorithm Process

| No.    | Algorithm                        | Process                                                                                                                                                                                                           |
| ------ | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **01** | **BFS & DFS**                    | **BFS:** Starts from a node, visits neighboring nodes level-by-level using a queue, and tracks visited nodes. **DFS:** Starts from a node and explores as deeply as possible using recursion before backtracking. |
| **02** | **Best-First Search**            | Assigns a **heuristic value** to each node, places nodes in a priority queue, and always expands the node with the lowest heuristic value until the target is reached.                                            |
| **03** | **Means-End Analysis**           | Compares the **current state with the goal state**, identifies the difference, selects an operator to reduce that difference, checks its preconditions, and applies the operator to reach the goal.               |
| **04** | **Rule-Based System**            | Starts with known facts, checks rules whose conditions are satisfied, adds newly inferred facts to the knowledge base, and continues until no new facts can be derived.                                           |
| **05** | **Find-S Algorithm**             | Starts with the most specific hypothesis from the first positive example and generalizes it whenever attributes differ in other positive examples. Negative examples are ignored.                                 |
| **06** | **Candidate Elimination**        | Maintains both **Specific (S)** and **General (G)** boundaries. Positive examples generalize S and eliminate inconsistent G hypotheses, while negative examples specialize G.                                     |
| **07** | **ID3 Decision Tree**            | Calculates **entropy and information gain**, selects the attribute with the highest information gain, splits the dataset, and recursively builds the decision tree.                                               |
| **08** | **Perceptron & Backpropagation** | The **Perceptron** learns weights by comparing predictions with target values. **Backpropagation** performs forward propagation, calculates error, propagates the error backward, and updates network weights.    |
| **09** | **Naïve Bayes**                  | Calculates class **prior probabilities** and feature **conditional probabilities**, applies them to a test instance, and selects the class with the highest probability.                                          |
| **10** | **K-Means Clustering**           | Selects initial centroids, assigns data points to the nearest centroid, recalculates centroids, and repeats the process until the centroids stabilize. The silhouette score is then used for cluster validation.  |

## 🧠 Concepts Covered

* State Space Search
* Breadth First Search (BFS)
* Depth First Search (DFS)
* Heuristic Search
* Best-First Search
* Means-End Analysis
* Knowledge Representation
* Rule-Based Systems
* Concept Learning
* Find-S Algorithm
* Candidate Elimination
* Decision Tree Learning
* Entropy & Information Gain
* Perceptron
* Backpropagation
* Naïve Bayes Classification
* K-Means Clustering
* Cluster Validation

## 🛠️ Technologies

* **Python**
* **NumPy**
* Artificial Intelligence
* Machine Learning

## 📁 Repository Structure

```text
AI-PROGRAMS/
│
├── PROGRAMS/
│   ├── 01_BFS_DFS.py
│   ├── 02_Best_First_Search.py
│   ├── 03_Means_End_Analysis.py
│   ├── 04_Rule_Based_System.py
│   ├── 05_Find_S.py
│   ├── 06_Candidate_Elimination.py
│   ├── 07_ID3_Decision_Tree.py
│   ├── 08_Perceptron_Backpropagation.py
│   ├── 09_Naive_Bayes.py
│   └── 10_KMeans_Clustering.py
│
├── OUTPUTS/
│   ├── 01_BFS_DFS.png
│   ├── 02_Best_First_Search.png
│   ├── 03_Means_End_Analysis.png
│   ├── ...
│   └── 10_KMeans_Clustering.png
│
└── README.md
```

## 🎯 Objective

The objective of this laboratory is to gain practical understanding of fundamental **AI search techniques, knowledge representation, machine learning algorithms, neural networks, classification methods, and clustering techniques** through Python implementations.

## 🚀 How to Run

Clone the repository and navigate to the `PROGRAMS` directory:

```bash
git clone <repository-url>
cd AI-PROGRAMS/PROGRAMS
```

Run any program using:

```bash
python 01_BFS_DFS.py
```

Replace the filename with the program you want to execute.

---

### 📌 Laboratory Work

This repository contains implementations and execution outputs for **10 Artificial Intelligence and Machine Learning laboratory programs**.

**Happy learning! 🚀**
