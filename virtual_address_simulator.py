PAGE_SIZE = 1024
VIRTUAL_ADDRESS_SPACE = 4096

page_table = {
    0: {"frame": 2, "valid": True},
    1: {"frame": 0, "valid": True},
    2: {"frame": 3, "valid": True},
    3: {"frame": None, "valid": False}
}

while True:
    address = input("Enter a virtual adress(q to quit): ")


    if address.lower() == "q":
        print("Program terminated.")
        break

    try:
        address = int(address)
    except ValueError:
        print("Error: enter a number or q.")
        continue

    if address < 0:
        print("Error: negative addresses are not allowed.")
        continue

    if address >= VIRTUAL_ADDRESS_SPACE:
        print("Error: address must be between 0 and 4095.")
        continue

    vpn = address // PAGE_SIZE
    offset = address % PAGE_SIZE

    print(f"Virtual Page Number (VPN): {vpn}")
    print(f"Page Offset: {offset}")

    page = page_table[vpn]

    if page["valid"]:
        frame = page["frame"]
        physical_address = (frame * PAGE_SIZE) + offset

        print(f"Physical Frame={frame}")
        print(f"Physical Address={physical_address}")
    else:
        print("PAGE FAULT")

    print("-" * 40)
