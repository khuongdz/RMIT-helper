'''Module for maze'''

from typing import Literal

class Maze:
    '''Creating class stimulating maze descripted in the statement'''
    def __init__(self) -> None:

        # read data from input file
        with open('input.txt',encoding='utf8') as inputfile:
            self.__data: list[str] = [ i.replace('\n','') for i in inputfile.readlines()]

        # iterate to find the exit
        for i, vali in enumerate(self.__data):
            for j, valj in enumerate(vali):
                if  valj == 'X' :
                    self.__winx: int = i
                    self.__winy: int = j

        # iterate to find the starting point
        for i, vali in enumerate(self.__data):
            for j, valj in enumerate(vali):
                if  valj == 'o' :
                    self.__curx: int = i
                    self.__cury: int = j


    def go_func (self, direction : Literal['LEFT','RIGHT','UP','DOWN'] ) -> str:
        '''
        Function GO to call to guide the robot

        direction: the direction you want the robot to go
        

        '''



        
            
