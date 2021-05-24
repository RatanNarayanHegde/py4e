fh = open('mbox-short.txt')

hc = dict()
for line in fh:
    if not line.startswith('From '):
        continue
    words = line.split()
    time = words[5]
    hours = time.split(':')[0]
    hc[hours] = hc.get(hours, 0) + 1
sl = sorted(hc.items())
for h, c in sl:
    print(h, c)
