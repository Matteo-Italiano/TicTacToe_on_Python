
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

def gewinner(Spieler):
    if f"{a}{b}{c}" == "XXX":
        return True
    if f"{d}{e}{f}" == "XXX":
        return True
    if f"{g}{h}{i}" == "XXX":
        return True
    if f"{a}{d}{g}" == "XXX":
        return True
    if f"{b}{e}{h}" == "XXX":
        return True
    if f"{c}{f}{i}" == "XXX":
        return True
    if f"{a}{e}{i}" == "XXX":
        return True
    if f"{g}{e}{c}" == "XXX":
        return True
    if f"{a}{b}{c}" == "OOO":
        return True
    if f"{d}{e}{f}" == "OOO":
        return True
    if f"{g}{h}{i}" == "OOO":
        return True
    if f"{a}{d}{g}" == "OOO":
        return True
    if f"{b}{e}{h}" == "OOO":
        return True
    if f"{c}{f}{i}" == "OOO":
        return True
    if f"{a}{e}{i}" == "OOO":
        return True
    if f"{g}{e}{c}" == "OOO":
        return True
                
while(not gewinner()):

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
        print_Area()
        continue

    print_Area()
        

    current_turn = "O" if current_turn == "X" else "X"

print("Spiel beendet!")