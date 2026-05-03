#!/usr/bin/env python3

from my_jatek import *


class KavicsJatek(Jatek):
    def __init__(self):
        mezok = {(x, y) for x in range(1, 5) for y in range(1, 5)}
        self.kezdo = Struct(tabla=mezok, kovetkezik="A", eredmeny=0)

    def legalis_lepesek(self, allapot):
        """Meghatározza az összefüggő soron/oszlopon belüli elvételeket."""
        lepesek = []
        tabla = allapot.tabla

        for i in range(1, 5):
            for j in range(1, 5):
                for db in range(1, 5):
                    lehetoseg = {(i, j + k) for k in range(db)}
                    # Táblán belül, minden mező foglalt
                    if all(m in tabla for m in lehetoseg) and all(
                        1 <= m[0] <= 4 for m in lehetoseg
                    ):
                        lepesek.append(tuple(sorted(list(lehetoseg))))

                # Oszlopok vizsgálata
                for db in range(1, 5):
                    lehetoseg = {(i + k, j) for k in range(db)}
                    if all(m in tabla for m in lehetoseg) and all(
                        1 <= m[0] <= 4 for m in lehetoseg
                    ):
                        lepesek.append(tuple(sorted(list(lehetoseg))))

        # Duplikátumok eltávolítása
        return list(set(lepesek))

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        uj_tabla = allapot.tabla - set(lepes)

        eredmeny = 0
        if not uj_tabla:
            # Ha A lépett és üres lett, akkor B nyert (-1)
            eredmeny = -1 if allapot.kovetkezik == "A" else 1

        return Struct(
            tabla=uj_tabla,
            kovetkezik=if_(allapot.kovetkezik == "A", "B", "A"),
            eredmeny=eredmeny,
        )

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == "A", allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        return not allapot.tabla

    def kiir(self, allapot):
        for i in range(1, 5):
            for j in range(1, 5):
                print("O" if (i, j) in allapot.tabla else ".", end=" ")
            print()
        print(
            f"Maradt: {len(allapot.tabla)} kavics | Következik: {allapot.kovetkezik} Eredmény:{allapot.eredmeny}\n"
        )


def main():
    jatek = KavicsJatek()
    jatssz(jatek, random_jatekos, random_jatekos)


if __name__ == "__main__":
    main()
