import random

import tkinter as tk

player_1 = "X"
player_2 = "O"

a, b, c = 1, 2, 3
d, e, f = 4, 5, 6
g, h, i = 7, 8, 9

#Wer hat gewonnen
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


#TIE
def tie():
      
    global a, b, c, d, e, f, g, h, i
    

    if isinstance(a, int):
        return False
    if isinstance(b, int):
       return False
    if isinstance(c, int):
       return False
    if isinstance(d, int):
        return False
    if isinstance(e, int):
        return False
    if isinstance(f, int):
        return False
    if isinstance(g, int):
        return False
    if isinstance(h, int):
        return False
    if isinstance(i, int):
        return False
    return True

#Button-Raster

def button_click():

    window = tk.Tk()
    window.title("Tic-Tac-Toe")


    button00 = tk.Button(text=f"{a}", width=10, height=5, bg="white", fg="black", )
    button00.grid(row=0, column=0, padx=5, pady=5)

    button01 = tk.Button(text=f"{b}", width=10, height=5, bg="white", fg="black",)
    button01.grid(row=0, column=1, padx=5, pady=5)

    button02 = tk.Button(text=f"{c}", width=10, height=5, bg="white", fg="black",)
    button02.grid(row=0, column=2, padx=5, pady=5)

    button10 = tk.Button(text=f"{d}", width=10, height=5, bg="white", fg="black",)
    button10.grid(row=1, column=0, padx=5, pady=5)

    button11 = tk.Button(text=f"{e}", width=10, height=5, bg="white", fg="black",)
    button11.grid(row=1, column=1, padx=5, pady=5)

    button12 = tk.Button(text=f"{f}", width=10, height=5, bg="white", fg="black",)
    button12.grid(row=1, column=2, padx=5, pady=5)

    button20 = tk.Button(text=f"{g}", width=10, height=5, bg="white", fg="black",)
    button20.grid(row=2, column=0, padx=5, pady=5)

    button21 = tk.Button(text=f"{h}", width=10, height=5, bg="white", fg="black",)
    button21.grid(row=2, column=1, padx=5, pady=5)

    button22 = tk.Button(text=f"{i}", width=10, height=5, bg="white", fg="black",)
    button22.grid(row=2, column=2, padx=5, pady=5)

    window.mainloop()

button_click()

number_of_players = input(f"Wie viele Spieler (1/2)?:   ")

if number_of_players == "2":
    print("Viel Spaß!")
    button_click()

    current_turn = f"{player_1}"
    while not (has_won(f"{player_1}") or has_won(f"{player_2}") or tie()):
        user_input_field = input(f"Wähle ein Feld aus ({current_turn}): ")

        if user_input_field == f"{player_1}" or user_input_field == f"{player_2}":
            print("HEY NICHT SCHUMMELN!")
            button_click()
            continue

        if user_input_field == str(a):
            a = current_turn
        elif user_input_field == str(b):
            b = current_turn
        elif user_input_field == str(c):
            c = current_turn
        elif user_input_field == str(d):
            d = current_turn
        elif user_input_field == str(e):
            e = current_turn
        elif user_input_field == str(f):
            f = current_turn
        elif user_input_field == str(g):
            g = current_turn
        elif user_input_field == str(h):
            h = current_turn
        elif user_input_field == str(i):
            i = current_turn
        else:
            print("Ungültige Auswahl. Versuche es erneut.")
            button_click()
            continue
        button_click()

        current_turn = f"{player_2}" if current_turn == f"{player_1}" else f"{player_1}"

    last_turn = f"{player_2}" if current_turn == f"{player_1}" else f"{player_1}"
    print(f"Spiel beendet!\n({last_turn}) HAT GEWONNEN!!!")


