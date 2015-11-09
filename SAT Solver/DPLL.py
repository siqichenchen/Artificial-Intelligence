import copy
import sys
import os

    
inputFile=sys.argv[2]
outputFile="CNF_satisfiability.txt"
ope=['and','or','iff','implies','not']

#collect symbols in CNF
def AddSymbol(CNF,symbol):
    for item in CNF:
        if item in symbol:
            continue
        if type(item)==str:
            symbol.append(item)
        elif type(item)==list and item[0]=='not':
            if (item[1] not in symbol):
                symbol.append(item[1])
        elif type(item)==list:
            AddSymbol(item,symbol)
            
#PURE-SYMBOLS:
##def Pure (single,CNF):
##    if type(single)==str:
##        for item in CNF:
##            if type(item)==list:
##                if item[0]=='not'and item[1]==single:
##                    item[0]=[]
##                elif item[0]!='not':
##                    for sub in item:
##                        if type(sub)==list and sub[1]==single:
##                            item.pop(item.index(sub)




#caculate 'or' sentences
def Caculate(each,model):
    #print 'aa',each,model
    #print model
    if type(each)==str:
        if (each not in model.keys() )or model[each]==True:
            return True
        else:
            return False
    if type(each)==list and each[0]=='not':
        if (each[1] not in model.keys() )or model[each[1]]==False:
            return True
        else:
            return False
    for item in each:
        
        if type(item)==str and item in model.keys():
            if model[item]==True:
                return True
        if type(item)==list and item[1] in model.keys():
            if model[item[1]]==False:
                return True
        if type(item)==str and (item not in model.keys()):
            return True
        if type(item)==list and (item[1] not in model.keys()):
            return True
    return False

successModel={}
#implement DPLL
def DPLL(CNF,model2,symbol,point):
    model=copy.deepcopy(model2)
    #print model
    #print point
 
    if point>-1:
        item=symbol[point]
        model[item]=True
        flag=True
        for each in CNF:
            if Caculate(each,model)==False:
                flag=False
                break
        if flag==True:
            result=DPLL(CNF,model,symbol,point-1)
            if result==True:
                return True
        
        model[item]=False
        #print 'bb',model
        flag=True
        for each in CNF:
            if Caculate(each,model)==False:
                flag=False
                break
        if flag==False:
            return False
        else:
            result=DPLL(CNF,model,symbol,point-1)
            if result==True:
                return True
            else:
                return False
    else:
        flag=True
        for each in CNF:
            if Caculate(each,model)==False:
                flag=False
                break
        if flag==True:
            for item in model.keys():
                successModel[item]=model[item]
            #print successModel
            return True
        else:
            return False



fr=open(inputFile,'r')
fw=open(outputFile,'w')
#the number of CNF sentences
CNFNumber=int(fr.readline())
count=1
while count<=CNFNumber:
    #get CNF sentences and change it to list type
    CNF=fr.readline()
    CNF=eval(CNF)
    
    #change CNF style to list containing only variants
## ["or", "R", ["not", "B"], "W"]-->   [['R', ['not', 'B'], 'W']]
## ["and", ["or", "P", ["not", "R"]], ["or", ["not", "Q"], ["not", "R"], "P"]]-->   [['P', ['not', 'R']], [['not', 'Q'], ['not', 'R'], 'P']]
## ["and", "A", ["or", "B", "C"], ["or", "B", "D"]]-->   ['A', ['B', 'C'], ['B', 'D']]
    newList=[]
    if CNF[0]=='and':
        ind=0
        for item in CNF:
            if ind>0:
                newList.append(item)
            ind=ind+1
    else:
        newList.append(CNF)

    for item in newList:
        if type(item)==list and item[0]=='or':
            item.pop(0)
            
    #implement DPLL
    ##print 'bbb',newList
    modelCNF={}
    successModel=copy.deepcopy(modelCNF)
    symbol=[]
    #collect symbols in CNF
    AddSymbol(newList,symbol)
    copySymbol=copy.deepcopy(symbol)
    #find pure item
    pureItem=[[],[]]
    pureCount=0
    #find positive pure item
    for item in symbol:
        flag=0
        for clause in newList:
            if type(clause)==list and clause[0]=='not':
                if clause==['not',item]:
                    flag=1
                    break
            elif type(clause)==list:
                for subClause in clause:
                    if subClause==['not',item]:
                        flag=1
                        break
                if flag==1:
                    break
        if flag==0:
            pureItem[0].append(item)
            modelCNF[item]=True
            pureCount=pureCount+1
            symbol.pop(symbol.index(item))
            
    #find negetive pure item
    for item in symbol:
        flag=0
        for clause in newList:
            if type(clause)==str:
                if clause==item:
                    flag=1
                    break
            elif type(clause)==list and clause[0]!='not':
                for subClause in clause:
                    if subClause==item:
                        flag=1
                        break
                if flag==1:
                    break
                
        if flag==0:
            pureItem[1].append(item)
            modelCNF[item]=False
            pureCount=pureCount+1
            symbol.pop(symbol.index(item))
    print pureItem,symbol
    ##print 'ccc',symbol
    result=DPLL(newList,modelCNF,symbol,len(symbol)-1)
    printList=[]
    if result==False:
        printList.append("false")
    else:
        printList.append("true")
        print successModel
        for element in copySymbol:
            printList.append(element+"="+str(successModel[element]).lower())
    fw.write(str(printList).replace('\'','\"')+'\n')
    count=count+1
fr.close()
fw.close()
