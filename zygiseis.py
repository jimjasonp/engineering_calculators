import numpy as np
import pandas as pd


list_metrhseis = pd.read_csv('metrhseis_zygisewn.csv')
list_metrhseis = list_metrhseis.dropna()
column_names = list_metrhseis.columns
fortio_epanalipsimotitas = list_metrhseis['fortio_epanalipsimotitas']
endeiksi_epanalipsimotitas = list_metrhseis['endeiksi_epanalipsimotitas']
fortio_ekkentris = list_metrhseis['fortio_ekkentris']
endeiksi_ekkentris = list_metrhseis['endeiksi_ekkentris']
fortio_sfalmatos_organou = list_metrhseis['fortio_sfalmatos_organou']
endeiksi_sfalmatos_organou = list_metrhseis['endeiksi_sfalmatos_organou']

print(list_metrhseis)