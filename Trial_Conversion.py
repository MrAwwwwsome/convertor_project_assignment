import tkinter as tk
from tkinter import ttk

# -----------------------------
# Conversion helpers
# -----------------------------

def ascii_to_decimal_list(text):
    return [ord(c) for c in text]

def decimal_to_ascii(n):
    return chr(n)

def binary_to_decimal(b):
    return int(b, 2)

def hex_to_decimal(h):
    return int(h, 16)

def decimal_to_binary(n):
    return format(n, '08b')

def decimal_to_hex(n):
    return hex(n)[2:].upper()

# -----------------------------
# Universal converter
# -----------------------------

def universal_convert(value, from_mode, to_mode):
    try:
        # Convert input to decimal(s)
        if from_mode == "ASCII":
            decimals = ascii_to_decimal_list(value)
        elif from_mode == "Binary":
            decimals = [binary_to_decimal(value)]
        elif from_mode == "Hexadecimal":
            decimals = [hex_to_decimal(value)]
        elif from_mode == "Decimal":
            decimals = [int(value)]
        else:
            return "Unknown input mode"

        # Convert decimal(s) to target format
        results = []
        for d in decimals:
            if to_mode == "ASCII":
                results.append(decimal_to_ascii(d))
            elif to_mode == "Binary":
                results.append(decimal_to_binary(d))
            elif to_mode == "Hexadecimal":
                results.append(decimal_to_hex(d))
            elif to_mode == "Decimal":
                results.append(str(d))
            else:
                return "Unknown output mode"

        return " ".join(results)

    except Exception as e:
        return f"Error: {str(e)}"

# -----------------------------
# GUI logic
# -----------------------------

def convert():
    value = input_box.get("1.0", tk.END).strip()
    from_mode = from_var.get()
    to_mode = to_var.get()

    result = universal_convert(value, from_mode, to_mode)

    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)
    output_box.config(state="disabled")

# -----------------------------
# GUI setup
# -----------------------------

root = tk.Tk()
root.title("Universal Converter")
root.geometry("650x450")

modes = ["Binary", "Decimal", "Hexadecimal", "ASCII"]

# Dropdowns
from_var = tk.StringVar(value="Binary")
to_var = tk.StringVar(value="Decimal")

ttk.Label(root, text="From:").pack()
ttk.Combobox(root, textvariable=from_var, values=modes).pack(pady=5)

ttk.Label(root, text="To:").pack()
ttk.Combobox(root, textvariable=to_var, values=modes).pack(pady=5)

# Input box
tk.Label(root, text="Input:").pack()
input_box = tk.Text(root, height=5, width=70)
input_box.pack(pady=5)

# Convert button
tk.Button(root, text="Convert", command=convert).pack(pady=10)

# Output box
tk.Label(root, text="Output:").pack()
output_box = tk.Text(root, height=5, width=70, state="disabled")
output_box.pack(pady=5)

root.mainloop()