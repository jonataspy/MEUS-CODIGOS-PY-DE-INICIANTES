import math
angulo = float(input('qual o angulo que deseja ??'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente =math.tan(math.radians(angulo))
print('o angulo de {:.2f} tem o seno de {:.2f} o cosseno de {:.2f} e o tangente de {:.2f}'.format(angulo,seno,cosseno,tangente))