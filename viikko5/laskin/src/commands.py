class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self.__sovellus_logiikka = sovelluslogiikka
        self.__syote = syote

    def suorita(self):
        arvo = 0
        try:
            arvo = int(self.__syote())
        except Exception:
            pass
        
        self.__sovellus_logiikka.plus(arvo)

class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self.__sovellus_logiikka = sovelluslogiikka
        self.__syote = syote

    def suorita(self):
        arvo = 0
        try:
            arvo = int(self.__syote())
        except Exception:
            pass
        self.__sovellus_logiikka.miinus(arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka, syote):
        self.__sovellus_logiikka = sovelluslogiikka
        self.__syote = syote

    def suorita(self):
        self.__sovellus_logiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka, syote):
        self.__sovellus_logiikka = sovelluslogiikka
        self.__syote = syote
