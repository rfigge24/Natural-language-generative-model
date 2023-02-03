# -*- coding: utf-8 -*-
"""
Created on Thu May 19 21:17:18 2022

@author: rfigg
"""
from ngram_probability import readprobability_ngrams
import sys

class Predicter:
    def __init__(self, model_file):
        self.n_min_one2ngram_dict = None
        self.ngram_probability_table = readprobability_ngrams(model_file)
        if len(list(self.ngram_probability_table.keys())[0]) > 1:
            self.n_min_one2ngram_dict = dict()
            for ngram in self.ngram_probability_table:
                if not ngram[:-1] in self.n_min_one2ngram_dict:
                    self.n_min_one2ngram_dict[ngram[:-1]] = [ngram]
                else:
                    self.n_min_one2ngram_dict[ngram[:-1]].append(ngram)

    def predict_nextword(self, string):
        lastword = string.split()[-1]

        if (lastword,) in self.n_min_one2ngram_dict:
            followingwords = self.n_min_one2ngram_dict[(lastword,)]
            followingw = [(wp1, self.ngram_probability_table[(w,wp1)]) for w,wp1 in self.n_min_one2ngram_dict[(lastword,)]]
            followingw.sort(key= lambda x: x[1], reverse = True)
            nextword = followingw[0][0]
            print(nextword)
            if len(followingw) > 1:
                print(followingw[1][0])
            if len(followingw) > 2:
                print(followingw[2][0])
        else:
            print("cannot predict a next word !")
        

#tests and other stuff:

predict2 = Predicter("./models/2-sprookjes-cleaned.txt")

if __name__ == "__main__":
    predict2.predict_nextword(sys.argv[1])