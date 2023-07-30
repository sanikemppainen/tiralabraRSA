from alkuluvut import loytaa_alkuluvut_erasthoteen_seulalla, tarkistaa_alkuluvut_miller_rabin_algoritmilla
import unittest


class TestAlkuluvut(unittest.TestCase):
    
    def test_ei_loyda_alkuluvuista_erasthotheen_seulalla_1(self):
        self.assertNotIn(1, loytaa_alkuluvut_erasthoteen_seulalla(10))
    
    def test_ei_loyda_alkuluvuista_erasthotheen_seulalla_0(self):
        self.assertNotIn(0, loytaa_alkuluvut_erasthoteen_seulalla(10))

    def test_ei_loyda_alkulukuja_jos_n_ei_sisalla_niita(self):
        self.assertEqual(loytaa_alkuluvut_erasthoteen_seulalla(1), [])

    def test_loytaa_alkuluvut_erasthoteen_seulalla(self):
        self.assertEqual(loytaa_alkuluvut_erasthoteen_seulalla(10), [2, 3, 5, 7])

    def test_tarkistaa_alkuluvut_miller_rabin_algoritmilla_ei_alkuluvuilla(self):
        self.assertEqual(tarkistaa_alkuluvut_miller_rabin_algoritmilla([4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20], 5), [])

    def test_tyhja_lista_tyhjalla_inputilla(self):
        self.assertEqual(tarkistaa_alkuluvut_miller_rabin_algoritmilla([], 10), [])

    def test_ei_palauta_1(self):
        self.assertEqual(tarkistaa_alkuluvut_miller_rabin_algoritmilla([1], 5), [])

if __name__ == "__main__":
    unittest.main()
