import os


class Board():

    def __init__(self):
        self.grid_test=["X","X","O","X","O","X","X","O","X"]
        self.grid=[" "*3 for item in range(9)]
        #print (self.grid)
        self.game_over=False
        self.row1=[1,2,3]
        self.row2=[4,5,6]
        self.row3=[7,8,9]
        self.col1=[1,4,7]
        self.col2=[2,5,8]
        self.col3=[3,6,9]
        self.dia1=[1,5,9]
        self.dia2=[3,5,7]
        self.rows=[self.row1,self.row2,self.row3]
        self.cols=[self.col1,self.col2,self.col3]
        self.diag=[self.dia1,self.dia2]
        self.matrix=[self.rows,self.cols,self.diag]
        self.free_spots=[1,2,3,4,5,6,7,8,9]
        
        
        

    def __str__(self):
        return f"{self.grid[0]}|{self.grid[1]}|{self.grid[2]}\n-----------\n{self.grid[3]}|{self.grid[4]}|{self.grid[5]}\n-----------\n{self.grid[6]}|{self.grid[7]}|{self.grid[8]}\n"

    def mark(self,spot,player):
        self.grid[spot]=" " + player + " "
        os.system('clear')
        self.free_spots.remove(spot+1)
        print (self)
        self.check_game(spot,player)
        
    def check_game(self,spot,player):
        for _ in self.matrix:
            for r in _:
                for v in r:
                    if v == spot+1:
                        ind=r.index(v)
                        r[ind]=player
                        if len(set(r))==1:
                            os.system('clear')
                            print (f"We have a winner {player}")
                            self.game_over=True
                            print (self)
                 
