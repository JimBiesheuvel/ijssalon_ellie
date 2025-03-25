from algemene_functies import mijn_functie_2

def aanbieding(smaak, prijs, korting):
    aanbiedinsprijs = prijs*(1-korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {aanbiedinsprijs} euro."
    return uitvoer

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for i in inkomsten:
        totaal += i
    btw_bedrag = btw*totaal
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald moet worden."
    return uitvoer

def laag_en_hoog(mijn_lijst):
    uitvoer = []
    uitvoer.append(max(mijn_lijst))
    uitvoer.append(min(mijn_lijst))
    return uitvoer

def gemiddelde(mijn_lijst):
    aantal_in_mijn_lijst = 0
    totaal = 0
    for i in mijn_lijst:
        aantal_in_mijn_lijst += 1
        totaal += i
    gemiddelde = totaal/aantal_in_mijn_lijst
    uitvoer = f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
    return uitvoer

def meervoudig(invoer_lijst):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer