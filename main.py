from stressState import *
import tkinter as tk
import settings

# Create the main window
root = tk.Tk()
root.title("Mohr Circle Calculator")

# Disable both horizontal and vertical resizing
root.resizable(False, False)  

# Set the window size
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")

# Define the padding and starting x-coordinate for the right side elements
right_side_x = settings.WIDTH/2  # Approximately the middle of the window

# Create Lablel for input section heading
inputsHeadingLabel = tk.Label(root, text='Inputs',
                               font=('Helvetica', 16, 'bold'))
inputsHeadingLabel.place(x=right_side_x + 10, y=20)

# Labels and entries for Sxx, Syy and Sxy
tk.Label(root, text = 'Sxx =').place(x=right_side_x+10, y=60)
tk.Entry(root).place(x=right_side_x+50, y=60)

tk.Label(root, text = 'Syy =').place(x=right_side_x+10, y=80)
tk.Entry(root).place(x=right_side_x+50, y=80)

tk.Label(root, text = 'Sxy =').place(x=right_side_x+10, y=100)
tk.Entry(root).place(x=right_side_x+50, y=100)


# Create labels and entry widgets for inputs
labels = ['Sxx', 'Syy', 'Sxy']
""" entries = {}
for i, label in enumerate(labels):
    tk.Label(root, text=f"{label} =").place(
        x=right_side_x+9,
        y=19+i*settings.INPUTHEIGHT)
    entries[label] = tk.Entry(root)
    entries[label].place(x=right_side_x+49, y=20+i*settings.INPUTHEIGHT) """


# Angle scale
tk.Label(root, text="Angle").place(x=right_side_x+10, y=120)
angle_scale = tk.Scale(root, from_=0, to=360, orient='horizontal')
angle_scale.place(x=right_side_x + 40, y=140)


resultHeadingLabel = tk.Label(root, text='Results',
                               font=('Helvetica', 16, 'bold'))
resultHeadingLabel.place(x=right_side_x + 10, y=190)


# Results labels and entry widgets
""" results = {}
for i, label in enumerate(labels):
    tk.Label(root, text=f"{label} =").place(x=right_side_x, y=160+i*settings.INPUTHEIGHT)
    results[label] = tk.Entry(root, state='readonly')
    results[label].place(x=right_side_x + 40, y=160+i*settings.INPUTHEIGHT) """


tk.Label(root, text = "Sx'x' =").place(x=right_side_x+10, y=230)
tk.Entry(root, state = 'readonly').place(x=right_side_x+50, y=230)

tk.Label(root, text = "Sy'y' =").place(x=right_side_x+10, y=250)
tk.Entry(root, state = 'readonly').place(x=right_side_x+50, y=250)

tk.Label(root, text = "Sx'y' =").place(x=right_side_x+10, y=270)
tk.Entry(root, state = 'readonly').place(x=right_side_x+50, y=270)


# Ok button
ok_button = tk.Button(root, text="Ok")
ok_button.place(x=right_side_x + 40, y=350)

# Canvas for plotting Mohr's circle, placed on the left side
canvas = tk.Canvas(root, bg='white', width=settings.WIDTH/2, height=415)
canvas.place(x=0, y=0)

# Start the GUI event loop
root.mainloop()



# Create and instance of the class and get principal stresses
stress_State = StressState(100, 20, 30)
print("Principal Stresses:", stress_State.principalStresses)

# Print Mohr's radius
print(f"Mohr's radius: {stress_State.radius}")