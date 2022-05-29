# Cezara z dowolnym przesunięciem

n = int(input("Podaj przesunięcie: "))

tekst = str(input("Wprowadź tekst (bez polskich znaków): "))

tekst_po = ''

for i in range(len(tekst)):
    tekst_po += str(chr(ord(tekst[i]) + n))

print(tekst)
print(tekst_po)
