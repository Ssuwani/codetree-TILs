hex_input = input()

num = int(f"0o{hex_input}", 8)
bin_num = bin(num)[2:]
print(bin_num)