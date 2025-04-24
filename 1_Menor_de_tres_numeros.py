# 1. Menor de tres números

#     Pide tres números al usuario.
#     Usa condicionales (if) para decir cuál es el más pequeño.
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

if n1 <= n2 and n1<=n3 :
    print("El numero menor es: ",n1)
elif n2 <= n1 and n2<=n3 :
    print("El numero menor es: ",n2)
elif n3 <= n1 and n3<=n2 :
    print("El numero menor es: ",n3)


