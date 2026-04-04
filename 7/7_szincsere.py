from keres import *

# Mezők indexei:
# A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7, I=8, J=9
# Szomszédossági lista
SZOMSZEDOK = {
    0: [1],  # A: B
    1: [0, 2, 3],  # B: A, C, D
    2: [1],  # C: B
    3: [1, 4],  # D: B, E
    4: [3, 5, 6],  # E: D, F, G
    5: [4],  # F: E
    6: [4, 8],  # G: E, I
    7: [8],  # H: I
    8: [6, 7, 9],  # I: G, H, J
    9: [8],  # J: I
}


class SzinCsere(Feladat):
    def __init__(self, kezdo, cel):
        self.kezdo = kezdo
        self.cel = cel

    def celteszt(self, allapot):
        return allapot == self.cel

    def rakovetkezo(self, allapot):
        for i, c in enumerate(allapot):
            if c in ["G", "R"]:
                for j in SZOMSZEDOK[i]:
                    if allapot[j] == "0":
                        uj = list(allapot)
                        uj[j] = c
                        uj[i] = "0"

                        # print(f"{i}->{j}")
                        yield (f"{i}->{j}", tuple(uj))


def heurisztika(csucs):
    allapot = csucs.allapot
    osszeg = 0
    for i in range(10):
        if allapot[i] == "G":
            osszeg += abs(i - 8)
        elif allapot[i] == "R":
            osszeg += abs(i - 1)
    return osszeg


def main():
    kezdo = ("G", "G", "G", "0", "0", "0", "0", "R", "R", "R")
    cel = ("R", "R", "R", "0", "0", "0", "0", "G", "G", "G")

    feladat = SzinCsere(kezdo, cel)

    """ Ki kelett kommentelni hogy münködjön
    else:
        perem.extend(csucs.kiterjeszt(feladat))
    """

    print("Szelessegi grafkereso")
    result1 = szelessegi_grafkereso(feladat)
    print(result1.megoldas())
    print("Lépések száma:", len(result1.megoldas()))

    print("Melysegi grafkereso")
    result2 = melysegi_grafkereso(feladat)
    print(result2.megoldas())
    print("Lépések száma:", len(result2.megoldas()))

    print("A csillag")
    result3 = a_csillag(feladat, heurisztika)
    print(result3.megoldas())
    print("Lépések száma:", len(result3.megoldas()))


if __name__ == "__main__":
    main()
