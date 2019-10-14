hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

if h > 40.0 :
    ex=h-40.0
    gross=(40.0*r)+(ex*1.5*r)
else :
    gross=(h*r)

print (gross)
