# -*- coding: utf-8 -*-
"""
Created on Thu May 19 19:04:14 2022

@author: rfigg
"""
from collections import Counter
import re

def preparetext(text):
    
    #split the text into sentences: the easy way:
    sentence_list = re.split(r"""[!?.]"?\s+""", text)
    
    #clean the sentences:
    for i in range(len(sentence_list)):
        cleanedstring = sentence_list[i]
        for c in """",()<>""":
            cleanedstring = cleanedstring.replace(c, " ")   
        sentence_list[i] = cleanedstring
                                
    return sentence_list





def word_ngrams(sentence_list, n=2):
    ngram_list = []
    
    for sentence in sentence_list:
        wordslist = sentence.split()
        for i in range(len(wordslist) - n+1):
            ngram_list.append(tuple(wordslist[i:i+n]))
        
    return ngram_list





def ngram_count_table(text, n=2):
    count_table = Counter()
    sentence_list = preparetext(text)
    
    #adding begin and end sentence markers <s> and </s>
    for i in range(len(sentence_list)):
        sentence_list[i] = "<s> " + sentence_list[i] + " </s>"
    
    ngram_list = word_ngrams(sentence_list, n)
    
    for ngram in ngram_list:
        count_table[ngram] +=1
      
    return count_table
    


    

def ngram_probability_table(text, n=2):
    probability_table = Counter()
    count_table_for_n = ngram_count_table(text, n)
    
    if n > 1:
        count_table_for_n_min1 = ngram_count_table(text, n-1)
        
        for ngram, count in count_table_for_n.items():
            probability_table[ngram] = count / count_table_for_n_min1[ngram[:n-1]]
    
    if n <= 1:
        total_count = 0
        for v in count_table_for_n.values():
            total_count += v
        
        for ngram, count in count_table_for_n.items():
            probability_table[ngram] = count / total_count
    
    return probability_table






def write_probability_ngrams(probability_table, filename):
    with open(filename, "w", encoding="utf-8") as outfile:
        for k, v in probability_table.items():
            linestr = f"{v}"
            for word in k:
                linestr += f" {word}"
            outfile.write(linestr + "\n")






def readprobability_ngrams(filename):
    probability_table = Counter()
    with open(filename, "r", encoding="utf-8") as readingfile:
        for line in readingfile:
            parts_list = line.split()
            
            #check if the line contains 2 parts with the first being a digit:
            if isfloat(parts_list[0]):
                probability_table[tuple(parts_list[1:])] = float(parts_list[0])

    return probability_table






def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
