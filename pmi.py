import pandas as pd
import numpy as np
import math
class pmi():

    def __init__(self, text):
        self.text = text
    #
    def obtener_dicc_conteo(ventana,df,diccionario_conteo_word_word):
        for ind,j in df.iterrows():
            lwords=j[1].split()
            i=0
            while(i<len(lwords)):
                #print(lwords)
                conjunto_palabras=set(lwords[i:i+ventana])
                conjunto_palabras2=conjunto_palabras.copy()
                for word_i in conjunto_palabras:
                    conjunto_palabras2.remove(word_i)
                    for word_j in conjunto_palabras2:
                        if((word_i,word_j) in diccionario_conteo_word_word):
                            diccionario_conteo_word_word[(word_i,word_j)]+=1
                        elif((word_j,word_i) in diccionario_conteo_word_word):
                            diccionario_conteo_word_word[(word_j,word_i)]+=1
                        #else:
                        #    print("Tupla no encontrada: ",(word_i,word_j))
                i+=ventana    
        return diccionario_conteo_word_word
    def obtener_dicc_PMI(diccionario_conteo_word_word,diccionario_conteo_words,m):
        diccionario_PMI_word_word={}
        for clave in diccionario_conteo_word_word:
            w_i=clave[0]
            w_j=clave[1]
            #print("wi: ",w_i)
            #print("wj: ",w_j)
            
            x=(diccionario_conteo_word_word[clave] * m)/(diccionario_conteo_words[w_i]*diccionario_conteo_words[w_j])
            if(diccionario_conteo_word_word[clave]!=0):
                diccionario_PMI_word_word[clave]=np.log2(x)
        global diccionario_PMI_wordword
        diccionario_PMI_wordword = diccionario_PMI_word_word
        return diccionario_PMI_word_word

    def similarity_PMI(w1,w2,f1,f2,n,gamma,delta): 
        #obtener conjuntos de palabras que se repiten, (car,w) y (w,automobile)
        subc_w1=set()
        subc_w2=set()
        for clave in diccionario_PMI_wordword:
            #ws=clave.split(',')
            w_i=clave[0]
            w_j=clave[1]
            if(w1 in clave and diccionario_PMI_wordword[clave]>0.0):
                #print(clave,diccionario_PMI_word_word[clave])
                if(w_i==w1):
                    subc_w1.add(w_j)
                else:
                    subc_w1.add(w_i)
            if(w2 in clave and diccionario_PMI_wordword[clave]>0.0):
                if(w_i==w2):
                    subc_w2.add(w_j)
                else:
                    subc_w2.add(w_i)
        sub_inter=subc_w1.intersection(subc_w2)
        #b1=(math.log(f1)**2)*(math.log2(n)/delta)
        b1=len(subc_w1)
        #print(b1)
        #b2=(math.log(f2)**2)*(math.log2(n)/delta)
        b2=len(subc_w2)
        #print(b2)
        suma1=0
        suma2=0
        for e in sub_inter:
            if((w1,e) in diccionario_PMI_wordword):
                suma1+=diccionario_PMI_wordword[(w1,e)]**gamma
                #print(w1,e,diccionario_PMI_wordword[(w1,e)]**gamma)
            else:
                suma1+=diccionario_PMI_wordword[(e,w1)]**gamma
                #print(e,w1,diccionario_PMI_wordword[(e,w1)]**gamma)
            #print("suma1",suma1)
            if((e,w2) in diccionario_PMI_wordword):
                suma2+=diccionario_PMI_wordword[(e,w2)]**gamma
                #print(e,w2,diccionario_PMI_wordword[(e,w2)]**gamma)
            else:
                suma2+=diccionario_PMI_wordword[(w2,e)]**gamma
                #print(w2,e,diccionario_PMI_wordword[(w2,e)]**gamma)
            #print("suma2",suma2)
        if(b1==0):
            b1=1
        if(b2==0):
            b2=1

        #print("fb1: ",suma1/b2)
        #print("fb2: ",suma2/b1)
        #print("Similaridad_PMI: ",suma1/b2+suma2/b1)
        return suma1/b2+suma2/b1