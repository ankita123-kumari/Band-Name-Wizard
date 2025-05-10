import tkinter as tk
from tkinter import simpledialog, messagebox

def generate_band_name():
    # Create the main window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask the user for their favorite color
    color = simpledialog.askstring("Input", "What's your favorite color?")
    if not color:
        messagebox.showinfo("Error", "You must enter a color!")
        return

    # Ask the user for their favorite animal
    animal = simpledialog.askstring("Input", "What's your favorite animal?")
    if not animal:
        messagebox.showinfo("Error", "You must enter an animal!")
        return

    # Combine the inputs to create a band name
    band_name = f"{color} {animal}"

    # Display the generated band name in a message box
    messagebox.showinfo("Your Band Name", f"Your band name could be: {band_name}")

# Run the generator
if __name__ == "__main__":
    generate_band_name()