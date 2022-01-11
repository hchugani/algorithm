import collections
from typing import List

"""
353. Design Snake Game
Medium

Design a Snake game that is played on a device with screen size height x width. Play the game online if you are not 
familiar with the game.

The snake is initially positioned at the top left corner (0, 0) with a length of 1 unit.

You are given an array food where food[i] = (ri, ci) is the row and column position of a piece of food that the snake
 can eat. When a snake eats a piece of food, its length and the game's score both increase by 1.

Each piece of food appears one by one on the screen, meaning the second piece of food will not appear until the snake 
eats the first piece of food.

When a piece of food appears on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

The game is over if the snake goes out of bounds (hits a wall) or if its head occupies a space that its body occupies 
after moving (i.e. a snake of length 4 cannot run into itself).

Implement the SnakeGame class:

SnakeGame(int width, int height, int[][] food) Initializes the object with a screen of size height x width and the 
positions of the food.
int move(String direction) Returns the score of the game after applying one direction move by the snake. If the game 
is over, return -1.
"""

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = collections.deque([(0,0)])
        self.snake_set = {(0,0): 1}
        self.w = width
        self.h = height
        self.food = food
        self.food_ind = 0
        self.movement = {"U": [-1,0], "L":[0,-1], "R": [0,1], "D":[1,0]}


    def move(self, direction: str) -> int:
        movement = self.movement[direction]

        new_head = (self.snake[0][0] + movement[0], self.snake[0][1] + movement[1])

        if new_head[0]<0 or new_head[0]>=self.h or new_head[1]<0 or new_head[1]>=self.w:
            return -1

        if new_head in self.snake_set and new_head != self.snake[-1]:
            return -1


        if self.food_ind<len(self.food)  and new_head[0]==self.food[self.food_ind][0] and new_head[1]==self.food[self.food_ind][1]:
            self.food_ind+=1
        else:
            tail = self.snake.pop()
            del self.snake_set[tail]
        self.snake.appendleft(new_head)

        self.snake_set[new_head]=1

        return len(self.snake)-1



# Your SnakeGame object will be instantiated and called as such:
obj = SnakeGame(3, 2, [[1,2],[0,1]])
param_1 = obj.move("R")
param_1 = obj.move("D")
param_1 = obj.move("R")
param_1 = obj.move("U")
param_1 = obj.move("L")
param_1 = obj.move("U")