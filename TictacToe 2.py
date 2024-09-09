
a, b, c = 1, 2, 3
d, e, f = 4, 5, 6
g, h, i = 7, 8, 9

#ONLY FOR TEST
xyz = 2

einzelinput = input(f"Wie viele Spieler(1/2)?")

einzelinput
      
def print_area():
    print(f" >>> {a} {b} {c}\n >>> {d} {e} {f}\n >>> {g} {h} {i}")


current_turn = "X"
#Dieer Code ist immer gültig ----------------------------------------------------------------------------------------------
def gewinner():
    if f"{a}{b}{c}" == "XXX":
        print("Spiel beendet!")
        return True
    if f"{d}{e}{f}" == "XXX":
        print("Spiel beendet!")
        return True
    if f"{g}{h}{i}" == "XXX":
        print("Spiel beendet!")
        return True
    if f"{a}{d}{g}" == "XXX":
        print("Spiel beendet!")
        return True
    if f"{b}{e}{h}" == "XXX":
        print("Spiel beendet!")
        return True
    if f"{c}{f}{i}" == "XXX":
        print("Spiel beendet!")
        return True
    if f"{a}{e}{i}" == "XXX":
        print("Spiel beendet!")
        return True
    if f"{g}{e}{c}" == "XXX":
        print("Spiel beendet!")
        return True
    if f"{a}{b}{c}" == "OOO":
        print("Spiel beendet!")
        return True
    if f"{d}{e}{f}" == "OOO":
        print("Spiel beendet!")
        return True
    if f"{g}{h}{i}" == "OOO":
        print("Spiel beendet!")
        return True
    if f"{a}{d}{g}" == "OOO":
        print("Spiel beendet!")
        return True
    if f"{b}{e}{h}" == "OOO":
        print("Spiel beendet!")
        return True
    if f"{c}{f}{i}" == "OOO":
        print("Spiel beendet!")
        return True
    if f"{a}{e}{i}" == "OOO":
        print("Spiel beendet!")
        return True
    if f"{g}{e}{c}" == "OOO":
        print("Spiel beendet!")
        return True
#------------------------------------------------------------------------------------------------------------------------
    
if einzelinput == "2":
    print_area()
    print("Viel Spass!")             
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
        elif inputFUN == "C":
            gewinner == True
        else:
            print("Ungültige Auswahl. Versuche es erneut.")
            continue
        
        print_area()

        
        current_turn = "O" if current_turn == "X" else "X"

def Ultimate():
    if inputFun2 == str(a): #or c or g or i
        e == current_turn

# Computer = "O"

if einzelinput == "1":
    input1 = input("Welches Level([U]ltimate/[E]asy)?")
    if input1 == "U":
        print_area()
        print("Viel Spass!")
        while(not gewinner()):

            inputFun2 = input(f"Wähle ein Feld aus ({current_turn}): ")
            
            if inputFun2 == str(a):
                a = current_turn
            elif inputFun2 == str(b):
                b = current_turn
            elif inputFun2 == str(c):
                c = current_turn
            elif inputFun2 == str(d):
                d = current_turn
            elif inputFun2 == str(e):
                e = current_turn
            elif inputFun2 == str(f):
                f = current_turn
            elif inputFun2 == str(g):
                g = current_turn
            elif inputFun2 == str(h):
                h = current_turn
            elif inputFun2 == str(i):
                i = current_turn
            elif inputFun2 == "C":
                gewinner == True
            else:
                print("Ungültige Auswahl. Versuche es erneut.")
                print_area()
                continue

            print_area()
            Ultimate()

