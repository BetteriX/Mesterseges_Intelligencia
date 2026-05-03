#!/usr/bin/env python3

from my_jatek import *


class SzamJatek(Jatek):
    def __init__(self, kezdo_szam):
        update(self, kezdo_szam=kezdo_szam)
        self.kezdo = Struct(szam=kezdo_szam, kovetkezik="A", eredmeny=0)

    def legalis_lepesek(self, allapot):
        if allapot.eredmeny != 0:
            return []

        s = allapot.szam
        lepesek = []

        # 1. Csökkentés: minden pozíción, ahol a számjegy > 0
        for i, digit in enumerate(s):
            if int(digit) > 0:
                lepesek.append(("csokkent", i))

        # 2. Törlés: Csak olyan i indexű nullánál vághatjuk, amei előtt van legalább egy NEMnulla számjegy.
        van_nem_nulla_elotte = False
        for i, digit in enumerate(s):
            if int(digit) > 0:
                van_nem_nulla_elotte = True

            if digit == "0" and van_nem_nulla_elotte:
                lepesek.append(("torol", i))

        return lepesek

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        tipus, index = lepes
        s_lista = list(allapot.szam)

        if tipus == "csokkent":
            uj_ertek = int(s_lista[index]) - 1
            s_lista[index] = str(uj_ertek)
            uj_szam = "".join(s_lista)
        else:
            # Törlés az adott indextől a végéig
            uj_szam = "".join(s_lista[:index])

        uj_eredmeny = 0
        # Vereség
        if uj_szam != "" and all(d == "0" for d in uj_szam):
            uj_eredmeny = -1 if allapot.kovetkezik == "A" else 1
        # Győzelem
        elif uj_szam == "":
            uj_eredmeny = 1 if allapot.kovetkezik == "A" else -1

        return Struct(
            szam=uj_szam,
            kovetkezik=if_(allapot.kovetkezik == "A", "B", "A"),
            eredmeny=uj_eredmeny,
        )

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == "A", allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        return allapot.eredmeny != 0 or allapot.szam == ""

    def kiir(self, allapot):
        s = allapot.szam
        if s == "":
            print("SZÁM: [ÜRES]")
        else:
            print(f"SZÁM: {s}")

        if allapot.eredmeny != 0:
            gyoztes = "A" if allapot.eredmeny == 1 else "B"
            print(f"Győztes: {gyoztes}")
        else:
            print(f"Soron jön: {allapot.kovetkezik}")
        print()


def main():
    jatek = SzamJatek(kezdo_szam="58252010")
    jatssz(jatek, random_jatekos, random_jatekos)


if __name__ == "__main__":
    main()
