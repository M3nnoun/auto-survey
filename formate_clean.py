# -*- coding: utf-8 -*-
"""formate_data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fUblv8spE_3-5twH3icV0fl_2YMs33Ab
"""

import pandas as pd

df = pd.read_csv('data.csv', encoding='utf-8')

df.head()

def format_json_question(row):
  #new_row=[]
  repond={}
  if type(row)==str:
      lines=row.split('\n')
      repond={}
      for line in lines:
        q_a=line.split(':')
        repond[q_a[0]]=q_a[1]
        #new_row.append(repond)
  return repond

handicap_question=pd.DataFrame(list(df['هل واجهت أي صعوبات في حياتك اليومية بسبب ظروف صحية أو جسدية؟'].apply(format_json_question)))

energie_question=pd.DataFrame(list(df['ما هي أنواع مصادر الطاقة التي تستخدمها بشكل أساسي لتلبية احتياجات الطاقة المنزلية؟ (1)'].apply(format_json_question)))

data_set=df.iloc[:,2:]

print(data_set)

data_set

resutl=pd.concat([data_set, handicap_question], axis=1)

resutl=pd.concat([resutl, energie_question], axis=1)

resutl.iloc[:,11:16]

column_mapping = {
    'في وسط تعيش فيه(قروي/حضري)': 'MilieuVie',
    'في اي اقليم تقطن؟': 'RegionResidence',
    'من فضلك اخبرنا كم عمرك': 'Age',
    'ما هو جنسك؟': 'Genre',
    'ما هو مستوى تعليمكم (أعلى شهادة حصلتم عليها خلال مشواركم الدراسي)؟': 'NiveauEducation',
    'لقد اخترتم "اخر" للسؤال السابق،ماذا تقصدون ب"اخر":': 'Autre',
    'ما هو وضعك العائلي؟': 'EtatCivil',
    'ما هو نشاطك الحالي؟': 'Activite',
    'كم عدد الأشخاص الذين يعيشون حاليًا في نفس منزلك؟': 'NombreMenage',
    'هل واجهت أي صعوبات في حياتك اليومية بسبب ظروف صحية أو جسدية؟': 'Difficultés quotidiennes en raison de problèmes de santé ou physiques',
    'كم مدى توفر الكهرباء في منطقتك؟': 'Disponibilite-electricite',
    'ما هي أنواع مصادر الطاقة التي تستخدمها بشكل أساسي لتلبية احتياجات الطاقة المنزلية؟': 'PrincipalesSourcesEnergie',
    'ما هي أنواع مصادر الطاقة التي تستخدمها بشكل أساسي لتلبية احتياجات الطاقة المنزلية؟ (1)': 'Principales-sources-energie-2',
    'في اي قطاع من بين القطاعات الاربع يمكن تصنيف عملك؟': 'SecteurEmploi',
    'كم يقدر مدخولك الشهري ؟': 'Revenu',
    'كم يقدر مصروفك الشهري؟': 'Depenses',
    'هل تتابع اي تكوين حالي او تعليم اضافي،دورة تكوينية': 'Formation',
    'كم تبعد عن اقرب طريق معبدة صالحة للاستعمال؟': 'DistanceRoutePraticable',
    'ما بشبكة المحمول التي لدك وصول اليها؟': 'OperateurMobile',
    'هل لاحظت أي تحسن في دخلك خلال السنوات القليلة الماضيةّ؟': 'AmeliorationRevenu',
    'ما مقدار الزيادة في مدخولك؟': 'MontantAugmentationRevenu',
    'ما مقدار إجمالي تعويضات اوالمنح التي تتلقها كموظف': 'RemunerationEmploye',
    'هل تعمل لحسابك الخاص؟': 'TravailleurIndependant',
    'كيف تقيم الحي الذي تعيش فيه؟': 'EvaluationQuartier',
    'طريقة تخلصك من النفايات؟': 'MethodeElimination',
    'هل تقوم باعادة التدوير بعض من نفاياتك المنزلية؟': 'RecyclageDechets',
    'هل تعرف ماهي اهداف التمية المستدامة؟': 'ConnaissanceOdd',
    'ما مدى المامكم باهداف التنمية المستدامة؟': 'ConnaissanceOddNumber',
    'للإضاءة': 'MEclairage',
    'للطهي': 'MCuisine',
    'للتبريد/للتسخين': 'MRefroidissementChauffage',
    'للتدفئة': 'MChauffage',
    'هل تواجه أي صعوبات في التنقل أو الحركة؟': 'DifficultesDeplacement',
    'هل تستخدم أي أدوات مساعدة أو أجهزة خاصة لمساعدتك في حياتك اليومية؟': 'techniquesAider',
    'هل تواجه أي صعوبات في التواصل أو السمع أو البصر؟': 'DifficultesVision',
}

resutl.rename(columns=column_mapping, inplace=True)

resutl

resutl.columns

data_formated=resutl[['MilieuVie', 'RegionResidence', 'Age', 'Genre', 'EtatCivil', 'Activite', 'NombreMenage','NiveauEducation', 'Autre', 'SecteurEmploi', 'Revenu', 'Depenses', 'Formation','DifficultesDeplacement', 'techniquesAider', 'DifficultesVision', "PrincipalesSourcesEnergie",'MEclairage', 'MCuisine', 'MRefroidissementChauffage', 'MChauffage','DistanceRoutePraticable', 'OperateurMobile', 'AmeliorationRevenu', 'MontantAugmentationRevenu', 'RemunerationEmploye', 'TravailleurIndependant','EvaluationQuartier', 'MethodeElimination', 'RecyclageDechets', 'ConnaissanceOdd', 'ConnaissanceOddNumber']]

#Trim white-spaces
columns_names=['DifficultesDeplacement','techniquesAider','DifficultesVision','MEclairage','MCuisine','MRefroidissementChauffage','MChauffage','PrincipalesSourcesEnergie']
def trim_whitespace(text):
    return text.strip() if isinstance(text, str) else text

for col in data_formated.columns:
  print('============',col,'============')
  print(data_formated[col].unique())
  print(data_formated[col].apply(trim_whitespace))
  print(data_formated[col].value_counts())


data_formated['MilieuVie']=data_formated['MilieuVie'].replace({'حضري': 'Urbain', 'قروي': 'Rural'})

data_formated['MilieuVie'].value_counts()

translations = {
    "MilieuVie": {'حضري': 'Urbain', 'قروي': 'Rural', },
    "RegionResidence": {'العيون': 'Laayoune', 'السمارة': 'Semara', 'اخر': 'Autre', },
    "Age": {20.0: 20, 15.0: 15, 32.0: 32, 22.0: 22, 33.0: 33, 30.0: 30, 38.0: 38, 21.0: 21, 24.0: 24, 18.0: 18,
            35.0: 35, 26.0: 26, 19.0: 19, 23.0: 23, 58.0: 58, 34.0: 34, 27.0: 27, 36.0: 36, 25.0: 25, 29.0: 29,
            45.0: 45, 28.0: 28, 31.0: 31, 16.0: 16, 200.0: 200, },
    "Genre": {'أنثى': 'Femme', 'ذكر': 'Homme', },
    "EtatCivil": {'أعزب(ة)': 'Celibataire', 'أفضل عدم الإفصاح': 'Prefere ne pas divulguer', 'متزوج(ة)': 'Marie',
                   'مطلق(ة)': 'Divorce', 'منفصل(ة)': 'Separe', },
    "Activite": {'تلميذ /طالب': 'Etudiant', 'نشيط مشتغل': 'Actif', 'عاطل عن العمل': 'Chomeur',
                 'ربة بيت': 'Femme au foyer', 'حالات اخري': 'Autre', 'متقاعد': 'Retraite', },
    "NombreMenage": {0.0: 0, 2.0: 2, 3.0: 3, 4.0: 4, 5.0: 5, 6.0: 6, 7.0: 7, 8.0: 8, 9.0: 9, 10.0: 10, 11.0: 11, 12.0: 12, },
    "NiveauEducation": {'التعليم العالي': 'Enseignement superieur', 'الثانوي': 'Secondaire', 'مستوى اخر': 'Autre niveau',
                         'بدون': 'Aucun', 'الاعدادي': 'Collégial', 'التعليم الثانوي الإعدادي': 'Secondaire collégial', },
    "Autre": {'الباك': 'Baccalaureat', 'باكلوريا': 'Baccalaureat', 'مجازة': 'Licence', 'تقني متخصص': 'Technicien specialise',
                          'عامين بعد شهادة الباكالوريا في المعهد التقني المتخصص': 'Diplome de technicien specialise', 'دبلوم جامعي': 'Diplôme universitaire'},
    "SecteurEmploi": {'القطاع التجاري والخدماتي': 'Commerce et services', 'قطاع البناء والعقارات': 'Construction et immobilier',
                        'قطاع النقل واللوجستيات': 'Transport et logistique',
                        'القطاع العام والخدمات العامة(مثل الصحة والتعليم والنقل والبنية التحتية,الامن والمجال العسكري)': 'Secteur public et services publics',
                        'قطاع التكنولوجيا والاتصالات': 'Technologie et telecommunications'},
    "Revenu": {'من 2000 درهم الى اقل من 4000 درهم': '2000-4000'},
    "Depenses": {'اقل من 500 درهم': '0-500', 'من 2000درهم الى اقل من 4000 درهم': '2000-4000',
                 'من 1000 درهم الى اقل من 2000درهم': '1000-2000',
                 'من 4000 درهم الى اقل من 6000 درهم': '4000-6000',
                 'من 500 درهم الى اقل من 1000 درهم': '500-1000', '10000و اكثر': '+10000',
                 'من 6000 درهم الى اقل من 10000 درهم': '6000-10000', },
    "Formation": {'لا': 'Non', 'نعم': 'Oui', },
    "DifficultesDeplacement": {'لا': 'Non', 'نعم': 'Oui'},
    "techniquesAider": {'لا': 'Non', 'نعم': 'Oui', },
    "DifficultesVision": {'لا': 'Non', 'نعم': 'Oui'},
    "MEclairage": {'شبكة الكهرباء': 'Electricite', 'الغاز الطبيعي': 'Gaz naturel', 'الطاقة المتجددة': 'Energie renouvelable',
                     'اخر': 'Autre','شبكة الكهرباء, اخر':'Electricite,Autre' },
    "MCuisine": {'الغاز الطبيعي': 'Gaz naturel', 'شبكة الكهرباء': 'Electricite', 'الطاقة المتجددة': 'Energie renouvelable',
                  'الغاز الطبيعي, شبكة الكهرباء': 'Gaz naturel, Electricite',
                  'شبكة الكهرباء, الغاز الطبيعي': 'Electricite, Gaz naturel',
                 'شبكة الكهرباء, الغاز الطبيعي, اخر':'Electricite, Gaz naturel,Autre',
                 'الغاز الطبيعي, اخر':'Gaz naturel,Autre'
                 },
    "MRefroidissementChauffage": {'شبكة الكهرباء': 'Electricite', 'الغاز الطبيعي': 'Gaz naturel', 'الطاقة المتجددة': 'Energie renouvelable',
                                     'شبكة الكهرباء, الغاز الطبيعي': 'Electricite, Gaz naturel',
                                     'الغاز الطبيعي, شبكة الكهرباء': 'Gaz naturel, Electricite', 'اخر': 'Autre',
                                     'الوقود الأحفوري': 'Combustibles fossiles', },
    "MChauffage": {'شبكة الكهرباء': 'Electricite', 'الغاز الطبيعي': 'Gaz naturel', 'الطاقة المتجددة': 'Energie renouvelable',
                     'شبكة الكهرباء, الوقود الأحفوري': 'Electricite, Combustibles fossiles', 'اخر': 'Autre',
                     'الوقود الأحفوري': 'Combustibles fossiles', 'شبكة الكهرباء, الغاز الطبيعي': 'Electricite, Gaz naturel',
                     'الغاز الطبيعي, اخر':'Gaz naturel,Autre'
                     },
    "DistanceRoutePraticable": {0.0: 0, 1.0: 1, 3.0: 3, 6.0: 6},
    "OperateurMobile": {'4G': '4G', '2G': '2G', '3G': '3G', 'بدون': 'Aucun', },
    "AmeliorationRevenu": {'لا': 'Non', 'نعم': 'Oui','نعم,لا': 'Oui,Non'},
    "MontantAugmentationRevenu": {'0': 0, '500': 500, '2000': 2000, '5': 5, '0.25': 0.25, '200': 200, '300': 300, '20': 20,
                                     '1000': 1000, '2500': 2500, '10': 10, '10000': 10000, '3000': 3000, '100': 100, '5000': 5000,
                                     '6565': 6565, '{\n  "value": 18,\n  "convertedValue": null\n}': 18, },
    "RemunerationEmploye": {'0': 0, '20000': 20000, '600': 600, '1000': 1000, '500': 500, '3680': 3680, '10000': 10000,
                              '2000': 2000, '1900': 1900, '800': 800, '66': 66, '{\n  "value": 85,\n  "convertedValue": null\n}': 85, },
    "TravailleurIndependant": {'لا': 'Non', 'نعم': 'Oui','نعم,لا': 'Oui,Non'},
    "EvaluationQuartier": {1.0: 1, 2.0: 2, 3.0: 3, 4.0: 4, 5.0: 5, 6.0: 6, 7.0: 7, 8.0: 8, 9.0: 9, 10.0: 10, },
    "MethodeElimination": {'صندوق قمامة خاص بالجماعة': 'Poubelle communale', 'حالات اخرى': 'Autre', 'شاحنة جماعية او خاصة': 'Camion de collecte',
                             'الافراغ في الطبيعة': 'Décharge à ciel ouvert', },
    "RecyclageDechets": {'لا': 'Non', 'نعم': 'Oui', },
    "ConnaissanceOdd": {'لا': 'Non', 'نعم': 'Oui', },
    "ConnaissanceOddNumber": {'معرفة\nجيدة': 'Bien connu', 'معرفة متوسطة': 'Connaissance moyenne',
                                 'معرفة\nجيدة جدا': 'Très bien connu', 'معرفة ضعيفة': 'Peu connu', 'سمعت عنها فقط': 'Entendu parler uniquement'}
,  "PrincipalesSourcesEnergie": {
        'الغاز الطبيعي,شبكة الكهرباء': 'Gaz naturel, Electricite',
        'شبكة الكهرباء': 'Electricite',
        'الغاز الطبيعي,الوقود الأحفوري(مثل :الفحم)': 'Gaz naturel, Combustibles fossiles',
        'الغاز الطبيعي': 'Gaz naturel',
        'شبكة الكهرباء,الغاز الطبيعي': 'Electricite,Gaz naturel',
        'شبكة الكهرباء,الطاقة المتجددة (مثل الطاقة الشمسية أو طاقة الرياح، لتلبية احتياجاتك من الطاقة؟)': 'Electricite, Energies renouvelables',
        'شبكة الكهرباء,الغاز الطبيعي,الوقود الأحفوري(مثل :الفحم)': 'Electricite, Gaz naturel, Combustibles fossiles',
        'شبكة الكهرباء,الوقود الأحفوري(مثل :الفحم)': 'Electricite, Combustibles fossiles'
    }


    }

# Loop through each translation dictionary and translate the arrays
for key, translation_dict in translations.items():
    print(f"============ {key} ============")
    #data_formated.loc[:,key]=data_formated[key].str.strip()
    data_formated.loc[:,key] = data_formated[key].apply(trim_whitespace)
    data_formated.loc[:,key]=data_formated.loc[:,key].replace(translation_dict)

for col in data_formated.columns:
  print('============',col,'============')
  print(data_formated[col].unique())
  print(data_formated[col].value_counts())

excel_file_path = "translated_data.xlsx"

data_formated.to_excel(excel_file_path, index=False)

hd=data_formated.copy()

hd['PrincipalesSourcesEnergie']

multi_value_cols = ['PrincipalesSourcesEnergie','MCuisine','MEclairage','MRefroidissementChauffage','MChauffage']
for index, row in hd.iterrows():
    for col in multi_value_cols:
        values = row[col].split(',') if isinstance(row[col], str) else []
        for value in values:
            new_col_name = f"{col}_{value.strip().replace(' ','_')}"
            hd.loc[index, new_col_name] = 'Oui' if 'oui' in value.lower() else ''

new_indixes=[]
for col in hd.columns:
  if ~(col in multi_value_cols):
    new_indixes.append(col)

new_indixes+multi_value_cols

new_indixes

hd['PrincipalesSourcesEnergie'].unique()

len(hd.columns)==len(new_indixes)

hd[new_indixes].to_excel(excel_file_path, index=False)

