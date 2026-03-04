with open("vigenere.txt") as lines:
    f = lines.read()
    isi = []
    for i in range(0, len(f)-1, 8):
        if (i+7>=len(f)):
            break
        a = chr((ord(f[i]) - ord('S') + 26)%26 + ord('A'))
        b = chr((ord(f[i+1]) - ord('H') + 26)%26 + ord('A'))
        c = chr((ord(f[i+2]) - ord('O') + 26)%26 + ord('A'))
        d = chr((ord(f[i+3]) - ord('W') + 26)%26 + ord('A'))
        e = chr((ord(f[i+4]) - ord('T') + 26)%26 + ord('A'))
        line_a = a+b+c+d+e+f[i+5]+f[i+6]+f[i+7]
        if line_a in isi:
            continue
        isi.append(line_a)
    x = 1
    for i in isi:
        print(x, i)
        x+=1