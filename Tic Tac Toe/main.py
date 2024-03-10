
class Piece:
    
    def __init__(self) -> None:
        self.name = None


class Zero(Piece):
    
    def __init__(self) -> None:
        super().__init__()
        self.name = '0'


class Cross(Piece):

    def __init__(self) -> None:
        super().__init__()
        self.name = 'X'

class Board:
    _instance = None

    def get_instance():
        if Board._instance is None:
            Board._instance = Board()
        return Board._instance

    def __init__(self) -> None:
        self.board = [[None for _ in range(3)] for _ in range(3)]
        _instance = None

    def reset_board(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]

    def board_full(self):
        full = True

        for row in self.board:
            if None in row:
                full = False
                break

        return full
    
    def print_board(self):
        for row in self.board:
            for col in row:
                print(col.name if col is not None else "None", end=' ')
            print()

    def checkWinner(self, player):
        piece = Player.get_piece(player)

        for row in self.board:
            if row.count(piece) == 3:
                return True
            
        for i in range(3):
            if self.board[0][i] == piece and self.board[1][i] == piece and self.board[2][i] == piece:
                return True
            
        if self.board[0][0] == piece and self.board[1][1] == piece and self.board[2][2] == piece:
            return True
        
        if self.board[0][2] == piece and self.board[1][1] == piece and self.board[2][0] == piece:
            return True
        
        return False

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.piece = None

    def get_piece(self):
        return self.piece

    def set_piece(self, piece):
        self.piece = piece

    def make_move(self, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2:
            return False
        if Board.get_instance().board[x][y] is None:
            Board.get_instance().board[x][y] = self.piece
            return True
        return False

class Game:
    def __init__(self, player1, player2) -> None:
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.board = Board.get_instance()

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def start_game(self):
        while True:
            print("Player's turn:", self.current_player.name)
            x, y = map(int, input().split())
            if self.current_player.make_move(x, y):
                if self.board.checkWinner(self.current_player):
                    print(f'{self.current_player.name} wins!')
                    break
                self.switch_player()
                self.board.print_board()
            else:
                print('Invalid move')

            if self.board.board_full():
                print('Draw!')
                break

player1 = Player('Player1')
piece = Zero()
player1.set_piece(piece)
player2 = Player('Player2')
piece = Cross()
player2.set_piece(piece)

game = Game(player1, player2)
game.start_game()