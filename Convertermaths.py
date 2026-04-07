import sys
print(">>> Running the NEW converter file <<<")

def binary_to_decimal_and_hex(binary_str):
    decimal_value = int(binary_str, 2)
    hex_value = hex(decimal_value)[2:].upper()
    return decimal_value, hex_value

def main():
    print("Binary Converter (Binary -> Decimal -> Hexadecimal)")
    binary_input = input("Enter a binary number: ")

    try:
        decimal_result, hex_result = binary_to_decimal_and_hex(binary_input)
        print(f"Decimal: {decimal_result}")
        print(f"Hexadecimal: {hex_result}")
    except ValueError:
        print("Error: That is not a valid binary number.")

if __name__ == "__main__":
    main()

sys.exit