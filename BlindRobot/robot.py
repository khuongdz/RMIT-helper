'''Robot class for descripted'''

import sys
from typing import Literal  # typing library
import random  # RNG
from maze import Maze  # Maze module

INCLUDE_RNG: bool = False
MAZE_SZ: int = 100

sys.setrecursionlimit(MAZE_SZ**2)


class Robot:
    '''Required robot class'''

    def __init__(self) -> None:
        self.__maze: Maze = Maze()
        self.__map: list[list[str]] = [
            ['?' for j in range(MAZE_SZ)] for i in range(MAZE_SZ)]
        # map with unknown position being '?', the other symbols stay the same
        self.__directions: list[str] = ['UP', 'LEFT', 'RIGHT', 'DOWN']
        # x_index change corresponding to the directions
        self.__dx: list[int] = [-1, 0, 0, 1]
        # y_index change corresponding to the directions
        self.__dy: list[int] = [0, -1, 1, 0]
        self.__cur_x: int = 0  # variable to save current position
        self.__cur_y: int = 0  # variable to save current position
        # mark the current standing position to known
        self.__map[self.__cur_x][self.__cur_y] = 'o'

    def __peek_state(self, dir_num: int) -> str:
        '''peak the next square state in the map'''
        next_x: int = self.__cur_x + self.__dx[dir_num]
        next_y: int = self.__cur_y + self.__dy[dir_num]
        return self.__map[next_x][next_y]

    def __move(self, dir_num: int) -> Literal['true', 'false', 'win']:
        '''
        ## Custom go function to optimize by memoization

        | dir_num | value |
        |:-:|:-|
        |0 | UP |
        | 1 | LEFT |
        | 2 | DOWN |
        | 3 | RIGHT |
        '''

        # catch error if cant find any exit
        if dir_num == 4:
            print('No exit found')
            with open('log.txt', 'w', encoding='utf8') as file:
                for line in self.__map:
                    file.write(' '.join(line)+'\n')
            sys.exit()

        go_state = self.__maze.go_func(self.__directions[dir_num])
        match go_state:
            case 'true':
                # change the current position using direction number
                self.__cur_x += self.__dx[dir_num]
                self.__cur_y += self.__dy[dir_num]
                # mark standing point empty
                self.__map[self.__cur_x][self.__cur_y] = ' '
                # print(self.__cur_x,self.__cur_y)
                return 'true'
            case 'false':
                # mark the wall
                self.__map[self.__cur_x+self.__dx[dir_num]
                           ][self.__cur_y+self.__dy[dir_num]] = '.'
                return 'false'
            case _:  # win
                return 'win'

    def __dfs(self, prev_dir: int = -1) -> None:
        '''Use depth first search to search for empty squares'''
        rng_range = list(range(4))
        # include rng to get the result closer to average case
        if INCLUDE_RNG:
            random.shuffle(rng_range)
        for dir_num in rng_range:
            if self.__peek_state(dir_num) != '?':
                # if the state is known, then skip that direction
                continue
            move_state = self.__move(dir_num)
            if move_state == 'false':
                # if the move is to the wall, then skip that direction
                continue
            if move_state == 'win':
                # terminate immediately if win
                sys.exit()
            if move_state == 'true':
                # if the move is valid, then start dfs at that square
                self.__dfs(dir_num)

        # after finished, move the robot back to previous step

        self.__move(3-prev_dir)

    def navigate(self) -> None:
        '''function required by the statement'''
        self.__dfs()


a = Robot()
a.navigate()
