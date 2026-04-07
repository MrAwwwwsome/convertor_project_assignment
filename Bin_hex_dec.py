
while True:
    binary_input = input("Enter binary number (or 'q' to quit): ").strip()
    if binary_input.lower() == 'q':
        break
    if not all(c in '01' for c in binary_input):
        print("Invalid binary string. Use only 0s and 1s.\n")
        continue
    decimal = int(binary_input, 2)
    hexadecimal = hex(decimal) [2:].upper()
    print(f"Binary: {binary_input}")
    print(f"Decimal: {decimal}")
    print(f"Hexadecimal: {hexadecimal}\n")