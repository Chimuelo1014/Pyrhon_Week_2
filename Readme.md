Se decide crear un menú con un match con todas las opciones, todo en un while para que se cierre unicamente cuando se digite la opción 5 teniendo en cuenta las funcionalidades requeridas para el programa.
En la primera opción se puede verificar si la nota única que ingresa el usuario fue aprobada o reprobada en un rango de aprobación mayor o igual a 70
siendo menor reprobada. y validando el tipo de dato ingresado (validación la cual hago en las 4 secciones) y que este en rango de 0-100.
devolviendo "Aprobada" o "Reprobada" siendo el caso. 

En la opción 2 se pide el ingreso de varias notas separadas por coma, allí uso un split para "dividir" el string y luego lo casteo a int y por ultimo para el promedio sumo todos los valores de la lista y lo divido por el len de los valores que hay.

En la opción 3 se utiliza la lista que se ingreso en la opción 2, dado el caso que no se halla ingresado aun se imprime un aviso y se redirecciona al menú principal para que lo pueda hacer, y cuando se ingresan las notas, cuenta los valores que hay mayores a ese con un contador.
Se tiene en cuenta que la lista que usara es la ultima que se ingreso en la opción 2.

En la opcion 4 sucede casi lo mismo que en el caso 3 pero el contador se "activa" cuando el valor ingresado esta en la lista.
Y por ultimo en la opción 5 se imprime un mensaje de despedida y se usa un exit para cerrar el programa
