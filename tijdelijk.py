from helper import decoreer
def print_aanbieding():
    dict_prijzen = {"aardbei" : 3, "vanille" : 4, "chocolade" : 5}
    aanbieding = 0.8 * dict_prijzen["aardbei"]
    reclame_tekst = f"Vandaag in de aanbieding: vanille ijs, 1 liter - slechts € {aanbieding}"
    reclame_tekst2 = reclame_tekst[:63]
    reclame_tekst3 = reclame_tekst2.upper()
    reclame_tekst4 = reclame_tekst3.split(" ")
    for el in reclame_tekst4:
        if(len(el) < 5):
            el = el.lower()
        print(el)
decoreer("Aanbieding")
print_aanbieding()