# DFS-BFS-UCS
This project contains the implementation of the three search algorithms using nodes in python.

These algorithsm were for a Machine Learning course CS156 - SJSU. 

First implementation in the DFS-Uniform file would be Depth First Search.
/** 
* First note ** during the implementation of these algortihms we have three main names for data structures that would be used throughout the python project
*   1 -- closed --> is s a set()
*   2 -- fringe --> is a stack(), Queue(), PriorityQueue().
*   3 -- currentState, goalState --> Node state
* */
<----------------->     <----------------->       <----------------->         <----------------->       <----------------->     <----------------->

-- DFS: Searches the deepest node first, solution used is a graph search algorithm
We create our visited nodes set (closed), a Stack used to keep nodes (fringe LIFO).
Start the graph search by pushing the first node which keeps going through the nodes until isGoalState return true for one of the nodes.
whicheve

-- BFS (Breadth First Search): searches the shallowest nodes in the tree first
We create our visited nodes set (closed), a Queue used to keep nodes (Queue used instead FIFO).
Start the graph search by pushing the first node which keeps going through the nodes until isGoalState return true for one of the nodes.

-- UCS (Uniform Cost Search): Searches the node with the least cost of ndodes
We create our visited nodes set (closed), a Priority-Queue used to keep nodes (fringe LIFO).
Start the graph search by pushing the first node which keeps going through the nodes until isGoalState return true for one of the nodes.
Priority starts with the parent and it is calculated at each visit. Then is lists through it and calculates the cumulative cost wit
the children nodes and it updates the priority which then the child node with the priority gets pushed.

