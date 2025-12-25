# Task 6 More on Classes

class TictactoeException(Exception):
    # custom exception
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board:
    # Board class plus valid moves
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.turn = "X"
    
    # __str__
    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("------------------------ \n")
        lines.append(f" {self.board_array [1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("------------------------ \n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)
    
    # move()
    def move(self, move_string):
        move_string = move_string.strip().lower()

        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3

        if self.board_array[row][column]!= " ":
            raise TictactoeException("That spot is taken.")
        
        self.board_array[row][column] = self.turn

        # switch turns
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
    
    # whats_next()
    def whats_next(self):
        # to chech if board full 
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                    break
            if not cat:
                break
        
        win = False

        # to check rows
        for i in range(3):
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
        
        # to check columns
        if not win:
            for i in range(3):
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
        
        # to check diagonals
        if not win:
            if self.board_array[1][1] != " ":
                if self.board_array[0][0] == self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] == self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True
        
        # to decide outcome
        if win:
            # because turn switched after move, the winner is the opposite of current turn
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")
            
        if cat:
            return (True, "Cat's Game.")
        
        if self.turn == "X":
            return (False, "X's turn.")
        else:
            return (False, "O's turn.")
        
    # mainline game
if __name__ == "__main__":        
    board = Board()
    print(board)
    
    finished, message = board.whats_next()
    
    while not finished:
        print(message)
        move_string = input("Enter your move (e.g. 'upper left'):")

        try:
            board.move(move_string)
        except TictactoeException as e:
            print(e.message)
            continue

        print(board)
        finished, message = board.whats_next()

    print(message)
        

        
                    






    
