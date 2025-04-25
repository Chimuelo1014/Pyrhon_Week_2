# 5. ¿Está en la lista de invitados?

#     Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
#     Pide al usuario su nombre.
#     Usa if para decir si está en la lista de invitados o no.
lista = ["Samuel","Ana","Juan","Sofia","Antony","Robin","Ramiro"]
name = input("Ingrese su nombre: ")
for i in lista :
    if name in lista :
        n = True
    else :
        n=False
if n:
    print("Esta en la lista")
else :
    print("No esta en la lista")
    