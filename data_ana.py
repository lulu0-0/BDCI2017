#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pds
import os
import numpy as np
from numpy import *

cur_path = os.getcwd()
filename = os.path.join(cur_path,'data\\train.csv')
data_x = pds.read_csv(filename, encoding='utf-8')
#print(data_x)
title_list = data_x.head(0)
#print(title_list)
sentiment_word = data_x[['sentiment_word-情感关键词']]
#print(shape(sentiment_word))
sent_word_total = {}
for i in range(shape(sentiment_word)[0]):
    s = str(sentiment_word._ixs(i))
    sp = s.strip()[24:].split(';')
    sp.pop()
    #print(sp)
    for word in sp:
        word = str(word)
        #print(word)
        if word in sent_word_total.keys():
            sent_word_total[word] += 1
        else:
            sent_word_total[word] = 1
print(sent_word_total)
print()
