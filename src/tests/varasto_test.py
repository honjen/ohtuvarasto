import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    # uudet testit alla

    def test_lisays_yli_tilavuuden(self):
        # varastoon yritetään laittaa tavaraa enemmän kuin on tilaa
        self.varasto.lisaa_varastoon(13)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_ottaminen_yli_saldon(self):
        # yritetään ottaa enemmän kuin varastossa on tavaraa
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(7)
        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_konstruktori_negatiivinen_tilavuus(self):
        # annetaan varastolle negatiivinen tilavuus
        varasto = Varasto(-2)
        self.assertAlmostEqual(varasto.tilavuus, 0)
    
    def test_konstruktori_negatiivinen_alku_saldo(self):
        # annetaan varastolle negatiivinen alkusaldo
        varasto = Varasto(10, -3)
        self.assertAlmostEqual(varasto.saldo, 0)
    
    def test_lisays_negatiivinen_maara(self):
        # lisätään negatiivinen määrä
        self.varasto.lisaa_varastoon(-4)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_ottaminen_negatiivinen_maara(self):
        # yritetään ottaa negatiivinen määrä varastosta
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara, 0)
    
    def test_varaston_tulostus(self):
        # onko tulostus oikein?
        self.varasto.lisaa_varastoon(4)
        self.assertEqual(str(self.varasto), "saldo = 4, vielä tilaa 6")