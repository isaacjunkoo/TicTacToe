"""This module establishes a connection between itself and player1 and launches a GUI for the tic-tac-toe game
it continues the game based on whether or not player1 wants to player1 wants to continue or not.

    player2_gui = gui()
"""
import socket
import tkinter as tk
from gameboard import BoardClass


class gui():
    """A class that creates a Tic-Tac-Toe GUI for the player and also establishes a connection between 2 players
while running the operations of the game.

    Attributes:
        title (str) = The title of the Gui
    

    """
    def __init__(self, title="Player2 Tic-Tac-Toe"):
        
        """Make a player2 GUI class by establishing variables and calling functions to start the game

        Args:
            title

        """
        
        #Create tkinter window
        self.setup_gui(title)

        #Create Tkinter variables
        self.host_id = tk.StringVar()
        self.port = tk.StringVar()
        self.player_name = tk.StringVar()
        self.player_move = tk.IntVar()
        self.play_again = tk.StringVar()
        self.results = tk.StringVar()
        self.stats = tk.StringVar()
        self.current_player = tk.StringVar()
        self.connection_button = tk.StringVar()
        self.start_name = tk.StringVar()
        self.button_1 = tk.StringVar()
        self.button_2 = tk.StringVar()
        self.button_3 = tk.StringVar()
        self.button_4 = tk.StringVar()
        self.button_5 = tk.StringVar()
        self.button_6 = tk.StringVar()
        self.button_7 = tk.StringVar()
        self.button_8 = tk.StringVar()
        self.button_9 = tk.StringVar()
        self.button = ''

        #creating variables for the whole GUI
        self.player1_name = ''

        #Create Tkinter Objects
        self.create_board()
        self.host_info_entry()
        self.player_name_entry()
        self.current_player_display()
        self.stats_display()
        self.result_display()
        self.connect_button()
        
        
    def setup_gui(self, title: str) -> None:
        """initializes the GUI for the player

        Args:
            title : the title of the GUI
        """
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry('580x570')
        self.root.resizable(0,0)

    
    def create_board(self) -> None:
        """Creates a the tic-tac-toe board in the GUI
        and makes each cell of the board into a button

        """
        self.b1 = tk.Button(self.root, textvariable = self.button_1, height = 4, width = 7, command = lambda: self.button_clicked('b1'))
        self.b2 = tk.Button(self.root, textvariable = self.button_2, height = 4, width = 7, command = lambda: self.button_clicked('b2'))
        self.b3 = tk.Button(self.root, textvariable = self.button_3, height = 4, width = 7, command = lambda: self.button_clicked('b3'))

        self.b4 = tk.Button(self.root, textvariable = self.button_4, height = 4, width = 7, command = lambda: self.button_clicked('b4'))
        self.b5 = tk.Button(self.root, textvariable = self.button_5, height = 4, width = 7, command = lambda: self.button_clicked('b5'))
        self.b6 = tk.Button(self.root, textvariable = self.button_6, height = 4, width = 7, command = lambda: self.button_clicked('b6'))

        self.b7 = tk.Button(self.root, textvariable = self.button_7, height = 4, width = 7, command = lambda: self.button_clicked('b7'))
        self.b8 = tk.Button(self.root, textvariable = self.button_8, height = 4, width = 7, command = lambda: self.button_clicked('b8'))
        self.b9 = tk.Button(self.root, textvariable = self.button_9, height = 4, width = 7, command = lambda: self.button_clicked('b9'))

        self.b1.grid(row=0, column=4)
        self.b2.grid(row=0, column=5)
        self.b3.grid(row=0, column=6)

        self.b4.grid(row=1, column=4)
        self.b5.grid(row=1, column=5)
        self.b6.grid(row=1, column=6)

        self.b7.grid(row=2, column=4)
        self.b8.grid(row=2, column=5)
        self.b9.grid(row=2, column=6)

        self.freeze_board()
        
    def reset_buttons(self) -> None:
        """Resets the gameboard by chaning all the cells back into empty cells

        """
        self.button_1.set(" ")
        self.button_2.set(" ")
        self.button_3.set(" ")
        self.button_4.set(" ")
        self.button_5.set(" ")
        self.button_6.set(" ")
        self.button_7.set(" ")
        self.button_8.set(" ")
        self.button_9.set(" ")

    def freeze_board(self) -> None:
        """Freezes the buttons/board so the board cannot be tampered with
        and players cannot make moves when its not their turn
        
        """
        self.b1["state"] = 'disabled'
        self.b2["state"] = 'disabled'
        self.b3["state"] = 'disabled'
        self.b4["state"] = 'disabled'
        self.b5["state"] = 'disabled'
        self.b6["state"] = 'disabled'
        self.b7["state"] = 'disabled'
        self.b8["state"] = 'disabled'
        self.b9["state"] = 'disabled'
        
        

    def unfreeze_board(self) -> None:
        """unfreezes the buttons/board so the player can make a move

        """
        self.b1["state"] = 'normal'
        self.b2["state"] = 'normal'
        self.b3["state"] = 'normal'
        self.b4["state"] = 'normal'
        self.b5["state"] = 'normal'
        self.b6["state"] = 'normal'
        self.b7["state"] = 'normal'
        self.b8["state"] = 'normal'
        self.b9["state"] = 'normal'
        
        
    
    def host_info_entry(self) -> None:
        """Creates an entry for the player to input the Host ID and Port number

        """
        self.host_id.set("Delete and Enter Host ID")
        self.host_entry = tk.Entry(self.root, textvariable = self.host_id, width = 21)
        self.host_entry.grid(row = 0, column = 1)

        self.port.set("Delete and Enter Port #")
        self.port_entry = tk.Entry(self.root, textvariable = self.port, width = 21)
        self.port_entry.grid(row=1, column = 1)

    def player_name_entry(self) -> None:
        """Creates an entry for the player to input their name into

        """
        self.left_spacer = tk.Label(self.root, text = '', width = 5)
        self.left_spacer.grid(row=0, column=0)
        self.right_spacer = tk.Label(self.root, text = '', width = 5)
        self.right_spacer.grid(row=0, column=2)
        
        self.start_name.set("Delete and Enter Name")
        self.player_entry = tk.Entry(self.root, textvariable = self.start_name, width = 20)
        self.player_entry.grid(row=2, column =1)

    def connect_button(self) -> None:
        """creates a button so that players can click to connect to another player

        """
        self.connection_button.set("Establish Connect")
        self.connect = tk.Button(self.root, textvariable = self.connection_button, width = 15, command = lambda: self.connect_players(self.host_id.get(), self.port.get()))
        self.connect.grid(row = 3, column = 1)

    def connect_players(self, host_id, port) -> None:
        """When the connect button is clicked, this method will attempt to establish a socket so that player1 will be able to connect,
        if connection is bad, it will ask for different inputs. After a successful connection, it will receive player1's name and send player2's name
        then starts the game.

        Args:
            host_id
            port

        """
        
        try:
            port = int(port)

            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverSocket.bind((host_id, port))
            serverSocket.listen(1)
            self.connection_button.set("Waiting for Player1")
            
            self.connect["state"] = "disabled"
            self.host_entry["state"] = "disabled"
            self.port_entry["state"] = "disabled"
            self.player_entry["state"] = "disabled"

            self.player2 = BoardClass('player2')

            self.clientSocket, clientAddress = serverSocket.accept()

            self.names = str(self.start_name.get())

            self.player1_name = self.clientSocket.recv(1024).decode('ascii')
            self.player_name.set("Player 1's Name: " + self.player1_name)


            self.clientSocket.send(self.start_name.get().encode())
            self.stats.set("Player Stats\n Player Name: " + self.names + "\nLast Move:" + self.player2.previous_turn_player + "\nGames Played: " + str(self.player2.num_played) +
                   "\nGames Won: " + str(self.player2.num_wins) + "\nGames Lost: " + str(self.player2.num_losses) + "\nGames Tied: " + str(self.player2.num_ties))
            self.player2.updateGamesPlayed()
            self.player1_res = self.clientSocket.recv(1024).decode('ascii')

            self.start_game()
       
        except:
            self.host_id.set("Invalid Input/Inputs... Try Again")
            self.port.set("Invalid Input/Inputs... Try Again")

    def start_game(self) -> None:
        """Starts game and receives player1's move and update's player2's board accordingly, then checks if the move resulted in a win/loss/tie, if so
        it receives a play again response from player1, if not, it unfreezes player2's board allowing them to make a move.

        """
        if self.player1_res == 'Play Again? Delete and Enter Y/N':
            self.current_player.set('Current Player: ' + self.player1_name)
            self.root.update()
            opponent_moves = self.clientSocket.recv(1024).decode('ascii')
            self.results.set("Game In Progress")

            self.player2.updateGameBoard(opponent_moves, self.player1_name)
            
            if opponent_moves == 'a1':
                self.button_1.set('X')
            elif opponent_moves == 'a2':
                self.button_2.set('X')
            elif opponent_moves == 'a3':
                self.button_3.set('X')
            elif opponent_moves == 'b1':
                self.button_4.set('X')
            elif opponent_moves == 'b2':
                self.button_5.set('X')
            elif opponent_moves == 'b3':
                self.button_6.set('X')
            elif opponent_moves == 'c1':
                self.button_7.set('X')
            elif opponent_moves == 'c2':
                self.button_8.set('X')
            elif opponent_moves == 'c3':
                self.button_9.set('X')

            self.root.update()
            check_loss_tie = self.player2.boardIsFull()
            if check_loss_tie == "True":
                self.player2.setPrevious(self.player1_name)
                self.results.set("Tie Game! Waiting for P1...")
                self.stats.set("Player Stats\n Player Name: " + str(self.names) + "\nLast Move:" + self.player1_name + "\nGames Played: " + str(self.player2.num_played) +
                               "\nGames Won: " + str(self.player2.num_wins) + "\nGames Lost: " + str(self.player2.num_losses) + "\nGames Tied: " + str(self.player2.num_ties))
                self.root.update()
                play_again_response = self.clientSocket.recv(1024).decode('ascii')
                if play_again_response == 'y' or play_again_response == 'Y':
                    self.reset_buttons()
                    self.player2.resetGameBoard()
                    self.player2.updateGamesPlayed()
                    self.results.set("Game in Progress")

                    self.root.update()
                    self.start_game()
                if play_again_response == 'n' or play_again_response == 'N':
                    self.clientSocket.close()
                    self.root.destroy()
                    quit()
            if check_loss_tie == True:
                self.player2.setPrevious(self.player1_name)
                self.results.set("You Lost! Waiting for P1...")
                self.stats.set("Player Stats\n Player Name: " + str(self.names) + "\nLast Move:" + self.player1_name + "\nGames Played: " + str(self.player2.num_played) +
                               "\nGames Won: " + str(self.player2.num_wins) + "\nGames Lost: " + str(self.player2.num_losses) + "\nGames Tied: " + str(self.player2.num_ties))
                self.root.update()
                play_again_response = self.clientSocket.recv(1024).decode('ascii')
                if play_again_response == 'y' or play_again_response == 'Y':
                    self.reset_buttons()
                    self.player2.resetGameBoard()
                    self.player2.updateGamesPlayed()
                    self.results.set("Game in Progress")
                    self.root.update()
                    self.start_game()
                if play_again_response == 'n' or play_again_response == 'N':
                    self.clientSocket.close()
                    self.root.destroy()
                    quit()
            self.current_player.set("Current Player: " + self.start_name.get())
            self.root.update()
            self.unfreeze_board()
            
            
    def button_clicked(self, button: str) -> bool:
        """reacts the a button being clicked, updating the board accordingly, and checking the results and receiving a response from player1 if they
        want to continue the game or not

        args:
            button

        """
        if button == 'b1':
            if self.button_1.get() != "X" and self.button_1.get() != "O":
                self.button = 'a1'
                self.button_1.set("O")
            else:
                return None
        elif button == 'b2':
            if self.button_2.get() != "X" and self.button_2.get() != "O":
                self.button = 'a2'
                self.button_2.set("O")
            else:
                return None
        elif button == 'b3':
            if self.button_3.get() != "X" and self.button_3.get() != "O":
                self.button = 'a3'
                self.button_3.set("O")
            else:
                return None
        elif button == 'b4':
            if self.button_4.get() != "X" and self.button_4.get() != "O":
                self.button = 'b1'
                self.button_4.set("O")
            else:
                return None
        elif button == 'b5':
            if self.button_5.get() != "X" and self.button_5.get() != "O":
                self.button = 'b2'
                self.button_5.set("O")
            else:
                return None
        elif button == 'b6':
            if self.button_6.get() != "X" and self.button_6.get() != "O":
                self.button = 'b3'
                self.button_6.set("O")
            else:
                return None
        elif button == 'b7':
            if self.button_7.get() != "X" and self.button_7.get() != "O":
                self.button = 'c1'
                self.button_7.set("O")
            else:
                return None
        elif button == 'b8':
            if self.button_8.get() != "X" and self.button_8.get() != "O":
                self.button = 'c2'
                self.button_8.set("O")
            else:
                return None
        elif button == 'b9':
            if self.button_9.get() != "X" and self.button_9.get() != "O":
                self.button = 'c3'
                self.button_9.set("O")
            else:
                return None
        self.freeze_board()
        self.root.update()
        self.player2.updateGameBoard(self.button, 'player2')
        self.clientSocket.send(self.button.encode())
        if self.player2.isWinner():
            self.player2.setPrevious(self.start_name)
            self.results.set("You Won! Waiting for P1...")
            self.stats.set("Player Stats\n Player Name: " + str(self.start_name.get()) + "\nLast Move:" + self.start_name.get() + "\nGames Played: " +
                           str(self.player2.num_played) + "\nGames Won: " + str(self.player2.num_wins) + "\nGames Lost: " + str(self.player2.num_losses) + "\nGames Tied: " + str(self.player2.num_ties))
            self.root.update()
            play_again_response = self.clientSocket.recv(1024).decode('ascii')
            if play_again_response == 'y' or play_again_response == 'Y':
                self.reset_buttons()
                self.player2.updateGamesPlayed()
                self.player2.resetGameBoard()
                self.root.update()
            if play_again_response == 'n' or play_again_response == 'N':
                self.clientSocket.close()
                self.root.update()
                self.root.destroy()
                quit()
        self.start_game()
            
            
        


    def current_player_display(self) -> None:
        """Creates a label for who the current player is making the move

        """
        self.current_player.set("Current Player : ")
        self.current_n = tk.Label(self.root, textvariable = self.current_player, height = 2, width = 20)
        self.current_n.grid(row=5, column=1)

        self.player_name.set("Player 1 Name: ")
        self.player_n = tk.Label(self.root, textvariable = self.player_name, height = 3, width = 20)
        self.player_n.grid(row = 4, column =1)

    def result_display(self) -> None:
        """Creates a label for the game's results

        """
        self.results.set("Game results : Game In Progress ")
        self.game_results = tk.Label(self.root, textvariable = self.results, height = 1, width = 25)
        self.game_results.grid(row = 6, column = 1)


    def stats_display(self) -> None:
        """creates a label for the player's stats according to each game played

        """
        self.stats.set("Player Stats\n Player Name:\n Last Move :\n Games Played:\n Games Won: \n Games Lost: \n Games Tied: \n")
        self.final_stats = tk.Label(self.root, textvariable = self.stats, height = 13, width = 20)
        self.final_stats.grid(row= 8, column = 1)



if __name__ == "__main__":
    player2_gui = gui()
    
