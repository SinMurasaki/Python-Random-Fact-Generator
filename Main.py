import tkinter as tk
from Function import generate_random_fact

def show_random_fact():
    # Generate and display a random fact
    fact = generate_random_fact()
    fact_label.config(text=fact)

# Create the main window
window = tk.Tk()
window.title("Random Earth and Underwater Facts")

# Create a button to generate random facts
fact_button = tk.Button(window, text="Generate Fact", command=show_random_fact)
fact_button.pack(pady=10)

# Create a label to display the random facts
fact_label = tk.Label(window, text="")
fact_label.pack(pady=10)

# Start the main loop
window.mainloop()
