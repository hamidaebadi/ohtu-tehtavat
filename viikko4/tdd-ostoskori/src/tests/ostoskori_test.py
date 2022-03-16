import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito_tuote = Tuote("Maito", 3)
        self.kurkku_tuote = Tuote("Kurkku", 1)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito_tuote)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_oikea_maara_hinta(self):
        self.kori.lisaa_tuote(self.maito_tuote)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jälkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito_tuote)
        self.kori.lisaa_tuote(self.kurkku_tuote)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_sama_kuin_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(self.maito_tuote)
        self.kori.lisaa_tuote(self.kurkku_tuote)
        self.assertEqual(self.kori.hinta(), 4)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito_tuote)
        self.kori.lisaa_tuote(self.maito_tuote)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_sama_kaksi_kertaa_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito_tuote)
        self.kori.lisaa_tuote(self.maito_tuote)
        self.assertEqual(self.kori.hinta(), (self.maito_tuote.hinta()*2))

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito_tuote)
        ostokset = self.kori.ostokset()
        # testaa että metodin palauttaman listan pituus 1
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito_tuote)
        ostos = self.kori.ostokset()[0]
 
        # testaa täällä, että palautetun listan ensimmäinen ostos on halutunkaltainen.
        self.assertEqual(ostos.tuotteen_nimi(), self.maito_tuote.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    def kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisalta_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito_tuote)
        self.kori.lisaa_tuote(self.kurkku_tuote)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)