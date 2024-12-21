"""
Student: dor binyamin
ID: 209460302
Assignment no. 6
Program:minesweeper.py
"""
import random
class MSSquare:
#An MSSquare class (short for square minesweeper) that defines a tile on the board
    def __init__(self,has_mine=False,hidden=True,neighbor_mines=0):
        self.__has_mine=has_mine
        self.__hidden=hidden
        self.__neighbor_mines=neighbor_mines

    def get_has_mine(self):#Returns a Boolean variable that is true if and only if the tile has a mine 
        return self.__has_mine
    
    def get_hidden(self):#Returns a Boolean variable that is true if the tile has not already been exposed
        return self.__hidden
    
    def get_neighbor_mines(self):#Returns a variable int that describes the number of mines in neighboring slots
        return self.__neighbor_mines
    
    def set_has_mine(self,has_mine):#Replace a Boolean variable that is true if and only if the tile has a mine 
        self.__has_mine=has_mine
    
    def set_hidden(self,hidden):# Replacea Boolean variable that is true if the tile has not already been exposed
        self.__hidden=hidden
    
    def set_neighbor_mines(self,neighbor_mines):#Replace Returns a variable int that describes the number of mines in neighboring slots
        self.__neighbor_mines=neighbor_mines
    
    
class MSGame:
 #MSGame class that manages a minesweeper game
    def __init__(self,size,num_mines):
#Constructor. Accepts two parameters (in addition to self :)board size and number of mines. 
#The constructor will drop ValueError if the size of the board is not an integer between 4 and 9 and if a number 
#Mines less than 1 or greater than size.__self* 2
        if type(size)==int and size >=4 and size<=9 and num_mines >1 and num_mines <size *2 :
            self.__num_mines=num_mines#Mines number
            self.__size=size# clipboard size
            self.__board=[[MSSquare() for j in range(size)]for i in range (size)]# Game board. Nested list of MS-type organs
            self.__generate_minefield()
            self.__generate_neighbor_info()
            self.__print_board()
        else:
            raise ValueError()
    
    @property
    def size(self):#Returns the size of the clipboard
        return self.__size
    
    
    def __print_board(self,with_mines=False):
#Prints the clipboard
#The parameter mines_with says whether the mines are also printed or not.
        print("    " + "+---" * self.__size, end="+")
        for i in range(self.__size):#run from i until size
            print(f"\n {i + 1}  ", end='')
            for j in range(self.__size):#run from j until size
                if with_mines and self.__board[i][j].get_has_mine():
                    print("| X",end=" ")
                elif self.__board[i][j].get_hidden():
                    print("|  ",end=" ")
                else:
                    print("| "+str(self.__board[i][j].get_neighbor_mines()),end=" ")
            print("|", end='')
            print(f'\n    ', end='')
            print("+---" * self.__size, end="+")
        print("\n     ", end='')
        for i in range(self.__size):#run from i until size
            print(f" {i + 1}  ", end='')
        print('\n')
        
    def __generate_minefield(self):
        count=0
        while(count<self.__num_mines):
             x=random.randint(0,self.__size-1)
             y=random.randint(0,self.__size-1)
             if not self.__board[x][y].get_has_mine():
                self.__board[x][y].set_has_mine(True)
                count+=1
        
    def __generate_neighbor_info(self):
# A method that randomly disperses mines on the board according to 
#Their number stored in the class variable num_mines
        summ = 0
        for i in range(self.__size):#run from i until size
            for j in range(self.__size):#run from j until size
                low = max(0,i-1)
                high = min(i+1,self.__size - 1)
                low_1 = max(0,j-1)
                high_1 = min(j+1,self.__size - 1)
                for k in range(low,high+1):#run from low until high
                    for t in range(low_1,high_1+1):#run from low_! until hugh_1
                        if self.__board[k][t].get_has_mine():
                            summ+=1
                if self.__board[i][j].get_has_mine():
                    summ-=1
                self.__board[i][j].set_neighbor_mines(summ)
                summ = 0

    def __update_board(self,row,column):
#Updates the clipboard after each row selection 
#and a column by the user
        if row < 0 or column < 0 or row >= self.__size or column >= self.__size:
            return
    
        if not self.__board[row][column].get_hidden():
            return
    
        if self.__board[row][column].get_has_mine():
            return
    
        if self.__board[row][column].get_neighbor_mines() > 0:
            self.__board[row][column].set_hidden(False)
            return
    
        self.__board[row][column].set_hidden(False)
        
        lst = [0,1,0,-1,1,0,-1,0,1,1,-1,1,1,-1,-1,-1]
        for i in range(len(lst)-1):#run from i until size of lst-1
            self.__update_board(row+lst[i],column+lst[i+1])

    
    def play(self):
#The function conducts a dialogue with the user
#Each time, she asks him to select a tile on the board using a pair of numbers (a row) 
#and Column
# After he chooses, she updates the board and manages the minesweeper game and catches anomalies 
        try:
            row,space,column = input("enter a row and column: ")
            while not self.__board[int(row)-1][int(column)-1].get_has_mine():#loop that chack that user not select bomb
                self.__update_board(int(row)-1, int(column)-1)
                self.__print_board()
                hidden = [1 for i in range(self.__size) for j in range(self.__size) if self.__board[i][j].get_hidden()]
                sums = sum(hidden) - self.__num_mines
                if sums == 0:
                    print("You won!")
                    return
                print(f'{sums} are still hidden keep going !')
                row,space,column = input("enter a row and column:")
            self.__print_board(True)
            print("You lose")
        except:
            print("invalid input")
def main():
#The program asks the user to enter the size of the board and the number of mines, and creates
#The MSGame object and through it activates the MSGame play method that actually manages the minesweeper game. 
#Incorrect data the program will print to him invalid input    
    try:
        box=int(input("Please Enter size between 4 to 9:"))
        mines=int(input("Please enter number of Bomb:"))
        g=MSGame(box,mines)
        g.play()
    except ValueError:
       print("invalid input")
main()
        
    
                
        