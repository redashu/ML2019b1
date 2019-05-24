#!/usr/bin/env python
# coding: utf-8

# In[14]:


# assume some facts  or  data  with features about  apple and orange 
          #  weight , texture 
features=[[120,0],[130,0],[140,0],[145,1],[150,1],[160,1]]
#  here  0 means smooth  and  1 means bumpy


# In[13]:


#  labels  or answer 
label=["apple","apple","apple","orange","orange","orange"]
#label1=[2,2,2,3,3,3]


# In[5]:


#  to use algo in ML we need to install scikit learn
#!sudo pip3  install sklearn 
# lets confirm
#!sudo pip3 list    |   grep -i sklearn


# In[6]:


#  lets call any of the classifier desicion tree
from  sklearn  import  tree


# In[10]:


#  let explore  creating decision tree classifier 
#dir(tree)
clf=tree.DecisionTreeClassifier()


# In[15]:


#  time for  allocating  data to classifier ---  for training of Decision Tree
trained=clf.fit(features,label)
#        Q  &     A


# In[17]:


#  time  for asking  question 
output=trained.predict([[150,0]])
print(output)


# In[ ]:




