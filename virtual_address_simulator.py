PAGE_SIZE = 1024
ADDRESS_SPACE = 4096

# Each page has a physical frame and a valid (present) bit.
page_table = {
    0: {"frame": 2, "valid": True},
    1: {"frame": 0, "valid": True},
    2: {"frame": 3, "valid": True},
    3: {"frame": None, "valid": False},
}


def translate_address(address):
    if address < 0:
        print("ERROR: negative addresses are not allowed.")
        return
    if address >= ADDRESS_SPACE:
        print("ERROR: address must be between 0 and 4095.")
        return

    vpn = address // PAGE_SIZE
    offset = address % PAGE_SIZE
    print("Virtual page number (VPN):", vpn)
    print("Offset:", offset)

    entry = page_table[vpn]
    if not entry["valid"]:
        print("PAGE FAULT: this page is not currently in RAM.")
        return

    frame = entry["frame"]
    physical_address = frame * PAGE_SIZE + offset
    print("Physical frame:", frame)
    print("Physical address:", physical_address)


def main():
    print("Virtual Address Translation Simulator")
    print("Page size: 1024 bytes | Valid addresses: 0-4095")
    while True:
        try:
            text = input("\nEnter a virtual address (q to quit): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if text.lower() == "q":
            print("Goodbye!")
            break
        try:
            address = int(text)
        except ValueError:
            print("ERROR: enter a whole number or q.")
            continue
        translate_address(address)


if __name__ == "__main__":
    main()
