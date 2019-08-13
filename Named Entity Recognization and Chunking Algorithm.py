chunk1 = ne_chunk(tagged1)
          
    
    ne_in_sent1 = []
    for subtree in chunk1:
        if type(subtree) == Tree: # If subtree is a noun chunk, i.e. NE != "O"
            ne_label = subtree.label()
            ne_string = " ".join([token for token, pos in subtree.leaves()])
            ne_in_sent1.append((ne_string, ne_label))
            
            
    g= len(ne_in_sent1)
    
    
    
    i=0
    person1=[]
    gpe1=[]
    organization1=[]
    for i in range(g):
        if ne_in_sent1[i][1]=='PERSON':
          j=ne_in_sent1[i][0]
          person1.append(j)
        
        elif ne_in_sent1[i][1]=='GPE':
          j=ne_in_sent1[i][0]
          gpe1.append(j)
          
        elif ne_in_sent1[i][1]=='ORGANIZATION':
          j=ne_in_sent1[i][0]
          organization1.append(j)  
          
    verb1=[]
    verb1.extend(vbd1)
    verb1.extend(vbg1)
    verb1.extend(vbz1)
    verb1.extend(vbn1)
    verb1.extend(vbp1)
      
    quest=[]
    quest.extend(wp)
    quest.extend(wrb10)
    
    
    print("question is " +str(quest))    
    
    
    
          
         
    print("Person is  "+ str(person1) ) 
    print("GPE is  "+ str(gpe1) )
    print("Organization is  "+ str(organization1))
    print("verb "+ str(verb1) )    
    print("Question "+ str(quest )) 
    
    
    return (verb1,nnp1,prp1,nn1,jj1,quest ,person1,gpe1,organization1 )
