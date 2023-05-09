from evidence import Evidencer


evidencer = Evidencer()
while True:
    print("___________________________")
    print("Evidence pojistenych")
    print("___________________________\n")
    print("Vyberte si akci:")
    print("1 - Pridat nového pojisteného")
    print("2 - Vypsat všechny pojistené")
    print("3 - Vyhledat pojisteného")
    print("4 - Konec\n")
    volba = input()
    if volba == "1":
        evidencer.pridej_pojisteneho()
        input("\nPokračujte libovolnou klávesou...")
    elif volba == "2":
        evidencer.vypis_pojistene()
        input("\nPokračujte libovolnou klávesou...")
    elif volba == "3":
        evidencer.najdi_pojisteneho()
        input("\nPokračujte libovolnou klávesou...")
    elif volba == "4":
        break
    else:
        print("Neplatna volba. Zkuste to znovu.")