paso = 255/50

rojo, azul = [0,255],[255,0]

for x in range(50):
    print(f"{x}% {'{'} background: linear-gradient(90deg, rgba({'%.1f' % rojo[0]},0,{'%.1f' %rojo[1]},1) 0%, rgba({'%.1f' %azul[0]},0,{'%.1f' %azul[1]},1) 100%); {'}'}")
    rojo[0] += paso
    rojo[1] -= paso
    azul[0] -= paso
    azul[1] += paso

for x in range(50,101):
    print(f"{x}% {'{'} background: linear-gradient(90deg, rgba({'%.1f' % rojo[0]},0,{'%.1f' %rojo[1]},1) 0%, rgba({'%.1f' %azul[0]},0,{'%.1f' %azul[1]},1) 100%); {'}'}")
    rojo[0] -= paso
    rojo[1] += paso
    azul[0] += paso
    azul[1] -= paso