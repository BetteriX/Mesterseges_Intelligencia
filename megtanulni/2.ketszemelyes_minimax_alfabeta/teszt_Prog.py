#!/usr/bin/env python3

from teszt_my_jatek import *


class KorongJatek(Jatek):
    def __init__(self):
        update(self, sor=6, oszlop=7, tiltott={(3, 3), (4, 5)})

        piros = {(1, y) for y in range(1, 8)}
        kek = {(6, y) for y in range(1, 8)}

        self.kezdo = Struct(
            piros=piros,
            kek=kek,
            kovetkezik="P",
            eredmeny=0,
        )

    def legalis_lepesek(self, allapot):
        lepesek = []
        sajat = allapot.piros if allapot.kovetkezik == "P" else allapot.kek
        ellenfel = allapot.kek if allapot.kovetkezik == "P" else allapot.piros
        irany = 1 if allapot.kovetkezik == "P" else -1

        for sor, oszlop in sajat:
            # Lehetséges célok: (x+irany, y-1), (x+irany, y), (x+irany, y+1)
            for doszlop in [-1, 0, 1]:
                uj_sor, uj_oszlop = sor + irany, oszlop + doszlop
                if (
                    1 <= uj_sor <= self.sor
                    and 1 <= uj_oszlop <= self.oszlop
                    and (uj_sor, uj_oszlop) not in self.tiltott
                ):
                    if doszlop == 0:  # Előre: Üres mezőre
                        if (uj_sor, uj_oszlop) not in sajat and (
                            uj_sor,
                            uj_oszlop,
                        ) not in ellenfel:
                            lepesek.append(((sor, oszlop), (uj_sor, uj_oszlop)))
                    else:  # Átlósan: Üresre vagy Ütés
                        if (uj_sor, uj_oszlop) not in sajat:
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
            if hova in uj_kek:
                uj_kek.remove(hova)  # Ütés
        else:
            uj_kek.remove(honnan)
            uj_kek.add(hova)
            if hova in uj_piros:
                uj_piros.remove(hova)  # Ütés

        uj_allapot = Struct(
            piros=uj_piros,
            kek=uj_kek,
            kovetkezik=if_(allapot.kovetkezik == "P", "K", "P"),
            eredmeny=0,
        )

        # Ha a következő nem tud lépni, az aktuális nyert
        if not self.legalis_lepesek(uj_allapot):
            uj_allapot.eredmeny = 1 if allapot.kovetkezik == "P" else -1

        return uj_allapot

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == "P", allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        return allapot.eredmeny != 0

    def kiir(self, allapot):
        for x in range(1, self.sor + 1):
            for y in range(1, self.oszlop + 1):
                if (x, y) in allapot.piros:
                    print("P", end=" ")
                elif (x, y) in allapot.kek:
                    print("K", end=" ")
                elif (x, y) in self.tiltott:
                    print("X", end=" ")
                else:
                    print(".", end=" ")
            print()
        print(f"Jön: {allapot.kovetkezik} Eredmény:{allapot.eredmeny}\n")


def main():
    jatek = KorongJatek()
    jatssz(jatek, minimax_jatekos, random_jatekos)


if __name__ == "__main__":
    main()
