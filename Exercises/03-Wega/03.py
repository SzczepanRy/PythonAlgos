plik = open("sygnaly.txt", "r")
tekst = plik.readlines()

for wiersz in tekst:
    tekst_wiersza = sorted(set(wiersz[:-1]))
    if ord(tekst_wiersza[-1])-ord(tekst_wiersza[0]) <= 10:
        print(wiersz[:-1])

plik.close()