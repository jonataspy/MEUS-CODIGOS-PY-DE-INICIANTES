#treino fds
medida =float(input('uma digita  medida'))
cm = medida * 100
mm = medida * 1000
dam = medida /10
hm = medida /100
km = medida /1000
print('a medida de {}m corresponde a {:.0f}cm e {:.0f}mm {:.1f}dam {:.2f}hm e {:.3f}km'.format(medida,cm,mm,dam,hm,km))