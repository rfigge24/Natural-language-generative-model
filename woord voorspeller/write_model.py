# -*- coding: utf-8 -*-
"""
Created on Thu May 19 21:59:19 2022

@author: rfigg
"""
import os
import ngram_probability


def make_model(datafile, n, encoding="utf-8"):  
    #if ./models doesnt exist, creates one:
    if not os.path.exists("./models/"):
        os.makedirs("./models/")
            
    datafile_name = os.path.split(datafile)[1]
    datafile_name = os.path.splitext(datafile_name)[0]
    
    #reading in the corpus into a probabilitytable file        
    with open(datafile, "r", encoding=encoding) as conn:
        text = conn.read()
            
        probability_table = ngram_probability.ngram_probability_table(text, n)
        ngram_probability.write_probability_ngrams(
            probability_table, f"./models/{n}-{datafile_name}.txt")





if __name__ == "__main__":
    #make_model("./corpus.txt", 2)
    make_model("./sprookjes-cleaned.txt", 3)
