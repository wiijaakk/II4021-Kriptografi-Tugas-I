with open("stega6.txt") as lines:
    f = lines.read()
    hex_values = f.split(',')
    key = 0xC5    
    for hex_val in hex_values:
        hex_val = hex_val.strip()
        if hex_val:
            num = int(hex_val, 16)
            result = num ^ key
            print(f"0x{result:02x}", end=' ')