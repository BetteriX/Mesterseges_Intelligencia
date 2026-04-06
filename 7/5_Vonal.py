from keres import *
from seged import *

class Vonaltabla(Feladat):
    def __init__(self, kezdő, cél):
        self.kezdő = kezdő
        self.cél = cél
        
    def célteszt(self, állapot):
        return állapot == self.cél


    def rákövetkező(self, állapot):
        utodok = []
        
        if állapot == self.cél:
            return utodok
            
        tábla, (i, j), d_elozo = állapot
        aktualis_cella = tábla[i][j]
        
        iranyok = {'fel': (-1, 0), 'le': (1, 0), 'bal': (0, -1), 'jobb': (0, 1)}
        meroleges = {'fel': ['bal', 'jobb'], 'le': ['bal', 'jobb'], 'bal': ['fel', 'le'], 'jobb': ['fel', 'le']}
        vissza = {'fel': 'le', 'le': 'fel', 'bal': 'jobb', 'jobb': 'bal'}
        
        if aktualis_cella == 0:
            lehetseges_iranyok = ['fel', 'le', 'bal', 'jobb']
            if d_elozo in vissza:
                lehetseges_iranyok.remove(vissza[d_elozo])
        elif aktualis_cella == 'n':
            lehetseges_iranyok = meroleges[d_elozo]
        else:
            lehetseges_iranyok = []
            
        for d in lehetseges_iranyok:
            di, dj = iranyok[d]
            uj_i, uj_j = i + di, j + dj
            
            if 0 <= uj_i < 8 and 0 <= uj_j < 8:
                if tábla[uj_i][uj_j] in [0, 'n']:
                    uj_tabla = [list(sor) for sor in tábla]
                    uj_tabla[i][j] = 'l'  # Behúzzuk a vonalat
                    uj_tabla_tuple = tuple(tuple(sor) for sor in uj_tabla)
                    
                    maradek = sum(sor.count(0) + sor.count('n') for sor in uj_tabla_tuple)
                    
                    if maradek == 1:
                        utodok.append((f"utolsó_lépés_{d}({uj_i},{uj_j})", self.cél))
                    else:
                        uj_allapot = (uj_tabla_tuple, (uj_i, uj_j), d)
                        utodok.append((f"lépés_{d}({uj_i},{uj_j})", uj_allapot))
                        
        return utodok

    def heurisztika(self, csúcs):
        állapot = csúcs.állapot
        
        if állapot == self.cél:
            return 0
            
        tábla, (i, j), d_elozo = állapot
        
        maradek = sum(sor.count(0) + sor.count('n') for sor in tábla)
        
        szam = 0
        iranyok = {'fel': (-1, 0), 'le': (1, 0), 'bal': (0, -1), 'jobb': (0, 1)}
        meroleges = {'fel': ['bal', 'jobb'], 'le': ['bal', 'jobb'], 'bal': ['fel', 'le'], 'jobb': ['fel', 'le']}
        vissza = {'fel': 'le', 'le': 'fel', 'bal': 'jobb', 'jobb': 'bal'}
        
        cella = tábla[i][j]
        if cella == 0:
            jovo_iranyok = ['fel', 'le', 'bal', 'jobb']
            if d_elozo in vissza:
                jovo_iranyok.remove(vissza[d_elozo])
        elif cella == 'n':
            jovo_iranyok = meroleges[d_elozo]
        else:
            jovo_iranyok = []
            
        for jd in jovo_iranyok:
            jdi, jdj = iranyok[jd]
            nr, nc = i + jdi, j + jdj
            if 0 <= nr < 8 and 0 <= nc < 8 and tábla[nr][nc] in [0, 'n']:
                szam += 1
                
        return maradek + (szam * 0.1)

if __name__ == "__main__":
    
    kezdo_tabla = (
        ('n',  0 ,  0 ,  0 , 'n',  0 ,  0 ,  0 ),
        ( 0 ,  0 ,  0 , 'n',  0 ,  0 , 'n',  0 ),
        ( 0 ,  0 , 'n',  0 ,  0 ,  0 ,  0 ,  0 ),
        ( 0 ,  0 ,  0 ,  0 ,  0 , 'n',  0 ,  0 ),
        ( 0 , 'n',  0 ,  0 , 'n',  0 ,  0 ,  0 ),
        ( 0 ,  0 , 'n',  0 ,  0 ,  0 ,  0 , 'n'),
        ('n',  0 ,  0 ,  0 ,  0 , 'n',  0 ,  0 ),
        ( 0 ,  0 ,  0 , 'n',  0 ,  0 ,  0 , 'n')
    )
    
    kezdo_allapot = (kezdo_tabla, (0, 0), 'le')
    
    cel_allapot = "KÉSZ"
    
    feladat = Vonaltabla(kezdo_allapot, cel_allapot)
    eredmeny = best_first(feladat, feladat.heurisztika)
    print("Best-First: ")
    print(eredmeny.megoldás())
    
    