#logic

def lemm(verb0, verb1):
            
            stem1 = nltk.stem.WordNetLemmatizer().lemmatize(verb0[0], 'v')
            stem2 = nltk.stem.WordNetLemmatizer().lemmatize(verb1[0], 'v')
            print(stem1)
            print(stem2)
    
            if (stem1==stem2):
                stem=1
                y="stem are equal"
                return (y,stem)
            else:
                stem=0 
                n="stem are unequal"
                return (n,stem)
