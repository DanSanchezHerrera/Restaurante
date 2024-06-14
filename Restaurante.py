acumulador= 0
sfrec= False

print("Bienvenido a Restaurante Flor de Loto")

#socio frecuente

resp = input("¿Es socio frecuente? ").lower()
if resp == "si":
    sfrec = True

#colaciones
    
colacion = int(input("¿Qué tipo de colación desea?\n1-Colación Carne Mongoliana\n2-Colación Pollo Mongoliano\n "))
if colacion == 1:
    cantidad= int(input("¿Cuántas colaciones desea?"))
    acumulador = acumulador+3800*cantidad
if colacion == 2:
    cantidad= int(input("¿Cuántas colaciones desea?"))
    acumulador = acumulador+3500*cantidad
    
if sfrec:
    acumulador = acumulador*0.85
    
print(f"Su total hasta el momento es ${acumulador}")

# Wantán y arrollados

agregados = int(input("¿Desea agregar extras?\n1-Arrollados Primavera: tres por porción\n2-Wantán: seis por porción\n3-Ambos: Arollados y Wantán "))
if agregados == 1:
    cantidad= int(input("¿Cuántas porciones de Arollados Primavera desea?"))
    acumulador = acumulador+2000*cantidad
if agregados == 2:
    cantidad= int(input("¿Cuántas porciones de Wantán desea?"))
    acumulador = acumulador+3000*cantidad
if agregados == 3:
    wantan= int(input("¿Cuántas porciones de Wantán desea?"))
    acumulador = acumulador+3000*wantan
    arollados= int(input("¿Cuántas porciones de Arollados Primavera desea?"))
    acumulador= acumulador+2000*arollados

print(f"Su total hasta el momento es ${acumulador}")

# Bebidas

bebidas = int(input("¿Desea agregar bebidas?\n1-Bebida Pequeña\n2-Bebida Mediana\n3-Bebida Grande"))
if bebidas == 1:
    cantidad= int(input("¿Cuántas Bebidas Pequeñas desea?"))
    acumulador = acumulador+1000*cantidad
if bebidas == 2:
    cantidad= int(input("¿Cuántas Bebidas Medianas desea?"))
    acumulador = acumulador+1500*cantidad
if bebidas == 3:
    cantidad= int(input("¿Cuántas Bebidas Grandes desea?"))
    acumulador = acumulador+2000*wantan

#Total a pagar
    
print(f"Su total a pagar es ${acumulador}")

#Efectivo

efectivo = int(input("¿Con cuánto cancela? "))
if efectivo < acumulador:
    print("Dinero insuficiente")
else:
    vuelto = efectivo - acumulador
    print(f"Su vuelto es ${vuelto}")