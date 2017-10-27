#!/usr/bin/python3
#coding=utf-8

import jieba
import pandas as pd

filename = "./data/train.csv"
data = pd.read_csv(filename, encoding="utf-8")
content = data['content-评论内容']

with open('./data/train_cut.txt', 'w') as f:
    for i in range(len(content)):
        seg_list = jieba.cut(content[i], cut_all=False)
        f.write('/'.join(seg_list) + '\n')

