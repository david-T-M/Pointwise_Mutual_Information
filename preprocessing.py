import pandas as pd
import numpy as np
import re, string
import spacy
#Listado de STOPWORDS dependiendo del lenguaje
from spacy.lang.en.stop_words import STOP_WORDS
tipos_no_acepted=['NUM','DET','ADP','SYM','PRP','PART','SCONJ','INTJ','PUNCT','X','SPACE']
dic_borrar={"!":" ",'"':" ","#":" ","$":" ","%":" ","&":" ","'":" ","(":" ",")":" ","*":" ","+":" ",",":" ","-":" ",".":" ","/":" ",":":" ",";":" ","<":" ","=":" ",">":" ",'?':" ",'@':" ",'[':" ",']':" ",'^':" ",'_':" ",'`':" ",'{':" ",'|':" ",'}':" ","~":" ","1":" ","2":" ","3":" ","4":" ","5":" ","6":" ","7":" ","8":" ","9":" ","0":" "}
palabras_omitidas=['an','a','of','and','s','t','to','for','so','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
punct = string.punctuation
punct+="1234567890"

class prepocessing():
    def __init__(self, text):
        self.text = text
       
    #
    def limpiar(temp):
        temp['texto_A']=""
        train=temp.copy()
        for index,string in temp.iterrows():
            string_limpio = string[0].replace('\n',' ').lower().translate(str.maketrans(dic_borrar))
            train.loc[index,'texto_A']=string_limpio
        return train
    def lematizado(temp):
        temp['texto_A_l']=""
        nlp = spacy.load('en_core_web_sm')
        train=temp.copy()
        for index,string in temp.iterrows():
            string_limpio=""
            t=string[2].split()
            texto=""
            for a in t:
                texto+=a+" "
            doc = nlp(texto)
            for token in doc:
                if(token.pos_ not in tipos_no_acepted and token.text not in punct and token.text not in palabras_omitidas and token.text not in STOP_WORDS):
                    string_limpio+=token.lemma_+"{"+token.pos_+"}"+" "
            train.at[index,'texto_A_l']=string_limpio
        return train
    def getTokens(train,indice):
        #vocabulario
        big_string = ''
        for index,string in train.iterrows():
            a=string[indice].split()
            for pal in a:
                big_string += pal + " "
        #### to evaluate the size of the sample (N tokens, vocabulary v)
        string_list1 = big_string.split()
        M = len(string_list1)
        return string_list1,M
    