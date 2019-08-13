def splitter(D_text,Q_text):
    
    def splitParagraphIntoSentences(paragraph):
        ''' break a paragraph into sentences
            and return a list '''
        import re
        # to split by multile characters
    
        #   regular expressions are easiest (and fastest)
        sentenceEnders = re.compile('[.!?]')
        sentenceList = sentenceEnders.split(paragraph)
        return sentenceList
     
    def gh(x):
        p = x 
        sentences = splitParagraphIntoSentences(p)
        in_bound=[]
        for i in sentences:
           lt_i =[]
           lt_i=i.strip()+"."
           in_bound.append(lt_i)
        return in_bound
    word_list=[]
    def split_line(query):
        words=query.split()
        #word_list=words
        l=len(words)
        #for i in range (l):
            #word_list[i]=words[0]
        
    
        a= words[0]
        txt=""
        for word in words:
            txt=txt+word+" "
        #print txt
        
        
        tt=txt.lstrip(a+" ")
        l2=len(tt)
        word_list=tt.split()
        return word_list
