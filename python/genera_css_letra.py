paso = 255/50
paso_tam = 20/50
paso_pad = 25/50

rojo = 0
tam = 5
pad = 25

z = 0

# for x in range(0):# Pasos previos
#     rojo -= paso
#     tam -= paso_tam
#     pad += paso_pad


for x in range(50,101):
    print(f"{z}% {'{'} color: rgb({'%.1f' % rojo},255,0) ; font-size: {'%.1f' % tam}vw; padding-top: {'%.1f' % pad}vh; {'}'}")
    rojo += paso
    tam += paso_tam
    pad -= paso_pad
    z+= 1

for x in range(50):
    print(f"{z}% {'{'} color: rgb({'%.1f' % rojo},255,0) ; font-size: {'%.1f' % tam}vw; padding-top: {'%.1f' % pad}vh; {'}'}")
    rojo -= paso
    tam -= paso_tam
    pad += paso_pad
    z+= 1