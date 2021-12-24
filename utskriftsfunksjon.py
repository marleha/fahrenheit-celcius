#Oppgave 1

#Programmet ser først at vi har en funksjon og deretter hopper programmet ned til 
# prosedyrekallet. Programmet går inn i funksjonen. Den ber bruker skrive
#inn navn, deretter bosted, og printer begge med tekst lagt til. Funksjonen
# returnerer. Nå blir prosedyren kalt på igjen og det samme skjer. Dette
#skjer en gang til. Da har dette skjedd tre ganger og vi har kalt på prosedyren
#tre ganger.

def MittProsedyreNavn():
	navn=input("Skriv inn navn: ")
	bosted=input("Hvor kommer du fra? ")
	print("Hei, " + navn + "! Du er fra " + bosted + ".")

MittProsedyreNavn()
MittProsedyreNavn()
MittProsedyreNavn()