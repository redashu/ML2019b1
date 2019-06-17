# -*- coding: utf-8 -*-
"""nlppp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jZTb52rru0DXGqV8Qvb033lLyVxfb3Mw
"""

import  nltk
#nltk.download('all')

from   nltk.corpus  import   stopwords

stopw=[i for  i  in   stopwords.words('english')]
stopw[:10]

from    nltk.tokenize  import  sent_tokenize,word_tokenize
from   nltk.stem  import  WordNetLemmatizer   #  for lemmatization 
from   nltk.stem   import  PorterStemmer   #  for stemming

data="i am doing  great sometimes then i use feet to do not know"

wtoken=word_tokenize(data)  #  word tokenize  -- on behalf of space  sep words

#  removing  stopwords 
removesw=[word for  word  in   wtoken  if  word not in  stopw]
removesw

#  stemming 
ps=PorterStemmer()
for  i  in  removesw:
  print("stemming of word is  ",ps.stem(i))

#  now its time for lemmatization 
lem=WordNetLemmatizer()
for  i  in  removesw:
  print("lemma of  word  is  ",lem.lemmatize(i))