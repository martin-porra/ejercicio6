from clase import FechaHora
import os
def menu():
 os.system('cls') # NOTA para windows tienes que cambiar clear por cls
 print ("Selecciona una opción")
 print ("\t1 - sumar fechas")
 print ("\t2 - restar fechas")
 print ("\t3 - distinguir fecha mayor")

if __name__ == '__main__':
 print('ingresar primera fecha')
 año = int(input('año '))
 mes = int(input('mes '))
 dia = int(input('dia '))
 hora = int(input('hora '))
 min = int(input('minuto '))
 seg = int(input('segundo '))
 t1 = FechaHora(año,mes,dia,hora,min,seg)
 print('ingrese segunda fecha')
 print('ingresar primera fecha')
 año = int(input('año '))
 mes = int(input('mes '))
 dia = int(input('dia '))
 hora = int(input('hora '))
 min = int(input('minuto '))
 seg = int(input('segundo '))
 t2 = FechaHora(año,mes,dia,hora,min,seg)
 t1.Mostrar()
 t2.Mostrar()
 a = True
 while a == True:
   menu()
   opcion = input()
   if opcion == '1':
    t1.__Add__(t2)
    t1.Mostrar()
   elif opcion == '2':
    t1.__sub__(t2)
    t1.Mostrar()
   elif opcion == '3':
    if t1.__gt__(t2) == 1:
     print('la primera fecha es mayor')
    else:
      print('la segunda fecha es mayor')
   else:
    a = False
    print('opcion incorrecta')
 print('programa terminado')