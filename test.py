##def verifyInteger(a):
##
##    allIntegers=[]
##
##    rows = len(a)
##
##    for i in range(rows):
##    
##        for j in range (len(a[i])):
##        
##            if((str(a[i][j])).isdigit()):
##
##                allIntegers+=[ (a[i][j]) ]
##
##                if(allIntegers.count((a[i][j]))>1):
##                    
##                    return False
##
##                continue
##
##            return False
##  
##a = [ [ 2, 3, 5],[1,2,3,4] ]
##
##print(verifyInteger(a))
##
##
#################################################################################
##
##def isSqaure(a):
##
##    rows=len(a)
##    
##    for i in range(rows):
##        
##        cols=len(a[i])
##
##        if(cols==rows):
##            
##            continue
##        
##        return False
##        
##a = [ [ 2, 3, 5],[1,2,3,4] ]
##
##print(isSqaure(a))
##
#########################################################################
##
##def isNonEmpty(a):
##    
##    if(a==[]):
##        
##     return False
##    
##a = [ [ 2, 3, 5],[1,2,3,4] ]
##
##print(isNonEmpty(a))
##
##
#########################################################################
##
##def is2d(a):
##
##    rows=len(a)
## 
##    for i in range(rows):
##     
##        if(type(a[i])==list):
##      
##            continue
##        
##        return False
##        
##a = [ [ 2, 3, 5],[1,2,3,4] ]
##      
##print(is2d(a))

#######################################################################

def computeSumRows(a):

    rows=len(a)
    
    cols=len(a[0])

    for i in range (rows):

        finalSum_rows=0

        summedRows=0
          
        for j in range(cols):

            finalSum_rows+=a[0][j]
          
            summedRows+=a[i][j]
   
        if(summedRows==finalSum_rows):
          
            continue
          
        return False
          
    return finalSum_rows
          
def computeSumCols(a):
    
    rows=len(a)
          
    cols=len(a[0])
          
    for j in range(cols):

        summedCols=0
        
        finalSum_cols=0
        
          
        for i in range(rows):

            finalSum_cols+=a[0][i]
          
            summedCols+=a[j][i]
   
        if(summedCols==finalSum_cols):
          
            continue
          
        return False

    return finalSum_cols

def computeSumDiagonal(a):

    summedDiagonal_One=0
          
    summedDiagonal_Two=0
          
    rows=len(a)
          
    cols=len(a[0])

    for i in range(rows):
 
        summedDiagonal_One+=a[i][(cols-1)]
          
        summedDiagonal_Two+=a[i][i]
          
        cols=cols-1
   
    if(summedDiagonal_One==summedDiagonal_Two):
          
            return summedDiagonal_One
          
    return False


def computeAllSum(a):
          
            aRows=computeSumRows(a)
          
            aCols=computeSumCols(a)
          
            aDiagonals=computeSumDiagonal(a)

            print("aRows",aRows)
            print("aCols",aCols)
            print("aDiagonals",aDiagonals)

            if(aRows!=aCols!=aDiagonals):

                return False
            


a=[ [2,7,6],[9,5,1],[4,3,8] ]

print(computeAllSum(a))
          
    
  
