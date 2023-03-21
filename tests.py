from Domain.gast import Gast
from Domain.zimmer import Zimmer
from Domain.reservierung import Reservierung
from Menus import GasteMenu,ZimmernMenu,OtherMenu


def tests():
    TSTaddGuest()
    TSTupdateGast()
    TSTdeleteGuest()
    TSTaddRoom()
    TSTupdatePrice()
    TSTdeleteRoom()
    TSTfilterRooms()
    TSTcheckEmpty()

def TSTaddGuest():
    l=[]
    a=GasteMenu(l)
    a.add_gast(Gast("iulia","pop"))
    assert len(a.gaste)==1
    assert a.gaste[0].vorname=="iulia"
    assert a.gaste[0].nachname == "pop"
   # assert g.vorname=="iulia" and g.nachname=="pop"


def TSTupdateGast():
    l=[]
    a=GasteMenu(l)
    a.add_gast(Gast("alex","popescu"))
    a.update_gast("popescu","rus")
    o=a.find(Gast("alex","rus"))
    nume="rus"
    assert o.nachname == nume


def TSTdeleteGuest():
    l = []
    c = GasteMenu(l)
    c.add_gast(Gast("iulia", "pop"))
    c.delete_gast(Gast("iulia", "pop"))
    assert len(l) == 0

    # try:
    #     c.find(Gast("iulia","pop"))
    # except:
    #     return 0
    # raise ValueError("Delete Guest Test Failed!")

def TSTaddRoom():
    l=[]
    m=[]
    a=ZimmernMenu(l,m)
    a.add_zimmer(Zimmer("1",2,120,"red",True))
    assert len(a.zimmern)==1
    assert a.zimmern[0].nummer =="1"
    assert a.zimmern[0].maxGast == 2
    assert a.zimmern[0].preis == 120
    assert a.zimmern[0].farbe == "red"
    assert a.zimmern[0].meerblick == True

def TSTupdatePrice():
    l=[]
    m=[]
    b=ZimmernMenu(l,m)
    b.add_zimmer(Zimmer("1",1,80,"rot",True))
    b.update_preis("1",150)
    o=b.findRoom("1")
    var=150
    assert o.preis ==var

    # if o.preis!= 150:
        # raise ValueError("Correct Price Test Failed")


def TSTdeleteRoom():
    l=[]
    m=[]
    b=ZimmernMenu(l,m)
    b.add_zimmer(Zimmer("1",1,80,"rot",True))
    b.add_zimmer(Zimmer("2", 2, 180, "green", True))
    b.delete_zimmer("2")
    assert len(l)==1
    assert b.zimmern[0].nummer=="1"
    assert b.zimmern[0].maxGast==1
    assert b.zimmern[0].preis == 80
    assert b.zimmern[0].farbe == "rot"
    assert b.zimmern[0].meerblick == True


def TSTfilterRooms():
    l=[]
    m=[]
    n=[]
    b=ZimmernMenu(m,l)
    b.add_zimmer(Zimmer("1",1,30,"blau",True))
    b.add_zimmer(Zimmer("2", 1,130, "blau", True))
    b.add_zimmer(Zimmer("3", 1, 60, "blau", False))
    b.add_zimmer(Zimmer("4", 1, 110, "blau", False))
    a=OtherMenu(l,m,n)

    # if a.filterRooms(100,False)!=Zimmer("3", 1, 60, "blau", False):
    #     raise ValueError("Filter Rooms Test Failed")

    #neu_liste = list(filter(lambda room: int(room.preis) <= int(b.price),b.zimmern))

    expected_liste=[b.zimmern[2]]
    assert a.filterRooms(100,False) == expected_liste

def TSTcheckEmpty():
    l=[]
    m=[]
    n=[]
    a=OtherMenu(l,m,n)
    res=[Reservierung(Gast("iulia","pop"),"1",a.convertTime("01.01.2010"),a.convertTime("10.01.2010"))]
    assert a.checkEmpty("1",a.convertTime("02.01.2010"),a.convertTime("10.01.2010"),res) == False


TSTaddGuest()
TSTupdateGast()
TSTaddRoom()
TSTupdatePrice()
TSTdeleteRoom()
TSTcheckEmpty()

