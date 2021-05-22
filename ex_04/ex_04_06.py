def computepay(hours, rate):
    if hours > 40:
        pay = 40*rate + (hours-40) * (rate*1.5)
        return pay
    else:
        pay = hours * rate
        return pay


fh = float(input("Enter hours: "))
fr = float(input("Enter rates: "))
fp = computepay(fh, fr)
print("Pay", fp)
