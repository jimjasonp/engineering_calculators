import numpy as np
import pandas as pd


list_metrhseis = pd.read_csv('metrhseis_zygisewn.csv')
column_names = list_metrhseis.columns
fortio_epanalipsimotitas = list_metrhseis['fortio_epanalipsimotitas'].dropna()
endeiksi_epanalipsimotitas = list_metrhseis['endeiksi_epanalipsimotitas'].dropna()
fortio_ekkentris = list_metrhseis['fortio_ekkentris'].dropna()
endeiksi_ekkentris = list_metrhseis['endeiksi_ekkentris'].dropna()
fortio_sfalmatos_organou = list_metrhseis['fortio_sfalmatos_organou'].dropna()
endeiksi_sfalmatos_organou = list_metrhseis['endeiksi_sfalmatos_organou'].dropna()
ypodoxeas_fortiou = pd.read_csv('ypodoxeas_fortiou.csv')
ypodoxeas_fortiou = ypodoxeas_fortiou.iloc[0]['ypodoxeas_fortiou']
