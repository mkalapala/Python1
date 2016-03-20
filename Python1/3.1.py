hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)
if h <= 40:
    pay = h*r
elif h > 40:
    pay = float(h-40)*r*1.5 + float(40*r)
print pay