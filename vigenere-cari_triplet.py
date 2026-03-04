with open("vigenere.txt") as lines:
    f = lines.read()
    triplet = {}
    for i in range(len(f)-2):
        count = 0
        line_a = f[i]+f[i+1]+f[i+2]
        if line_a in triplet:
            continue
        x = 0
        for j in range(i+3, len(f)-2):
            line_b = f[j]+f[j+1]+f[j+2]
            if line_a == line_b:
                if line_a not in triplet:
                    triplet[line_a] = []
                triplet[line_a].append(j-i)
                x+=1
    sorted_triplets = sorted(triplet.items(), key=lambda item: len(item[1]), reverse=True)
    for key, value in sorted_triplets[:25]:
        print(key, value)