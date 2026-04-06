#!/usr/bin/env python3

from keres import *


class TablaKorongok(Feladat):
    def __init__(self, ke, c):
        self.kezdő = ke
        self.cél = c

    def rákövetkező(self, állapot):
        tabla = állapot
        n_sor = m_oszlop = len(tabla)

        s, o = -1, -1
        u_van = False
        for i in range(n_sor):
            for j in range(m_oszlop):
                if tabla[i][j] == "u":
                    s, o = i, j
                    u_van = True
                    break
            if u_van:
                break

        lépések = [
            (-1, 0, "k", "le"),
            (0, -1, "k", "jobbra"),
            (-2, 0, "k", "le ugrással"),
            (0, -2, "k", "jobbra ugrással"),
            (1, 0, "p", "fel"),
            (0, 1, "p", "balra"),
            (2, 0, "p", "fel ugrással"),
            (0, 2, "p", "balra ugrással"),
        ]

        for ls, lo, ltipus, lirany in lépések:
            s_honnan, o_honnan = s + ls, o + lo

            if 0 <= s_honnan < n_sor and 0 <= o_honnan < m_oszlop:
                if tabla[s_honnan][o_honnan] == ltipus:
                    if abs(ls) == 2 or abs(lo) == 2:
                        s_ugrot, o_ugrot = s + ls // 2, o + lo // 2
                        atugrot = tabla[s_ugrot][o_ugrot]

                        if atugrot == "u" or atugrot == ltipus:
                            continue

                    uj = [list(t) for t in tabla]
                    uj[s_honnan][o_honnan] = "u"
                    uj[s][o] = ltipus
                    muvelet = f"{s_honnan},{o_honnan}:{s},{o} {ltipus} {lirany}"
                    yield muvelet, tuple(tuple(t) for t in uj)

    def célteszt(self, állapot):
        return állapot == self.cél


def heurisztika(csúcs):
    aktuális = csúcs.állapot
    cél = feladat.cél
    hiba = 0
    for s in range(len(aktuális)):
        for o in range(len(aktuális)):
            if aktuális[s][o] != "u" and aktuális[s][o] != cél[s][o]:
                hiba += 1

    return hiba


if __name__ == "__main__":
    kezdő = (
        ("k", "k", "k", "p", "p"),
        ("k", "k", "k", "p", "p"),
        ("k", "k", "u", "p", "p"),
        ("k", "k", "p", "p", "p"),
        ("k", "k", "p", "p", "p"),
    )

    cél = (
        ("p", "p", "p", "k", "k"),
        ("p", "p", "p", "k", "k"),
        ("p", "p", "u", "k", "k"),
        ("p", "p", "k", "k", "k"),
        ("p", "p", "k", "k", "k"),
    )

    feladat = TablaKorongok(kezdő, cél)

    # print('Szélességi gráfkereső')
    # result1 = szélességi_gráfkereső(feladat)
    # print(result1.megoldás())
    # print('Szélességi fakereső')
    # result2 = szélességi_fakereső(feladat)
    # print(result2.megoldás())
    print("Mélységi gráfkereső")
    result3 = mélységi_gráfkereső(feladat)
    print(result3.megoldás())
    print("Mélységi fakereső")
    result4 = mélységi_fakereső(feladat)
    print(result4.megoldás())

    print("Best First")
    result5 = best_first(feladat, heurisztika)
    print(result5.megoldás())
    print("A Csillag")
    result6 = a_csillag(feladat, heurisztika)
    print(result6.megoldás())
