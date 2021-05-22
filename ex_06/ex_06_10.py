text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find(':')
val = text[ipos+1:]
fval = float(val)
print(fval)
