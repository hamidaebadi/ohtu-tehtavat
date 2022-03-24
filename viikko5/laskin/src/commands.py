class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self.__sovellus_logiikka = sovelluslogiikka
        self.__syote = syote

    def _get_value(self):
        arvo = 0
        try:
            arvo = int(self.__syote())
        except Exception:
            pass
        return arvo

    def suorita(self):
        arvo = self._get_value()
        self.__sovellus_logiikka.plus(arvo)

class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self.__sovellus_logiikka = sovelluslogiikka
        self.__syote = syote

    def _get_value(self):
        arvo = 0
        try:
            arvo = int(self.__syote())
        except Exception:
            pass
        return arvo

    def suorita(self):
        arvo = self._get_value()
        self.__sovellus_logiikka.miinus(arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka, syote):
        self.__sovellus_logiikka = sovelluslogiikka
        self.__syote = syote

    def suorita(self):
        self.__sovellus_logiikka.nollaa()


    def _get_value(self):
        arvo = 0
        try:
            arvo = int(self.__syote())
        except Exception:
            pass
        return arvo

class Kumoa:
    def __init__(self, sovelluslogiikka, syote):
        self.__sovellus_logiikka = sovelluslogiikka
        self.__syote = syote

    def suorita(self):
        self.__sovellus_logiikka.aseta_arvo(self.__sovellus_logiikka.edellinen_tulos)
