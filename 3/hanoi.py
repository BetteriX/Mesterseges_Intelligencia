#!/usr/bin/env python3

from keres import *


class Hanoi(Feladat):
    def __init__(self, kezdo: tuple, cel: tuple):
        self.kezdo = kezdo
        self.cel = cel
        self.N = len(kezdo)

    def celteszt(self, a: tuple):  # a=(a1, a2, ..., an)
        return a == self.cel

    def rakovetkezo(self, a: tuple):
        gyerekek = []

        for melyiket in range(0, self.N):
            for hova in ["P", "Q", "R"]:
                tmp = True  # feltételezem, hogy  alkalmazható
                if a[melyiket] != hova:
                    for i in range(0, melyiket):
                        if a[i] != a[melyiket] and a[i] != hova:
                            pass
                        else:
                            tmp = False
                            break
                else:
                    tmp = False

                if tmp:
                    gyerek_allapot = list(a)
                    gyerek_allapot[melyiket] = hova
                    gyerekek.append((f"{melyiket}-> {hova}", tuple(gyerek_allapot)))

        return gyerekek


def heurisztika(csucs):
    a = csucs.allapot
    n = len(a)  # korongok száma
    # megszámoljuk hánőy legnagyobb korong nincs még  a helyén:
    for i in range(len(a) - 1, -1, -1):
        if a[i] == "R":
            n = n - 1
        else:
            break

    return 2**n - 1


def main():
    feladat = Hanoi(("P", "P", "P", "P"), ("R", "R", "R", "R"))
    feladat2 = Hanoi(("P", "P", "P"), ("R", "R", "R"))

    result1 = szelessegi_grafkereso(feladat)
    print(result1.megoldas())
    ut = result1.ut()
    ut.reverse()
    print(ut)

    result2 = melysegi_grafkereso(feladat)
    print(result2.megoldas())
    ut = result2.ut()
    ut.reverse()
    print(ut)

    print("best-first")
    result3 = best_first(feladat, heurisztika)
    print(result3.megoldas())


if __name__ == "__main__":
    main()
