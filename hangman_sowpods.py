with open('sowpods.txt', 'r') as f:
  line = f.readline()
  all_worlds=[]
  while line:
    all_worlds.append(line)
    line = f.readline()

"""
all_worlds =[n.replace('\n','') for n in all_worlds]
print(all_worlds[10])
"""
all_worlds=list(map(lambda x: x.replace('\n',""),all_worlds))

import random
word=list(random.choice(all_worlds))
 

a="_"*len(word) 

guess=list(a) 

print("Your word to guess has {} letters".format(len(guess))) 
counter=0
while guess!=word: 

    y=input("Type a letter\n").upper()   
    counter=counter+1
    for i in range (0,len(word)): 

        if word[i]==y: 

            guess[i]=y 

    print ("".join(guess))
    print ("That was your {}.try {}".format(counter,3))

