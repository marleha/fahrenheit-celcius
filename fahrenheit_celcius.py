#Oppgave 2

#Først ber programmet brukeren skrive inn temperaturen i fahrenheit. Deretter
#setter den variabelen fahrenhet til å bli et flyttall. Etterpå printer
#den variabelen. Deretter regner den ut hva fahrenheit er i celcius og til slutt
#printer celcius. 

fahrenheit= input("Skriv inn temperaturen i fahrenheit: ")
fahrenheit=float(fahrenheit)
print(fahrenheit)
celcius=((fahrenheit)-32)*5/9
print("{0:.2f}".format(celcius))


#printe bare to siffer etter komma?