'''
o xristis eisagei ena array me metrhseis h csv (den exw apofasisei akoma)
basei twn opoiwn ginontai oi upologismoi pou krinoun an h gefuroplastigga 
einai sumfwnh me thn pistopoihsh
To programma kanei extract ena csv to opoio periexei tiw metrhseis pou grafontai sto 
pistopoihtiko diakrivwshs
'''
import pandas as pd

from periballontikes_sunthikes import therm_anaf,therm_organ,ygr_anaf,ygr_organ,piesi_organ,piesi_anaf


def sfalma(anaf,organ):
    sfalma = organ-anaf
    print(sfalma)

def shmeia_allaghs(organ):
    i = 0 
    while i<len(organ)-1:
        shmeia_allaghs = (organ[i]+organ[i+1])/2
        i = i+1


sfalma_therm = sfalma(therm_anaf,therm_organ)


shmeia_allaghs_therm = shmeia_allaghs(therm_organ)

### thelo na kano extract ta apotelesmata se csv