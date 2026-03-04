x = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
b = 4
n = 26

with open("affine.txt") as lines:
    f = lines.read()
    for m in x:
        for i in range(1, 27):
            hasil = ""
            if ((m*i)%26)==1:
                for j in range(len(f)):
                    e = chr((i*(ord(f[j])-ord('A')-b))%26 + ord('A'))
                    hasil+=e
                print(i, b, hasil)