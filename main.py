import tkinter as tk
from tkinter import ttk
import object_counter

# Calls the object_counter.py when the "Object Counter" button is clicked
def on_object_counter():
    object_counter.run()
    print("Running Object Counter...")


# -- GUI stuff --
# Create the main application window
root = tk.Tk()
root.focus_force()  # Ensure the window is focused when it opens
root.title("Object and Hand Gesture Detection")
root.geometry("400x250")

# Main frame
mainframe = ttk.Frame(root, padding=30)
mainframe.pack(expand=True)

# Title
title = ttk.Label(mainframe, text="Object and Hand Gesture Detection",)
title.pack(pady=(0, 15))

# Options label
options_label = ttk.Label(mainframe, text="Options",)
options_label.pack(pady=(0, 10))

# Buttons
object_button = ttk.Button(
    mainframe,
    text="Object Counter",
    command=on_object_counter,
    width=25
)
object_button.pack(pady=5)

hand_gesture_button = ttk.Button(
    mainframe,
    text="Hand Gesture Detection",
    command=lambda: print("Hand Gesture Detection selected"),
    width=25
)
hand_gesture_button.pack(pady=5)

root.mainloop()