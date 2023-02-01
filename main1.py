print("Tanulók feldolgozása!")

tanulok = []
while True:
    print("\nKérem a tanuló adatait: ")
    nev = input("Add meg a tanuló nevét: ")
    szId = input("Add meg a születési dátumot: ")
    magassag = int(input("Magasság: "))

    tanulo = (nev, szId, magassag)
    tanulok.append(tanulo)

    valasz = input("Tuvábbi tanulo? y/N ")
    if valasz.lower() != 'y':
        break

