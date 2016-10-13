import re
from nltk import sent_tokenize

#patt1 = r"[\d\w]+[^\s\d\w]?[\d\w]+|[^\sa-zA-Z0-9]?|[\d\w]+[^\s\d\w]?[\d\w]+[^\s\d\w]?[\d\w]+"
#patt2 = r"[\d\w]+[^\s\d\w]?[\d\w]*[^\s\d\w]?[\d\w]+|^[^\s\w\d]?|[^\s\w\d]|[\d\w]"
#patt3 =r"([\w\d]+[^\s\w\d]*)+[\w\d]+|[^\s\w\d]|[\w\d]+|[\d\w]+[^\s\d\w]?[\d\w]*[^\s\d\w]?[\d\w]+"
patt4 = r"[\d]+%|\w\.\w\.\-[\w\d]+|[\d\w]+[^\s\d\w]?[\d\w]*[^\s\d\w]?[\d\w]+|[\d\w]+[^\s\d\w]?[\d\w]+|[^\s\w\d]|[\w\d]+|[\d\w]+[^\s\d\w]?[\d\w]*[^\s\d\w]?[\d\w]+"

def word_tokenizer(text,pattern):
    final_text = text.lstrip().rstrip()
    t_list_final = [t + '/TOK' for t in re.findall(pattern,final_text)]
    return ' '.join(t_list_final)

path ="C:\\Users\\aoguntuga\\Documents\\Sentiment Analysis Research\\Sentiment analysis iPython notebooks\\"
txt_file_path = path + "abstract.txt"
file_reader = open(txt_file_path,'rb')
txt_outfile_path = path + "adetomiwaTokenizedAbstract.txt"
file_writer = open(txt_outfile_path,'wb')
file_content = file_reader.read()
for sentence in sent_tokenize(file_content):
    #print sentence
    #print "......................................................................................................."
    #print word_tokenizer(sentence,patt4)
    #print "-------------------------------------------------------------------------------------------------------"
    file_writer.write(word_tokenizer(sentence,patt4))
    file_writer.write('\n')
file_reader.close()
file_writer.close()
print "Done!!!"