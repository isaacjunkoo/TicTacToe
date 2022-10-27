class BoardClass:
    """A class to store and handle information about the Player's Board

    Attributes:
        player_name (str) : The players user name
        previous_turn_player (str) : user name of the last player to have a turn
        num_wins (int) : Number of wins
        num_ties (int) : Number of ties
        num_losses (int) : Number of losses

    """

    def __init__(self, player_name: str = "", previous_turn_player: str = "No Previous Player",
                 num_wins: int = 0, num_ties: int = 0, num_losses: int = 0, num_played: int = 0,
                board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]) -> None:

        """Make a BoardClass

        Args:
            player_name
            previous_turn_player
            num_wins
            num_ties
            num_losses
            num_played
            board

        """
        self.setName(player_name)
        self.setPrevious(previous_turn_player)
        self.setNumWins(num_wins)
        self.setNumTies(num_ties)
        self.setNumLosses(num_losses)
        self.setNumPlayed(num_played)
        self.setBoard(board)

    def setName(self, player_name: str) -> None:
        """initializes player_name from user's input

        Args:
            player_name : the player's name
        """
        self.player_name = player_name

    def setPrevious(self, previous_turn_player: str) -> None:
        """Sets the name for the last player to make a move

        Args:
            previous_turn_player : The name of the last player to make a move
        """
        self.previous_turn_player = previous_turn_player

    def setNumWins(self, num_wins: int) -> None:
        """Sets the default number of wins for the player to zero

        Args:
            num_wins : The number of wins a player has
        """
        self.num_wins = num_wins

    def setNumTies(self, num_ties: int) -> None:
        """Sets the default number of Ties for the player to zero

        Args:
            num_ties : The number of Ties a player has
        """
        self.num_ties = num_ties

    def setNumLosses(self, num_losses: int) -> None:
        """Sets the default number of Loss for the player to zero

        Args:
            num_losses : The number of losses a player has
        """
        self.num_losses = num_losses

    def setBoard(self, board: list) -> None:
        """Sets the board of a player as the defauly empty board

        Args:
            board : the default empty board
        """
        self.board = board

    def setNumPlayed(self, num_played: int) -> None:
        """Sets the default number of rounds played for the player to zero

        Args:
            num_played : The number of rounds played
        """
        self.num_played = num_played


    def printBoard(self) -> str:
        """prints the current state of the board

        Returns:
            A formatted version of the current state of the board
        """
        show_board = '            1  2  3\n          '
        rows = ['A', 'B', 'C']
        counter = 0

        for i in self.board:
            print_row = ''
            for spot in i:
                print_row = print_row + '[' + spot + ']'
            show_board = show_board + str(rows[counter])+ print_row + '\n          '
            counter += 1
        return show_board

    def addWin(self) -> None:
        """Increments the times a player wins by 1
        """
        self.num_wins += 1

    def addTie(self) -> None:
        """Increments the times a player Ties by 1
        """
        self.num_ties += 1

    def addLoss(self) -> None:
        """Increments the times a player Loses by 1
        """
        self.num_losses += 1

    def updateGamesPlayed(self) -> None:
        """Increments the times a player plays a game by 1
        """
        self.num_played += 1

    def resetGameBoard(self) -> None:
        """Resets the game board for the player
        """
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    def updateGameBoard(self, player_move, player) -> str:
        """Updates the board for the player according to their move

        Args:
            player_move : the move of the player
            player : the name of the player corresponding to the move

        Returns:
            True if the move was valid, False otherwise
        """
        board_row = [['a', 'A'],['b', 'B'], ['c','C']]
        spot_checker = ['X', 'O']
        valid_move = False
        player_identity = player
        while not valid_move:
            if len(player_move) == 2:
                chosen_row = player_move[0]
                chosen_column = int(player_move[1]) - 1
                if chosen_column < 3:
                    if chosen_row in board_row[0]:
                        if self.board[0][chosen_column] in spot_checker:
                            valid_move = False
                        elif self.board[0][chosen_column] == ' ':
                            if player_identity == 'player2':
                                self.board[0][chosen_column] = 'O'
                                valid_move = True
                            else:
                                self.board[0][chosen_column] = 'X'
                                valid_move = True

                    elif chosen_row in board_row[1]:
                        if self.board[1][chosen_column] in spot_checker:
                            valid_move = False
                        elif self.board[1][chosen_column] == ' ':
                            if player_identity == 'player2':
                                self.board[1][chosen_column] = 'O'
                                valid_move = True
                            else:
                                self.board[1][chosen_column] = 'X'
                                valid_move = True

                    elif chosen_row in board_row[2]:
                        if self.board[2][chosen_column] in spot_checker:
                            valid_move = False
                        elif self.board[2][chosen_column] == ' ':
                            if player_identity == 'player2':
                                self.board[2][chosen_column] = 'O'
                                valid_move = True
                            else:
                                self.board[2][chosen_column] = 'X'
                                valid_move = True
                    else:
                        valid_move = False
                else:
                    valid_move = False
            else:
                valid_move = False
        return player_move
                
                
                

    def isWinner(self) -> bool:
        """Checks if the board has a winner by first checking if there is a horizontal match,
        then checks if there is a vertical match, and finally checks if there is a diagonal match

        Returns:
            True or False if there is a winner or not
        """
        #check every row for Horizontal Match
        player_not_won = True
        for row in self.board:
            X_counter = 0
            O_counter = 0
            for space in row:
                if space == row[0] and row[0] == "X":
                    X_counter += 1
                if space == row[0] and row[0] == "O":
                    O_counter += 1
            if X_counter == 3 and self.player_name != 'player2':
                self.addWin()
                return False
            elif O_counter == 3 and self.player_name != 'player2':
                self.addLoss()
                return False
            elif O_counter == 3 and self.player_name == 'player2':
                self.addWin()
                return True
            elif X_counter == 3 and self.player_name == 'player2':
                self.addLoss()
                return True

        #check vertical Match
        counter = 0
        if player_not_won == True:
            while counter < 3:
                x_vertical_confirm = 0
                o_vertical_confirm = 0
                for row in self.board:
                    if row[counter] == "X":
                        x_vertical_confirm += 1
                    if row[counter] == "O":
                        o_vertical_confirm += 1

                if x_vertical_confirm == 3 and self.player_name != 'player2':
                    self.addWin()
                    return False
                elif o_vertical_confirm == 3 and self.player_name != 'player2':
                    self.addLoss()
                    return False
                elif o_vertical_confirm == 3 and self.player_name == 'player2':
                    self.addWin()
                    return True
                elif x_vertical_confirm == 3 and self.player_name == 'player2':
                    self.addLoss()
                    return True
                counter += 1

        #check diagonal
        top_left = self.board[0][0]
        middle_spot = self.board[1][1]
        bottom_right = self.board[2][2]
        top_right = self.board[0][2]
        bottom_left = self.board[2][0]
        if player_not_won == True:
            if self.player_name != 'player2':
                if top_left == "X" and middle_spot == "X" and bottom_right == "X":
                    self.addWin()
                    return False
                elif top_right == "X" and middle_spot == "X" and bottom_left == "X":
                    self.addWin()
                    return False
                elif top_right == "O" and middle_spot == "O" and bottom_left == "O":
                    self.addLoss()
                    return False
                elif top_left == "O" and middle_spot == "O" and bottom_right == "O":
                    self.addLoss()
                    return False
            else:
                if top_left == "O" and middle_spot == "O" and bottom_right == "O":
                    self.addWin()
                    return True
                elif top_right == "O" and middle_spot == "O" and bottom_left == "O":
                    self.addWin()
                    return True
                elif top_right == "X" and middle_spot == "X" and bottom_left == "X":
                    self.addLoss()
                    return True
                elif top_left == "X" and middle_spot == "X" and bottom_right == "X":
                    self.addLoss()
                    return True
        if self.player_name == 'player2':
            return False
        return player_not_won
    
    
    def boardIsFull(self) -> bool:
        """Checks if the board is full and if there is a winner or if it is a tie

        Returns:
            True if the board is full and it is a tie game and returns false if the board is not full
            or it is not a tie
        """
        full_rows = 0
        for row in self.board:
            if " " not in row:
                full_rows += 1

        x = self.isWinner()
        if self.player_name == 'player2':
            if full_rows == 3 and not x:
                self.addTie()
                return "True"
            elif full_rows == 3 and x:
                return True
        if full_rows == 3 and x:
            self.addTie()
            return "True"
        elif self.player_name == 'player2':
            if x:
                return True
        elif not x:
            return True
        else:
            return False
            
            

    def printStats(self) -> None:
        """Prints the stats for the player, including the number of games played, won, lost, tied,
        and the player's name and the name of the last player to make a move.

        """
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~\n\nPlayer Name: " + self.player_name + '\n' + "Previous Player: " + self.previous_turn_player + '\n' +
              "Games Played: " + str(self.num_played) + '\n' + "Games Won: " + str(self.num_wins) + '\n' +
              "Games Lost: " + str(self.num_losses) + '\n' + "Games Tied: " + str(self.num_ties))
