KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(self.alkioiden_lkm):
            if n == self.lukujono[i]:
                return True
        return False

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.lukujono[0] = n
            self.alkioiden_lkm += 1
            return True

        if not self.kuuluu(n):
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.lukujono) == 0:
               # lukujono on täynnä! lisää tilaa
               self.lisaa_tilaa_intjoukolle()
            return True

        return False

    def lisaa_tilaa_intjoukolle(self):
        taulukko_old = self.lukujono
        self.kopioi_taulukko(self.lukujono, taulukko_old)
        self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(taulukko_old, self.lukujono)

    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(self.alkioiden_lkm):
            if n == self.lukujono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.lukujono[kohta] = 0
                break

        if kohta != -1:
            self.siirra_luvut(kohta)
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def siirra_luvut(self, indeksi):
        for j in range(indeksi, self.alkioiden_lkm - 1):
            apu = self.lukujono[j]
            self.lukujono[j] = self.lukujono[j + 1]
            self.lukujono[j + 1] = apu

    def kopioi_taulukko(self, from_arr, new_arr):
        for i in range(len(from_arr)):
            new_arr[i] = from_arr[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [self.lukujono[i] for i in range(self.alkioiden_lkm)]
        return taulu

    @staticmethod
    def yhdiste(first_tbl, second_tbl):
        yhdiste_taulu = IntJoukko()
        yhdistettu = first_tbl.to_int_list() + second_tbl.to_int_list()
        for luku in yhdistettu:
            yhdiste_taulu.lisaa(luku)
        return yhdiste_taulu

    @staticmethod
    def leikkaus(eka_taulu, toka_taulu):
        leikkaus_taulu = IntJoukko()
        
        for luku in eka_taulu.to_int_list():
            if luku in toka_taulu.to_int_list():
                leikkaus_taulu.lisaa(luku)
        return leikkaus_taulu

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            tuotos += ", ".join([str(self.lukujono[i]) for i in range(self.alkioiden_lkm)])
            tuotos += "}"
            return tuotos
