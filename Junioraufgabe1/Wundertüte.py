#!/usr/bin/env python3

import sys
from tabulate import tabulate
import pandas

def Tabellenoutput(Tüteen):
    df = pandas.DataFrame(Tüteen).fillna(0)
    print(tabulate(df, headers = ['Tüte'] + list(df.columns), tablefmt = 'orgtbl'))

def Einlesung(Datei):
    Tüten = 0
    Spiele = []
    d = open(Datei, 'r')
    for Zeile in d:
        Z = Zeile.strip('\n')
        if Z == '':
            break
        Spiele.append(int(Z))
    Tüten = Spiele[0]
    Spielarten = Spiele[1]
    Spiele = Spiele[2:]
    if len(Spiele) == Spielarten:
        return Tüten, Spiele, Spielarten

def Wundertüte(Tütenan, Spiele):
    Tüten = [{} for _ in range(Tütenan)]
    if Tütenan > sum(Spiele):
        print('Es bleibt/en (eine) leere Tüte/n übrig.')
        return
    j = 0
    i = 0
    Alphabeta = 'WKGABCDEFHIJLMNOPQRSTUVXYZÄÖÜß'
    while Spiele != []:
        n_Spielart = Spiele[0]
        Spiel_id = Alphabeta[j] if j < len(Alphabeta) else j
        while n_Spielart > 0:
            if Spiel_id not in Tüten[i]:
                Tüten[i][Spiel_id] = 1
            else:
                Tüten[i][Spiel_id] += 1
            n_Spielart -= 1
            i += 1
            i %= len(Tüten)
        j += 1
        Spiele = Spiele[1:]
    return Tüten

if __name__ == "__main__":
    Tüten, Spiele, Spielarten = Einlesung(sys.argv[1])
    Tabellenoutput(Wundertüte(Tüten, Spiele))