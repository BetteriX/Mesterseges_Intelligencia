#!/usr/bin/env python3

from my_jatek import *


class RekeszJatek(Jatek):
    def __init__(self, n=32):
        update(self, n=n)
        self.kezdo = Struct(
            foglalt=set(),
            kovetkezik="A",
            eredmeny=0,
        )

    def legalis_lepesek(self, allapot):
        lepesek = []
        for i in range(1, self.n + 1):
            if i not in allapot.foglalt:
                # Szomszédok ellenőrzése
                bal_szomszed_ures = i == 1 or (i - 1) not in allapot.foglalt
                jobb_szomszed_ures = i == self.n or (i + 1) not in allapot.foglalt

                if bal_szomszed_ures and jobb_szomszed_ures:
                    lepesek.append(i)
        return lepesek

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        uj_foglalt = allapot.foglalt.copy()
        uj_foglalt.add(lepes)

        uj_allapot = Struct(
            foglalt=uj_foglalt,
            kovetkezik=if_(allapot.kovetkezik == "A", "B", "A"),
            eredmeny=0,
        )

        # Ha a következő játékosnak nincs lépése, az aktuális nyert
        if not self.legalis_lepesek(uj_allapot):
            uj_allapot.eredmeny = 1 if allapot.kovetkezik == "A" else -1

        return uj_allapot

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == "A", allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        return not self.legalis_lepesek(allapot)

    def kiir(self, allapot):
        sor = ""
        for i in range(1, self.n + 1):
            sor += "O" if i in allapot.foglalt else "."
        print(sor)
        print(f"Következik: {allapot.kovetkezik} Eredmény:{allapot.eredmeny}\n")


def main():
    jatek = RekeszJatek()
    jatssz(jatek, random_jatekos, random_jatekos)


if __name__ == "__main__":
    main()
