import tkinter as tk
 
window = tk.Tk()

#label = tk.Label(
#    text="Hello, Tkinter!",
#    fg="white",
#    bg="black",
#    width=10,
#    height=10
#    )
#label.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow"
)

#button.pack()

#entry = tk.Entry(fg="yellow", bg="blue", width=50)
#
#border_effects = {
#    "flat": tk.FLAT,
#    "Sunken": tk.SUNKEN,
#    "raised": tk.RAISED,
#    "groove": tk.GROOVE,
#    "ridge": tk.RIDGE,
#}
#
#for relief_name, relief in border_effects.items():
#    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#    frame.pack(side=tk.LEFT)
#    label = tk.Label(master=frame, text=relief_name)
#    label.pack()
#
#window.mainloop()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack()

frame2 = tk.Frame(master=window, width=50, height=50 bg="yellow")
frame2.pack()

frame3 = tk.Frame(master)