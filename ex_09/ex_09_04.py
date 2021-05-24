fname = input("Enter file: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)

di = dict()
for line in fh:
    if not line.startswith('From '):
        continue
    words = line.split()
    sender = words[1]
    di[sender] = di.get(sender, 0) + 1

hs = None
hc = None
for sender, count in di.items():
    if hc is None or count > hc:
        hc = count
        hs = sender
print(hs, hc)
