def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    closed = set() #visited nodes closed set
    fringe = util.Stack() #stack to keep the problem nodes in
    currentState = problem.getStartState() #current state
    node = util.Node(currentState)
    fringe.push(node) #starts the graph search
    while fringe:
        if fringe.isEmpty():
            return False
        node = fringe.pop()  #stores most recent node
        if problem.isGoalState(node.state):
            return node.solution()  #return current node
        if node.state not in closed:
            closed.add(node.state)  #adds recent visited node to closed set
            for nextState, act, cost in problem.getSuccessors(node.state):
                childnode = util.Node(nextState, node, act)
                fringe.push(childnode)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    closed = set()  # visited nodes closed set
    fringe = util.Queue()  # Queue to keep the problem nodes in
    currentState = problem.getStartState()  # current state
    node = util.Node(currentState)
    fringe.push(node)  # starts the graph search
    while fringe:
        if fringe.isEmpty():
            return False
        node = fringe.pop()  # stores most recent node
        if problem.isGoalState(node.state):
            return node.solution()  # return current node
        if node.state not in closed:
            closed.add(node.state)  # adds recent visited node to closed set
            for nextState, act, cost in problem.getSuccessors(node.state):
                childnode = util.Node(nextState, node, act)
                fringe.push(childnode)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    closed = set()  # visited nodes closed set
    fringe = util.PriorityQueue()   # Priority Queue to give priority for node with least cost
    currentState = problem.getStartState()  # current state
    node = util.Node(currentState)
    fringe.push(node,node.path_cost)  # starts the graph search with priority of parent
    nodePriority = node.path_cost
    while fringe:
        if fringe.isEmpty():
            return False
        node = fringe.pop()  # stores most recent node
        if problem.isGoalState(node.state):
            return node.solution()  # return current node
        if node.state not in closed:
            closed.add(node.state)  # adds recent visited node to closed set
            for nextState, action, cost in problem.getSuccessors(node.state): #lists through
                    childnode = util.Node(nextState, node, action, cost+node.path_cost) # makes child node with cumulative cost
                    priority = nodePriority + childnode.path_cost # updates priority
                    fringe.push(childnode, priority) # pushes new node with priority




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch