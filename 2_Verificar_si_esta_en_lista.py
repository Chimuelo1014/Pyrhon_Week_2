# 2. Verificar si un número está en una lista

#     Crea una lista con 5 números.
#     Pide un número al usuario y verifica si está en la lista usando in.

lista = [1,2,3,4,5]

num = int((input("Ingrese su numero: ")))
for i in lista :
    if num in lista :
       n = True
       break
    else :
        n= False
        break
if n == True :
    print("El numero esta en la lista")
else :
    print("El numero no esta en la lista")