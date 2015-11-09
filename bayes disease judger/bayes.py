import os
import sys
import copy

inputFile=sys.argv[2]
dot=inputFile.find('.')
outputFile=inputFile[0:dot]+'_inference'+inputFile[dot:]

print 'aaaaa',outputFile
fr=open(inputFile,'r')
fw=open(outputFile,'w')
line=fr.readline()
diseaseNum=int((line.split(' '))[0])
patientNum=int((line.split(' '))[1])

ill=[]
noIll=[]
noIllList=[]

illCount=1
while illCount<=diseaseNum:

    line=fr.readline()
    illName=(line.split(' '))[0]
    illSym=int((line.split(' '))[1])
    illPossibility=float((line.split(' '))[2])
    illStructure=[]
    illStructure.append(illName)
    illStructure.append(illSym)
    illStructure.append(illPossibility)
    symName=eval(fr.readline())
    tem=fr.readline()
    ##print tem
    symYes=eval(tem)
    symNo=eval(fr.readline())

    pd=[]
    symCount=1
    while symCount<=illSym:
        pSym=illPossibility*symYes[symCount-1]+(1-illPossibility)*symNo[symCount-1]
        pd.append(pSym)
        symCount=symCount+1
    illStructure.append(symName)
    illStructure.append(symYes)
    illStructure.append(symNo)
    illStructure.append(pd)

    
    ill.append(illStructure)

    
    illCount=illCount+1

##print ill

peopleCount=1
while peopleCount<=patientNum:
    fw.write("Patient-"+str(peopleCount)+":\n")
    illCount=1
    dic1={}
    dic2={}
    dic3={}
    while illCount<=diseaseNum:
        possibility=ill[illCount-1][2]
        symJudge=eval(fr.readline())

        ##q1
        i=0
        pdYes=ill[illCount-1][2]
        pdNo=1-ill[illCount-1][2]

        pdYes2max=ill[illCount-1][2]
        pdNo2max=1-ill[illCount-1][2]
        pdYes2min=ill[illCount-1][2]
        pdNo2min=1-ill[illCount-1][2]
 ##       pd=float(pd)
        pdc=1
        pdc2max=1
        pdc2min=1
        pdc=float(pdc)
        for item in symJudge:
             ##print item
             if item=='T':
                 ##q1
                 pdYes=pdYes*ill[illCount-1][4][i]
                 pdNo=pdNo*ill[illCount-1][5][i]
                 pdc=pdc*ill[illCount-1][4][i]

##                 ##q2
##                 pdYes2min=pdYes2min*ill[illCount-1][4][i]
##                 pdNo2min=pdNo2min*ill[illCount-1][5][i]
##                 pdYes2max=pdYes2max*ill[illCount-1][4][i]
##                 pdNo2max=pdNo2max*ill[illCount-1][5][i]
##                 pdc2min=pdc2min*ill[illCount-1][4][i]
##                 pdc2max=pdc2max*ill[illCount-1][4][i]
             elif item=='F':
                 ##q1:
                 pdYes=pdYes*(1-ill[illCount-1][4][i])
                 pdNo=pdNo*(1-ill[illCount-1][5][i])
                 pdc=pdc*(1-ill[illCount-1][4][i])
##                 ##q2
##                 pdYes2min=pdYes2min*(1-ill[illCount-1][4][i])
##                 pdNo2min=pdNo2min*(1-ill[illCount-1][5][i])
##                 pdYes2max=pdYes2max*(1-ill[illCount-1][4][i])
##                 pdNo2max=pdNo2max*(1-ill[illCount-1][5][i])
##                 pdc2min=pdc2min*(1-ill[illCount-1][4][i])
##                 pdc2max=pdc2max*(1-ill[illCount-1][4][i])
        
                 
             
             i=i+1

        possibility=possibility*pdc/(pdYes+pdNo)
        dic1[ill[illCount-1][0]]=possibility
        
        #print possibility
                ##q2
        allSym=[]
        oneOfSym=[]
        allSym.append(oneOfSym)
        for item in symJudge:
            if item=='T' or item=='F':
                for choice in allSym:
                    choice.append(item)
                #print item,'1'
            else:
                copyAllSym=copy.deepcopy(allSym)
                i=0
                for choice in copyAllSym:
                    newChoice=[]
                    newChoice=copy.deepcopy(choice)
                    choice.append('T')
                    newChoice.append('F')
                    allSym[i]=copy.deepcopy(choice)
                    allSym.append(newChoice)
                    i=i+1
                #print item,'2'
        #print allSym
        resultList=[]
        for eachSym in allSym:
            possibility=ill[illCount-1][2]
            i=0
            pdc=1
            pdYes=ill[illCount-1][2]
            pdNo=1-ill[illCount-1][2]
            for item in eachSym:
                if item=='T':
                    pdYes=pdYes*ill[illCount-1][4][i]
                    pdNo=pdNo*ill[illCount-1][5][i]
                    pdc=pdc*ill[illCount-1][4][i]
                elif item=='F':
                    pdYes=pdYes*(1-ill[illCount-1][4][i])
                    pdNo=pdNo*(1-ill[illCount-1][5][i])
                    pdc=pdc*(1-ill[illCount-1][4][i])
                i=i+1
            possibility=possibility*pdc/(pdYes+pdNo)
            resultList.append(possibility)
        maxPossibility=max(resultList)
        minPossibility=min(resultList)
        minmaxList=[]
        minmaxList.append("%.4f" %minPossibility)
        minmaxList.append("%.4f" %maxPossibility)
        dic2[ill[illCount-1][0]]=copy.deepcopy(minmaxList)


######q3
        allSym=[]
 ##       oneOfSym=copy.deepcopy(symJudge)
 ##       allSym.append(oneOfSym)
        i=0
        flag=0
        for item in symJudge:
            if item=='U':
                flag=1
                copyF=copy.deepcopy(symJudge)
                copyF[i]='F'
                allSym.append([ill[illCount-1][3][i],'F',copyF])
                copyT=copy.deepcopy(symJudge)
                copyT[i]='T'
                allSym.append([ill[illCount-1][3][i],'T',copyT])
            i=i+1
        ##print allSym
        resultList=[]
        if flag==0:
            resultList.append('none')
            resultList.append('N')
            resultList.append('none')
            resultList.append('N')
        else:
            for eachSym in allSym:
                possibility=ill[illCount-1][2]
                i=0
                pdc=1
                pdYes=ill[illCount-1][2]
                pdNo=1-ill[illCount-1][2]
                
                for item in eachSym[2]:            
                    if item=='T':
                        pdYes=pdYes*ill[illCount-1][4][i]
                        pdNo=pdNo*ill[illCount-1][5][i]
                        pdc=pdc*ill[illCount-1][4][i]
                    elif item=='F':
                     
                        pdYes=pdYes*(1-ill[illCount-1][4][i])
                        pdNo=pdNo*(1-ill[illCount-1][5][i])
                        pdc=pdc*(1-ill[illCount-1][4][i])
                    i=i+1
                possibility=possibility*pdc/(pdYes+pdNo)
                resultList.append(possibility)
            ##print resultList
            maxValue=resultList[0]
            maxSym=allSym[0]
            minValue=resultList[0]
            minSym=allSym[0]
            i=0
            for eachPossibility in resultList:
                if eachPossibility>maxValue:
                    maxValue=eachPossibility
                    maxSym=allSym[i]
                if eachPossibility==maxValue:
                    if allSym[i][0]<maxSym[0]:
                        maxValue=eachPossibility
                        maxSym=allSym[i]
                if eachPossibility<minValue:
                    minValue=eachPossibility
                    minSym=allSym[i]
                if eachPossibility==minValue:
                    if allSym[i][0]<minSym[0]:
                        minValue=eachPossibility
                        minSym=allSym[i]
                i=i+1
        if flag==0:
            dic3[ill[illCount-1][0]]=['none','N','none','N']
        else:
            if maxValue<dic1[ill[illCount-1][0]] and minValue<dic1[ill[illCount-1][0]]:
                dic3[ill[illCount-1][0]]=['none','N',minSym[0],minSym[1]]
            elif maxValue>dic1[ill[illCount-1][0]] and minValue>dic1[ill[illCount-1][0]]:
                dic3[ill[illCount-1][0]]=[maxSym[0],maxSym[1],'none','N']
            elif maxValue<dic1[ill[illCount-1][0]] and minValue>dic1[ill[illCount-1][0]]:
                dic3[ill[illCount-1][0]]=['none','N','none','N']
            else:
                dic3[ill[illCount-1][0]]=[maxSym[0],maxSym[1],minSym[0],minSym[1]]
        illCount=illCount+1
    peopleCount=peopleCount+1
    for item in dic1.keys():
        dic1[item]="%.4f" %dic1[item]
    fw.write(str(dic1)+'\n')
    fw.write(str(dic2)+'\n')
    fw.write(str(dic3)+'\n')

fr.close()
fw.close()

















             
