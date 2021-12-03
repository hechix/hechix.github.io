paso = 255/50
paso_tam = 20/50


rojo = 255
tam = 25

for x in range(50):
    print(f"{x}% {'{'} color: rgb({'%.2f' % rojo},255,0) ; font-size: {'%.2f' % tam}vw; padding-top: {x/2}vh; {'}'}")
    rojo -= paso
    tam -= paso_tam

for x in range(50,101):
    print(f"{x}% {'{'} color: rgb({'%.2f' % rojo},255,0) ; font-size: {'%.2f' % tam}vw; padding-top: {(100-x)/2}vh; {'}'}")
    rojo += paso
    tam += paso_tam