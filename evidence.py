from pojisteny import Pojisteny

class Evidencer:
    def __init__(self):
        self.pojisteni = []

    def pridej_pojisteneho(self):
        jmeno = input("Zadejte jméno pojisteného: ")
        prijmeni = input("Zadejte příjmení: ")
        telefon = input("Zadejte telefoní číslo: ")
        vek = input("Zadejte věk: ")
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojisteni.append(pojisteny)
        print("Data byla ulozena.")
    
    def vypis_pojistene(self):
        if not self.pojisteni:
            print("Zatím nejsou evidováni žádní pojištění.")
        else:
            print("Jméno\tPříjmení\tVěk\tTelefonní číslo")
            for pojisteny in self.pojisteni:
                print(pojisteny)
    
    def najdi_pojisteneho(self):
        jmeno = input("Zadejte jméno pojisteného: ")
        prijmeni = input("Zadejte příjmení: ")
        nalezeni = False
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno.lower() == jmeno.lower() and pojisteny.prijmeni.lower() == prijmeni.lower():
                nalezeni = True
                print(pojisteny)
                break
        if not nalezeni:
            print("Pojištěný s tímto jménem a příjmením nebyl nalezen.")