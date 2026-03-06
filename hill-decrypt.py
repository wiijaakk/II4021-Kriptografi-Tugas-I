with open("hill.txt") as lines:
    f = lines.read()
    K_inv = [[8,5,10],[21,8,21],[21,12,8]]
    result=""
    for x in range(0, len(f), 3):
        num1 = ord(f[x])-ord('A')
        num2 = ord(f[x+1])-ord('A')
        num3 = ord(f[x+2])-ord('A')
        c1 = (K_inv[0][0]*num1 + K_inv[0][1]*num2 + K_inv[0][2]*num3)%26
        c2 = (K_inv[1][0]*num1 + K_inv[1][1]*num2 + K_inv[1][2]*num3)%26
        c3 = (K_inv[2][0]*num1 + K_inv[2][1]*num2 + K_inv[2][2]*num3)%26
        result+=chr(c1+ord('A'))
        result+=chr(c2+ord('A'))
        result+=chr(c3+ord('A'))
    print(result)