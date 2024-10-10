#area de dolar
real =float(input('quanto dinheiro voce tem na carteira? R$'))
dolar = real / 5.45
print('com {:.2f}R$ voce pode comprar {:.2f} dolares'.format(real,dolar,))
#area de euro
print('= ='*20)
print('valor em euro')
real2 = float(input('quantos voce tem na carteira R$'))
euro = real2 / 6.10
print('R${:.2f} equivale a {:.2f} euros'.format(real2,euro))
#ienes bucha
print('valor em iene')
print('= ='*210)
real3 =float(input('quanto voce tem na carteira R$'))
iene = real3 / 0.038
print('R${:.2f} equivale a {:.2f} iene'.format(real,iene))