
a, b, c = 1, 2, 3
d, e, f = 4, 5, 6
g, h, i = 7, 8, 9

def print_area():
    print(f" >>> {a} {b} {c}\n >>> {d} {e} {f}\n >>> {g} {h} {i}")

current_turn = "X"

# DO NOT TOUCH THIS ONE WORKS

def Game():
    if NumberOfPlayers == "C":
        return True
    if FieldChanger == "C":
        return True
    if EasyOrUltimate == "C":
        return True
    return False

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

def Unbeateble():
    print()

def Blocker():
    print()
    if f"{a}{c}" == "XX":
        b = "O"



# DO NOT TOUCH THIS ONE WORKS


NumberOfPlayers = input(f"Wie viele Spieler(1/2)?")
if NumberOfPlayers == "2":
    print("Viel Spass!")

    print_area()
    while not (gewinner("XXX") or gewinner("OOO")):


        FieldChanger = input(f"Wähle ein Feld aus ({current_turn}): ")

        if FieldChanger == "X" or FieldChanger == "O":
            print("HEY NICHT SCHUMELN!")
            print_area()
            continue
        
        elif FieldChanger == str(a):
            a = current_turn
        elif FieldChanger == str(b):
            b = current_turn
        elif FieldChanger == str(c):
            c = current_turn
        elif FieldChanger == str(d):
            d = current_turn
        elif FieldChanger == str(e):
            e = current_turn
        elif FieldChanger == str(f):
            f = current_turn
        elif FieldChanger == str(g):
            g = current_turn
        elif FieldChanger == str(h):
            h = current_turn
        elif FieldChanger == str(i):
            i = current_turn
        else:
            print("Ungültige Auswahl. Versuche es erneut.")
            print_area()

            continue
        
        print_area()


        current_turn = "O" if current_turn == "X" else "X"

    last_turn = "O" if current_turn == "X" else "X"
    print(f"Spiel beendet!\n({last_turn}) HAT GEWONNEN!!!")

# Variante 1 des Spieles OBERHALB

elif NumberOfPlayers == "1":
    EasyOrUltimate = input("[E]asy or [U]ltimate?: ")
    if EasyOrUltimate == "U":
            print("DU WIRST NIE GEWINNEN!")
            print_area()
            while not (gewinner("XXX") or gewinner("OOO")):
                FieldChanger = input(f"Wähle ein Feld aus MENSCH: ")
                if f"{a}{c}" == "XX":
                    b = "O"
                elif f"{d}{f}" == "XX":
                    e = "O"
                elif f"{g}{i}" == "XX":
                    h = "O"
                
                if FieldChanger == "X":
                    print("HEY NICHT SCHUMELN!")
                if FieldChanger == "O":
                    print("HEY NICHT SCHUMELN!")
                if FieldChanger == str(a):
                    a = "X"
                elif FieldChanger == str(b):
                    b = "X"
                elif FieldChanger == str(c):
                    c = "X"
                elif FieldChanger == str(d):
                    d = "X"
                elif FieldChanger == str(e):
                    e = "X"
                elif FieldChanger == str(f):
                    f = "X"
                elif FieldChanger == str(g):
                    g = "X"
                elif FieldChanger == str(h):
                    h = "X"
                elif FieldChanger == str(i):
                    i = "X"
                else:
                    print("Ungültige Auswahl. Versuche es erneut.")
                    print_area()
                    continue
                    
                print_area()
    last_turn = "O" if current_turn == "X" else "X"
    print(f"Spiel beendet!\n({last_turn}) HAT GEWONNEN!!!")


    if EasyOrUltimate == "E":
           print("Möge der Bessere Gewinnen")
else:
    print("Ungültige Auswahl")


