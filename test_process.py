#!/usr/bin/python3
#coding=utf-8

import pandas as pd

def analyse_words():
    '''only detect the noun before the adj and behind the last adj
    '''

    noun = []
    adj = []
    
    for line in open('./data/test_cut.txt'):
        seg = line[:-1].split(' ');
        while True:
            try:
                ind = seg.index('')
                seg.remove('')
                seg[ind] = '' + seg[ind]
            except:
                break
        i = -1
        seg_noun = []
        seg_adj = []
        for k in range(len(seg)):
            if seg[k].split('/')[1] == 'a':
                seg_adj.append(seg[k].split('/')[0])
                flag = 0
                for j in range(k, i, -1):
                    if seg[j].split('/')[1] == 'x':
                        seg_noun.append('NULL')
                        i = j
                        flag = 1
                        break
                    elif seg[j].split('/')[1] == 'n':
                        i = j
                        seg_noun.append(seg[j].split('/')[0])
                        flag = 1
                        break
                if not flag:
                    seg_noun.append('NULL')
    
        noun.append(seg_noun)
        adj.append(seg_adj)
    
    return (noun, adj)

def analyse_sentiment(adjs):
    pos = []
    neg = []

    for line in open('./words/negative(10018).txt'):
        neg.append(line[:-2])
    for line in open('./words/positive(18989).txt'):
        pos.append(line[:-2])

    sentis = []

    for adj in adjs:
        senti = []
        for a in adj:
            if a in pos:
                senti.append('1')
            elif a in neg:
                senti.append('-1')
            else:
                senti.append('0')
        sentis.append(senti)
    
    return sentis




if __name__ == '__main__':
    (noun, adj) = analyse_words()
    sentis = analyse_sentiment(adj)

    for i in range(len(noun)):
        noun[i] = ';'.join(noun[i])
        if noun[i]:
            noun[i] += ';'
    for i in range(len(adj)):
        adj[i] = ';'.join(adj[i])
        if adj[i]:
            adj[i] += ';'
    for i in range(len(sentis)):
        sentis[i] = ';'.join(sentis[i])
        if sentis[i]:
            sentis[i] += ';'

    df_test = pd.read_csv('./data/test.csv', names=['row_id', 'content-评论内容'])
    df_test['theme-主题'] = noun
    df_test['sentiment_word-情感关键词'] = adj
    df_test['sentiment_anls-情感正负面'] = sentis

    df_test.to_csv('./data/result.csv', index=False)
