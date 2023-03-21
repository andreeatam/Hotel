from Domain.gast import Gast
from Domain.zimmer import Zimmer
from Domain.reservierung import Reservierung
import time, datetime
import pickle
from errors import handling


class GasteMenu():
    def __init__(self,gaste):
        self.gaste=gaste

    def add_gast(self,neu_gast):
        self.gaste.append(neu_gast)

    def update_gast(self,alt_nachname,neu_nachname):
        ok=0
        for i in range(len(self.gaste)):
            if self.gaste[i].nachname==alt_nachname:
                self.gaste[i].nachname=neu_nachname
                ok=1
        if ok==0:
            handling("NoGuest")

    def delete_gast(self,nume_fam):
        ok=0
        for i, var in enumerate(self.gaste):
            if var.nachname==nume_fam:
                self.gaste.pop(i)
                ok=1
        if ok==0:
            handling("NoGuest")

    def print_all_gaste(self):
        for guest in self.gaste:
            print (f'{guest.vorname} {guest.nachname}')

    def find(self, a):
        ok = 0
        for i, var in enumerate(self.gaste):
            if var.vorname == a.vorname and var.nachname == a.nachname:
                return self.gaste[i]
        if ok == 0:
            raise ValueError("Guest not in list")

    def correctName(self, a, b):
        ok = 0
        for i, var in enumerate(self.gaste):
            if var.vorname == a.vorname and var.nachname == a.nachname:
                var.nachname = b.nachname
                ok = 1
        if ok == 0:
            handling("NoGuest")

    def run1(self):
        """
            Sub-meniu "general" ce gestioneaza toate optiunile pt meniul general GasteMenu
            :return:
        """
        print("""
        1.Fuge ein neuer Gast hin
        2.Aktualisierung der Nachname eines Gastes
        3.Loschung eines Gastes
        4.Anzeige die Liste von Gasten
        5.Exit
        """)

        nr=int(input("Gebe eine Option: "))

        if nr==1:
            vorname=input("vorname: ")
            nachname=input("nachname: ")
            new_gast=Gast(vorname,nachname)
            self.add_gast(new_gast)

        if nr==2:
            old_nachname=input("nachname: ")
            new_nachname=input("neu_nachname: ")
            self.update_gast(old_nachname,new_nachname)

        if nr==3:
            nachname=input("nachname: ")
            self.delete_gast(nachname)

        if nr==4:
            self.print_all_gaste()

        if nr==5:
            exit()


class ZimmernMenu():
    def __init__(self,zimmern,gaste):
        self.zimmern=zimmern
        self.gaste=gaste

    def add_zimmer(self,neu_zimmer):
        self.zimmern.append(neu_zimmer)

    def update_preis(self,zimmer_nummer,neu_preis):
        ok=0
        for i in range(len(self.zimmern)):
            if self.zimmern[i].nummer== zimmer_nummer:
                self.zimmern[i].preis=neu_preis
                ok=1
        if ok==0:
            handling("NoRoom")

    # def delete_zimmer(self,zimmer_nummer): #metoda 1
    #     for i, var in enumerate(self.zimmern):
    #         if var.nummer==zimmer_nummer:
    #             self.zimmern.pop(i)

    def delete_zimmer(self,zimmer_nummer): #metoda 2
        ok=0
        l = len(self.zimmern)
        for i in range(l):
            if i < l:
                if self.zimmern[i].nummer==zimmer_nummer:
                    self.zimmern.pop(i)
                    l-=1
                    ok=1
        if ok==0:
            handling("NoRoom")

    def print_all_zimmern(self):
        for zimmer in self.zimmern:
            print(f'Das Zimmer hat das Nummer {zimmer.nummer}, hat {zimmer.maxGast} max Gaste, ist {zimmer.preis} Euro, ist {zimmer.farbe} als Farbe, Meerblick={zimmer.meerblick}')

    def giveRoomNumList(self):
        l = []
        for i, ar in enumerate(self.zimmern):
            l.append(ar.nummer)
        return l

    def findRoom(self, num):
        for i, ar in enumerate(self.zimmern):
            if ar.nummer == num:
                return self.zimmern[i]
        raise ValueError("Room not in list")

    def run2(self):
        """
            Sub-meniu "general" ce gestioneaza toate optiunile pt meniul general ZimmernMenu
            :return:
        """
        print("""
        1.Fuge ein Zimmer hin
        2.Aktualisierung des Preises eines Zimmers
        3.Loschung eines Zimmers
        4.Anzeige die Liste von Zimmern
        5.Exit
        """)

        nr = int(input("Gebe eine Option: "))

        if nr==1:
            nummer=input("nummer: ")
            maxGast = input("maxGast: ")
            preis = input("preis: ")
            farbe = input("farbe: ")
            meerblick = input("meerblick(True/False): ")
            new_zimmer=Zimmer(nummer,maxGast,preis,farbe,meerblick)
            self.add_zimmer(new_zimmer)

        if nr==2:
            zimmer_nummer=input("nummer: ")
            new_preis=input("neu_preis: ")
            self.update_preis(zimmer_nummer,new_preis)

        if nr==3:
            zimmer_nummer=input("nummer: ")
            self.delete_zimmer(zimmer_nummer)

        if nr==4:
            self.print_all_zimmern()

        if nr==5:
            exit()

class OtherMenu():
    def __init__(self, gaste, zimmern,reservations):
        self.gaste=gaste
        self.zimmern=zimmern
        self.reservations=reservations

    def find(self, a):
        ok = 0
        for i, var in enumerate(self.gaste):
            if var.vorname == a.vorname and var.nachname == a.nachname:
                return self.gaste[i]
        if ok == 0:
            raise ValueError("Guest not in list")

    def findRoom(self, a):
        ok = 0
        for i, var in enumerate(self.zimmern):
            if var.nummer == a:
                return self.zimmern[i]
        if ok == 0:
            raise ValueError("Room not in list")

    def giveRoomNumList(self):
        l = []
        for i, ar in enumerate(self.zimmern):
            l.append(ar.nummer)
        return l

    def add_gastToList(self,vorname,nachname):
        """
            cauta si returneaza un oaspete specific
            :param vorname: prenumele oaspetelui cautat
            :param nachname: numele oaspetelui cautat
            :return: oaspetele a carui nume a fost cautat
        """
        gast=self.find(Gast(vorname,nachname))
        return gast

    def convertTime(self,tdate):
        """
            :param tdate: data formatului "dd.mm.yyyy"
            :return: data formatului struct_time
        """
        tdate=tdate.split(".")
        for i,ar in enumerate(tdate):
            tdate[i]=int(ar)
        tdate[1]=self.getMonth(tdate[1])
        converted=time.strptime(f'{tdate[0]} {tdate[1]} {tdate[2]}',"%d %b %Y") #strptime converteste un string la un date time obj
        return converted

    def getMonth(self,month):
        """
            converteste luna anului in nume scurt
            :param month: luna [intre 1 si 12]
            :return: numele scurt al lunii
        """
        if month==1:
            return "Jan"
        if month == 2:
            return "Feb"
        if month == 3:
            return "Mar"
        if month == 4:
            return "Apr"
        if month == 5:
            return "May"
        if month == 6:
            return "Jun"
        if month == 7:
            return "Jul"
        if month == 8:
            return "Aug"
        if month == 9:
            return "Sep"
        if month == 10:
            return "Oct"
        if month == 11:
            return "Nov"
        if month == 12:
            return "Dec"

    def checkEmpty(self,zimmer,von,bis,reservations):
        """
           verifica daca o camera este libera intre datele introduse
           :param zimmer: nr camerei
           :param von: date de la care ar trebui sa fie libera, struct_time
           :param bis: data pana cand ar trebui sa fie libera, struct_time
           :param reservations: lista de rezervari
           :return: bool: starea camerei: libera/ocupata
        """
        for i,ar in enumerate(reservations):
            if ar.zimmer==zimmer:
                return self.cmpDate(ar,von,bis)
        return True

    def cmpDate(self,reser,von,bis):
        """
            verifica daca datele noi exista sau se suprapun
            :param reser: obiectul clasei de rezervare
            :param von: data de inceput a noii rezervari
            :param bis: date de final a noii rezervari
            :return: data este/nu este in intervalul de rezervari existente
        """
        if reser.von <=von <reser.bis:
            return False
        if reser.von <bis <=reser.bis:
            return False
        return True

    def findRoomCapacit(self,zimmer):
        """
           cauta o camera specifica si returneaza nr maxim de oaspeti
           :param zimmer: nr camerei a carei nr max de oaspeti dorim sa-l aflam
           :return: nr maxim de oaspeti
        """
        room=self.findRoom(zimmer)
        return int(room.maxGast)

    def convertToday(self):
        """
           :return: ziua curenta ca struct_time
        """
        date=datetime.datetime.now()
        day=date.strftime("%d")
        month=date.strftime("%m")
        year=date.strftime("%Y")
        return self.convertTime(f'{day}.{month}.{year}')

    def filterRooms(self, price, meer):
        # neu_liste = sorted(self.zimmern, key= lambda room: room.preis)
        neu_liste = list(filter(lambda room: int(room.preis) <= int(price), self.zimmern))
        if meer != "unwichtig" or meer == "True":
            neu_liste = list(filter(lambda room: room.meerblick == meer, neu_liste))
        for i in neu_liste:
            print( f'Zimmer {i.nummer} hat {i.maxGast} max Gaste, ist {i.preis} Euro , ist {i.farbe} als Farbe, Meeresblick: {i.meerblick}, Verfügbar: {i.verfugbar}')


    def run3(self):
        """
            Sub-meniu "general" ce gestioneaza toate optiunile pt meniul general OtherMenu
            :return:
        """
        print("""
        1.Mach eine Reservierung
        2.Anzeige die Liste von Gasten, die aktuelle Reservierungen haben
        3.Anzeige die Zimmern mit einigen Kriterien
        4.Anzeige alle Zimmer, die heute frei sind
        5.Exit
        """)

        nr = int(input("Gebe eine Option: "))

        if nr==1:
            vorname = input("vorname: ")
            nachname = input("nachname: ")
            gast = Gast(vorname, nachname)
            self.add_gastToList(vorname, nachname)
            zimmer=input("zimmer: ")
            von = self.convertTime(input("von: "))
            bis = self.convertTime(input("bis: "))
            if self.checkEmpty(zimmer,von,bis,self.reservations):
                self.reservations.append(Reservierung(gast,zimmer,von,bis))
                nrGast=1
                rooms=self.giveRoomNumList()
                for i in rooms:
                    if self.checkEmpty(i,self.convertToday(),self.convertToday(),self.reservations):
                        self.findRoom(i).setDisponib(False)
                while nrGast<self.findRoomCapacit(zimmer):
                    print("Wollen Sie noch ein Gast einfugen? (ja/nein): ")
                    if input()=="ja":
                        vorr=input("Vorname: ")
                        nachh= input("Nachname: ")
                        self.reservations[len(self.reservations)-1].addGuest(self.add_gastToList(vorr, nachh))
                        nrGast+=1
                    break
            else:
                print("Zimmer ist im Zeitraum besetzt!")

        if nr==2:
            heute=self.convertToday()
            for i in self.reservations:
                if i.bis > heute:
                    print(i)

        if nr == 3:
            preis_filtrat = input("Zimmer billiger als: ")
            meersblick = input("Meersblick? (True/False): ")
            self.filterRooms(preis_filtrat, meersblick)

        if nr == 4:
            rooms = self.giveRoomNumList()
            for i in rooms:
                if self.checkEmpty(i, self.convertToday(), self.convertToday(), self.reservations):
                    print(self.findRoom(i))
            rooms=self.giveRoomNumList()
            for i in rooms:
                if self.checkEmpty(i, self.convertToday(), self.convertToday(), self.reservations):
                    self.findRoom(i).setDisponib(True)
                else:
                    self.findRoom(i).setDisponib(False)
            pickle.dump(self.gaste, open("gasteliste.txt", 'wb'))
            pickle.dump(self.zimmern, open("zimmernliste.txt.txt", 'wb'))
            pickle.dump(self.reservations, open("reservationsliste.txt.txt", 'wb'))

        if nr==5:
            exit()





