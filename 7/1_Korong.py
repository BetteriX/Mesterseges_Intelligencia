from keres import *


class Korong(Feladat):
    def __init__(self, kezdő, cél):
        self.kezdő = kezdő
        self.cél = cél

    def célteszt(self, állapot):
        return állapot == self.cél

    def rákövetkező(self, állapot):

        utodok = []
        n = len(állapot)
        for i in range(2, n + 1):
            uj_allapot = állapot[:i][::-1] + állapot[i:]

            utodok.append((f"rak({i})", uj_allapot))

        return utodok

    def heurisztika(self, csúcs):

        állapot = csúcs.állapot

        res_db = 0
        n = len(állapot)

        for i in range(1, n):
            kulonbseg = abs(állapot[i] - állapot[i - 1])
            if kulonbseg != 1:
                res_db += 1

        if állapot[-1] != self.cél[-1]:
            res_db += 1

        return res_db


if __name__ == "__main__":
    kezdo = (6, 7, 3, 2, 8, 5, 4, 1)
    cel = (1, 2, 3, 4, 5, 6, 7, 8)

    feladat = Korong(kezdo, cel)

    print("Szélességi gráfkereső: ")
    result1 = szélességi_gráfkereső(feladat)
    print(result1.megoldás())
    ut = result1.út()
    ut.reverse()
    print(ut)

    result2 = a_csillag(feladat, feladat.heurisztika)
    print("A csillag: ")
    print(result2.megoldás())
    ut = result2.út()
    ut.reverse()
    print(ut)
