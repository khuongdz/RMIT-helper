''' Module for maze'''

from typing import Literal


class Maze:
    '''Creating class stimulating maze descripted in the statement'''

    def __init__(self) -> None:

        self.__move_count: int = 0

        # read data from input file
        with open('input.txt', encoding='utf8') as inputfile:
            self.__data: list[str] = [
                i.replace('\n', '') for i in inputfile.readlines()]


        # iterate to find the starting point
        for i, vali in enumerate(self.__data):
            for j, valj in enumerate(vali):
                if valj == 'o':
                    self.__init_x: int = i
                    self.__init_y: int = j
                    self.__cur_x: int = i
                    self.__cur_y: int = j

    def go_func (
        self,
        direction: Literal['LEFT', 'RIGHT', 'UP', 'DOWN']
        ) -> Literal['true', 'false', 'win']:
        '''
        # Function GO

        ## Parameters
        direction: the direction you want the robot to go

        ## Return value
        |  | |
        | :---- | -----------------: |
        | true | if the move is valid |
        | false | if the move is invalid |
        | win | if the move is to the exit |

        '''

        # increase the count
        self.__move_count += 1

        # getting info about the symbol in the next move
        symbol: str
        if direction == 'LEFT':
            symbol = self.__data[self.__cur_x][self.__cur_y-1]
        if direction == 'UP':
            symbol = self.__data[self.__cur_x-1][self.__cur_y]
        if direction == 'DOWN':
            symbol = self.__data[self.__cur_x+1][self.__cur_y]
        if direction == 'RIGHT':
            symbol = self.__data[self.__cur_x][self.__cur_y+1]




        # if the move is invalid, return 'false'
        if symbol == '.':
            return 'false'

        # if the move is to the exit, return 'win'
        if symbol == 'X':
            print(f'Reach exit successfully using {self.__move_count} move(s).')
            return 'win'

        # if the move is valid, then change the current position
        # and return 'true'
        if direction == 'LEFT':
            self.__cur_y -= 1
        if direction == 'UP':
            self.__cur_x -= 1
        if direction == 'DOWN':
            self.__cur_x += 1
        if direction == 'RIGHT':
            self.__cur_y += 1
        return 'true'

    def show_move_count (self) -> int:
        '''Return the number of move made'''
        return self.__move_count

    def restart (self) -> None:
        '''Restart the game'''
        self.__cur_x = self.__init_x
        self.__cur_y = self.__init_y
        self.__move_count = 0
