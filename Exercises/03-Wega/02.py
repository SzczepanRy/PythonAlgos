plik = open("sygnaly.txt", "r")
tekst = plik.readlines()
roznych_liter = tekst_wiersza = 0

for wiersz in tekst:
    wiersz = wiersz[:-1]
    if roznych_liter < len(set(wiersz)):
        roznych_liter = len(set(wiersz))
        tekst_wiersza = wiersz
print(tekst_wiersza, roznych_liter)

plik.close()