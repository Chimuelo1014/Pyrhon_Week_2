# El programa que vas a desarrollar en este entrenamiento debe:

#     Determinar el estado de aprobación:
#         Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
#         Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
#     Calcular el promedio:
#         Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
#         Calcular y mostrar el promedio de las calificaciones en la lista
#     Contar calificaciones mayores:
#         Preguntar al usuario por un valor específico
#         Contar cuántas calificaciones en la lista son mayores que este valor
#     Verificar y contar calificaciones específicas:
#         Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
#         Calcular y mostrar el promedio de las calificaciones en la lista
validate1 = True
validate2 = True
task=0
sw=0
while task != 5 :
        if sw==0 :
            task = int(input("-------------------------------------------------\n¡Bienvendio!\nIngrese\n1 Para determinar el estado de aprobacion \n2 Para calcular el promedio\n3 Para contar calificaciones mayores \n4 Para Verificar y contar calificaciones específicas\n5 Para salir\n-------------------------------------\nDigite un número valido : "))
            sw=1
        else :
            task = int(input("\nIngrese\n1 Para determinar el estado de aprobacion \n2 Para calcular el promedio\n3 Para contar calificaciones mayores \n4 Para Verificar y contar calificaciones específicas\n5 Para salir\nDigite un número valido : "))

        #podria haber un while
        if 5<task>1 :
            print("¡Ingrese un valor valido!")
            continue
        else :
            
            match task:
                
                    case 1:
                        while validate1 != False :
                            # Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
                        # Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
                            case1 = int(input("Ingrese la calificacion a revisar de 0 a 100: "))
                        
                            if (type(case1)) != int :
                                
                                print("¡Ingrese un valor valido!")
                                validate1==True

                            if 70<=case1<100 : 
                                print("APROBADO")
                                validate1==False
                                break
                            elif 0<=case1<70 :
                                print("REPROBADO")
                                validate1==False
                                break
                            else :
                                print("¡Ingrese un valor valido!")
                                validate1==True

                        
                    case 2:

                    # Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
                    # Calcular y mostrar el promedio de las calificaciones en la lista

                        case2 = int(input("Ingrese las notas a calcular\n¡Deben estar separadas por coma!: ")) #split
                    case 3:

                    # Preguntar al usuario por un valor específico
                    # Contar cuántas calificaciones en la lista son mayores que este valor

                        case3 = int(input("Ingrese el valor a comprobar: "))

                    case 4:


                    # Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
                    # Calcular y mostrar el promedio de las calificaciones en la lista
                        print("")
                    case 5:
                        print("Adios")
                        break  
                    case _:
                        print("Ingrese un numero valido")

            # Cerrraria while 
            #while dentro de cada parte 
