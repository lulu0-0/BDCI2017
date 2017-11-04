#!/usr/bin/python3
#coding=utf-8

import jieba.analyse
import jieba.posseg as pseg
import pandas as pd

def cut(content, fn):
    with open(fn, 'w') as f:
        for i in range(len(content)):
            seg_list = pseg.cut(content[i])
            words = []
            for word, flag in seg_list:
                words.append(word + '/' + flag)
            f.write(' '.join(words) + '\n')


def cutTrain():
    filename = "./data/train.csv"
    data = pd.read_csv(filename, encoding="utf-8")
    content = data['content-评论内容']
    cut(content, './data/train_cut.txt')
    

def cutTest():
    filename = './data/test.csv'
    data = pd.read_csv(filename, encoding="utf-8", header=None)
    data = data.iloc[:,1]
    jieba.load_userdict("./data/user_dict.txt")
    cut(data, './data/test_cut.txt')


if __name__ == '__main__':
    cutTest()
