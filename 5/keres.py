import sys
from seged import *


class Feladat:
    def __init__(self, kezdo, cel=None):
        self.kezdo = kezdo
        self.cel = cel

    def rakovetkezo(self, allapot):
        raise NotImplementedError

    def ertek(self):
        raise NotImplementedError

    def celteszt(self, allapot):
        # return allapot == self.cel
        raise NotImplementedError

    def utkoltseg(self, c, allapot1, lepes, allapot2):
        return c + 1


class Csucs:
    def __init__(self, allapot, szulo=None, lepes=None, utkoltseg=0):
        self.allapot = allapot
        self.szulo = szulo
        self.lepes = lepes
        self.utkoltseg = utkoltseg
        if szulo:
            self.melyseg = szulo.melyseg + 1
        else:
            self.melyseg = 0

    def __repr__(self):
        return "<Csúcs: %s>" % (self.allapot,)

        # return "%s" % (list(self.allapot),)

    def ut(self):
        x, valasz = self, [self]
        while x.szulo:
            valasz.append(x.szulo)
            x = x.szulo
        return valasz

    def megoldas(self):
        utam = self.ut()
        utam.reverse()
        return [csucs.lepes for csucs in utam[1:]]

    def kiterjeszt(self, feladat):
        for muvelet, kovetkezo in feladat.rakovetkezo(self.allapot):
            if kovetkezo not in [csucs.allapot for csucs in self.ut()]:
                yield Csucs(
                    kovetkezo,
                    self,
                    muvelet,
                    feladat.utkoltseg(self.utkoltseg, self.allapot, muvelet, kovetkezo),
                )
