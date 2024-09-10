'''
o xristis eisagei ena array me metrhseis h csv (den exw apofasisei akoma)
basei twn opoiwn ginontai oi upologismoi pou krinoun an h gefuroplastigga 
einai sumfwnh me thn pistopoihsh
To programma kanei extract ena csv to opoio periexei tiw metrhseis pou grafontai sto 
pistopoihtiko diakrivwshs
'''
from pathlib import Path
import pandas as pd
import numpy as np
from periballontikes_sunthikes import therm_anaf,therm_organ,ygr_anaf,ygr_organ,piesi_organ,piesi_anaf


def sfalma(name,anaf,organ):
    sfalma_list = []
    i=0
    while i<len(organ):
        sfalma = organ[i]-anaf[i]
        sfalma_list.append(sfalma)
        i = i+1
    df = pd.DataFrame(sfalma_list, columns=[name])
    filepath = Path(f'results/{name}.csv') 
    df.to_csv(filepath)
    

def shmeia_allaghs(name,organ):
    i = 0 
    shmeia_allaghs_list = []
    while i<len(organ)-1:
        shmeia_allaghs = (organ[i]+organ[i+1])/2
        shmeia_allaghs_list.append(shmeia_allaghs)
        i = i+1
    df = pd.DataFrame(shmeia_allaghs_list, columns=[name])
    filepath = Path(f'results/{name}.csv') 
    df.to_csv(filepath)

sfalma('sfalma_thermokrasias',therm_anaf,therm_organ)
sfalma('sfalma_ygrasias',ygr_anaf,ygr_organ)
sfalma('sfalma_piesis',piesi_anaf,piesi_organ)
shmeia_allaghs('shmeia_allaghs_thermokrasias',therm_organ)
shmeia_allaghs('shmeia_allaghs_ygrasias',ygr_organ)
shmeia_allaghs('shmeia_allaghs_piesis',piesi_organ)






### thelo na bazei ta csv se ksexwirsto fakelo "results"