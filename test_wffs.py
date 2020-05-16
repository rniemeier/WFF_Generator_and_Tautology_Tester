##Program 2 CS291
##Due April 29 2020
##Rebecca Niemeier

#This is global to reduce passing it from main to is_duplicate
already_explored = [] #our list of already examined

#globals
currentToken = ""
nextToken = ""
curWFF = ""
nextLocation = 0

def main():
    #Make the program work for a variable number of wffs
    no_wffs = int(input("How many tautological WFFs would you like to produce? "))

    #Basis for generating identities
    starting_term = 'W=W'
    already_explored.append(starting_term)

    tautologies = [] #Our list of tautologies

    #initialize the work list with the starting term
    nonterm_strs = [starting_term] 

    #W -> 
    replacements = ['F', 'T', 'A', 'B', 'C','W>W', 'W&W', 'W+W', '~W', '(W)']
    done = False
    while (not done):
        if(len(nonterm_strs) > 0):
            item = nonterm_strs[0]
            nonterm_strs.remove(item) #take it off the list
            w_index = item.find('W')
            if (w_index != -1):
                for rep in replacements:
                    newItem = item[:w_index] + rep + item[w_index+1:]
                    if(not is_duplicate(newItem) and not done):
                        if(newItem.count('W') == 0):
                            if(is_tautology(newItem)):
                                tautologies.append(newItem)
                            if(no_wffs <= len(tautologies)):
                                done = True
                        else:
                            nonterm_strs.append(newItem)
                        already_explored.append(newItem)   
    print("First 50:")
    for i in range(0,50,5):
        print(tautologies[i] + "\t" + tautologies[i+1] + "\t" +
              tautologies[i+2] + "\t" + tautologies[i+3] + "\t" + tautologies[i+4])
    print("\nLast 50: ")
    for i in range(-50,0,5):
        print(tautologies[i] + "\t" + tautologies[i+1] + "\t" +
              tautologies[i+2] + "\t" + tautologies[i+3] + "\t" + tautologies[i+4])

def is_duplicate(item):
    #check if its a simple copy
    if item in already_explored:
        return True

    #make sure vars are in order
    #find returns index of first match
    locA = item.find('A')
    locB = item.find('B')
    locC = item.find('C')

    #make sure the vars are in alphabetical order
    #for their first appearance in the wff
    flag = False
    if(locA != -1):
        if(locB != -1):
            flag = (locA > locB)
        if(locC != -1):
            flag = (locA > locC)
    if (locB != -1 and locC != -1):
        flag =(locB > locC)
        

    #check for duplicates that just have different vars
    if('A' not in item and ('B' in item or 'C' in item)):
        temp = item.replace("B", "A")
        if(temp in already_explored):
            return True      
        temp = item.replace("C", "A")
        if(temp in already_explored):
            return True
    if('B' not in item and ('A' in item and 'C' in item)):
        temp = item.replace("C", "B")
        if(temp in already_explored):
            return True

    #Check for palindromic duplicates
    temp = item[::-1]
    if(temp in already_explored):
        return True
            
    return flag

def is_tautology(wff):
    #return true if is tautology, false if otherwise
    if('A' in wff):
        if('B' in wff):
            if('C' in wff): #all three vars exist
                #a = t, b = t, c = t
                try1 = wff.replace('A', 'T')
                try1 = try1.replace('B', 'T')
                try1 = try1.replace('C', 'T')
                try1 += '$'
                
                #a = t, b = t, c = f
                try2 = wff.replace('A', 'T')
                try2 = try2.replace('B', 'T')
                try2 = try2.replace('C', 'F')
                try2 += '$'
                
                #a = t, b = f, c = t
                try3 = wff.replace('A', 'T')
                try3 = try3.replace('B', 'F')
                try3 = try3.replace('C', 'T')
                try3 += '$'
                
                #a = t, b = f, c = f
                try4 = wff.replace('A', 'T')
                try4 = try4.replace('B', 'F')
                try4 = try4.replace('C', 'F')
                try4 += '$'
                
                #a = f, b = t, c = t
                try5 = wff.replace('A', 'F')
                try5 = try5.replace('B', 'T')
                try5 = try5.replace('C', 'T')
                try5 += '$'
                
                #a = f, b = t, c = f
                try6 = wff.replace('A', 'F')
                try6 = try6.replace('B', 'T')
                try6 = try6.replace('C', 'F')
                try6 += '$'
                
                #a = f, b = f, c = t
                try7 = wff.replace('A', 'F')
                try7 = try7.replace('B', 'F')
                try7 = try7.replace('C', 'T')
                try7 += '$'
                
                #a = f, b = f, c = f
                try8 = wff.replace('A', 'F')
                try8 = try8.replace('B', 'F')
                try8 = try8.replace('C', 'F')
                try8 += '$'

                if(search(try1) and search(try2) and
                   search(try3) and search(try4) and
                   search(try5) and search(try6) and
                   search(try7) and search(try8)):
                    return True
                else:
                    return False
                
            else: #just A and B
                #a = t, b = t
                try1 = wff.replace('A', 'T')
                try1 = try1.replace('B', 'T')
                try1 += '$'
                
                #a = t, b = f
                try2 = wff.replace('A', 'T')
                try2 = try2.replace('B', 'F')
                try2 += '$'
                
                #a = f, b = t
                try3 = wff.replace('A', 'F')
                try3 = try3.replace('B', 'T')
                try3 += '$'
                
                #a = f, b = f
                try4 = wff.replace('A', 'F')
                try4 = try4.replace('B', 'F')
                try4 += '$'

                if(search(try1) and search(try2) and
                   search(try3) and search(try4)):
                    return True
                else:
                    return False
                
        else: #just A
            #a = t
            try1 = wff.replace('A', 'T')
            try1 += '$'
            
            #a = f
            try2 = wff.replace('A', 'F')
            try2 += '$'

            if(search(try1) and search(try2)):
                return True
            else:
                return False

    else:
        return(search(wff+'$')) #no variables to replace

def search(wff):
    global curWFF
    global currentToken
    global nextToken
    global nextLocation
    
    curWFF = wff
    currentToken = curWFF[0]
    nextToken = curWFF[1]
    nextLocation = 1
    return (B() and (currentToken == '$'))
    
def getNextToken():
    global nextLocation
    global curWFF
    global currentToken
    global nextToken
    currentToken = nextToken
    nextLocation += 1
    nextToken = curWFF[nextLocation:nextLocation + 1]    

def B():
    return E()

def E():
    temp = I()
    return EPrime(temp)

def EPrime(incoming):
    global currentToken
    if(currentToken == '='):
        getNextToken()
        temp = I()
        intermediateResult = (incoming == temp) #incoming == temp
        temp2 = EPrime(intermediateResult)
        return temp2
    else: # no = present
        return incoming

def I():
    temp = D()
    return IPrime(temp)

def IPrime(incoming):
    global currentToken
    if (currentToken == '>'):
        getNextToken()
        temp = D()
        if((incoming == True) and (temp == False)): #incoming -> temp?
            intermediateResult = False
        else:
            intermediateResult = True
        temp2 = IPrime(intermediateResult)
        return temp2
    else: #no > present
        return incoming

def D():
    temp = C()
    return DPrime(temp)

def DPrime(incoming):
    global currentToken
    if (currentToken == '+'):
        getNextToken()
        temp = C()
        intermediateResult = (incoming or temp) #incoming + temp
        temp2 = DPrime(intermediateResult)
        return temp2
    else: #no + present
        return incoming

def C():
    temp = A()
    return CPrime(temp)

def CPrime(incoming):
    global currentToken
    if (currentToken == '&'):
        getNextToken()
        temp = A()
        intermediateResult = (incoming and temp) #incoming & temp
        temp2 = CPrime(intermediateResult)
        return temp2
    else: #no & present
        return incoming

def A():
    global currentToken
    global nextToken
    #~A
    if (currentToken == '~'):
        getNextToken()
        temp = A()
        return not temp
    #L -> T | F
    elif (currentToken == 'T'):
        getNextToken()
        return True
    elif (currentToken == 'F'):
        getNextToken()
        return False
    #(B)
    elif (currentToken == '('):
        getNextToken()
        temp = B()
        if (currentToken == ')'):
            getNextToken()
            return temp  
            
main()
