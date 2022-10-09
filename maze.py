import random
from unittest import result
import numpy as np
import math

class Maze:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.solutions = []
        self.empty = set()
        self.obstacle_loc = set()
        self.goal_state = None
        self.start_state = None
        self.start_state = (0, 0)
        self.solution_in_steps = 0
        self.generate_maze()
    
    def generate_maze(self):

        a_height = 2*self.height+1
        a_width = 2*self.width+1
        
        self.maze = []
        for i in range(a_height):
            if i%2 == 0:
                self.maze.append([1]*a_width)
            else:
                row = []
                for j in range(a_width):
                    if j%2 == 0:
                        row.append(1)
                    else:
                        row.append(0)
                self.maze.append(row)
        self.maze[1][1] = 2
        self.start_state = (1, 1)
        self.create_paths()
        self.set_goal_state()
    
    def create_paths(self):
        path = [(0, 0)]
        pos = (1, 1)
        steps_count = 0
        visited = {(1, 1)}
        while(len(visited)<self.height*self.width):
            possible_moves = self.generate_moves(pos,visited)
            if possible_moves == []:
                pos = path.pop()
                if pos == (1, 1):
                    break
                steps_count -= 1
                continue
            pos,wall = random.choice(possible_moves) 
            steps_count += 1
            path.append(pos)
            visited.add(pos)
            self.maze[wall[0]][wall[1]] = 0
        self.solution_in_steps = steps_count
    
    def set_goal_state(self):
        a_height = 2*self.height+1
        a_width = 2*self.width+1
        self.goal_state = (a_height-2, a_width-2)
        self.maze[a_height-2][a_width-2] = 3
             
    def generate_moves(self, pos, visited):
        possible_moves = []
        a_height = 2*self.height+1
        a_width = 2*self.width+1
        # moving up
        if pos[0] > 1 and (pos[0]-2, pos[1]) not in visited :
            possible_moves.append([(pos[0]-2, pos[1]), (pos[0]-1, pos[1])])
        # moving down
        if pos[0] < a_height-2 and (pos[0]+2, pos[1]) not in visited:
            possible_moves.append([(pos[0]+2, pos[1]), (pos[0]+1, pos[1])])
        # moving left
        if pos[1] > 1 and (pos[0], pos[1]-2) not in visited:
            possible_moves.append([(pos[0], pos[1]-2), (pos[0], pos[1]-1)])
        # moving right
        if pos[1] < a_width-2 and (pos[0], pos[1]+2) not in visited :
            possible_moves.append([(pos[0], pos[1]+2), (pos[0], pos[1]+1)])
        return possible_moves
  
    def show_path(self, path):
        
        a_width = 2*self.width+1
        pos = self.start_state
        self.empty = set()
        for next in path:
            if next == 0:
                pos = (pos[0], pos[1])
            elif next == 1:
                if self.maze[pos[0]-1][pos[1]] == 1:
                    continue
                pos = (pos[0]-1, pos[1])
            elif next == 2:
                if self.maze[pos[0]][pos[1]-1] == 1:
                    continue
                pos = (pos[0], pos[1]-1)
            elif next == 3:
                if self.maze[pos[0]+1][pos[1]] == 1:
                    continue
                pos = (pos[0]+1, pos[1])
            elif next == 4:
                if self.maze[pos[0]][pos[1]+1] == 1:
                    continue
                pos = (pos[0], pos[1]+1)
            if pos == self.goal_state:
                break
            self.empty.add(pos[0]*a_width+pos[1])
        print(self.__str__(show_path = True))
    def __str__(self,show_path = False):
        result = ''
        a_width = 2*self.width+1
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 3:
                    result += 'E '
                elif i*a_width+j in self.empty and show_path:
                    result += '0 '
                elif self.maze[i][j] == 0:
                    result += '  '
                elif self.maze[i][j] == 1:
                    result += '# '
                elif self.maze[i][j] == 2:
                    result += 'S '
            result += '\n'
        return result

# maze = Maze(10,10)
# print(maze)