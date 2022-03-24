class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen_tulos = 0

    def miinus(self, arvo):
        self.edellinen_tulos = self.tulos
        self.tulos = self.tulos - int(arvo)

    def plus(self, arvo):
        self.edellinen_tulos = self.tulos
        self.tulos = self.tulos + int(arvo)

    def nollaa(self):
        self.edellinen_tulos = self.tulos
        self.tulos = 0
        
    def aseta_arvo(self, arvo):
        self.tulos = int(arvo)
