#import calculadora.calculos as calc #alias

#print(calc.suma(2, 3))

#-------------------------------------------------------------

#from calculadora import calculos

#print(calculos.suma(2, 3))
#print(calculos.resta(2, 3))
#print(calculos.multiplicacion(2, 3))
#print(calculos.division(2, 3))
#print(calculos.cuadrado(2))
#-------------------------------------------------------------
#from calculadora.calculos import suma, resta

#print(suma(2, 3))
#print(resta(2, 3))
#print(multiplicacion(2, 3))

#-------------------------------------------------------------

#from calculadora.calculos import suma as s
#from calculadora.calculos import resta as r

#print(s(2, 3))
#print(r(2, 3))

#-------------------------------------------------------------

from calculadora.calculos import suma as s, resta as r

print(s(2, 3))
print(r(2, 3))


