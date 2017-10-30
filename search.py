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
from game import Directions
from game import Agent
from game import Actions
import util
import time
import search

class SearchProblem:


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

def genericSearch(problem, fringe, heuristic=None):
	visited = []  # List of already visisted nodes
	action_list = []  # List of actions taken to get to the current node
	initial = problem.getStartState()  # Starting state of the problem

	if isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):
		fringe.push((initial, action_list))
	elif isinstance(fringe, util.PriorityQueue):
		fringe.push((initial, action_list), heuristic(initial, problem))


	while fringe:
		if isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):
			node, actions = fringe.pop()
		elif isinstance(fringe, util.PriorityQueue):
			node, actions = fringe.pop()

		if not node in visited:
			visited.append(node)
			if problem.isGoalState(node):
				return actions
			successors = problem.getSuccessors(node)
			for successor in successors:
				coordinate, direction, cost = successor
				newActions = actions + [direction]
				if isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):
					fringe.push((coordinate, newActions))
				elif isinstance(fringe, util.PriorityQueue):
					newCost = problem.getCostOfActions(newActions) + \
							  heuristic(coordinate, problem)
					fringe.push((coordinate, newActions), newCost)

	return []



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    # Use the genericSearch method, with the fringe maintained using a Stack
    # so that the search proceeds in the order of exploring from the node last
    # discovered
    fringe=util.Stack()
    visited = []  # List of already visisted nodes
    action_list = []  # List of actions taken to get to the current node
    initial = problem.getStartState()
    fringe.push((initial, action_list))
    while fringe:
		node, actions = fringe.pop()
		if not node in visited:
			visited.append(node)
			if problem.isGoalState(node):
				return actions
			successors = problem.getSuccessors(node)
			for successor in successors:
				coordinate, direction, cost = successor
				newActions = actions + [direction]
				fringe.push((coordinate, newActions))


    return []

def breadthFirstSearch(problem):
	fringe = util.Queue()
	visited = []  # List of already visisted nodes
	action_list = []  # List of actions taken to get to the current node
	initial = problem.getStartState()
	fringe.push((initial, action_list))
	while fringe:
		node, actions = fringe.pop()
		if not node in visited:
			visited.append(node)
			if problem.isGoalState(node):
				return actions
			successors = problem.getSuccessors(node)
			for successor in successors:
				coordinate, direction, cost = successor
				newActions = actions + [direction]
				fringe.push((coordinate, newActions))

def uniformCostSearch(problem):

    return aStarSearch(problem)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch1(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = []  # List of already visisted nodes
    action_list = []  # List of actions taken to get to the current node
    initial = problem.getStartState()  # Starting state of the problem
    fringe=util.PriorityQueue()
    while fringe:
        node, actions = fringe.pop()
    if not node in visited:
        visited.append(node)
        if problem.isGoalState(node):
            return actions
        successors = problem.getSuccessors(node)
        for successor in successors:
            coordinate, direction, cost = successor
            newActions = actions + [direction]
            newCost = problem.getCostOfActions(newActions) + \
                heuristic(coordinate, problem)
            fringe.push((coordinate, newActions), newCost)
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
