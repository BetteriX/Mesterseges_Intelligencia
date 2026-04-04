from keres import *
from seged import *

class Domino(Feladat):
    def __init__(self,kezdő,cél):
        self.kezdő = kezdő
        self.cél = cél

    def célteszt(self, állapot):
        return állapot == self.cél
    

    def rákövetkező(self, állapot):

        utodok = []

        for i in range(8):
            for j in range (8):
                if állapot[i][j] == 0:
                    if (j + 1 < 8) and állapot[i][j] == 0:
                        uj_tabla_lista = [list(sor) for sor in állapot]
                        uj_tabla_lista[i][j] = 1
                        uj_tabla_lista[i][j+1] = 1

                        uj_allapot = tuple(tuple(sor) for sor in uj_tabla_lista)

                        utodok.append((f"lerak: ({i},{j})", uj_allapot))

                    if i + 1 < 8 and állapot[i+1][j] == 0:
                        uj_tabla_lista = [list(sor) for sor in állapot]
                        uj_tabla_lista[i][j] = 1
                        uj_tabla_lista[i+1][j] = 1

                        uj_allapot = tuple(tuple(sor) for sor in uj_tabla_lista)

                        utodok.append((f"lerak: ({i},{j})", uj_allapot))
        
        return utodok

    def heurisztika(self, csúcs):
        állapot = csúcs.állapot
        nullak_szama = 0

        for sor in állapot:
            nullak_szama += sor.count(0)
        
        return nullak_szama // 2


if __name__ == "__main__":

    kezdo_allapot = (
        (0,0,0,0,0,0,0,0),
        (0,0,0,0,0,0,0,0),
        (0,0,0,0,0,0,0,0),
        (0,0,0,0,0,0,0,0),
        (0,0,0,0,0,0,0,0),
        (0,0,0,0,0,0,0,0),
        (0,0,0,0,0,0,0,0),
        (0,0,0,0,0,0,0,0)
    )
    
    cel_allapot = (
        (1,1,1,1,1,1,1,1),
        (1,1,1,1,1,1,1,1),
        (1,1,1,1,1,1,1,1),
        (1,1,1,1,1,1,1,1),
        (1,1,1,1,1,1,1,1),
        (1,1,1,1,1,1,1,1),
        (1,1,1,1,1,1,1,1),
        (1,1,1,1,1,1,1,1)
    )

    feladat = Domino(kezdo_allapot, cel_allapot)
    eredmeny = best_first(feladat, feladat.heurisztika)
    print("Best-First: ")
    print(eredmeny.megoldás())

