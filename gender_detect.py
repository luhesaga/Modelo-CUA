import pandas as pd
import operator
import re

def clean_text(txt):
    txt = re.sub("[^a-záéíóúñüäë]", " ", txt.lower())
    txt = re.sub(' +',' ', txt)
    return txt.strip().split()

def df_to_dict(df, key_column, val_column):
    """convierte dos pandas series en un diccionario"""
    xkey = df[key_column].tolist()
    xval = df[val_column].tolist()
    return dict(zip(xkey,xval))

def get_gender2(names, gender_list):
    names = clean_text(names)
    names = [x for x in names if gender_list.get(x,'a') != 'a']
    gender ={'m':0, 'f':0, 'a':0}
    for i, name in enumerate(names):
        g = gender_list.get(name,'a')
        gender[g] += 1
        gender[g] += 2 if len(names) > 1 and i == 0 and g != 'a' else 0
    gender['a'] = 0 if (gender['f']+gender['m']) > 0 else 1
    return max(gender.items(), key=operator.itemgetter(1))[0]
