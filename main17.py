from math import hypot
co = float(input('comprimento do cateto oposto'))
ca = float(input('comprimento do csteto adjacente'))
hi = hypot(co,ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))