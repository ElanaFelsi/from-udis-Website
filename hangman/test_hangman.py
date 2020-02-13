import unittest
from hangman import Hangman


class HangmanTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Hangman("hello", 10)
        self.game2 = Hangman("goodbye", 10)

    def test_status(self):
        self.assertEqual(self.game2.status(), "???????")

    def test_bad_guess(self):
        self.assertEqual(self.game.status(), "?????")
        self.assertEqual(self.game.guess('x'), 0)
        self.assertEqual(self.game.status(), "?????")

    def test_good_guess(self):
        self.assertEqual(self.game.status(), "?????")
        self.assertEqual(self.game.guess('h'), 1)
        self.assertEqual(self.game.status(), "h????")

    def test_multiple_guess(self):
        self.assertEqual(self.game2.status(), "???????")
        self.assertEqual(self.game2.guess('o'), 2)
        self.assertEqual(self.game2.status(), "?oo????")

    def test_more_letters(self):
        self.assertEqual(self.game.guess('h'), 1)
        self.assertEqual(self.game.status(), "h????")
        self.assertEqual(self.game.guess('i'), 0)
        self.assertEqual(self.game.status(), "?????")
        self.assertEqual(self.game.status(), "h????")
        self.assertEqual(self.game.guess('l'), 2)
        self.assertEqual(self.game.status(), "h?ll?")
        self.assertEqual(self.game.guess('e'), 1)
        self.assertEqual(self.game.status(), "hell?")


if __name__ == '__main__':
    unittest.main()