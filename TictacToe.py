import random


a, b, c = 1, 2, 3
d, e, f = 4, 5, 6
g, h, i = 7, 8, 9


def print_area():
    print(f" >>> {a} {b} {c}\n >>> {d} {e} {f}\n >>> {g} {h} {i}")


def gewinner(player):
    if f"{a}{b}{c}" == player:
        return True
    if f"{d}{e}{f}" == player:
        return True
    if f"{g}{h}{i}" == player:
        return True
    if f"{a}{d}{g}" == player:
        return True
    if f"{b}{e}{h}" == player:
        return True
    if f"{c}{f}{i}" == player:
        return True
    if f"{a}{e}{i}" == player:
        return True
    if f"{g}{e}{c}" == player:
        return True
    return False


def Computer():
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

    if available_fields:
        choice = random.choice(available_fields)
        if choice == "a":
            a = "O"
        elif choice == "b":
            b = "O"
        elif choice == "c":
            c = "O"
        elif choice == "d":
            d = "O"
        elif choice == "e":
            e = "O"
        elif choice == "f":
            f = "O"
        elif choice == "g":
            g = "O"
        elif choice == "h":
            h = "O"
        elif choice == "i":
            i = "O"


NumberOfPlayers = input(f"Wie viele Spieler (1/2)?:   ")


if NumberOfPlayers == "2":
    print("Viel Spaß!")
    print_area()

    current_turn = "X"
    while not (gewinner("XXX") or gewinner("OOO")):
        FieldSetter = input(f"Wähle ein Feld aus ({current_turn}): ")

        if FieldSetter == "X" or FieldSetter == "O":
            print("HEY NICHT SCHUMMELN!")
            print_area()
            continue

        if FieldSetter == str(a):
            a = current_turn
        elif FieldSetter == str(b):
            b = current_turn
        elif FieldSetter == str(c):
            c = current_turn
        elif FieldSetter == str(d):
            d = current_turn
        elif FieldSetter == str(e):
            e = current_turn
        elif FieldSetter == str(f):
            f = current_turn
        elif FieldSetter == str(g):
            g = current_turn
        elif FieldSetter == str(h):
            h = current_turn
        elif FieldSetter == str(i):
            i = current_turn
        else:
            print("Ungültige Auswahl. Versuche es erneut.")
            print_area()
            continue

        print_area()
        current_turn = "O" if current_turn == "X" else "X"

    last_turn = "O" if current_turn == "X" else "X"
    print(f"Spiel beendet!\n({last_turn}) HAT GEWONNEN!!!")


elif NumberOfPlayers == "1":
    print("DU WIRST NIE GEWINNEN!")
    print_area()

    current_turn = "X"
    while not (gewinner("XXX") or gewinner("OOO")):
        if current_turn == "X":
            FieldSetter = input(f"Wähle ein Feld aus ({current_turn}): ")

            if FieldSetter == "X" or FieldSetter == "O":
                print("HEY NICHT SCHUMMELN!")
                print_area()
                continue

            if FieldSetter == str(a):
                a = current_turn
            elif FieldSetter == str(b):
                b = current_turn
            elif FieldSetter == str(c):
                c = current_turn
            elif FieldSetter == str(d):
                d = current_turn
            elif FieldSetter == str(e):
                e = current_turn
            elif FieldSetter == str(f):
                f = current_turn
            elif FieldSetter == str(g):
                g = current_turn
            elif FieldSetter == str(h):
                h = current_turn
            elif FieldSetter == str(i):
                i = current_turn
            else:
                print("Ungültige Auswahl. Versuche es erneut.")
                print_area()
                continue
        else:
            print("Der Computer macht seinen Zug...")
            Computer()

        print_area()
        current_turn = "O" if current_turn == "X" else "X"

    last_turn = "O" if current_turn == "X" else "X"
    print(f"Spiel beendet!\n({last_turn}) HAT GEWONNEN!!!")
