#!/usr/bin/python3
#coding=utf-8

import jieba.posseg as pseg
import pandas as pd

filename = "./data/train.csv"
data = pd.read_csv(filename, encoding="utf-8")
content = data['content-评论内容']

with open('./data/train_cut.txt', 'w') as f:
    for i in range(len(content)):
        seg_list = pseg.cut(content[i])
        words = []
        for word, flag in seg_list:
            words.append(word + '/' + flag)
        f.write(' '.join(words) + '\n')

