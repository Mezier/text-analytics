# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 02:03:13 2017

@author: Mezier
"""


import math
import nltk
def entropy(labels):
    freqdist=nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in freqdist]
    return -sum(p*math.log(p,2) for p in probs)
spamTextFile=open('F:/courses/COMP47600 text analytic/practice/practice 4/spam_Twitter.txt')
randomTextFile=open('F:/courses/COMP47600 text analytic/practice/practice 4/random_Twitter.txt')
spam_set=spamTextFile.read().split()
random_set=randomTextFile.read().split()
together=spam_set+random_set
print(entropy(spam_set))
print(entropy(random_set))
print(entropy(together))
