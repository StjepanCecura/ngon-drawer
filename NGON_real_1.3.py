#importovi za program
import turtle
from turtle import *

# varijable za namjestanje mnogokuta
n = int(input("Broj kutova u N-kutu: "))
s = int(input("brzina crtanja: "))

# rjecnici za boje
boje_sve = {
    #kljucevi su redni brojevi
    1: "black",
    2: "red",
    3: "blue",
    4: "yellow",
    5: "custom"
}
#prazni rjecnik u koji se stavljaju boje koje se izaberu
boje_izabrane = {}

#petlja za biranje boja
#namjesta varijable i brojace
jos_boja = "nista"
e = 1
#pocetak petlje
while jos_boja != "ne":
    #printa citav rjecnik svih boja
    print(boje_sve)
    #trazi unos rednog broja boje
    d = int(input("Redni broj boje:"))
    #provjera je li trazi unijet custom boju ili neku koja vec postoji u rjecniku
    #ako ne trazi custom boju, logicno trazi neku koja vec postoji
    if d != 5:
        #kopira izabranu boju u rjecnik
        boje_izabrane[e] = boje_sve[d]
    elif d == 5:
        #trazi unos custom boje
        boje_izabrane[e] = input("Unesi boju:")
    #povecava brojac
    e = e + 1
    #pita zelis li jos boja birati
    jos_boja = input("Jos boja? ukucaj ne ako ne:")

# namjesta velicinu onog prozora i brzinu kojom crta
screensize(750, 750, "white")
speed(s)

# penup podize olovku da ne crta dok se pomjera
penup()
# postavljam na poziciju prvog kuta
setpos(0, -260)
# okrecem olovku da krece u smjeru kazaljke na satu
# da, smeta mi ako ide suprotno i to je moj problem
right(180)

# pravi rjecnike i brojace koje namjesta na 1
xkord = {}
ykord = {}
a = 1
b = 1
c = 1
f = 1
#racuna kut i duzinu ruba da ih ne racuna svaki put kad je potrebno
kut = 360 / n
rub = 1800 / n

# petlja koja popisuje kutove
while a <= n:
    # namjesta mis na poziciju sljedeceg kuta
    right(kut)
    #pomjera ga do sljedeceg kuta
    forward(rub)
    # zapisuje njegove koordinate u rjecnike
    xkord[a] = xcor()
    ykord[a] = ycor()
    # brojac za petlju a
    a = a + 1

# petlja sa b pomjera mis na poziciju kuta
while b <= n:
    # postavlja koordinate koje se koriste u petlji c
    x = xkord[b]
    y = ykord[b]
    # postavlja mis na koordinate kuta
    setpos(xkord[b], ykord[b])
    # petlja s brojacem c povlaci crte
    while c <= n:
        # spusta olovku
        pendown()
        # mijenja boju crte kroz rjecnik u kojem su izabrane boje
        pencolor(boje_izabrane[f])
        # pomjera olovku na koordinate kuta do kojeg povlaci crtu
        setpos(xkord[c], ykord[c])
        # podize olovku
        penup()
        # vraca mis na koordinate kuta iz kojeg se povlace crte
        setpos(x, y)
        # brojac za petlju c
        c = c + 1
        # brojac da šalta kroz boje
        f = f + 1
        #provjera da ako je doslo do zadnje izabrane boje, vrati na prvu
        if f == e:
            f = 1
    # brojac za petlju b
    b = b + 1
    # resetira brojac za petlju c
    c = b

turtle.exitonclick()
