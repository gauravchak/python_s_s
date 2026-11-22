import random


class Sim:

    def __init__(self, word: str, num_allowed_mistakes: int) -> None:
        self.guessed = set()
        self.missed = set()
        self.word = word
        self.chars_to_guess = len(set(word))
        self.num_allowed_mistakes = num_allowed_mistakes

    def play(self):
        on = True
        while on:
            ch = input("Guess: ")
            ch = ch.strip().split()[0]
            if ch in self.missed:
                print(f"{ch} is a failed guess already.")
                continue
            if ch in self.guessed:
                print(f"{ch} you have guessed correctly already.")
                continue
            if ch in self.word:
                self.guessed.add(ch)
            else:
                self.missed.add(ch)
            if len(self.guessed) == self.chars_to_guess:
                print(f"You have guessed {self.word} correctly.")
                on = False
            if len(self.missed) == self.num_allowed_mistakes:
                print(f"Game ended. Word was {self.word}.")
                on = False
            partial = []
            for wch in self.word:
                if wch in self.guessed:
                    partial.append(wch)
                else:
                    partial.append("_")
            print("".join(partial))


def __main__():
    dictionary = "/Users/gchak/code/adversarial_word_guessing/words.txt"
    len2words = {}
    len2charcount = {}
    with open(dictionary, "r") as f:
        for line in f:
            if not line or len(line) < 1:
                continue
            word = line.strip().split()[0]
            word = word.lower()
            wordlen = len(word)
            if wordlen < 1 or not word.isalpha():
                continue
            if wordlen not in len2charcount:
                len2charcount[wordlen] = {}
            for ch in set(word):
                len2charcount[wordlen][ch] = (
                    len2charcount[wordlen].get(ch, 0) + 1
                )
            if wordlen not in len2words:
                len2words[wordlen] = []
            len2words[wordlen].append(word)
    word = ""
    while not word:
        wordlen = int(input("Enter the length of the word: "))
        if wordlen not in len2words:
            print(f"No word of length {wordlen}")
        wordcount = len(len2words[wordlen])
        wordidx = random.randint(0, wordcount - 1)
        word = len2words[wordlen][wordidx]
    num_allowed_mistakes = int(
        input("Enter num allowed mistakes [10]: ") or "10"
    )
    sim = Sim(word, num_allowed_mistakes)
    sim.play()


__main__()
