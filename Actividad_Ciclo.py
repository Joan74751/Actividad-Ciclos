#Solicitud de datos
nombre = input("\nNombre Completo:\n")
materias = 5

f = 1
sumatoria = 0

while f <= materias:
    name_materia = input(f'\nIngresa el nombre de la ({f}) materia\n')
    calificacion = float(input(f'\nCalificacion obtenidas en {name_materia}\n'))

#Sumar la calificación a la sumatoria

    sumatoria = sumatoria + calificacion

#Aumentar el contador para no hacer un ciclo infinito

    f = f + 1

#Hacer calculos e imprimir resultados
promedio = sumatoria / materias
print("\n***RESULTADOS***")
print(f'Hola, {nombre} tienes un promedio de {promedio} en el 5to semestre.\n')

'''
¿Cual es tu nombre y promedio obtuviste?

Nombre Completo:
Joan Cubillos

Ingresa el nombre de la (1) materia
Seguridad Informática

Calificacion obtenidas en Seguridad Informática
5.0

Ingresa el nombre de la (2) materia
Ingeniería Web

Calificacion obtenidas en Ingeniería Web
4.5

Ingresa el nombre de la (3) materia
Inteligencia Artificial

Calificacion obtenidas en Inteligencia Artificial
3.6

Ingresa el nombre de la (4) materia
Programación Móvil

Calificacion obtenidas en Programación Móvil
3.9

Ingresa el nombre de la (5) materia
Redes

Calificacion obtenidas en Redes
4.3

***RESULTADOS***
Hola, Joan Cubillos tienes un promedio de 4.26 en el 5to semestre.

'''