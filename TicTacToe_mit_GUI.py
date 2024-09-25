import copy
import tkinter as tk
import random

player_X = "X"
player_O = "O"  # Auch Computer
playing_vs_computer = False
computers_turn = False


# Initiale Werte für das Spielfeld
def reset_game_state():
    global a, b, c, d, e, f, g, h, i, current_turn
    a, b, c = 1, 2, 3
    d, e, f = 4, 5, 6
    g, h, i = 7, 8, 9
    current_turn = "X"  # Spiel beginnt immer mit X
reset_game_state()

def mode_selection():
    def start_game(single_player):
        global playing_vs_computer
        playing_vs_computer = single_player
        selection_window.destroy()

    selection_window = tk.Tk()
    selection_window.title("Spielmodus auswählen")

    tk.Label(selection_window, text="Möchtest du alleine oder zu zweit spielen?", font=("Arial", 16)).pack(pady=10)

    single_player_button = tk.Button(selection_window, text="Alleine (gegen Computer)", font=("Arial", 14), command=lambda: start_game(True))
    single_player_button.pack(pady=5)

    multiplayer_button = tk.Button(selection_window, text="Zu zweit (mit einem Freund)", font=("Arial", 14), command=lambda: start_game(False))
    multiplayer_button.pack(pady=5)

    selection_window.mainloop()

def has_won(player):

    player_validation_string = f"{player}{player}{player}"

    if f"{a}{b}{c}" == player_validation_string:
        return True
    if f"{d}{e}{f}" == player_validation_string:
        return True
    if f"{g}{h}{i}" == player_validation_string:
        return True
    if f"{a}{d}{g}" == player_validation_string:
        return True
    if f"{b}{e}{h}" == player_validation_string:
        return True
    if f"{c}{f}{i}" == player_validation_string:
        return True
    if f"{a}{e}{i}" == player_validation_string:
        return True
    if f"{g}{e}{c}" == player_validation_string:
        return True
    return False

def tie():
    if isinstance(a, int) or isinstance(b, int) or isinstance(c, int) or isinstance(d, int):
        return False
    elif isinstance(e, int) or isinstance(f, int) or isinstance(g, int) or isinstance(h, int) or isinstance(i, int):
        return False
    return True

def disable_all_buttons():
    for button in buttons:
        button.config(state="disabled")

# Restart Game!
def ask_for_restart():
    restart_window = tk.Toplevel(window)
    restart_window.title("Nochmal spielen?")
    label = tk.Label(restart_window, text="Möchtest du nochmal spielen?", font=("Arial", 14))
    label.pack(pady=10)

    yes_button = tk.Button(restart_window, text="Ja", font=("Arial", 12), command=lambda: [restart_game(), restart_window.destroy()])
    yes_button.pack(side="left", padx=20, pady=10)

    no_button = tk.Button(restart_window, text="Nein", font=("Arial", 12), command=window.quit)
    no_button.pack(side="right", padx=20, pady=10)

def restart_game():
    reset_game_state()  # Spielfeld zurücksetzen
    label.config(text=f"Wähle ein Feld aus ({current_turn}):")
    
    # Buttons zurücksetzen
    for idx, button in enumerate(buttons):
        button.config(text=globals()[chr(97 + idx)], state="normal")


def button_input_changer(button, field_var_name):
    global current_turn, label, used_buttons

    used_buttons = []

    if isinstance(globals()[field_var_name], int):
        globals()[field_var_name] = current_turn  
        button.config(text=current_turn)
        used_buttons.append(field_var_name)
        
        
        if has_won(current_turn):
            label.config(text=f"Spiel beendet! {current_turn} hat gewonnen!")
            disable_all_buttons()
            ask_for_restart()
        elif tie():
            label.config(text="Unentschieden! Kein freies Feld mehr.")
            disable_all_buttons()
            ask_for_restart()
        else:
            current_turn = "O" if current_turn == "X" else "X"
            label.config(text=f"Wähle ein Feld aus ({current_turn}):")
        
            if playing_vs_computer == True and current_turn == "O":
                computer_input_changer()
                
    
                

def computer_input_changer():
    global current_turn, a, b, c, d, e, f, g, h, i

    almost_loosing_constelation = f"{player_X}{player_X}"
    almost_winning_constelation = f"{player_O}{player_O}"

    available_fields = [field for field in ["a", "b", "c", "d", "e", "f", "g", "h", "i"] if isinstance(globals()[field], int)]   
    
    #the code below is used for winning horizontally
    if f"{a}{b}" == almost_winning_constelation and "c"in available_fields:
        button_input_changer(buttons[2], 'c')
        
    elif f"{b}{c}" == almost_winning_constelation and "a" in available_fields:
        button_input_changer(buttons[0], 'a')
        
    elif f"{a}{c}" == almost_winning_constelation and "b" in available_fields:
        button_input_changer(buttons[1], 'b')
        
    elif f"{d}{e}" == almost_winning_constelation and "f" in available_fields:
        button_input_changer(buttons[5], 'f')
        
    elif f"{e}{f}" == almost_winning_constelation and "d" in available_fields:
        button_input_changer(buttons[3], 'd')
        
    elif f"{d}{f}" == almost_winning_constelation and "e" in available_fields:
        button_input_changer(buttons[4], 'e')
        
    elif f"{g}{h}" == almost_winning_constelation and "i" in available_fields:
        button_input_changer(buttons[8], 'i')
        
    elif f"{h}{i}" == almost_winning_constelation and "g" in available_fields:
        button_input_changer(buttons[6], 'g')

    elif f"{g}{i}" == almost_winning_constelation and "h" in available_fields:
        button_input_changer(buttons[7], 'h')
        
    elif f"{a}{d}" == almost_winning_constelation and "g" in available_fields:
        button_input_changer(buttons[6], 'g') 
    
    #the code below is used for winning Verticaly
    elif f"{d}{g}" == almost_winning_constelation and "a" in available_fields:
        button_input_changer(buttons[0], 'a')
        
    elif f"{a}{g}" == almost_winning_constelation and "d" in available_fields:
        button_input_changer(buttons[3], 'd')
        
    elif f"{b}{e}" == almost_winning_constelation and "h" in available_fields:
        button_input_changer(buttons[7], 'h')
        
    elif f"{e}{h}" == almost_winning_constelation and "b" in available_fields:
        button_input_changer(buttons[1], 'b')
        
    elif f"{b}{h}" == almost_winning_constelation and "e" in available_fields:
        button_input_changer(buttons[4], 'e')
        
    elif f"{c}{f}" == almost_winning_constelation and "i" in available_fields:
        button_input_changer(buttons[8], 'i')
        
    elif f"{f}{i}" == almost_winning_constelation and "c" in available_fields:
        button_input_changer(buttons[2], 'c')
        
    elif f"{c}{i}" == almost_winning_constelation and "f" in available_fields:
        button_input_changer(buttons[5], 'f')

    #the code below is used for diagonal winning  
    elif f"{a}{e}" == almost_winning_constelation and "i" in available_fields:
        button_input_changer(buttons[8], 'i')
        
    elif f"{e}{i}" == almost_winning_constelation and "a" in available_fields:
        button_input_changer(buttons[0], 'a')
        
    elif f"{a}{i}" == almost_winning_constelation and "e" in available_fields:
        button_input_changer(buttons[4], 'e')
        
    elif f"{c}{e}" == almost_winning_constelation and "g" in available_fields:
        button_input_changer(buttons[6], 'g')
        
    elif f"{e}{g}" == almost_winning_constelation and "c" in available_fields:
        button_input_changer(buttons[2], 'c')
        
    elif f"{g}{c}" == almost_winning_constelation and "e" in available_fields:
        button_input_changer(buttons[4], 'e')

   # The Code Below is used for Blocking the Opponent Horizontal
    elif f"{a}{b}" == almost_loosing_constelation and "c" in available_fields:
        button_input_changer(buttons[2], 'c')
        
    elif f"{b}{c}" == almost_loosing_constelation and "a" in available_fields:
        button_input_changer(buttons[0], 'a')
        
    elif f"{a}{c}" == almost_loosing_constelation and "b" in available_fields:
        button_input_changer(buttons[1], 'b')
        
    elif f"{d}{e}" == almost_loosing_constelation and "f" in available_fields:
        button_input_changer(buttons[5], 'f')
        
    elif f"{e}{f}" == almost_loosing_constelation and "d" in available_fields:
        button_input_changer(buttons[3], 'd')
        
    elif f"{d}{f}" == almost_loosing_constelation and "e" in available_fields:
        button_input_changer(buttons[4], 'e')
        
    elif f"{g}{h}" == almost_loosing_constelation and "i" in available_fields:
        button_input_changer(buttons[8], 'i')
        
    elif f"{h}{i}" == almost_loosing_constelation and "g" in available_fields:
        button_input_changer(buttons[6], 'g')
        
    elif f"{g}{i}" == almost_loosing_constelation and "h" in available_fields:
        button_input_changer(buttons[7], 'h')
        
    # The Code below is used for Blocking Vertical
    elif f"{a}{d}" == almost_loosing_constelation and "g" in available_fields:
        button_input_changer(buttons[6], 'g')
        
    elif f"{d}{g}" == almost_loosing_constelation and "a" in available_fields:
        button_input_changer(buttons[0], 'a')
        
    elif f"{a}{g}" == almost_loosing_constelation and "d" in available_fields:
        button_input_changer(buttons[3], 'd')
        
    elif f"{b}{e}" == almost_loosing_constelation and "h" in available_fields:
        button_input_changer(buttons[7], 'h')
        
    elif f"{e}{h}" == almost_loosing_constelation and "b" in available_fields:
        button_input_changer(buttons[1], 'b')
        
    elif f"{b}{h}" == almost_loosing_constelation and "e" in available_fields:
        button_input_changer(buttons[4], 'e')
        
    elif f"{c}{f}" == almost_loosing_constelation and "i" in available_fields:
        button_input_changer(buttons[8], 'i')
        
    elif f"{f}{i}" == almost_loosing_constelation and "c" in available_fields:
        button_input_changer(buttons[2], "c")
        
    elif f"{c}{i}" == almost_loosing_constelation and "f" in available_fields:
        button_input_changer(buttons[5], "f")
        
    #The Code Below is used to Block the Opponent Diagonally
    elif f"{a}{e}" == almost_loosing_constelation and "i" in available_fields:
            button_input_changer(buttons[8], 'i')
            
    elif f"{e}{i}" == almost_loosing_constelation and "a" in available_fields:
            button_input_changer(buttons[0], 'a')
            
    elif f"{a}{i}" == almost_loosing_constelation and "e" in available_fields:
            button_input_changer(buttons[4], 'e')
            
    elif f"{c}{e}" == almost_loosing_constelation and "g" in available_fields:
            button_input_changer(buttons[6], 'g')
            
    elif f"{e}{g}" == almost_loosing_constelation and "c" in available_fields:
            button_input_changer(buttons[2], 'c')
            
    elif f"{g}{c}" == almost_loosing_constelation and "e" in available_fields:
            button_input_changer(buttons[4], 'e')


    elif available_fields:

        avaiable_buttons = [] 

        choice = random.choice(buttons)
        index = buttons.index(choice)
        Field_VAR_NAME = chr(97 + index)
        button_input_changer(buttons[index], Field_VAR_NAME)

def game_window():
    global label, buttons, window, field_list

    window = tk.Tk()
    window.title("TicTacToe")

    label = tk.Label(window, text=f"Wähle ein Feld aus ({current_turn}):", font=("Arial", 16))
    label.grid(row=0, column=0, columnspan=3, pady=10)

    buttons = []

    row = 4
    column = 0
    Name = 97
    #Loop erstellen der die buttons erstellt..
    #Für jede Variable a, b, c, d, e, f, g, h, i,
    field_list = [a, b, c, d, e, f, g, h, i]

    for field in field_list:
        button = tk.Button(window, text=f"{field}", width=10, height=5, bg="white", fg="black")
        button.config(command=lambda fld=chr(Name), btn=button:  button_input_changer(btn, fld))
        button.grid(row=row , column=column , padx=5, pady=5)
        buttons.append(button)
        column +=1
        Name += 1
        if column % 3 == 0:
            row += 1
            column = 0

    window.mainloop()

mode_selection()
game_window()