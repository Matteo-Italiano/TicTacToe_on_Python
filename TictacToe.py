import random


player_1 = "X"
player_2 = "O"

a, b, c = 1, 2, 3
d, e, f = 4, 5, 6
g, h, i = 7, 8, 9


def print_area():
    print(f" >>> {a} {b} {c}\n >>> {d} {e} {f}\n >>> {g} {h} {i}")


def has_won(player):
    player_validation_string =f"{player}{player}{player}"

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


def computer():
    global a, b, c, d, e, f, g, h, i
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
#Macht liste Oben

    if f"{a}{b}" == f"{player_1}{player_1}":
        if c in available_fields:
            c = f"{player_2}"
    elif f"{b}{c}" == f"{player_1}{player_1}":
        if a in available_fields:
            a = f"{player_2}"
    elif f"{a}{c}" == f"{player_1}{player_1}":
        if b in available_fields:
            b = f"{player_2}"
    elif f"{d}{e}" == f"{player_1}{player_1}":
        if f in available_fields:
            f = f"{player_2}"
    elif f"{e}{f}" == f"{player_1}{player_1}":
        if d in available_fields:
            d = f"{player_2}"
    elif f"{d}{f}" == f"{player_1}{player_1}":
        if e in available_fields:
            e = f"{player_2}"
    elif f"{g}{h}" == f"{player_1}{player_1}":
        if i in available_fields:
            i = f"{player_2}"
    elif f"{h}{i}" == f"{player_1}{player_1}":
        if g in available_fields:
            g = f"{player_2}"
    elif f"{g}{i}" == f"{player_1}{player_1}":
        if h in available_fields:
            h = f"{player_2}"
            

    elif available_fields:
        choice = random.choice(available_fields)
        if choice == "a":
            a = f"{player_2}"
        elif choice == "b":
            b = f"{player_2}"
        elif choice == "c":
            c = f"{player_2}"
        elif choice == "d":
            d = f"{player_2}"
        elif choice == "e":
            e = f"{player_2}"
        elif choice == "f":
            f = f"{player_2}"
        elif choice == "g":
            g = f"{player_2}"
        elif choice == "h":
            h = f"{player_2}"
        elif choice == "i":
            i = f"{player_2}"

# Nimmt die random Choice und Setzt sie ein


number_of_players = input(f"Wie viele Spieler (1/2)?:   ")


if number_of_players == "2":
    print("Viel Spaß!")
    print_area()


    current_turn = f"{player_1}"
    while not (has_won(f"{player_1}") or has_won(f"{player_2}")):
        user_input_field = input(f"Wähle ein Feld aus ({current_turn}): ")

        if user_input_field == f"{player_1}" or user_input_field == f"{player_2}":
            print("HEY NICHT SCHUMMELN!")
            print_area()
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
            print_area()
            continue

        print_area()
        current_turn = f"{player_2}" if current_turn == f"{player_1}" else f"{player_1}"

    last_turn = f"{player_2}" if current_turn == f"{player_1}" else f"{player_1}"
    print(f"Spiel beendet!\n({last_turn}) HAT GEWONNEN!!!")


elif number_of_players == "1":
    print("DU WIRST NIE GEWINNEN!")
    print_area()

    current_turn = f"{player_1}"
    while not (has_won(f"{player_1}") or has_won(f"{player_2}")):
        if current_turn == f"{player_1}":
            user_input_field = input(f"Wähle ein Feld aus ({current_turn}): ")

            if user_input_field == f"{player_1}" or user_input_field == f"{player_2}":
                print("HEY NICHT SCHUMMELN!")
                print_area()
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
                print_area()
                continue
        else:
            print("Der Computer macht seinen Zug...")
            computer()

        print_area()
        current_turn = f"{player_2}" if current_turn == f"{player_1}" else f"{player_1}"

    last_turn = f"{player_2}" if current_turn == f"{player_1}" else f"{player_1}"
    print(f"Spiel beendet!\n({last_turn}) HAT GEWONNEN!!!")