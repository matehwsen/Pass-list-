# fisrt step 
# initialize files
# you should make these files(1.txt and 2.txt) with these names 
# or make what you want just put the same name on them !
# but remember to name them 
one=(open('1.txt', 'r')).readlines() #names
two=(open('2.txt', 'r')).readlines() #symbols
three=(open('3.txt', 'r')).readlines() #numbers
#making the wordlist
wordlist=[]
for word1 in one:
    for word2 in two:
        for word3 in three:
            new1=word1+word2+word3
            #new2=word3+word2+word1
            #new3=word2+word3+word1
            wordlist.append(new1)
            #wordlist.append(new2)
            #wordlist.append(new3)
prin("making wordlist finished...trying to arrange them.. ")


#arrange the wordlist
wordlist = [item.replace('\r', '').replace('\n', '') for item in wordlist]
print (wordlist)
#print('the wordlist you made:\n',wordlist)
WordList='\n'.join(wordlist)
Wlist=open('wordlist.txt','w')
Wlist.write(WordList)
print("SAVED to ----> 'wordlist.txt' ")