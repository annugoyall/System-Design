# design n*n tic-tac-toe board for m players

class Board:
    def __init__(self, size):
        self.size = size
        self.moves = set()
    
    def is_full(self):
        return len(self.moves) == self.size ** 2
    
    def is_valid_move(self, move):
        return move not in self.moves and move[0] < self.size and move[1] < self.size
    
    def make_move(self, move):
        if self.is_valid_move(move):
            if move not in self.moves:
                self.moves.add(move)
                return True
        return False
    
class Player:
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
        self.moves = set()

    def check_winner(self, board_size):
        if len(self.moves) < board_size:
            return False
        for i in range(board_size):
            if all((i, j) in self.moves for j in range(board_size)):
                return True
            if all((j, i) in self.moves for j in range(board_size)):
                return True
        if all((i, i) in self.moves for i in range(board_size)):
            return True
        if all((i, board_size - i - 1) in self.moves for i in range(board_size)):
            return True
        return False

class Game:
    def __init__(self, n):
        self.board = Board(n)
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        ind = 0
        current_player = self.players[ind]
        while not self.board.is_full():
            print("Current player: ", current_player.name, ind)
            move = input("Enter move: ").split()
            move = (int(move[0]), int(move[1]))
            if self.board.make_move(move):
                print("Valid move")
                current_player.moves.add(move)
                if current_player.check_winner(self.board.size):
                    return current_player.name
                ind += 1
                current_player = self.players[ind % len(self.players)]
        return None

    def make_move(self, player, move):
        if self.board.make_move(move):
            player.moves.add(move)
            return True
        return False
    
game = Game(6)
player1 = Player("Player 1", "X")
player2 = Player("Player 2", "O")
player3 = Player("Player 3", "Y")
game.add_player(player1)
game.add_player(player2)
game.add_player(player3)
print(game.start_game())
