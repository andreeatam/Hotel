class Gast:
    def __init__ (self,vorname,nachname):
        self.vorname=vorname
        self.nachname=nachname

    def __str__(self):
        return f'{self.vorname} {self.nachname}'