# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    expanded_nodes = [] #Initialise expanded nodes
    #Initialise frontier with the initial state
    frontier = util.Stack() 
    frontier.push((problem.getStartState(), [])) #Frontier is a stack (LIFO) of states and actions that ended up in that state

    while True:
        if frontier.isEmpty():
            return -1 #Return failure
        
        state, path = frontier.pop() #Pop most recently added node (states and actions)
        
        if problem.isGoalState(state):
            return path #Return solution
        
        if state not in expanded_nodes:
            expanded_nodes.append(state) #Add node to expanded nodes
            for (next_state, action, _) in problem.getSuccessors(state): 
                if (next_state, action) not in frontier.list and next_state not in expanded_nodes:
                    frontier.push((next_state, path + [action])) #Push node to the top of the frontier stack

            
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    expanded_nodes = [] #Initialise expanded nodes
    #Initialise frontier with the initial state
    frontier = util.Queue() 
    frontier.push((problem.getStartState(), [])) #Frontier is a queue (FIFO) of states and actions that ended up in that state
    
    while True:
        if frontier.isEmpty():
            return -1 #Return failure
        
        state, path = frontier.pop() #Pop node (states and actions) that was added to the queue first 
        
        if problem.isGoalState(state):
            return path #Return solution
        
        if state not in expanded_nodes:
            expanded_nodes.append(state) #Add node to expanded nodes
            for (next_state, action, _) in problem.getSuccessors(state): 
                if (next_state, action) not in frontier.list and next_state not in expanded_nodes:
                    frontier.push((next_state, path + [action])) #Enqueue node to the end of the frontier queue


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    expanded_nodes = [] #Initialise expanded nodes
    #Frontier is a priority queue (FIFO) of states and actions where the node with the lowest priority is the head of the queue 
    frontier = util.PriorityQueue()
    frontier.push((problem.getStartState(), []), 0) #Initialise frontier with the initial state and a cost equal to 0
    
    while True:
        if frontier.isEmpty():
            return -1 #Return failure

        cost = frontier.heap[0][0] #??? #Minimum cost in frontier
        state, path = frontier.pop() #Pop node (states, actions. costs) with lowest cost 

        if problem.isGoalState(state):
            return path #Return solution


        if state not in expanded_nodes:
            expanded_nodes.append((state, path)) #Add node to expanded nodes
            for next_state, next_action, step_cost in problem.getSuccessors(state):
                # Flag variables for searching into frontier and extended_nodes
                in_frontier = False
                in_expanded = False
                idx = 0
                
                for i in range(len(frontier.heap)): # Search if next state is in frontier
                    if frontier.heap[i][2][0] == next_state: ##??? [i][2][0]
                        in_frontier = True
                        idx = i #??? #Index of already found state
                for i in range(len(expanded_nodes)): # Search if next state is in expanded_nodes
                    if expanded_nodes[i][0] == next_state: ##??? [i][0]
                        in_expanded = True

                #If the child state is not in frontier and not in the expanded node we add it to the frontier
                if not in_frontier and not in_expanded:
                    frontier.push((next_state, path + [next_action]), cost + step_cost) # Add child state, path and cost to frontier
                #Else if the child state is in the frontier and has a higher path-cost we replace the frontier node with the child
                elif in_frontier and frontier.heap[idx][0] > cost + step_cost:
                    frontier.heap.remove(frontier.heap[idx]) #Remove frontier
                    frontier.push((next_state, path + [next_action]), cost + step_cost) #Modify path and cost of state if found a better path to it


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
