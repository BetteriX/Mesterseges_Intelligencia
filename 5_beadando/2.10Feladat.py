#!/usr/bin/env python3

from my_jatek import *


class KorongJatek(Jatek):
    def __init__(self):
        osszes_mezo = {(sor, oszlop) for sor in range(1, 6) for oszlop in range(1, 6)}
        kek_poziciok = {(1, 5), (3, 3), (5, 1)}
        piros_poziciok = osszes_mezo - kek_poziciok

        # print(sorted(piros_poziciok))
        # exit(0)
        self.kezdo = Struct(
            piros=piros_poziciok,
            kek=kek_poziciok,
            kovetkezik="K",
            eredmeny=0,
        )

    def legalis_lepesek(self, allapot):
        lepesek = []
        is_piros = allapot.kovetkezik == "P"
        sajat = allapot.piros if is_piros else allapot.kek
        ellenfel = allapot.kek if is_piros else allapot.piros
        foglalt = allapot.piros | allapot.kek

        for sor, oszlop in sajat:
            for dsor, doszlop in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                uj_sor, uj_oszlop = sor + dsor, oszlop + doszlop
                if 1 <= uj_sor <= 5 and 1 <= uj_oszlop <= 5:
                    if is_piros:
                        # Piros csak üres mezőre léphet
                        if (uj_sor, uj_oszlop) not in foglalt:
                            lepesek.append(((sor, oszlop), (uj_sor, uj_oszlop)))
                    else:
                        # Kék csak piros mezőre léphet
                        if (uj_sor, uj_oszlop) in ellenfel:
                            lepesek.append(((sor, oszlop), (uj_sor, uj_oszlop)))
        return lepesek

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        honnan, hova = lepes
        uj_piros = set(allapot.piros)
        uj_kek = set(allapot.kek)

        if allapot.kovetkezik == "P":
            uj_piros.remove(honnan)
            uj_piros.add(hova)
        else:  # Kék lép (üt)
            uj_kek.remove(honnan)
            uj_kek.add(hova)
            uj_piros.remove(hova)  # Piros korong lekerül

        uj_allapot = Struct(
            piros=uj_piros,
            kek=uj_kek,
            kovetkezik=if_(allapot.kovetkezik == "P", "K", "P"),
            eredmeny=0,
        )

        # 1. Piros nyer: kék korongok egy SORban vagy OSZLOPban
        rows = {sor for sor, _ in uj_kek}
        cols = {oszlop for _, oszlop in uj_kek}
        if len(rows) == 1 or len(cols) == 1:
            uj_allapot.eredmeny = 1  # Piros nyert
            return uj_allapot

        # 2. Kék nyer: a soron következő nem tud lépni
        if not self.legalis_lepesek(uj_allapot):
            uj_allapot.eredmeny = -1  # Kék nyert

        return uj_allapot

    def hasznossag(self, allapot, jatekos):
        # 1 ha piros nyert, -1 ha kék
        return if_(jatekos == "P", allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        return allapot.eredmeny != 0

    def kiir(self, allapot):
        for sor in range(1, 6):
            for oszlop in range(1, 6):
                if (sor, oszlop) in allapot.piros:
                    print("P", end=" ")
                elif (sor, oszlop) in allapot.kek:
                    print("K", end=" ")
                else:
                    print(".", end=" ")
            print()
        print(f"Következik: {allapot.kovetkezik} Eredmény:{allapot.eredmeny}\n")


def main():
    jatek = KorongJatek()

    jatssz(jatek, random_jatekos, random_jatekos)


if __name__ == "__main__":
    main()
