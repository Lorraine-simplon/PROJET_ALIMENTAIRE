import pandas as pd

alimconfiance_dataset = pd.read_csv('C:/Users/utilisateur/Desktop/RENDUS/PROJET_ALIMENTAIRE/export_alimconfiance.csv', sep=';')
alimconfiance_dataset_clean_raw_import = alimconfiance_dataset.copy()
alimconfiance_dataset_clean_inspection_import = alimconfiance_dataset.copy()

alimconfiance_dataset_clean_raw_import.rename(columns={"APP_Libelle_etablissement":"nom_etablissement"}, inplace=True)
alimconfiance_dataset_clean_raw_import.rename(columns={"SIRET":"numero_siret"}, inplace=True)
alimconfiance_dataset_clean_raw_import.rename(columns={"Adresse_2_UA":"adresse_etablissement"}, inplace=True)
alimconfiance_dataset_clean_raw_import.rename(columns={"Code_postal":"code_postal_etablissement"}, inplace=True)
alimconfiance_dataset_clean_raw_import.rename(columns={"Libelle_commune":"ville_etablissement"}, inplace=True)
alimconfiance_dataset_clean_raw_import.rename(columns={"APP_Libelle_activite_etablissement":"activite_etablissement"}, inplace=True)
alimconfiance_dataset_clean_raw_import.rename(columns={"Agrement":"agrement_etablissement"}, inplace=True)
alimconfiance_dataset_clean_raw_import.rename(columns={"geores":"geoloc_etablissement"}, inplace=True)
alimconfiance_dataset_clean_raw_import.rename(columns={"filtre":"filtre_etablissement"}, inplace=True)
alimconfiance_dataset_clean_raw_import.rename(columns={"ods_type_activite":"ods_etablissement"}, inplace=True)
alimconfiance_dataset_clean_raw_import.drop(columns='Numero_inspection', inplace=True)
alimconfiance_dataset_clean_raw_import.drop(columns='Date_inspection', inplace=True)
alimconfiance_dataset_clean_raw_import.drop(columns='Synthese_eval_sanit', inplace=True)
alimconfiance_dataset_clean_raw_import.to_csv('C:/Users/utilisateur/Desktop/RENDUS/PROJET_ALIMENTAIRE/export_alimconfiance_clean_import.csv')

alimconfiance_dataset_clean_raw_import = pd.read_csv('C:/Users/utilisateur/Desktop/RENDUS/PROJET_ALIMENTAIRE/export_alimconfiance_clean_import.csv', sep=',')
alimconfiance_dataset_clean_raw_import.columns.values[0] = 'index'
alimconfiance_dataset_clean_raw_import["index"] = alimconfiance_dataset_clean_raw_import["index"] + 1
alimconfiance_dataset_clean_raw_import.to_csv('C:/Users/utilisateur/Desktop/RENDUS/PROJET_ALIMENTAIRE/export_alimconfiance_clean_import.csv', index=False)

alimconfiance_dataset_clean_inspection_import.rename(columns={"Numero_inspection":"numero_inspection"}, inplace=True)
alimconfiance_dataset_clean_inspection_import.rename(columns={"Date_inspection":"date_inspection"}, inplace=True)
alimconfiance_dataset_clean_inspection_import.rename(columns={"Synthese_eval_sanit":"resultat_inspection"}, inplace=True)
alimconfiance_dataset_clean_inspection_import.drop(columns='APP_Libelle_etablissement', inplace=True)
alimconfiance_dataset_clean_inspection_import.drop(columns='SIRET', inplace=True)
alimconfiance_dataset_clean_inspection_import.drop(columns='Adresse_2_UA', inplace=True)
alimconfiance_dataset_clean_inspection_import.drop(columns='Code_postal', inplace=True)
alimconfiance_dataset_clean_inspection_import.drop(columns='Libelle_commune', inplace=True)
alimconfiance_dataset_clean_inspection_import.drop(columns='APP_Libelle_activite_etablissement', inplace=True)
alimconfiance_dataset_clean_inspection_import.drop(columns='Agrement', inplace=True)
alimconfiance_dataset_clean_inspection_import.drop(columns='geores', inplace=True)
alimconfiance_dataset_clean_inspection_import.drop(columns='filtre', inplace=True)
alimconfiance_dataset_clean_inspection_import.drop(columns='ods_type_activite', inplace=True)
alimconfiance_dataset_clean_inspection_import.to_csv('C:/Users/utilisateur/Desktop/RENDUS/PROJET_ALIMENTAIRE/export_alimconfiance_clean_inspection_import.csv', index=False)