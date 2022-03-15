from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.__summa_hinta = 0
        self.__ostos_lista = []

    def tavaroita_korissa(self):
        pass
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        total = 0
        for ostos in self.__ostos_lista:
            total += ostos.lukumaara()
        return total

    def hinta(self):
        return self.__summa_hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self,  lisattava: Tuote):
        self.__ostos_lista.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on