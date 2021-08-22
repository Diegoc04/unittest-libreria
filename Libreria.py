import math
#suma de dos numeros complejos
def Suma(X,Y):
    x1 = X.real
    x2 = X.imag
    y1 = Y.real
    y2 = Y.imag
    Suma_real= x1 + y1 
    suma_imag = x2 + y2
    return (Suma_real, suma_imag)
if __name__ == "__main__":
    print(Suma(11+6j,30-50j))
 
#resta de dos numeros complejos
def Resta(X,Y): 
    x1 = X.real
    x2 = X.imag
    y1 = Y.real
    y2 = Y.imag
    Resta_real = x1 + (y1*-1)
    resta_imag = x2 + (y2*-1)
    return (Resta_real, resta_imag)
if __name__ == "__main__":
    print(Resta(10+6j,30-50j))
#multiplicacion de dos numeros complejos
def Multiplicacion(X,Y):
    x1 = X.real
    x2 = X.imag
    y1 = Y.real
    y2 = Y.imag
    Multiplicacion_real = x1*y1 + (x2*y2)*-1
    multiplicacion_imag = x1*y2 + x2*y1 
    return(Multiplicacion_real, multiplicacion_imag)
    
if __name__ == "__main__":
    print(Multiplicacion(10+6j,30-50j))
#division de dos numeros complejos
def Division(X,Y): 
    x1 = X.real
    x2 = X.imag
    y1 = Y.real
    y2 = Y.imag
    Mul_real = x1*y1 + (x2*(y2*-1))*-1 
    Mul_imag = x1*(y2*-1) + x2*y1
    denominador = y1**2 + y2**2
    return(Mul_real/denominador, Mul_imag/denominador)
    
if __name__ == "__main__":
    print(Division(10+6j,30-50j))


#Modulo de un numero complejo
def Modulo(Z):
    a = Z.real
    b = Z.imag
    t = math.sqrt(a**2 + b**2)
    return(t)
if __name__ == "__main__":
    print(Modulo(8+6j))
    
#Conjugado de un numero complejo
def Conjugado(Z):
    c = Z.imag
    c = c*-1
    return(Z.real, c)
if __name__ == "__main__":
    print(Conjugado(8+6j))
#Conversión entre representaciones polar y cartesiano

#cartesiano a polar
def Car_Pol(Z):
    a = Z.real
    b = Z.imag
    r = math.sqrt(a**2 + b**2)
    θ = math.atan(b/a)
    θ = θ * 180/3.14
    return(r, θ)
if __name__ == "__main__":
    print(Car_Pol(8+6j))
"""""
#polar a cartesiano ///
a = r * math.cos(θ)
b = r * math.sin(θ)

print(f"{a} + {b}j")
"""""
#fase de un numero complejo
def Fase(Z):
    a = Z.real
    b = Z.imag
    r = math.sqrt(a**2 + b**2)
    θ = math.atan(b/a)
    θ = θ * 180/3.14
    return(θ)
if __name__ == "__main__":
    print(Fase(8+6j))
"""""
def main():
    X = input("introduzca el primer numero complejo en la forma (a+bj): ")
    Y = input("introduzca el segundo numero complejo en la forma (a+bj): ")
    X = complex(X)
    Y = complex(Y)
    result= Suma(X,Y)
    result= Resta(X,Y)
    result= Multiplicacion(X,Y)
    result= Division(X,Y)
    Z = input("introduzca el tercer numero complejo en la forma (a+bj): ")
    Z = complex(Z)
    result= Modulo(Z)
    result= Conjugado(Z)
    result= Car_Pol(Z)
    result= Fase(Z)
    

main()
"""""