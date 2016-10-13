import os
from nltk import word_tokenize,sent_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
import pandas as pd

def checker(bigrams):
    stop = set(stopwords.words('english'))
    #print stop
    l =[]
    for b in bigrams:
        if b[0].isalpha() and b[1].isalpha():
            if b[0].lower() in stop or b[1].lower() in stop:
                #print b
                continue
            else:
                l.append((b[0].lower(),b[1].lower()))
        else:
            continue
    return l

path = '/Users/blaknerd/Downloads/random_1000/'
list_of_files = os.listdir(path)

bigram_dict={}
ignore_list = ['out_mutual.txt','out_chisquare.txt','out_frequency.txt']
#temp_file_list =['10329137.txt']
#,'10329407.txt','10329502.txt'
for filr in list_of_files:
    if filr in ignore_list:
        continue
    else:
        input_file = path + filr
        file_handle = open(input_file,'rb')
        content = file_handle.read()
        file_handle.close()
        tokens = word_tokenize(content)
        bigrams = checker(ngrams(tokens,2))
        for big in bigrams:
            #print"................"
            #print big
            if bigram_dict.has_key(big):
                bigram_dict[big] = bigram_dict[big] + 1
            else:
                bigram_dict[big] = 1

#out_file_handle = open('out_frequency.txt','wb')
dict_list = [(key[0],key[1],bigram_dict[key]) for key in bigram_dict]
cols = ['Token_1','Token_2','Frequency']
df = pd.DataFrame(dict_list,columns = cols).sort_values(['Frequency'],axis=0,ascending=False)
df.to_csv('output_frequency.csv',sep ='\t',header=False,columns=cols,index=False)
print "Done"