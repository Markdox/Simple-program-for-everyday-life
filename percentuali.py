"""
Autore: Marco Dottori
Questo programma permette di calcolare le percentuali
sia come sconti che come rincari in base a quello che si sceglie
Fa parte della collezzione di programmi "Siple program for everyday life"

"""

print ("Ciao, questo programma calcola le percentuali sia come sconti che come rincari \n")
scelta = input ("Il prezzo finale da calcolare è uno sconto o un rincaro? r = rincaro e s = sconto (r/s): ")

if scelta == 's':
    prezzo = int(input("Inserisci il prezzo: "))
    sconto = int(input("Inserisci la percentuale di sconto: "))
    conto = (prezzo*sconto)/100
    prezzo_finale = prezzo - conto
    print ("Il prezzo finale è: ", prezzo_finale)
    
elif scelta == 'r':
    prezzo = int(input("Inserisci il prezzo: "))
    sconto = int(input("Inserisci la percentuale di rincaro: "))
    conto = (prezzo*sconto)/100
    prezzo_finale = prezzo + conto
    print ("Il prezzo finale è: ", prezzo_finale)


