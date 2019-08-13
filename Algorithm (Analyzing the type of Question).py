def type_quest(person1,person,gpe1,gpe,quest,organization1,organization,prp1,jj1,jj_i,ptr,jjval,stem, cd_i):
    if quest[0]=='Where':
       print('A where question')
       v=len(gpe)
       u=len(organization)
       u1=len(organization1)
       p1=len(person1)
       p0=len(person)
       prp1len=len(prp1)
       c=[]
       print("Your answer is")
       if u==0 and v==0:
           print("inadequate question")
       elif p1>0 and p0>0:
          print("Person is available")
          for person1x in person1:
              if person1x in person:
                     c.append(person1x)
                     clen=len(c)
                     if clen>0:
                        print("Person found")
                        if (u==0 and v==0):
                          print("inadequate question")
                        else:
                         
                          print("Organization "+str(organization))
                          speak.Speak(organization)
                          print("GPE is "+str(gpe))
                          speak.Speak(gpe)
              else :
                   print("No data about this person")
       
       elif p0==0 and p1>0:
          print("Person not specified")
           
     
       elif  (v>0 or u>0) and prp1len>0:
           
              print("47")
              print( "Organization "+str(organization)) 
              speak.Speak(organization)
              print("GPE is "+str(gpe))   
              speak.Speak(gpe)
       elif u1>=1:
           print("heya")
           print v
           if v==0:
              print("Data not Provided Regarding the place")
           elif v>0:
              d=[]
              for organization1x in organization1:
                  if organization1x in organization:
                     d.append(organization1x)
                     dlen=len(d)
                     print(dlen)
                     if dlen>0:
                           print("Organization found")
                           print("GPE is "+str(gpe))
                           speak.Speak(gpe)
                  else:
                     print("Not Sufficiant Organization Data")
