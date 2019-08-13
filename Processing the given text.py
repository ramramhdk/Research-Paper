def fun():
    speak.Speak('Hello! Deepak Tripathi, I am Robot, I am currently working for you.')
    #question
    #print "Your question is ..."
    #print "\n"
    x="John is playing football in America. Steve was born at 25/04/1900. Tom is living in America.Tom cruise is a goood person.Paris is the capital of france. Paris is good place. Tata is a well known person"
    y='when was Steve born'
    print "Your question is =" 
    speak.Speak("Your question is ")
    print y
    speak.Speak(y)
    #print ' '
    A_ans = splitter(x,y)
    speak.Speak('Your Approximate answer is ...')
    speak.Speak(A_ans)
    txt=A_ans
    global a
    a=txt
    
    #print A_ans
    
    # text is given 
    txt = str(A_ans)
    #print "a"
    print txt
    query = y
    verbQ,nnp1,prp1,nn1,jj1,quest ,person1,gpe1,organization1=query_single(query)
    
    print "***********************Text processing starts.*******************************"
    speak.Speak(" Text processing starts to find the factoid answer of your question on approximate answer")
    speak.Speak(" The answer is ..")
    #para to list of sentences
    in_bound=para_to_list(txt)
    
    m=len(in_bound)
    
    #tokenization for single sentences
    for i in range(m-2):
        part=str(in_bound[i])
        print part
        nnp_i=[]
        vbz_i=[]
        vbd_i=[]
        vbg_i=[]
        vbn_i=[]
        vbp_i=[]
        prp_i=[]
        wit_i=[]
        jj_i= []
        nn_i= []
        cd_i=[]
        tokenized = sent_tokenize(part)
        for i in tokenized:
            wordsList = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(wordsList)
