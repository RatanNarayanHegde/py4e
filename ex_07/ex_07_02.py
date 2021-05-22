fname = input('Enter the name of the file: ')
try:
    fh = open(fname)
except:
    print('Enter a valid filename')
    quit()
total = 0
count = 0
for line in fh:
    line = line.rstrip()
    if 'X-DSPAM-Confidence:' in line:
        ipos = line.find(':')
        sval = line[ipos+1:]
        fval = float(sval)
        total = total + fval
        count = count + 1

avg = total / count
print('Average spam confidence:', avg)
