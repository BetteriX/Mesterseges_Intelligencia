#!/usr/bin/env python3

from teszt_my_jatek import *


class KekPiros(Jatek):
    def __init__(self, n):
        update(self, n=n)
        lepesek = [
            (x, y)
            for x in range(n)
            for y in range(n)
            if x % 2 == y % 2  # Azonos paritás
        ]

        # Kezdő tábla legenerálása
        tabla = []
        for x in range(n):
            sor = []
            for y in range(n):
                if x % 2 == 1 and y % 2 == 0:
                    sor.append(1)
                elif x % 2 == 0 and y % 2 == 1:
                    sor.append(2)
                else:
                    sor.append(0)
            tabla.append(sor)

        self.kezdo = Struct(tabla=tabla, kovetkezik="p", lepesek=lepesek, eredmeny=0)

    def legalis_lepesek(self, allapot):
        return allapot.lepesek

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        if lepes not in allapot.lepesek:
            return allapot

        x, y = lepes
        uj_tabla = [sor[:] for sor in allapot.tabla]
        uj_tabla[x][y] = 1 if allapot.kovetkezik == "P" else 2

        uj_lepesek = [lep for lep in allapot.lepesek if lep != lepes]

        uj_allapot = Struct(
            tabla=uj_tabla,
            lepesek=uj_lepesek,
            kovetkezik=if_(allapot.kovetkezik == "P", "K", "P"),
            eredmeny=0,
        )

        uj_allapot.eredmeny = self.ertekel(uj_allapot)

        return uj_allapot

    def ertekel(self, allapot):
        """
        - Piros nyer (1), ha van olyan SOR, amiben csak 1-es van.
        - Kék nyer (-1), ha van olyan OSZLOP, amiben csak 2-es van.
        """
        n = self.n

        # Piros - Sor
        for x in range(n):
            if all(allapot.tabla[x][y] == 1 for y in range(n)):
                return 1

        # Kék - Oszlop
        for y in range(n):
            if all(allapot.tabla[x][y] == 2 for x in range(n)):
                return -1

        return 0

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == "p", allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        return allapot.eredmeny != 0 or len(allapot.lepesek) == 0

    def kiir(self, allapot):
        for sor in allapot.tabla:
            print(" ".join(map(str, sor)))
        print(f"Következik: {allapot.kovetkezik}  | Eredmény:{allapot.eredmeny}\n")


def main():
    jatek = KekPiros(n=15)
    jatssz(jatek, random_jatekos, random_jatekos)


if __name__ == "__main__":
    main()
