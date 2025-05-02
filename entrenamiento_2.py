validate1 = True
task=0
sw=0
prom = 0                        #Se inicializan variables que necesitaremos en el programa 
counter = 0                     #la variable sw es un swithces 
case2 = 0
validate3 = True
countin = 0
#while para que se cierre solo cuando sea 5, y se inicializo antes con un numero diferente a 5 para que se ejecute almenos una vez (una bandera)
while task != 5 :
    
    while True:
        try :#evitar que se cierre el programa cuando ingrese un valor de diferente tipo
            if sw==0 :#se inicializa en 0 asi que el Bienvenido solo aparecera la primera vez que se ejecute 
                task = int(input("-------------------------------------------------\n¡Bienvendio!\nIngrese\n1 Para determinar el estado de aprobacion \n2 Para calcular el promedio\n3 Para contar calificaciones mayores \n4 Para Verificar y contar calificaciones específicas\n5 Para salir\n-------------------------------------\n\nDigite un número valido : "))
                sw=1 #se da valor a  1 para que cuando se ejecute por primera vez diga bienvenido luego ya no.
            else :
                task = int(input("\nIngrese\n1 Para determinar el estado de aprobacion \n2 Para calcular el promedio\n3 Para contar calificaciones mayores \n4 Para Verificar y contar calificaciones específicas\n5 Para salir\nDigite un número valido : "))
                #la variable task dirigira el menu principal
            
            if 5<task>1 : #Que el valor digitado no sea diferente a los del menu
                print("¡Ingrese un valor valido!")
                continue
            else :
                
                match task:
                    
                        case 1: # case 1 que determina si fue aprobado o reprobado
                            while True:
                                try :
        
                                    while validate1 != False :
                                        # Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
                                    # Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
                                        case1 = int(input("\nIngrese la calificacion a revisar de 0 a 100: "))
                                    
                                        
                                        #valida aprobado o reprobado segun sea el caso, si ingresa un valor diferente da un aviso y sigue el cilo while
                                        if 70<=case1<=100 : 
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
                                    break
                                except : #maneja error si ingresa un valor de tipo diferente
                                    print("¡Ingrese un valor valido!")
                            
                        case 2:  #case 2 ingresa lista de valores y da promedio, esta lista se reutilizara en case 3 y 4
                            
                            while True:
                                try :
        
                                    # while validate1 != False :
                                        case2 = []
                                        case22 = input("Ingrese las notas a calcular\n¡Deben estar separadas por coma!: ") #split
                                        case22 = case22.split(",")  #divide el str por comas
                                        case2 = [float(num) for num in case22]  #va convirtiendo a entero 
                                        
                                        prom = sum(case2)/len(case2) 
                                        print("EL promedio de las notas ingresadas es de: ",prom)
                                        break

                                except :
                                    print("¡Ingrese un valor valido!")
                                   

                        # Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
                        # Calcular y mostrar el promedio de las calificaciones en la lista

                           
                        case 3:
                            #mira cuantas veces hay numeros mayores en la ultima lista ingrasada en la opcion 2 a el valor ingresado
                            while True:
                                try :
                                    case3 = int(input("Ingrese el valor a comprobar: "))
                                    if not case2 :
                                        print("Ingrese valores primero en la seccion 2: ")
                                        break
                                    else:
                                        for i in case2:
                                            if i > case3 :
                                                counter+=1
                                        
                                        break
                                    
                                except :
                                    print("¡Ingrese un valor valido!")   
                            print("Hay",counter," valores mayores") 
                            counter = 0        
                                  

                        # Preguntar al usuario por un valor específico
                        # Contar cuántas calificaciones en la lista son mayores que este valor

                            # case3 = int(input("Ingrese el valor a comprobar: "))

                        case 4:
                            #lo mismo que el caso 3 pero envez de ontar mayores cuenta iguales 
                            while True:
                                try :
                                    case3 = int(input("Ingrese el valor a comprobar: "))
                                    if not case2 :
                                        print("Ingrese valores primero en la seccion 2: ")
                                        break
                                    else:
                                        countin = case2.count(case3) #se utiliza count que nos cuentas las vece que esta la variable en la lista
                                        
                                    break
                                    
                                except :
                                    print("¡Ingrese un valor valido!")   
                            print("Hay",countin," valores iguales") 
                            countin = 0        

                        # Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
                        # Calcular y mostrar el promedio de las calificaciones en la lista
                            # print("")
                        case 5:
                            print("Adios")
                            break  
                        case _:
                            print("Ingrese un numero valido")

               
            #para cuando ingrese el valor de diferente tipo     
        except :
            print("¡¡¡Ingrese un valor valido: !!!")
        