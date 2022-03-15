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