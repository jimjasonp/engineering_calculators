import numpy as np
import pandas as pd


list_metrhseis = pd.read_csv('metrhseis.csv')
list_metrhseis = list_metrhseis.dropna()
column_names = list_metrhseis.columns
therm_anaf = list_metrhseis['Thermokrasia_anaforas']
therm_organ = list_metrhseis['Thermokrasia_organou']
ygr_anaf = list_metrhseis['Ygrasia_anaforas']
ygr_organ = list_metrhseis['Ygrasia_organou']
piesi_anaf = list_metrhseis['Barometriki_piesi_anaforas']
piesi_organ = ['barometriki_piesi_organou']

