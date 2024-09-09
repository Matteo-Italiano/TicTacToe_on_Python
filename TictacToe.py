
a, b, c = 1, 2, 3
d, e, f = 4, 5, 6
g, h, i = 7, 8, 9

def print_area():
    print(f" >>> {a} {b} {c}\n >>> {d} {e} {f}\n >>> {g} {h} {i}")

current_turn = "X"

# DO NOT TOUCH THIS ONE WORKS

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


NumberOfPlayers = input(f"Wie viele Spieler(1/2)?")
if NumberOfPlayers == "2":
    print("Viel Spass!")
else:
    if NumberOfPlayers == "1":
       EasyOrUltimate = input("[E]asy or [U]ltimate")
       if EasyOrUltimate == "U":
        print("DU WIRST NIE GEWINNEN!")
    else:
        print("Ungültige Auswahl")




print_area()
while not (gewinner("XXX") or gewinner("OOO")):
    

    FieldChanger = input(f"Wähle ein Feld aus ({current_turn}): ")

    if FieldChanger == str(a):
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
print(f"Spiel beendet! ({last_turn}) HAT GEWONNEN!!!")
