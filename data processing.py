import pandas as pd 
import numpy as np 
import xlrd #To open Excel files

df=pd.read_excel('Consommation Collaborative.xls')

#Sexe : Femme=0 // Homme= 1
df['Sexe_Binaire']=np.where(df['SEXE']=='Une femme',0,1)

#Profession - Variable PCS_REP
#"Professions intermÃ©diaires", "RetraitÃ©s", "Cadres et professions intellectuelles supÃ©rieures","EmployÃ©s","Ouvriers","LycÃ©en, Ã©tudiant","Sans activitÃ© professionnelle "
#Ref = sans activité pro
df['Agri']=np.where(df['PCS_REP']=='Agriculteurs exploitants',1,0)
df['Artisan']=np.where(df['PCS_REP']=="Artisans, commerçants et chefs d'entreprise",1,0)
df['Cadre']=np.where(df['PCS_REP']=='Cadres et professions intellectuelles supÃ©rieures',1,0)
df['Prof_Int']=np.where(df['PCS_REP']=='Professions intermÃ©diaires',1,0)
df['Employe']=np.where(df['PCS_REP']=='EmployÃ©s',1,0)
df['Ouvrier']=np.where(df['PCS_REP']=='Ouvriers',1,0)
df['Retraite']=np.where(df['PCS_REP']=='RetraitÃ©s',1,0)
df['Etudiant']=np.where(df['PCS_REP']=='LycÃ©en, Ã©tudiant',1,0)

# Taille de l'agglomération - Variable REC_agglo
df['Village']=np.where(df['REC_agglo']=='MOINS DE 2000 (ZONE RURALE)',1,0)
df['PVille']=df.REC_agglo.apply(lambda x:1 if x=='2 000 A 5 000' or x=='5 000 A 10 000' else 0)
df['MVille']=df.REC_agglo.apply(lambda x:1 if x=='10 000 A 20 000' or x=='20 000 A 50 000' else 0)
df['GVille']=df.REC_agglo.apply(lambda x:1 if x=='50 000 A 100 000' or x=='100 000 A 200 000' else 0)
df['EVille']=df.REC_agglo.apply(lambda x:1 if x=='+ DE 200 000' or x=='PARIS' else 0)

