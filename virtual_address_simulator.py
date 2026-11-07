PAGE_SIZE = 1024
VIRTUAL_ADDRESS_SPACE = 4096

page_table = {
    0: {"frame": 2, "valid": True},
    1: {"frame": 0, "valid": True},
    2: {"frame": 3, "valid": True},
    3: {"frame": None, "valid": False}
}

while True:
    user_input = input("\nEnter a virtual address (q to quit): ").strip()

    if user_input.lower() == "q":
        print("Program terminated.")
        break

    try:
        virtual_address = int(user_input)
    except ValueError:
        print("Error: enter a whole number or q.")
        continue

    if virtual_address < 0:
        print("Error: negative addresses are not allowed.")
        continue

    if virtual_address >= VIRTUAL_ADDRESS_SPACE:
        print("Error: address must be between 0 and 4095.")
        continue

    page_number = virtual_address // PAGE_SIZE
    offset = virtual_address % PAGE_SIZE

    print(f"Virtual Page Number: {page_number}")
    print(f"Page Offset: {offset}")

    entry = page_table[page_number]

    if not entry["valid"]:
        print("PAGE FAULT")
    else:
        frame_number = entry["frame"]
        physical_address = frame_number * PAGE_SIZE + offset

        print(f"Physical Frame: {frame_number}")
        print(f"Physical Address: {physical_address}")

    print("-" * 40)
