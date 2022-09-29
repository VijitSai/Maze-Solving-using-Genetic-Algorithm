import random

class Maze:
    
    def __init__(self, height, width, obstacles_percent = 0.5, solutions_count = 1, solution_in_steps = None):
        self.height = height
        self.width = width
        self.solutions_count = solutions_count
        self.obstacles_count = int(self.height*self.width*obstacles_percent)
        self.solutions = []
        self.empty = set()
        self.obstacle_loc = set()
        self.solution_in_steps = solution_in_steps if solution_in_steps else self.height+self.width-1
        self.generate_maze()
    
    def generate_maze(self):
        
        self.maze = [[0 for i in range(self.width)] for j in range(self.height)]
        self.generate_solutions()
        obs_count = 0
        for i in range(self.obstacles_count):
            x = random.randint(0, self.height-1)
            y = random.randint(0, self.width-1)
            if x*self.width+y not in self.empty and (x, y) != (0, 0) and (x, y) != (self.height-1, self.width-1):
                self.maze[x][y] = 1
                self.obstacle_loc.add((x*self.width+y))
                obs_count += 1
            else:
                i-=1
        self.maze[0][0] = 2
        self.maze[self.height-1][self.width-1] = 3
        print('Obstacles count: ', obs_count)
        
    def generate_solutions(self):
        count = 0
        while(count < self.solutions_count):
            path = [(0, 0)]
            pos = (0, 0)
            steps_count = 0
            while(pos != (self.height-1, self.width-1) and steps_count < self.solution_in_steps):
                if pos[0] == self.height-1:
                    pos = (pos[0], pos[1]+1)
                elif pos[1] == self.width-1:
                    pos = (pos[0]+1, pos[1])
                else:
                    pos = random.choice([(pos[0]+1, pos[1]), (pos[0], pos[1]+1)])
                steps_count += 1
                path.append(pos)
                self.empty.add(pos[0]*self.width+pos[1])
            if pos == (self.height-1, self.width-1):
                self.solutions.append(path)
                count += 1
            
            
    
    def show_maze(self,show_path = False):
        for i in range(self.height):
            for j in range(self.width):
                if self.maze[i][j] == 3:
                    print('|E|', end='')
                elif i*self.width+j in self.empty and show_path:
                    print('|0|', end='')
                elif self.maze[i][j] == 0:
                    print('| |', end='')
                elif self.maze[i][j] == 1:
                    print('|#|', end='')
                elif self.maze[i][j] == 2:
                    print('|S|', end='')
            print()

maze = Maze(10, 10, 0.8, 1)

maze.show_maze(True)
 