class EightPuzzle:
    def __init__(self, state):
        self.state = state
        self.goal_state = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]

    def move(self, action):
        # Find the position of the empty tile
        empty_pos = None
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == 0:
                    empty_pos = (i, j)
                    break
            if empty_pos:
                break

        # Determine the new position of the empty tile based on the action
        new_pos = None
        if action == "up":
            new_pos = (empty_pos[0] - 1, empty_pos[1])
        elif action == "down":
            new_pos = (empty_pos[0] + 1, empty_pos[1])
        elif action == "left":
            new_pos = (empty_pos[0], empty_pos[1] - 1)
        elif action == "right":
            new_pos = (empty_pos[0], empty_pos[1] + 1)

        # Swap the values of the empty tile and the tile in the new position
        self.state[empty_pos[0]][empty_pos[1]], self.state[new_pos[0]][new_pos[1]] = self.state[new_pos[0]][new_pos[1]], self.state[empty_pos[0]][empty_pos[1]]

    def pretty_print(self):
        for row in self.state:
            formatted_row = [str(elem) if elem != 0 else ' ' for elem in row]
            print(' '.join(formatted_row))

    def check_goal(self):
        return self.state == self.goal_state

    def h_1(self):
        misplaced_tiles = 0
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] != self.goal_state[i][j]:
                    misplaced_tiles += 1
        return misplaced_tiles

#method for calculating the Manhattan distance
    def h_2(self):
        total_distance = 0
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                value = self.state[i][j]
                if value != 0:
                    goal_pos = self.find_goal_position(value)
                    distance = abs(i - goal_pos[0]) + abs(j - goal_pos[1])
                    total_distance += distance
        return total_distance

    def find_goal_position(self, value):
        for i in range(len(self.goal_state)):
            for j in range(len(self.goal_state[i])):
                if self.goal_state[i][j] == value:
                    return (i, j)