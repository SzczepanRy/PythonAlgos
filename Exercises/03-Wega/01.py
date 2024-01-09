plik = open("sygnaly.txt", "r")
wyniki = open("wyniki4.txt", "w")
tekst = plik.readlines()

odp = "Zadanie 4.1 " + "".join(i[9] for i in tekst[39::40])
print(odp)
wyniki.write(odp)

plik.close()
wyniki.close()