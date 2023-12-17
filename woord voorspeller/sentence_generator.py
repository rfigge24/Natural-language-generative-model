# -*- coding: utf-8 -*-
"""
Created on Thu May 19 21:17:18 2022

@author: rfigg
"""
import random
from ngram_probability import readprobability_ngrams


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


#-----------------------------------------------------------------
# Models currently in use:
#-----------------------------------------------------------------

predict2 = Predicter("./models/2-Het-Boek-cleaned.txt")
predict3 = Predicter("./models/3-Het-Boek-cleaned.txt")
predict4 = Predicter("./models/4-Het-Boek-cleaned.txt")



def gen_first_word():

    startwords = predict2.n_min_one2ngram_dict[('<s>',)]
    startwordspobability = tuple([predict2.ngram_probability_table[ngram] for ngram in startwords])

    chosenngram = random.choices(startwords, weights=startwordspobability)[0]
    return chosenngram

def gen_second_word(old_ngram):

    startwords = predict3.n_min_one2ngram_dict[old_ngram]
    startwordspobability = tuple([predict3.ngram_probability_table[ngram] for ngram in startwords])

    chosenngram = random.choices(startwords, weights=startwordspobability)[0]
    return chosenngram

def gen_thirt_word(old_ngram):

    startwords = predict4.n_min_one2ngram_dict[old_ngram]
    startwordspobability = tuple([predict4.ngram_probability_table[ngram] for ngram in startwords])

    chosenngram = random.choices(startwords, weights=startwordspobability)[0]
    return chosenngram


#-----------------------------------------------------------------

# Usable functions from the console to generate sentences:

#-----------------------------------------------------------------
def gensentence_3grams():
    old_ngram = None
    sentence = ""
    
    firstwords = gen_first_word()
    sentence += " ".join(firstwords)
    old_ngram = firstwords
    
    while old_ngram[-1] != "</s>":
        nextwords = gen_second_word(old_ngram)
        sentence += " " + nextwords[-1]
        old_ngram = nextwords[1:]
        
    print(sentence)

def gensentence_4grams():
    old_ngram = None
    sentence = ""
    
    firstwords = gen_first_word()
    sentence += " ".join(firstwords)
    old_ngram = firstwords
    
    secondwords = gen_second_word(old_ngram)
    sentence += " " + secondwords[-1]
    old_ngram = secondwords
    
    while old_ngram[-1] != "</s>":
        nextwords = gen_thirt_word(old_ngram)
        sentence += " " + nextwords[-1]
        old_ngram = nextwords[1:]
        
    print(sentence)
    
