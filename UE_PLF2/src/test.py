class Test:
    def __init__(self, text):
        self._text = text

    # Getter
    @property
    def text(self):
        return self._text

    # Setter
    @text.setter
    def text(self, newText):
        self._text = newText

    def __str__(self):
        return f"{self.text}"


if __name__ == '__main__':
    t1 = Test("Hallo")
    t1.text = "Welt"
    print(t1)


import argparse
parser = argparse.ArgumentParser(description="Demo Argparser by WAL / HTL Rennweg")
args = parser.parse_args()