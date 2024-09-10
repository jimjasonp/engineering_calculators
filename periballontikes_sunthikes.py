import numpy as np
import pandas as pd


list_metrhseis = pd.read_csv('metrhseis_periballontos.csv')
column_names = list_metrhseis.columns
therm_anaf = list_metrhseis['Thermokrasia_anaforas'].dropna()
therm_organ = list_metrhseis['Thermokrasia_organou'].dropna()
ygr_anaf = list_metrhseis['Ygrasia_anaforas'].dropna()
ygr_organ = list_metrhseis['Ygrasia_organou'].dropna()
piesi_anaf = list_metrhseis['Barometriki_piesi_anaforas'].dropna()
piesi_organ = list_metrhseis['barometriki_piesi_organou'].dropna()
