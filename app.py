# --- app.py (Polished and Commented Version) ---

import tkinter as tk
from tkinter import ttk, messagebox

# --- Main Logic Function ---
def convert_temperature():
    """
    This function is triggered by the 'Convert' button.
    It gets values from the GUI, performs temperature conversions,
    and updates the result label.
    """
    
    # Use a try-except block to handle non-numeric input gracefully.
    try:
        # Retrieve the user's input from the Entry widget.
        temp_value = float(temp_entry.get())
        
        # Retrieve the selected unit from the Combobox's special variable.
        original_unit = unit_var.get()
        
        # Initialize an empty string to build the result message.
        result_text = ""

        # Perform the conversions based on the selected unit.
        if original_unit == "Celsius":
            fahrenheit = (temp_value * 9/5) + 32
            kelvin = temp_value + 273.15
            result_text = f"Fahrenheit: {fahrenheit:.2f}°F\nKelvin: {kelvin:.2f} K"
        
        elif original_unit == "Fahrenheit":
            celsius = (temp_value - 32) * 5/9
            kelvin = celsius + 273.15
            result_text = f"Celsius: {celsius:.2f}°C\nKelvin: {kelvin:.2f} K"
            
        elif original_unit == "Kelvin":
            celsius = temp_value - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result_text = f"Celsius: {celsius:.2f}°C\nFahrenheit: {fahrenheit:.2f}°F"
            
        # Use .config() to update the text of the result label after it's created.
        result_label.config(text=result_text)

    except ValueError:
        # If float() fails, it means the input was not a number. Show an error popup.
        messagebox.showerror("Invalid Input", "Please enter a valid number for the temperature.")
    except Exception as e:
        # Catch any other unexpected errors and display them.
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


# --- GUI Setup ---
# Create the main application window.
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")
#root.resizable(False, False) # Prevent the window from being resized.

# Create a main frame to hold all the widgets. This helps with organization.
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill="both", expand=True)

# --- Define All Widgets ---

# Input field for temperature
temp_label = ttk.Label(main_frame, text="Enter Temperature:")
temp_entry = ttk.Entry(main_frame, width=15, font=("Helvetica", 12))

# Unit selection dropdown (Combobox)
unit_label = ttk.Label(main_frame, text="Select Unit:")
# Create a special StringVar to hold the value of the dropdown menu.
unit_var = tk.StringVar()
unit_menu = ttk.Combobox(
    main_frame, 
    textvariable=unit_var, 
    values=["Celsius", "Fahrenheit", "Kelvin"], 
    state="readonly", # Prevents the user from typing in the box.
    font=("Helvetica", 12)
)
unit_menu.set("Celsius") # Set the default selection.

# Convert button that triggers the conversion logic.
# The `command` is linked to our function WITHOUT parentheses.
convert_button = ttk.Button(main_frame, text="Convert", command=convert_temperature)

# Result display label
result_label = ttk.Label(
    main_frame, 
    text="Results will be shown here.", 
    font=("Helvetica", 12, "bold"), 
    justify="center" # Ensures multiple lines of text are centered.
)

# --- Arrange Widgets on the Grid ---
# The .grid() method allows us to place widgets in a neat table-like structure.
temp_label.grid(row=0, column=0, padx=5, pady=10, sticky="w")
temp_entry.grid(row=0, column=1, padx=5, pady=10)

unit_label.grid(row=1, column=0, padx=5, pady=10, sticky="w")
unit_menu.grid(row=1, column=1, padx=5, pady=10)

convert_button.grid(row=2, column=0, columnspan=2, pady=20)

result_label.grid(row=3, column=0, columnspan=2, pady=10)


# --- Start the Application ---
# The mainloop() call keeps the window open and listening for events (like button clicks).
root.mainloop()