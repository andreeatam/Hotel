class Reservierung:
    def __init__(self,gaste,zimmer,anfangsdatum,enddatum):
        self.gaste=[gaste]
        self.zimmer=zimmer
        self.von=anfangsdatum
        self.bis=enddatum

    def addGuest(self, gast):
        self.gaste.append(gast)

    def __str__(self):
        if len(self.gaste)>1:
            text="Gaste: "
            for i in range(len(self.gaste)):
                 text+=f'{self.gaste[i]}, '
            text+= f'haben das Zimmer {self.zimmer}, von: {self.von.tm_mday}.{self.von.tm_mon}.{self.von.tm_year}, bis: {self.bis.tm_mday}.{self.bis.tm_mon}.{self.bis.tm_year}'
            return text
        return f'Gast {self.gaste[0]} hat das Zimmer {self.zimmer}, von: {self.von.tm_mday}.{self.von.tm_mon}.{self.von.tm_year}, bis: {self.bis.tm_mday}.{self.bis.tm_mon}.{self.bis.tm_year}'
