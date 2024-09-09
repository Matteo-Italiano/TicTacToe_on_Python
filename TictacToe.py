
a, b, c = 1, 2, 3
d, e, f = 4, 5, 6
g, h, i = 7, 8, 9


# DO NOT TOUCH THIS ONE WORKS



einzelinput = input(f"Wie viele Spieler(1/2)?")
if einzelinput == "2":
    print("Viel Spass!")
    
def print_Area():
    print(f" >>> {a} {b} {c}\n >>> {d} {e} {f}\n >>> {g} {h} {i}")

print_Area()

current_turn = "X"

def gewinner(player):
    # Gewinnkombinationen für den Spieler (entweder "XXX" oder "OOO")
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

while not (gewinner("XXX") or gewinner("OOO")):
    

    inputFUN = input(f"Wähle ein Feld aus ({current_turn}): ")

    if inputFUN == str(a):
        a = current_turn
    elif inputFUN == str(b):
        b = current_turn
    elif inputFUN == str(c):
        c = current_turn
    elif inputFUN == str(d):
        d = current_turn
    elif inputFUN == str(e):
        e = current_turn
    elif inputFUN == str(f):
        f = current_turn
    elif inputFUN == str(g):
        g = current_turn
    elif inputFUN == str(h):
        h = current_turn
    elif inputFUN == str(i):
        i = current_turn
    else:
        print("Ungültige Auswahl. Versuche es erneut.")
        
        continue

    print_Area()
        

    current_turn = "O" if current_turn == "X" else "X"

last_turn = "O" if current_turn == "X" else "X"
print(f"Spiel beendet! ({last_turn}) HAT GEWONNEN!!!")
