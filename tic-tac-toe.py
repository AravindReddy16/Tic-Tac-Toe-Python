class Game:
    def __init__(self):
        self.l=[1,2,3,4,5,6,7,8,9]
        self.turn=1
        self.over=0
    def board(self):
        print(f' {self.l[0]} | {self.l[1]} | {self.l[2]}')
        print(' --|---|--')
        print(f' {self.l[3]} | {self.l[4]} | {self.l[5]}')
        print(' --|---|--')
        print(f' {self.l[6]} | {self.l[7]} | {self.l[8]}')
    def play(self):
        while True:
            self.board()
            if self.turn==1:
                x=int(input("X's Turn: "))-1
                if self.l[x]!='X' and self.l[x]!='O':
                    self.l[x]='X'
                    self.turn=0
            else:
                x=int(input("O's Turn: "))-1
                if self.l[x]!='X' and self.l[x]!='O':
                    self.l[x]='O'
                    self.turn=1
            for i in range(3):
                if self.l[i*3]==self.l[i*3+1]==self.l[i*3+2]=='X':
                    self.board()
                    print("X's won the Game !...")
                    self.over=1
                elif self.l[i*3]==self.l[i*3+1]==self.l[i*3+2]=='O':
                    self.board()
                    print("O's won the Game !...")
                    self.over=1
                elif self.l[i]==self.l[i+3]==self.l[i+6]=='X':
                    self.board()
                    print("X's won the Game !...")
                    self.over=1
                elif self.l[i]==self.l[i+3]==self.l[i+6]=='O':
                    self.board()
                    print("O's won the Game !...")
                    self.over=1
                elif self.l[0]==self.l[4]==self.l[8]=='X':
                    self.board()
                    print("X's won the Game !...")
                    self.over=1
                elif self.l[0]==self.l[4]==self.l[8]=='O':
                    self.board()
                    print("O's won the Game !...")
                    self.over=1
                elif self.l[2]==self.l[4]==self.l[6]=='X':
                    self.board()
                    print("X's won the Game !...")
                    self.over=1
                elif self.l[2]==self.l[4]==self.l[6]=='O':
                    self.board()
                    print("O's won the Game !...")
                    self.over=1
            if self.over==1:
                break
oGame=Game()
oGame.play()