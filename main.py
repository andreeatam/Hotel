import pickle
from Menus import GasteMenu,ZimmernMenu,OtherMenu
from tests import tests

class App:

    def __init__(self):
        self.gaste=[]
        self.zimmern=[]
        self.reservations=[]
        self.load_data()
        self.gasteMenu=GasteMenu(self.gaste)
        self.zimmernMenu=ZimmernMenu(self.zimmern,self.gaste)
        self.otherMenu=OtherMenu(self.gaste,self.zimmern,self.reservations)

    @staticmethod
    def print_main_menus():
        print("""
        1.GasteMenu
        2.ZimmernMenu
        3.OtherMenu
        4.Exit
        """)

    def run(self):
        """
            E meniul principal ce deschide aplicatia, incarca datele si controleaza ce sub-meniu trebuie deschis
            :return:
        """
        while True:
            self.print_main_menus()

            nr=int(input("Gebe eine Zahl: "))

            if nr==1:
                self.gasteMenu.run1()
            if nr==2:
                self.zimmernMenu.run2()
            if nr==3:
                self.otherMenu.run3()
            if nr==4:
                exit()

            self.write_data()

    def load_data(self):
        try:
            with open("gasteliste.txt", 'rb') as f:
                self.gaste = pickle.load(f)
        except:
            self.gaste=[]

        try:
            with open("zimmernliste.txt", 'rb') as f:
                self.zimmern = pickle.load(f)
        except:
            self.zimmern=[]

        try:
            with open("reservationsliste.txt", 'rb') as f:
                self.reservations = pickle.load(f)
        except:
            self.reservations = []

    def write_data(self):
        with open("gasteliste.txt",'wb') as f:
            pickle.dump(self.gaste, f)

        with open("zimmernliste.txt",'wb') as f:
            pickle.dump(self.zimmern, f)

        with open("reservationsliste.txt",'wb') as f:
            pickle.dump(self.reservations, f)
#tests()
app=App()
app.run()




