from nltk.corpus import wordnet as wn
from nltk import word_tokenize,sent_tokenize
import pandas as pd
import numpy as np

def max_similarity_score(syn_sets,syn_set):
    max_score = None
    #print 'About to start comparison'
    for s in syn_sets:
        if s.name().split('.')[0] == syn_set.name().split('.')[0]:
            return 0.0
        #print s
        #print syn_set
        sim_score = s.wup_similarity(syn_set,simulate_root =False)
        
        if max_score == None or max_score < sim_score:
            max_score = sim_score
            #print max_score
    #print 'Done'
    if max_score:
        return max_score
    else:
        return 0.0

def categorize_intermediate(text,category):
    text_tokens = word_tokenize(text)
    category_name = category.name().split('.')[0]
    max_similarity_list =[]
    
    for token in text_tokens:
        token_synsets = wn.synsets(token)
        max_score = max_similarity_score(token_synsets,category)
        max_similarity_list.append(max_score)
    return pd.Series(max_similarity_list,index = text_tokens,name = category.name()).max()

def categorize(text):
    cat_dict = {'cold.n.01':'DISEASE',
                'cold.n.02':'LOW TEMPERATURE',
                'coldness.n.03':'LOW TEMPERATURE',
                'None':'UNDETERMINED'}
    cats =['cold.n.01','cold.n.02']
    categories = [wn.synset(cats[0]),wn.synset(cats[1])]
    d ={}
    for category in categories:
        d[category.name()] = categorize_intermediate(text,category)
    ser1 = pd.Series(d.values(),index = d.keys())
    ser2 = ser1.sort_values(ascending=False)
    if ser2.ix[0] == ser2.ix[1]:
        return 'None'
    else:
        g_dict = ser2.to_dict()
        key = None
        max_k = None
        for k in g_dict:
            if max_k == None or max_k < g_dict[k]:
                max_k = g_dict[k]
                key = k
        #return (key,max_k)
        #return g_dict
        return cat_dict[key]

file_path = "/Users/blaknerd/Documents/HI6330/cold_set.txt"
file_reader = open(file_path,'rb')
file_content = file_reader.read()
file_write = open("/Users/blaknerd/Documents/HI6330/hw2OutputAdetomiwa.txt",'wb')

sentences = sent_tokenize(file_content)
for sent in sentences:
    output = "%s:%s" % (categorize(sent),sent)
    file_write.write(output)
    file_write.write("\n")
    file_write.write("--------------------------------------------------------------------------------")
    file_write.write("\n\n")
file_reader.close()
file_write.close()
print "Done!!!"
 