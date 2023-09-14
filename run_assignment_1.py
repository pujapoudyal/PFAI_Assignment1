'''
Define problem and start execution of search problems

Author: Tony Lindgren
'''

from missionaries_and_cannibals import MissionariesAndCannibals 
from node_and_search import SearchAlgorithm
from eight_puzzle import EightPuzzle

init_state = [[0, 0], 'r', [3, 3]] 
goal_state = [[3, 3], 'l', [0, 0]] 
ep_init_state = [ [7, 2, 4], [5, 'e', 6], [8, 3, 1]]

def main():
    mc = MissionariesAndCannibals(init_state, goal_state)
    sa = SearchAlgorithm(mc)
    ep= EightPuzzle(ep_init_state)
    ep_sa= SearchAlgorithm(ep)

    #Performing Breadth First Search
    print('BFS')
    print('Start state: ')
    mc.pretty_print()
    goal_node = sa.bfs()
    print('goal state: ')
    goal_node.state.pretty_print()

    #Performing Depth First Search
    print('DFS')
    print('Start state: ')
    mc.pretty_print()
    goal_node1 = sa.dfs()
    print('goal state: ')
    goal_node1.state.pretty_print()

#Performing Iterative Deepning Search
    print('IDS')
    print('Start state: ')
    mc.pretty_print()
    goal_node = sa.ids()
    print('goal state: ')
    goal_node.state.pretty_print()

#Performing Eight Puzzle Greedy Search with heuristic 0
    print('Eight Puzzle Greedy Search (h_0)')
    print('Start state: ')
    ep.pretty_print()
    goal_node = ep_sa.greedy_search(heuristic=0)
    print('goal state: ')
    goal_node.state.pretty_print()

    #Performing Eight Puzzle Greedy Search with heuristic 1
    print('Eight Puzzle Greedy Search (h_1)')
    print('Start state: ')
    ep.pretty_print()
    goal_node = ep_sa.greedy_search(heuristic=1)
    print('goal state: ')
    goal_node.state.pretty_print()

    print('Eight Puzzle A* with heuristic (h_0)')
    print('Start state: ')
    ep.pretty_print()
    goal_node = ep_sa.a_star()
    print('goal state: ')
    goal_node.state.pretty_print()

    print('Eight Puzzle A* with heuristic(h_1)')
    print('Start state: ')
    ep.pretty_print()
    goal_node = ep_sa.a_star()
    print('goal state: ')
    goal_node.state.pretty_print()

if __name__ == "__main__":
    main()