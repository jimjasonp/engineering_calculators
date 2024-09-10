import pandas as pd
import numpy as np
from zygiseis import fortio_epanalipsimotitas,endeiksi_epanalipsimotitas,fortio_ekkentris,endeiksi_ekkentris,fortio_sfalmatos_organou,endeiksi_sfalmatos_organou





print(endeiksi_ekkentris)
'''



sfalma_list = []
i=0
name = 'therm'
while i<len(piesi_organ):
    sfalma = piesi_organ[i]-piesi_anaf[i]
    sfalma_list.append(sfalma)
    i = i+1
df = pd.DataFrame(sfalma_list, columns=['Numbers'])
df.to_csv(f"{name}.csv")
def shmeia_allaghs(organ):
    i = 0 
    shmeia_allaghs_list = []
    while i<len(organ)-1:
        shmeia_allaghs = (organ[i]+organ[i+1])/2
        shmeia_allaghs_list.append(shmeia_allaghs)
        i = i+1

'''