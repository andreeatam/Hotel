class Zimmer:
    def __init__(self,nummer,maxGast,preis,farbe,meerblick=False):
        self.nummer=nummer
        self.maxGast=maxGast
        self.preis=preis
        self.farbe=farbe
        self.meerblick=meerblick
        self.verfugbar=True

    def setDisponib(self,neu):
        self.verfugbar=neu

    def __str__(self):
        return f'Das Zimmer {self.nummer}, mit {self.maxGast} max Gaste, mit {self.preis} Euro, {self.farbe} als Farbe, mit Meerblick={self.meerblick} und Verfugbar={self.verfugbar} '