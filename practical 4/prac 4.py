# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 12:15:25 2017

@author: Mezier
"""
import collections
import math
from nltk import bigrams
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from itertools import tee, islice
initialTextFile=open('F:/courses/COMP47600 text analytic/practice/practice 4/p4.txt')
initialText=initialTextFile.read()
'''
stop_words=set(stopwords.words('english'))
word_tokens=word_tokenize(initialText)
filtered_text=[w for w in word_tokens if not w in stop_words]
filtered_text=[]
for w in word_tokens:
    if w not in stop_words:
        filtered_text.append(w)
'''

t1=initialText.split()
t2=collections.Counter(t1)
t3=collections.Counter(bigrams(t1))
t4=sum(t2[x]for x in t2)
t5=sum(t3[x]for x in t3)
t6={x:float(t2[x])/t4 for x in t2}  # word probability(w1 and w2)
t7={x:float(t3[x])/t5 for x in t3}  # joint probability(w1&w2)
u={}
v={}
for x in t6:
    k={x:round(math.log((t7[b]/(t6[x]*t6[y])),2),4) for b in t7 for y in t6 if x and y in b}
    u[x]=k[x]
    k={x:round(math.log((t7[b]/(t6[x]*t6[y])),2),4) for b in t7 for y in t6 if x in b and y in b}
    v[x]=k[x]
    

     