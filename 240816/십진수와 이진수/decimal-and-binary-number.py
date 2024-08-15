# 이진수 N이 주어짐, 십진수로 바꾸고 17배를하고 다시 이진수로 변환해서 출력

binary_num = input()

print(bin(int(f"0b{binary_num}", 2) * 17)[2:])