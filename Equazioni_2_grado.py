
"""
Autore: Marco Dottori
Questo programma fa parte della raccolta "Simple program for everyday life" 
e permette di calcolare le equazioni di secondo grado
10
"""
import math

a = int(input("Dammi la a: "))
b = int(input("Dammi la b: "))
c = int(input("Dammi la c: "))

delta = math.sqrt(b*b-4*a*c) #calcolo il delta e lo metto già sotto radice
if (delta < 0):
    print ("Equazione non possibile, delta minore di zero")
else:
    
    x1 = ((b*(-1))+delta)/(2*a) #ora calcolo x1
    print ("x1 è uguale a : ", x1)
    x2 = ((b*(-1))-delta)/(2*a) #ora calcolo x2
    print ("x2 è uguale a : ", x2)

