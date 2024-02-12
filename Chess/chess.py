class Chess:
    def __init__(self, PlayerA, PlayerB):
        self.PlayerA = PlayerA
        self.PlayerB = PlayerB
        self.board = Board()
        self.currPlayer = PlayerA

class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        self.resetBoard()

    def DisplayBoard(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != None:
                    print(self.board[i][j].piece.name(), end=" ")
                else:
                    print("Empty", end=" ")
            print()

    def resetBoard(self):
        for i in range(8):
            self.board[1][i] = Spot(0, i, Pawn(isWhite = False))
            self.board[6][i] = Spot(6, i, Pawn(isWhite = True))

        # Place the rooks
        self.board[0][0] = Spot(0, 0, Rook(isWhite = False))
        self.board[0][7] = Spot(0, 7, Rook(isWhite = False))
        self.board[7][0] = Spot(7, 0, Rook(isWhite = True))
        self.board[7][7] = Spot(7, 7, Rook(isWhite = True))

        # Place the knights
        self.board[0][1] = Spot(0, 1, Knight(isWhite = False))
        self.board[0][6] = Spot(0, 6, Knight(isWhite = False))
        self.board[7][1] = Spot(7, 1, Knight(isWhite = True))
        self.board[7][6] = Spot(7, 6, Knight(isWhite = True))

        # Place the bishops
        self.board[0][2] = Spot(0, 2, Bishop(isWhite = False))
        self.board[0][5] = Spot(0, 5, Bishop(isWhite = False))
        self.board[7][2] = Spot(7, 2, Bishop(isWhite = True))
        self.board[7][5] = Spot(7, 5, Bishop(isWhite = True))

        # Place the queens
        self.board[0][3] = Spot(0, 3, Queen(isWhite = False))
        self.board[7][3] = Spot(7, 3, Queen(isWhite = True))

        # Place the kings
        self.board[0][4] = Spot(0, 4, King(isWhite = False))
        self.board[7][4] = Spot(7, 4, King(isWhite = True))

    def move(self, start, end):
        piece = self.board[start[0]][start[1]].piece
        if piece.canMove(self, start, end):
            piece2 = self.board[end[0]][end[1]]
            if piece2 != None:
                piece2 = piece2.piece
                piece2.isKilled = True
            self.movePiece(piece, end)
            self.board[start[0]][start[1]] = None
            return True
        return False
    
    def movePiece(self, piece, end):
        self.board[end[0]][end[1]] = Spot(end[0], end[1], piece)

class Spot:
    def __init__(self, x, y, piece):
        self.x = x
        self.y = y
        self.piece = piece

class Piece:
    def __init__(self, isWhite):
        self.isWhite = isWhite
        self.isKilled = False

    def canMove(self, board, start, end):
        pass

    def Move(self, board, start, end):
        pass

    def name(self):
        pass

class King(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite)

    def canMove(self, board, start, end):
        return True
    
    def Move(self, board, start, end):
        pass

    def name(self):
        return "King"

class Queen(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite)

    def canMove(self, board, start, end):
        return True
    
    def Move(self, board, start, end):
        pass    

    def name(self):
        return "Queen"

class Bishop(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite)

    def canMove(self, board, start, end):
        return True
    
    def Move(self, board, start, end):
        pass

    def name(self):
        return "Bishop"

class Knight(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite)

    def canMove(self, board, start, end):
        return True
    
    def Move(self, board, start, end):
        pass

    def name(self):
        return "Knight"
    
class Rook(Piece):

    def __init__(self, isWhite):
        super().__init__(isWhite)

    def canMove(self, board, start, end):
        return True
    
    def Move(self, board, start, end):
        pass

    def name(self):
        return "Rook"

class Pawn(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite)

    def canMove(self, board, start, end):
        return True
    
    def Move(self, board, start, end):
        pass

    def name(self):
        return "Pawn"

class Player:
    def __init__(self, isWhite):
        self.isWhite = isWhite


# Implement a chess game using object oriented principles.

game = Chess(PlayerA = Player(isWhite = True), PlayerB = Player(isWhite = False))
game.board.DisplayBoard()
print()
game.board.move((1, 0), (3, 0))
game.board.DisplayBoard()