from pathlib import Path
import pandas as pd
import numpy as np

from zygiseis import fortio_epanalipsimotitas,endeiksi_epanalipsimotitas,fortio_ekkentris,endeiksi_ekkentris,fortio_sfalmatos_organou,endeiksi_sfalmatos_organou,ypodoxeas_fortiou 


#elegxos epanalipsimothtas
#ypologismos sample std
tup_apok = np.std(endeiksi_epanalipsimotitas,ddof = 1)



#elegxos ekkentrothtas
#elegxos typou ypodoxea fortiou
if str(ypodoxeas_fortiou)=='A':
    i = 0
    apolyth_list=[]
    #ypologismos apolyths apoklishs
    while i<len(endeiksi_ekkentris):
        apolyth=abs(endeiksi_ekkentris[i]
                       -0.5*(endeiksi_ekkentris[1]+endeiksi_ekkentris[4]))
        apolyth_list.append(apolyth)
        i = i+1
    #ypologismos megisths apolyths apoklishs
    Amax = max(apolyth_list)
    # ypologismos w hat 
    w_hat = Amax/(2*fortio_ekkentris[0]*3**(1/2))

elif str(ypodoxeas_fortiou)=='B':
    i = 0
    apolyth_list=[]
    #ypologismos apolyths apoklishs
    while i<len(endeiksi_ekkentris):
        apolyth=abs(endeiksi_ekkentris[i]
                       -0.5*(endeiksi_ekkentris[0]+endeiksi_ekkentris[5]))
        apolyth_list.append(apolyth)
        i = i+1
    #ypologismos megisths apolyths apoklishs
    Amax = max(apolyth_list)
    # ypologismos w hat 
    w_hat = Amax/(2*fortio_ekkentris[0]*3**(1/2))
else:
    apolyth = 'lathos typos ypodoxea fortiou'
