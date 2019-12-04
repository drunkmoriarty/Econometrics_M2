import pandas as pd 
import numpy as np 
import xlrd #To open Excel files

df=pd.read_excel('Consommation Collaborative.xls')

########################## VARIABLES EXPLIQUEES ##################################
#Partager trajet en voiture avec personne exté pour aller au travail 
df['ParTrav']=df.Q4_1.apply(lambda x:1 if x=='rÃ©guliÃ¨rement' or x=='occasionnellement' else 0)

#Partager trajet en voiture avec personne exté pour trajet +80km
df['Par80']=df.Q4_3.apply(lambda x:1 if x=='rÃ©guliÃ¨rement' or x=='occasionnellement' else 0)

################ VARIABLES EXPLICATIVES #######################################
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
#Ref = NC
df['Village']=np.where(df['REC_agglo']=='MOINS DE 2000 (ZONE RURALE)',1,0)
df['PVille']=df.REC_agglo.apply(lambda x:1 if x=='2 000 A 5 000' or x=='5 000 A 10 000' else 0)
df['MVille']=df.REC_agglo.apply(lambda x:1 if x=='10 000 A 20 000' or x=='20 000 A 50 000' else 0)
df['GVille']=df.REC_agglo.apply(lambda x:1 if x=='50 000 A 100 000' or x=='100 000 A 200 000' else 0)
df['EVille']=df.REC_agglo.apply(lambda x:1 if x=='+ DE 200 000' or x=='PARIS' else 0)

#Deserte lieu de résidence par transport en commun
#Ref = "Très bien déservie"
df['TC1']=np.where(df['S4']=='TrÃ¨s mal desservi',1,0)
df['TC2']=np.where(df['S4']=='Assez mal desservi',1,0)
df['TC3']=np.where(df['S4']=='Assez bien desservi',1,0)

#Utilisation voiture pour aller au travail
#ref="non concernée" & "jamais"
df['VTR1']=np.where(df['Q1_1']=='systÃ©matiquement',1,0)
df['VTR2']=np.where(df['Q1_1']=='le plus souvent',1,0)
df['VTR3']=np.where(df['Q1_1']=='occasionnellement',1,0)
df['VTR4']=np.where(df['Q1_1']=='jamais',1,0)

#Utilisation voiture pour trajet de +80km
#ref="non concernée" & "jamais"
df['UTV1']=np.where(df['Q1_3']=='systÃ©matiquement',1,0)
df['UVT2']=np.where(df['Q1_3']=='le plus souvent',1,0)
df['UVT3']=np.where(df['Q1_3']=='occasionnellement',1,0)
df['UVT4']=np.where(df['Q1_3']=='jamais',1,0)

#Fréquence trajet +80km - Possibilité de problème de colinéarité
#ref=
df['FT1']=np.where(df['Q2']=='1 fois par semaine ou plus',1,0)
df['FT2']=np.where(df['Q2']=='1 Ã 3 fois par mois',1,0)
df['FT3']=np.where(df['Q2']=='moins souvent',1,0)

#Perception de l'utilisation de la voiture 
#ref = "ne sait pas"
df['PV1']=np.where(df['Q3_1']=="plus d'avantages que d'inconvÃ©nients",1,0)
df['PV2']=np.where(df['Q3_1']=="autant d'avantages que d'inconvÃ©nients",1,0)
df['PV3']=np.where(df['Q3_1']=="plus d'inconvÃ©nients que d'avantages",1,0)

#Perception de l'utilisation des transports en commun
#ref = "ne sait pas"
df['PTC1']=np.where(df['Q3_2']=="plus d'avantages que d'inconvÃ©nients",1,0)
df['PTC2']=np.where(df['Q3_2']=="autant d'avantages que d'inconvÃ©nients",1,0)
df['PTC3']=np.where(df['Q3_2']=="plus d'inconvÃ©nients que d'avantages",1,0)

#Partage des frais
df['Frais']=df.Q8.apply(lambda x:1 if x=='TrÃ¨s souvent' or x=='Assez souvent' or x=='Rarement' else 0)

#Motivation partage trajet
#Ref= "Aucune autre raison" + "Pour une autre raison"
df['Mot1']=np.where(df['Q9A']=="Pour s'entraider",1,0)
df['Mot2']=np.where(df['Q9A']=="Pour faire des Ã©conomies",1,0)
df['Mot3']=np.where(df['Q9A']=="Pour rendre le trajet plus convivial",1,0)
df['Mot4']=np.where(df['Q9A']=="Pour diminuer la pollution automobile",1,0)

#Influence entourage trajet travail
#ref= “Non, aucune” / “Ne sait pas”
df['InfluTra1']=np.where(df['Q22_1']=="Oui, la plupart des personnes de mon entourage",1,0)
df['InfluTra2']=np.where(df['Q22_1']=="Oui, une partie",1,0)
df['InfluTra3']=np.where(df['Q22_1']=="Oui, mais trÃ¨s peue",1,0)

#Influence entourage trajet +80km
#ref= “Non, aucune” / “Ne sait pas”
df['Influ80_1']=np.where(df['Q22_2']=="Oui, la plupart des personnes de mon entourage",1,0)
df['Influ80_2']=np.where(df['Q22_2']=="Oui, une partie",1,0)
df['Influ80_1']=np.where(df['Q22_2']=="Oui, mais trÃ¨s peue",1,0)