#!/usr/bin/python3
senal = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print(chr(i - senal), end="")
    if senal == 0:
        senal = 32
    else:
        senal = 0
