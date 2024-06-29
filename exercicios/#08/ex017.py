'''Três maneiras de fazer: '''

from math import sqrt, hypot
CatOp = float(input('Digite o comprimento do cateto oposto do triângulo retângulo: '))
CatAd = float(input('Digite o comprimento do cateto adjacente do triângulo retângulo : '))
Hipotenusa = ((CatOp ** 2) + (CatAd ** 2))
Hipotenusa = Hipotenusa ** (1/2)
print(f'A hipotenusa é : {Hipotenusa:.2f}.')


CatOp = float(input('Digite o comprimento do cateto oposto do triângulo retângulo: '))
CatAd = float(input('Digite o comprimento do cateto adjacente do triângulo retângulo : '))
Hipotenusa = ((CatOp*CatOp)+(CatAd*CatAd))
Hipotenusa = sqrt(Hipotenusa)
print(f'A hipotenusa é : {Hipotenusa}.')


CatOp = float(input('Digite o comprimento do cateto oposto do triângulo retângulo: '))
CatAd = float(input('Digite o comprimento do cateto adjacente do triângulo retângulo : '))
Hipotenusa = hypot(CatOp,CatAd)
print(f'A hipotenusa é : {Hipotenusa}.')