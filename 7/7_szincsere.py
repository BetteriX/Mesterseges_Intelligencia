from keres import *

# Mezők indexei:
# A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7, I=8, J=9
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
    def __init__(self, kezdő, cél):
        self.kezdő = kezdő
        self.cél = cél

    def célteszt(self, állapot):
        return állapot == self.cél

    def rákövetkező(self, állapot):
        for i, c in enumerate(állapot):
            if c in ["G", "R"]:
                for j in SZOMSZEDOK[i]:
                    if állapot[j] == "0":
                        uj = list(állapot)
                        uj[j] = c
                        uj[i] = "0"

                        yield (f"{i}->{j}", tuple(uj))


def heurisztika(csucs):
    állapot = csucs.állapot
    osszeg = 0
    for i in range(10):
        if állapot[i] == "G":
            osszeg += abs(i - 8)
        elif állapot[i] == "R":
            osszeg += abs(i - 1)
    return osszeg


def main():
    kezdo = ("G", "G", "G", "0", "0", "0", "0", "R", "R", "R")
    cel = ("R", "R", "R", "0", "0", "0", "0", "G", "G", "G")

    feladat = SzinCsere(kezdo, cel)

    print("Szelessegi grafkereso")
    result1 = szélességi_gráfkereső(feladat)
    print(result1.megoldás())
    print("Lépések száma:", len(result1.megoldás()))

    print("Melysegi grafkereso")
    result2 = mélységi_gráfkereső(feladat)
    print(result2.megoldás())
    print("Lépések száma:", len(result2.megoldás()))

    print("A csillag")
    result3 = a_csillag(feladat, heurisztika)
    print(result3.megoldás())
    print("Lépések száma:", len(result3.megoldás()))

    print("Best-first")
    result4 = best_first(feladat, heurisztika)
    print(result4.megoldás())
    print("Lépések száma:", len(result4.megoldás()))


if __name__ == "__main__":
    main()
