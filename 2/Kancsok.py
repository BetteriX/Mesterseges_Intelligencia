#!/usr/bin/env python3

from keres import *


class Kancsok(Feladat):
    def __init__(self, ke, c):
        self.kezdo = ke
        self.cél = c
        self.Max1 = 3
        self.Max2 = 5
        self.Max3 = 8

    def celteszt(self, a):  # a =(a1,a2,a3) állapot
        return a[0] == self.cél or a[1] == self.cél or a[2] == self.cél

    def rakovetkezo(self, a):  # a =(a1,a2,a3) állapot
        gyerekek = []
        a1, a2, a3 = a

        # tölt1,2 operátor alalmazási előfeltátel:
        if a1 != 0 and a2 != self.Max2:
            T = min(a1, self.Max2 - a2)
            gyerekek.append(("tölt 1-ből 2-be", (a1 - T, a2 + T, a3)))

        # tölt 1,3 operátor alalmazási előfeltátel:
        if a1 != 0 and a3 != self.Max3:
            T = min(a1, self.Max3 - a3)
            gyerekek.append(("tölt 1-ből 3-be", (a1 - T, a2, a3 + T)))

        # tölt 2,1 operátor alalmazási előfeltátel:
        if a2 != 0 and a1 != self.Max1:
            T = min(a2, self.Max1 - a1)
            gyerekek.append(("tölt 2-ből 1-be", (a1 + T, a2 - T, a3)))

        # tölt 2,3 operátor alalmazási előfeltátel:
        if a2 != 0 and a3 != self.Max3:
            T = min(a2, self.Max3 - a3)
            gyerekek.append(("tölt 2-ből 3-be", (a1, a2 - T, a3 + T)))

        # tölt 3,1 operátor alalmazási előfeltátel:
        if a3 != 0 and a1 != self.Max1:
            T = min(a3, self.Max1 - a1)
            gyerekek.append(("tölt 3-ből 1-be", (a1 + T, a2, a3 - T)))

        # tölt 3,2 operátor alalmazási előfeltátel:
        if a3 != 0 and a2 != self.Max2:
            T = min(a3, self.Max2 - a2)
            gyerekek.append(("tölt 3-ből 2-be", (a1, a2 + T, a3 - T)))

        return gyerekek


def heurisztika(csucs):
    a = csucs.allapot
    return min([abs(a[0] - 4), abs(a[1] - 4), abs(a[2] - 4)])


if __name__ == "__main__":
    feladat = Kancsok((0, 0, 8), 4)
    print("Szélessig fakereső")
    result1 = szelessegi_fakereso(feladat)
    print(result1.megoldas())
    utam = result1.ut()
    utam.reverse()
    print(utam)

    print("melysegi grafkereso")
    result2 = melysegi_fakereso(feladat)
    print(result2.megoldas())
    utam = result2.ut()
    utam.reverse()
    print(utam)

    print("best-first")
    result2 = best_first(feladat, heurisztika)
    print(result2.megoldas())
