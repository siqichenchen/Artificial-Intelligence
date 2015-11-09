import os
import sys
import copy
inputFile=sys.argv[2]
outputFile='sentences_CNF.txt'
ope=['and','or','iff','implies','not']
fr=open(inputFile,'r')

#the number of sentences
totalLine=fr.readline()
totalLine=int(totalLine)

count=1

#remove iff
def RevIff(sentence):
    ind=0
    for item in sentence:
        if type(item)==list:
            item=RevIff(item)
            sentence[ind]=item
            #print 'aaa',item
        ind=ind+1

    if sentence[0]=='iff':
        newList1=[]
        newList1.append('implies')
        newList1.append(sentence[1])
        newList1.append(sentence[2])
        newList2=[]
        newList2.append('implies')
        newList2.append(sentence[2])
        newList2.append(sentence[1])
        newList3=[]
        newList3.append('and')
        newList3.append(newList1)
        newList3.append(newList2)
        sentence=newList3
    return sentence


#remove implies
def RevImp(sentence):
    #print sentence
    ind=0
    for item in sentence:
        if type(item)==list:
            item=RevImp(item)
            sentence[ind]=item
            #print 'aaa',item
        ind=ind+1
    if sentence[0]=='implies':
        newList1=[]
        newList1.append('not')
        newList1.append(sentence[1])
        newList3=[]
        newList3.append('or')
        newList3.append(newList1)
        newList3.append(sentence[2])
        sentence=newList3
    return sentence


#push negation download
def DownNeg(sentence):
    #print sentence
    ind=0
    for item in sentence:
        if type(item)==list:
            it=DownNeg(item)
            sentence[ind]=it
        ind=ind+1
    if sentence[0]=='not' and type(sentence[1])==str:
        return sentence
    if sentence[0]=='not' and type(sentence[1])==list:
        subSentence=sentence[1]
        if subSentence[0]=='and':
            newList=[]
            newList.append('or')
            newList.append(['not',subSentence[1]])
            newList.append(['not',subSentence[2]])
            sentence=newList
        elif subSentence[0]=='or':
            newList=[]
            newList.append('and')
            newList.append(['not',subSentence[1]])
            #print subSentence,'aaaa'
            newList.append(['not',subSentence[2]])
            sentence=newList
    ind=0
    for item in sentence:
        if type(item)==list:
            it=DownNeg(item)
            sentence[ind]=it
        ind=ind+1
    #print 'aaa',sentence
    
    return sentence

#remove double negation
def RevDoubleNeg(sentence):
    ind=0
    for item in sentence:
        if type(item)==list:
            item=RevDoubleNeg(item)
            sentence[ind]=item
        ind=ind+1
    if sentence[0]=='not'and type(sentence[1])==list:
        subSentence=sentence[1]
        if subSentence[0]=='not':
            sentence=subSentence[1]
    return sentence

#distribute and or
def Distri(sentence):
    ind=0
    newList=[]
    for item in sentence:
        if type(item)==list:
            item=Distri(item)
        newList.append(item)
        ind=ind+1
    sentence=copy.deepcopy(newList)
    if sentence[0]=='or':
        ind=0
        copyS=copy.deepcopy(sentence)
        for item in copyS:
            if type(item)==list:
                if item[0]=='and':
                    newList=[]
                    newList.append('and')
                    indd=0
                    for subItem in item:
                        subNewList=[]
                        if indd>0:
                            subNewList.append('or')
                            subNewList.append(subItem)
                            subInd=0
                            for otherItem in copyS:
                                if subInd!=ind and subInd!=0:
                                    subNewList.append(otherItem)
                                subInd=subInd+1
                            newList.append(subNewList)
                        indd=indd+1
                    sentence=newList
                    break
            ind=ind+1
    ind=0
    #print sentence
    
    newList2=[]
    for item in sentence:
        if type(item)==list:
            item=Distri(item)
        newList2.append(item)
        ind=ind+1
    return newList2

#after 5 standard steps above, we need a better format
#diminish or in [or [or A B]]
#diminish and in [and [and A B]]
def DiminishMultiOrAnd(sentence):
    ind=0
    for item in sentence:
        if type(item)==list:
            item=DiminishMultiOrAnd(item)
            sentence[ind]=item
        ind=ind+1
    copyS=copy.deepcopy(sentence)
    if sentence[0]=='or':
        for item in copyS:           
            if type(item)==list and item[0]=='or':
                subSentence=item
                subInd=0
                for subItem in subSentence:
                    if subInd>0:
                        sentence.append(subItem)
                    subInd=subInd+1
                sentence.pop(sentence.index(item))
    #print sentence
    copyS=copy.deepcopy(sentence)
    if sentence[0]=='and':
        for item in copyS:           
            if type(item)==list and item[0]=='and':
                #print 'bbb',item
                subSentence=item
                subInd=0
                for subItem in subSentence:
                    if subInd>0:
                        sentence.append(subItem)
                    subInd=subInd+1
                sentence.pop(sentence.index(item))
    #print 'aaa',sentence
    return sentence

#for argument cmp in sort function
def SortRule(a,b):
    if a in ope:
        return 1
    if b in ope:
        return -1
    if type(a)==type(b):
        if a<b:
            return 1
        else:
            return -1
    if type(a)==str:
        return 1
    else:
        return -1
#sort sentence use sort function
def SortSentence(sentence):
    ind=0
    for item in sentence:
        if type(item)==list:
            sentence[ind]=SortSentence(item)
        ind=ind+1
    sentence.sort(cmp=SortRule, key=None, reverse=True)
    return sentence

#delete duplicate in sentence
def DeleteDup(sentence):
    ind=0
    for item in sentence:
        if type(item)==list:
            sentence[ind]=DeleteDup(item)
        ind=ind+1
    newList=[]

    ind1=0
    for item1 in sentence:
        ind2=0
        flag=1
        for item2 in sentence:
            if ind2<=ind1:
                ind2=ind2+1
                continue
            if item1==item2:
                #print "haha"
                flag=0
                break
            ind2=ind2+1
        if flag==1:
            newList.append(item1)
        ind1=ind1+1
    return newList




#process every sentence:
fw=open(outputFile,'w')
lineNum=1
while count<=totalLine:
    print "processing line",lineNum
    lineNum=lineNum+1
    #print 'aaaaaaaa'
    strSentence=fr.readline()
    sentence=eval(strSentence)
    sentence=RevIff(sentence)
    sentence=RevImp(sentence)
    sentence=DownNeg(sentence)
    sentence=RevDoubleNeg(sentence)
    #print sentence
    sentence=Distri(sentence)
    #after 5 standard steps above, we need a better format
    #diminish or in [or [or A B]]
    #diminish and in [and [and A B]]
    sentence=DiminishMultiOrAnd(sentence)
    #sort
    sentence=SortSentence(sentence)
    #delete duplicate
    sentence=DeleteDup(sentence)
    
    count=count+1
    sentence=str(sentence)
    sentence=sentence.replace('\'','\"')
    fw.write(sentence+'\n')
fr.close()
fw.close()
