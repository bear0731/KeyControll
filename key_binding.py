import tkinter as tk
from tkinter import messagebox
import json


def save_key_bindings():
    bindings = {
        "FORWARD": entry_forward.get(),
        "BACKWARD": entry_backward.get(),
        "LEFTHAND": entry_left.get(),
        "RIGHTHAND": entry_right.get(),
        "JUMP": entry_jump.get(),
        "SQUAT": entry_squat.get(),
        "ATTACK": entry_attack.get()
    }
    with open("key_bindings.json", "w") as f:
        json.dump(bindings, f)
    messagebox.showinfo("Key Bindings", "Key bindings saved successfully!")

def on_key_press(event, entry):
    if len(event.keysym) == 1 and event.keysym.isalpha():
        entry.delete(0, tk.END)
        return
    entry.delete(0, tk.END)
    entry.insert(0, event.keysym)
    
# Create the main window
root = tk.Tk()
root.title("Custom Key Bindings")
root.geometry("300x350")

# Labels and entry fields
tk.Label(root, text="Forward").grid(row=0, column=0, pady=5)
entry_forward = tk.Entry(root)
entry_forward.grid(row=0, column=1, pady=5)
entry_forward.bind("<KeyPress>", lambda event: on_key_press(event, entry_forward))

tk.Label(root, text="Backward").grid(row=1, column=0, pady=5)
entry_backward = tk.Entry(root)
entry_backward.grid(row=1, column=1, pady=5)
entry_backward.bind("<KeyPress>", lambda event: on_key_press(event, entry_backward))

tk.Label(root, text="Left").grid(row=2, column=0, pady=5)
entry_left = tk.Entry(root)
entry_left.grid(row=2, column=1, pady=5)
entry_left.bind("<KeyPress>", lambda event: on_key_press(event, entry_left))

tk.Label(root, text="Right").grid(row=3, column=0, pady=5)
entry_right = tk.Entry(root)
entry_right.grid(row=3, column=1, pady=5)
entry_right.bind("<KeyPress>", lambda event: on_key_press(event, entry_right))

tk.Label(root, text="Jump").grid(row=4, column=0, pady=5)
entry_jump = tk.Entry(root)
entry_jump.grid(row=4, column=1, pady=5)
entry_jump.bind("<KeyPress>", lambda event: on_key_press(event, entry_jump))

tk.Label(root, text="Squat").grid(row=5, column=0, pady=5)
entry_squat = tk.Entry(root)
entry_squat.grid(row=5, column=1, pady=5)
entry_squat.bind("<KeyPress>", lambda event: on_key_press(event, entry_squat))

tk.Label(root, text="Attack").grid(row=6, column=0, pady=5)
entry_attack = tk.Entry(root)
entry_attack.grid(row=6, column=1, pady=5)
entry_attack.bind("<KeyPress>", lambda event: on_key_press(event, entry_attack))

# Save button
button_save = tk.Button(root, text="Save Key Bindings", command=save_key_bindings)
button_save.grid(row=7, column=0, columnspan=2, pady=20)

# Run the main loop
root.mainloop()
