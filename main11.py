larg =float(input('largura da parede '))
alt =float(input('altura da parede'))
area = larg * alt
print('sua parede tem a dimenção de {}x{} e a sua área é de {}m².'.format( larg, alt, area))
tinta = area / 2
print('para pintar essa parede vc precisa de {} de tinta '.format(tinta))