import sys
import decimal
import copy

#raad input
inputFile=open(sys.argv[2])

#open output
outputFile=open("sample_input3_inference.txt","wb")

diseasename={}

disease=dict()
dissymp=dict()
p=dict()
notp=dict()
question1=dict()
question2=dict()
question3=dict()

#read input info
line=inputFile.readline()
#first line, get disnum and patnum
num=line.split(" ")
disnum=int(num[0])
patnum=int(num[1])

#read disease infomation
print "disease part infomation"
for i in range(0,disnum):
    #disease name symptom num prio probability
    line=inputFile.readline()
    disinfo=line.split(" ")
    disname=disinfo[0]
    diseasename[i]=disname
    symtomnum=int(disinfo[1])
    disease[disname]=float(disinfo[2])

    #symptom name
    line=inputFile.readline()
    symtom=eval(line)
    dissymp[disname]=symtom

    #conditional probability
    line=inputFile.readline()
    probability=eval(line)
    psym=dict()
    for i in range(0,symtomnum):
        psym[symtom[i]]=probability[i]
    p[disname]=psym

    #not probabiligy
    line=inputFile.readline()
    probability=eval(line)
    psym=dict()
    for i in range(0,symtomnum):
        psym[symtom[i]]=probability[i]
    notp[disname]=psym


#read patient infomation
print "paitient part information"
for i in range(1,patnum+1):
    index=str(i)
    string="Patient-"+index+":\r\r\n"
    print string
    outputFile.write(string)
    for j in range(0,disnum):
        #disease j
        disname=diseasename[j]
        symptom=dissymp[disname]
        line=inputFile.readline()
        thisp=p[disname]
        thisnotp=notp[disname]
        Finding=eval(line)
        upper=disease[disname]
        down=1-disease[disname]
        newFind2=list()
        for k in range(0,len(symptom)):
            if Finding[k]=="T":
                #if the symptom exists
                upper=thisp[symptom[k]]*upper
                down=thisnotp[symptom[k]]*down
            elif Finding[k]=="F":
                #if the symptom not exists
                upper=upper*(1-thisp[symptom[k]])
                down=down*(1-thisnotp[symptom[k]])

        #question2
        haveU=0
        for k in range(0,len(symptom)):
            if k==0:
                temp=list()
                if Finding[k]=="U":
                    temp.append("T")
                    newFind2.append(temp)
                    temp=list()
                    temp.append("F")
                    newFind2.append(temp)
                else:
                    temp.append(Finding[k])
                    newFind2.append(temp)
            else:
                if Finding[k]=="T":
                    for m in range(0,len(newFind2)):
                        newFind2[m].append(Finding[k])
                elif Finding[k]=="F":
                    for m in range(0,len(newFind2)):
                        newFind2[m].append(Finding[k])
                elif Finding[k]=="U":
                    haveU+=1
                    length=len(newFind2)
                    for m in range(0,length):
                        temp=copy.deepcopy(newFind2[m])
                        temp.append("F")
                        newFind2[m].append("T")
                        newFind2.append(temp)
        
        result1=upper/(upper+down)
        resultstr=str(decimal.Decimal("%.4f" % float(result1)))
        orgupper=upper
        orgdown=down

        if haveU==0:
            temp=list()
            temp.append(resultstr)
            temp.append(resultstr)
            question2[disname]=temp
        else:
            minp=1
            maxp=0
            for k in range(0,len(newFind2)):
                upper=disease[disname]
                down=1-disease[disname]
                for m in range(0,len(symptom)):
                    if newFind2[k][m]=="T":
                        #if the symptom exists
                        upper=thisp[symptom[m]]*upper
                        down=thisnotp[symptom[m]]*down
                    elif newFind2[k][m]=="F":
                        #if the symptom not exists
                        upper=upper*(1-thisp[symptom[m]])
                        down=down*(1-thisnotp[symptom[m]])
                result=upper/(upper+down)
                if minp>result:
                    minp=result
                if maxp<result:
                    maxp=result
            temp=list()
            minp=str(decimal.Decimal("%.4f"%float(minp)))
            maxp=str(decimal.Decimal("%.4f"%float(maxp)))
            temp.append(minp)
            temp.append(maxp)
            question2[disname]=temp

        #question3
        maxdecrease=0
        maxincrease=0
        temp=list()
        if haveU==0:
            temp=['none','N','none','N']
            question3[disname]=temp
        else:
            temp=['none','N','none','N']
            for k in range(0,len(symptom)):
                if Finding[k]=="U":
                    upperT=orgupper*thisp[symptom[k]]
                    downT=thisnotp[symptom[k]]*orgdown
                    resultT=upperT/(upperT+downT)
                    upperF=orgupper*(1-thisp[symptom[k]])
                    downF=orgdown*(1-thisnotp[symptom[k]])
                    resultF=upperF/(upperF+downF)
                    if resultT<result1:
                        dif=result1-resultT
                        if dif==maxdecrease and dif!=0:
                            #alphabetical order
                            if cmp(symptom[k],temp[2])==-1:
                                temp[2]=symptom[k]
                                temp[3]="T"
                        if dif>maxdecrease:
                            maxdecrease=dif
                            temp[2]=symptom[k]
                            temp[3]="T"
                    if resultT>result1:
                        dif=resultT-result1
                        if dif==maxincrease and dif!=0:
                            #alphabetical order
                            if cmp(symptom[k],temp[0])==-1:
                                temp[0]=symptom[k]
                                temp[1]="T"
                        if dif>maxincrease:
                            maxincrease=dif
                            temp[0]=symptom[k]
                            temp[1]="T"
                    if resultF<result1:
                        dif=result1-resultF
                        if dif==maxdecrease and dif!=0:
                            #alphabetical order
                            if cmp(symptom[k],temp[2])==-1:
                                temp[2]=symptom[k]
                                temp[3]="F"
                        if dif>maxdecrease:
                            maxdecrease=dif
                            temp[2]=symptom[k]
                            temp[3]="F"
                    if resultF>result1:
                        dif=resultF-result1
                        if dif==maxincrease and dif!=0:
                            #alphabetical order
                            if cmp(symptom[k],temp[0])==-1:
                                temp[0]=symptom[k]
                                temp[1]="F"
                        if dif>maxincrease:
                            maxincrease=dif
                            temp[0]=symptom[k]
                            temp[1]="F"
            question3[disname]=temp
            
        question1[disname]=resultstr
    
    outputFile.write(str(question1))
    outputFile.write("\r\r\n")
    outputFile.write(str(question2))
    outputFile.write("\r\r\n")
    outputFile.write(str(question3))
    outputFile.write("\r\r\n")

#close file
inputFile.close()
outputFile.close()
