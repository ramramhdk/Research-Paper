#quetion 
def query_single(query):
    #print query
    i = 0 
    nnp1 = []
    vbz1=  []
    vbg1 = []
    vbd1 = []
    vbn1 = []
    vbp1 = []
    prp1 = []
    wp=[]
    wrb10 = []
    wit1=[]
    jj1=[]
    nn1=[]
    
    #tockenization
    tokenized = sent_tokenize(query)
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
     
        
        tagged1 = nltk.pos_tag(wordsList)
        
    
    #finding and extracting words
    v = len(tagged1)
    
    
    
    for i in range(v):
        if tagged1[i][1]=='NNP':
               j=tagged1[i][0]
               nnp1.append(j)
               
        elif tagged1[i][1]=='NN':
               j=tagged1[i][0]
               nn1.append(j)
               
        elif tagged1[i][1]=='VBZ':
             j=tagged1[i][0]
             vbz1.append(j)
            
             
        elif tagged1[i][1]=='VBG':
             j=tagged1[i][0]
             vbg1.append(j)
            
        elif tagged1[i][1]=='PRP':
             j=tagged1[i][0]
             prp1.append(j)
        
    
     
        elif tagged1[i][1]=='VBN':
             j=tagged1[i][0]
             vbn1.append(j)
             
        elif tagged1[i][1]=='VBP':
             j=tagged1[i][0]
             vbp1.append(j)
        
          
        elif tagged1[i][1]=='VBD':
             j=tagged1[i][0]
             vbd1.append(j)     
             
        elif tagged1[i][1]=='WRB':
             j=tagged1[i][0]
             wrb10.append(j)
             
        elif tagged1[i][1]=='WP':
             j=tagged1[i][0]
             wp.append(j)
             
        elif tagged1[i][1]=='IN':
             j=tagged1[i][0]
             wit1.append(j)           
        
        elif tagged1[i][1]=='IN':
             j=tagged1[i][0]
             wit1.append(j) 
             
        elif tagged1[i][1]=='JJS':
             j=tagged1[i][0]
             jj1.append(j)
             
        elif tagged1[i][1]=='JJ':
             j=tagged1[i][0]
             jj1.append(j)
             
