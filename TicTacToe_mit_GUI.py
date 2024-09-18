import tkinter as tk
import random

player_1 = "X"
player_2 = "O"  # Auch Computer
playing_vs_computer = False

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
    buttons[0].config(text=a, state="normal")
    buttons[1].config(text=b, state="normal")
    buttons[2].config(text=c, state="normal")
    buttons[3].config(text=d, state="normal")
    buttons[4].config(text=e, state="normal")
    buttons[5].config(text=f, state="normal")
    buttons[6].config(text=g, state="normal")
    buttons[7].config(text=h, state="normal")
    buttons[8].config(text=i, state="normal")

def button_input_changer(button, field_var_name):
    global current_turn, label

    if isinstance(globals()[field_var_name], int):
        globals()[field_var_name] = current_turn  
        button.config(text=current_turn)
        
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
        
        if playing_vs_computer and current_turn == "O":
            computer_input_changer()
            current_turn = "X"
        label.config(text=f"Wähle ein Feld aus ({current_turn}):")

def computer_input_changer():
    global current_turn, a, b, c, d, e, f, g, h, i

    available_fields = []

    if isinstance(a, int):
        available_fields.append("a")
    if isinstance(b, int):
        available_fields.append("b")
    if isinstance(c, int):
        available_fields.append("c")
    if isinstance(d, int):
        available_fields.append("d")
    if isinstance(e, int):
        available_fields.append("e")
    if isinstance(f, int):
        available_fields.append("f")
    if isinstance(g, int):
        available_fields.append("g")
    if isinstance(h, int):
        available_fields.append("h")
    if isinstance(i, int):
        available_fields.append("i")

    if available_fields:
        choice = random.choice(available_fields)
        if choice == "a":
            buttons[0].config(text=f"{current_turn}")
            a = current_turn
        elif choice == "b":
            buttons[1].config(text=f"{current_turn}")
            b = current_turn
        elif choice == "c":
            buttons[2].config(text=f"{current_turn}")
            c = current_turn
        elif choice == "d":
            buttons[3].config(text=f"{current_turn}")
            d = current_turn
        elif choice == "e":
            buttons[4].config(text=f"{current_turn}")
            e = current_turn
        elif choice == "f":
            buttons[5].config(text=f"{current_turn}")
            f = current_turn
        elif choice == "g":
            buttons[6].config(text=f"{current_turn}")
            g = current_turn
        elif choice == "h":
            buttons[7].config(text=f"{current_turn}")
            h = current_turn
        elif choice == "i":
            buttons[8].config(text=f"{current_turn}")
            i = current_turn

def game_window():
    global label, buttons, window

    window = tk.Tk()
    window.title("Tic-Tac-Toe")

    label = tk.Label(window, text=f"Wähle ein Feld aus ({current_turn}):", font=("Arial", 16))
    label.grid(row=0, column=0, columnspan=3, pady=10)

    buttons = []

    button_a = tk.Button(window, text=f"{a}", width=10, height=5, command=lambda: button_input_changer(button_a, 'a'), bg="white", fg="black")
    button_a.grid(row=1, column=0, padx=5, pady=5)
    buttons.append(button_a)

    button_b = tk.Button(window, text=f"{b}", width=10, height=5, command=lambda: button_input_changer(button_b, 'b'), bg="white", fg="black")
    button_b.grid(row=1, column=1, padx=5, pady=5)
    buttons.append(button_b)

    button_c = tk.Button(window, text=f"{c}", width=10, height=5, command=lambda: button_input_changer(button_c, 'c'), bg="white", fg="black")
    button_c.grid(row=1, column=2, padx=5, pady=5)
    buttons.append(button_c)
    
    button_d = tk.Button(window, text=f"{d}", width=10, height=5, command=lambda: button_input_changer(button_d, 'd'), bg="white", fg="black")
    button_d.grid(row=2, column=0, padx=5, pady=5)
    buttons.append(button_d)

    button_e = tk.Button(window, text=f"{e}", width=10, height=5, command=lambda: button_input_changer(button_e, 'e'), bg="white", fg="black")
    button_e.grid(row=2, column=1, padx=5, pady=5)
    buttons.append(button_e)

    button_f = tk.Button(window, text=f"{f}", width=10, height=5, command=lambda: button_input_changer(button_f, 'f'), bg="white", fg="black")
    button_f.grid(row=2, column=2, padx=5, pady=5)
    buttons.append(button_f)

    button_g = tk.Button(window, text=f"{g}", width=10, height=5, command=lambda: button_input_changer(button_g, 'g'), bg="white", fg="black")
    button_g.grid(row=3, column=0, padx=5, pady=5)
    buttons.append(button_g)

    button_h = tk.Button(window, text=f"{h}", width=10, height=5, command=lambda: button_input_changer(button_h, 'h'), bg="white", fg="black")
    button_h.grid(row=3, column=1, padx=5, pady=5)
    buttons.append(button_h)

    button_i = tk.Button(window, text=f"{i}", width=10, height=5, command=lambda: button_input_changer(button_i, 'i'), bg="white", fg="black")
    button_i.grid(row=3, column=2, padx=5, pady=5)
    buttons.append(button_i)

    window.mainloop()

mode_selection()
game_window()
