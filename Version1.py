import tkinter as tk

# Conversion Function

def convert_binary():
    binary_input = input_box.get("1.0", tk.END).strip()

    # Validate binary
    if not all(c in '01' for c in binary_input):
        result = "Invalid binary string. Use only 0s and 1s."
    else:
        decimal = int(binary_input, 2)
        hexadecimal = hex(decimal)[2:].upper()

        result = (
            f"Binary: {binary_input}\n"
            f"Decimal: {decimal}\n"
            f"Hexadecimal: {hexadecimal}"
        )

    # Output to GUI
    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)
    output_box.config(state="disabled"
                      
# GUI Setup

root = tk.Tk()
root.title("Binary Converter")
root.geometry("600x400")

# Input label + box
tk.Label(root, text="Enter Binary:").pack()
input_box = tk.Text(root, height=5, width=70)
input_box.pack(pady=5)

# Convert button
tk.Button(root, text="Convert", command=convert_binary).pack(pady=10)

# Output label + box
tk.Label(root, text="Result:").pack()
output_box = tk.Text(root, height=5, width=70, state="disabled")
output_box.pack(pady=5)

root.mainloop()