#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk


# In[3]:


text = nltk.word_tokenize("And now for something compeletly different")


# In[4]:


nltk.pos_tag(text)


# In[5]:


text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")


# In[6]:


nltk.pos_tag(text)


# In[7]:


text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())


# In[8]:


text.similar('woman')


# In[9]:


text.similar('bought')


# In[10]:


text.similar('over')


# In[11]:


text.similar('the')


# In[12]:


tagged_token = nltk.tag.str2tuple('fly/NN')


# In[13]:


tagged_token


# In[14]:


tagged_token[0]


# In[15]:


tagged_token[1]


# In[16]:


sent = 'They refuse to permit us to obtain the refuse permit'


# In[19]:


[nltk.tag.str2tuple(t) for t in sent.split()]


# In[22]:


nltk.corpus.brown.tagged_words()


# In[23]:


nltk.corpus.nps_chat.tagged_words()


# In[24]:


nltk.corpus.conll2000.tagged_words()


# In[25]:


nltk.corpus.treebank.tagged_words()


# In[26]:


nltk.corpus.brown.tagged_words(simplyfy_tags=True)


# In[27]:


nltk.corpus.brown.tagged_words(tagset='universal')


# In[28]:


nltk.corpus.brown.tagged_words(tagset='universal')[:10]


# In[29]:


nltk.corpus.treebank.tagged_words(tagset='universal')[:10]


# In[30]:


from nltk.corpus import brown


# In[31]:


brown_tagged_sents = brown.tagged_sents(categories='news')


# In[32]:


brown_sents = brown.sents(categories='news')


# In[33]:


tags = [tag for (word, tag) in brown.tagged_words(categories='news')]


# In[35]:


nltk.FreqDist(tags).max()


# In[36]:


brown_tagged_sents


# In[37]:


brown_sents


# In[38]:


raw1 = 'I do not like this food and that dish, I do not like them Jack'


# In[39]:


tokens = nltk.word_tokenize(raw1)


# In[41]:


deafualt_tagger = nltk.DefaultTagger('NN')


# In[43]:


deafualt_tagger.tag(tokens)


# In[44]:


deafualt_tagger.evaluate(brown_tagged_sents)


# In[50]:


import re


# In[51]:


patters = [
    (r'.*ing$', 'VGB'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ould$', 'MD'),
    (r'.*\'s$', 'NN$'),
    (r'.*s$', 'NNS'),
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
    (r'.*', 'NN'),
]


# In[52]:


regex_tagger = nltk.RegexpTagger(patters)


# In[54]:


regex_tagger.tag(brown_sents[3])


# In[57]:


regex_tagger.accuracy(brown_tagged_sents)


# In[58]:


from nltk.corpus import brown


# In[59]:


unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)


# In[60]:


unigram_tagger.tag(brown_sents[2007])


# In[61]:


unigram_tagger.accuracy(brown_tagged_sents)


# In[68]:


main_size = int(len(brown_tagged_sents))
main_size


# In[69]:


size = int(len(brown_tagged_sents)*0.9)
size


# In[70]:


train_sents = brown_tagged_sents[:size]


# In[71]:


test_sents = brown_tagged_sents[size:]


# In[72]:


unigram_tagger = nltk.UnigramTagger(train_sents)


# In[73]:


unigram_tagger.evaluate(test_sents)


# In[74]:


bigram_tagger = nltk.BigramTagger(train_sents)


# In[75]:


bigram_tagger.tag(brown_sents[2007])


# In[76]:


unseen_sent = brown_sents[4203]


# In[77]:


bigram_tagger.tag(unseen_sent)


# In[79]:


bigram_tagger.accuracy(test_sents)


# In[80]:


test_tags = [tag for sent in brown.sents(categories='editorial') 
            for (word, tag) in t2.tag(sent)]


# In[ ]:




