"""
Base Calculator
---------------
A simple command-line calculator that lets you:
1. Convert a number between Binary, Octal, Decimal, and Hexadecimal.
2. Perform arithmetic (+, -, *, /) on two numbers given in any base,
   with the result shown in all four bases.

Supported bases: Binary (2), Octal (8), Decimal (10), Hexadecimal (16)
"""

BASES = {
    "1": ("Binary", 2),
    "2": ("Octal", 8),
    "3": ("Decimal", 10),
    "4": ("Hexadecimal", 16),
}


def to_decimal(value: str, base: int) -> int:
    """Convert a string number in the given base to a decimal integer."""
    return int(value, base)


def from_decimal(value: int, base: int) -> str:
    """Convert a decimal integer to a string representation in the given base."""
    if base == 2:
        return bin(value)[2:] if value >= 0 else "-" + bin(value)[3:]
    elif base == 8:
        return oct(value)[2:] if value >= 0 else "-" + oct(value)[3:]
    elif base == 10:
        return str(value)
    elif base == 16:
        return hex(value)[2:].upper() if value >= 0 else "-" + hex(value)[3:].upper()
    else:
        raise ValueError("Unsupported base")


def show_all_bases(value: int):
    """Print a decimal integer converted into all supported bases."""
    print("\nResult in all bases:")
    for key, (name, base) in BASES.items():
        print(f"  {name:12}: {from_decimal(value, base)}")


def choose_base(prompt: str) -> int:
    print(prompt)
    for key, (name, base) in BASES.items():
        print(f"  {key}. {name} (base {base})")
    choice = input("Choose base (1-4): ").strip()
    while choice not in BASES:
        choice = input("Invalid choice. Choose base (1-4): ").strip()
    return BASES[choice][1]


def convert_mode():
    base = choose_base("\nWhich base is your number in?")
    num = input("Enter the number: ").strip()
    try:
        decimal_value = to_decimal(num, base)
    except ValueError:
        print("Invalid number for the selected base.")
        return
    show_all_bases(decimal_value)


def calculate_mode():
    base1 = choose_base("\nBase of the FIRST number:")
    num1 = input("Enter the first number: ").strip()
    base2 = choose_base("\nBase of the SECOND number:")
    num2 = input("Enter the second number: ").strip()

    try:
        val1 = to_decimal(num1, base1)
        val2 = to_decimal(num2, base2)
    except ValueError:
        print("Invalid number entered for the selected base.")
        return

    op = input("Choose operation (+, -, *, /): ").strip()

    try:
        if op == "+":
            result = val1 + val2
        elif op == "-":
            result = val1 - val2
        elif op == "*":
            result = val1 * val2
        elif op == "/":
            if val2 == 0:
                print("Error: Division by zero.")
                return
            result = val1 // val2  # integer division to keep result a whole number
        else:
            print("Invalid operation.")
            return
    except Exception as e:
        print(f"Error during calculation: {e}")
        return

    show_all_bases(result)


def main():
    print("=" * 40)
    print("        BASE CALCULATOR")
    print("=" * 40)

    while True:
        print("\nMenu:")
        print("  1. Convert a number between bases")
        print("  2. Calculate (add/subtract/multiply/divide) two numbers")
        print("  3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            convert_mode()
        elif choice == "2":
            calculate_mode()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()