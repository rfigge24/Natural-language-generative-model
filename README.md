# N-gram-based Sentence generator

## includes:
1. Corpus prepocessing for two corpus files
2. Model Setup tool
3. Next word predictor
4. Sentence predictor

### Next word predictor:
The Next word predictor works as following: 
```python word_predicter.py "sentence it has to predict the next word of"```
the result is the top-3 words with the highest probability to follow the word "of"
```
1. die
2. zij
3. het
```
If there are not enough next words the model will either show the top 2, top 1, or a message telling you that it could not predict a next word.

### Sentence generator:
The sentence generator only work for an IDE where you can run script functions in the console.<br>
It works as following:<br>
First you have to select the models you want to use:<br>
```python
#-----------------------------------------------------------------
# Models currently in use:
#-----------------------------------------------------------------

predict2 = Predicter("./models/2-Het-Boek-cleaned.txt")
predict3 = Predicter("./models/3-Het-Boek-cleaned.txt")
predict4 = Predicter("./models/4-Het-Boek-cleaned.txt")
```

Then you can use one of the following functions to generate a sentence:
```
gensentence_3grams()
gensentence_4grams()
```
The model predicts a next word using the ngrams, ngrams that apply to the latest generated words are selected (\<n-1 last generated words, next word\>). From this ngram pool 1 ngram is selected randomly. 
The ngrams have a weighted probability based on their occurance in the fitted corpus.

### model fitting
Using the ```model_write.py``` module you can fit a model to a cleaned corpus by replacing the file path on the bottom.
Make sure your corpus only contains sentences. If not the model will also generate the headers and other bload text.

For the 2 corpora included there are preprocessing modules, to use your own corpus you may have to create one of your own.
