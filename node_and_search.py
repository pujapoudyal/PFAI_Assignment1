import queue 
from queue import PriorityQueue
from time import process_time



class Node:

    def __init__(self, state, cost=0, parent=None, action=None):
        self.parent = parent
        self.state = state
        self.action = action
        self.cost = cost
        self.depth = 0
        self.heuristic = 0
        self.a_star = 0
        if parent:
            self.depth = parent.depth + 1 

    def goal_state(self):
        return self.state.check_goal()
    
    def successor(self):
        successors = queue.Queue()
        for action in self.state.action:                     
            child = self.state.move(action)      
            if child != None:                                
                childNode = Node(child, self.cost + 1, self, action)              
                successors.put(childNode)
        return successors  

    def pretty_print_solution(self, verbose=False):
      node = self
      path = []
      while node.parent is not None:
          path.append(node.action) 
          node = node.parent
      path.reverse()
      if verbose:
          for i,action in enumerate(path):
              print(f"Step {i+1}: {action}")  
      else:
          print("Actions: ", " -> ".join(path))

    def statistics(self):
      print(f"Depth: {self.depth}")
      print(f"Search cost: {SearchAlgorithm.search_cost}")  
      print(f"Solution cost: {self.depth}")
      print(f"CPU time: {process_time()} seconds")
      print(f"Effective branching factor: {SearchAlgorithm.search_cost/(self.depth+1)}")


class SearchAlgorithm:

  search_cost = 0

  def __init__(self, problem):
      self.start = Node(problem)
      self.visited = set()

#Breadth First Search
  def bfs(self, verbose=False, statistics=False):
    frontier = queue.Queue()
    frontier.put(self.start)
    stop = False

    while not frontier.empty():
        curr_node = frontier.get()
        if curr_node not in self.visited:
            self.visited.add(curr_node)
        if curr_node.goal_state():
            stop = True    
            return curr_node        
           
        successor = curr_node.successor() 
        for successor_node in successor:
            if successor_node not in self.visited:
                self.visited.add(successor_node)
                frontier.put(successor_node)

    if statistics:
        curr_node.statistics()

    return curr_node
  
  #Depth First Search
  def dfs(self, depth_limit=None, verbose=False, statistics=False):

    stack = []  
    stack.append(self.start)

    depth = 0   
    while stack:
        if depth_limit and depth > depth_limit:
              return None

        curr_node = stack.pop()  

        if curr_node not in self.visited:

            self.visited.add(curr_node)

            if curr_node.goal_state():
                goal_node = curr_node
                break  

        successor = curr_node.successor()

        while not successor.empty():
            successor_node = successor.get()
            if depth_limit is None or successor_node.depth <= depth_limit:
          
                stack.append(successor_node)

        depth = max(depth, curr_node.depth)

        if statistics:
            goal_node.statistics()

    return curr_node
  
#Iterative Deepning Depth-First Search
  def ids(self):

      for depth in range(1, 100):
          print(f"Searching depth {depth}...")
          goal = self.dfs(depth, statistics=True)
          if goal:
              return goal

      return None
  
def greedy_search(self, heuristic=0, verbose=False, statistics=False):
        start_time = process_time()
        frontier = PriorityQueue()
        frontier.put((heuristic, self.start))
        stop = False

        while not stop:
            if frontier.empty():
                return None
            _, curr_node = frontier.get()
            if curr_node.goal_state():
                self.goal = curr_node
                stop = True
                end_time = process_time()
                self.time_cost = end_time - start_time
                self.search_cost += 1
                curr_node.pretty_print_solution(verbose)
                if statistics:
                    curr_node.statistics()
                return curr_node

            successor = curr_node.successor()
            while not successor.empty():
                next_node = successor.get()
                self.search_cost += 1
                if next_node not in self.visited:
                    next_node.heuristic = heuristic
                    self.visited.add(next_node)
                    frontier.put((next_node.heuristic, next_node))

        return None

def a_star(self, heuristic=0, verbose=False, statistics=False):
        start_time = process_time()
        frontier = PriorityQueue()
        frontier.put((heuristic, self.start))
        stop = False

        while not stop:
            if frontier.empty():
                return None
            _, curr_node = frontier.get()
            if curr_node.goal_state():
                self.goal = curr_node
                stop = True
                end_time = process_time()
                self.time_cost = end_time - start_time
                self.search_cost += 1
                curr_node.pretty_print_solution(verbose)
                if statistics:
                    curr_node.statistics()
                return curr_node

            successor = curr_node.successor()
            while not successor.empty():
                next_node = successor.get()
                self.search_cost += 1
                if next_node not in self.visited:
                    next_node.heuristic = heuristic
                    next_node.a_star = next_node.cost + next_node.heuristic
                    self.visited.add(next_node)
                    frontier.put((next_node.a_star, next_node))

        return None
