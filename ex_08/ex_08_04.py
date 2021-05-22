fh = open('romeo.txt')
wl = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in wl:
            wl.append(word)
wl.sort()
print(wl)
