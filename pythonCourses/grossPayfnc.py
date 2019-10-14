hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

def computepay(h,r) :
    if h > 40.0 :
        return(((h-40)*1.5*r) + (40.0*r))
    else :
        return(r*h)

print(computepay(hours,rate))
