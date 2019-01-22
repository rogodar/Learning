def computepay(h,r):
    if h > 40:
        reg = r * h
        otp = (h - 40) * (r * 0.5)
        pay = reg + otp
    else:
        pay = h * r
    return pay

hoursDone = input('Enter Hours: ')
rateHour = input('Enter Rate: ')
hd = float(hoursDone)
rh = float(rateHour)

xp = computepay(hd, rh)
print('Pay',xp)
