class Hangman(object):
    def __init__(self, word, tries):
        self.word = word
        self.tries_left = tries
        self.my_guess = list("?" * len(word))

    def status(self):
        return ''.join(self.my_guess)

    def guess(self, g: str):
        self.tries_left -= 1
        ind = [c for c, ltr in enumerate(self.word) if ltr == g]
        for i in ind:
            self.my_guess[i] = g
        num = self.word.count(g)
        if num == 0:
            self.tries_left -= 1
        return num


class GameOver(Exception):
    def __init__(self, word):
        # Call the base class constructor with the parameters it needs
        super().__init__('The word was "{}"'.format(word))
        self.word = word


raise GameOver('Hello')