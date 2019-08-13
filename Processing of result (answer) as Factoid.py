# answer 
#function 1
def splitParagraphIntoSentences(paragraph):
    ''' break a paragraph into sentences
        and return a list '''
    import re
    # to split by multile characters

    #   regular expressions are easiest (and fastest)
    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList
 #function 2
def gh(x):
    p = x 
    sentences = splitParagraphIntoSentences(p)
    in_bound=[]
    for i in sentences:
       lt_i =[]
       lt_i=i.strip()+"."
       in_bound.append(lt_i)
    return in_bound
#function 3
def para_to_list(txt):
    in_bound=gh(txt)
    return in_bound
    print (len(in_bound)-1)
#funtion 3 will call function 1 and function 2



# create necessary list


b=[]
out_bound_i=[]
a_i=[]

#  tockenization

def chunker(x):
    tagged=x
    chunk = ne_chunk(tagged)
    #print("********************************************************************") 
    print chunk
    
    
    
    ne_in_sent =[]
    ne_out_sent=[]
    
    
    for subtree in chunk:
        if type(subtree) == Tree: # If subtree is a noun chunk, i.e. NE != "O"
            ne_label = subtree.label()
            ne_string = " ".join([token for token, pos in subtree.leaves()])
            ne_in_sent.append((ne_string, ne_label))
            
    g= len(ne_in_sent)
    
    
    
    i=0
    person=[]
    gpe=[]
    organization=[]
    for i in range(g):
        if ne_in_sent[i][1]=='PERSON':
          j=ne_in_sent[i][0]
          person.append(j)
        
        elif ne_in_sent[i][1]=='GPE':
          j=ne_in_sent[i][0]
          gpe.append(j)
        
        elif ne_in_sent[i][1]=='ORGANIZATION':
          j=ne_in_sent[i][0]
          organization.append(j)
