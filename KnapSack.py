import sys
import time


def kuruskalAlgorithm(noOfValues: int,knapSackWeight: int,weightValueList: list):
    def keyFunc(tup):
        return tup[0]

    weightValueList.sort(key=keyFunc)

    memo=[ [0] * (knapSackWeight+1) for _ in range((noOfValues+1))]
    for n in range(noOfValues):
        for w in range(knapSackWeight):
            if (w+1-weightValueList[n][0])>=0:
                memo[n+1][w+1]=max(memo[n][w+1],(memo[n][w+1-weightValueList[n][0]]+ weightValueList[n][1]))
            else:
                memo[n+1][w+1]=memo[n][w+1]
    return memo[noOfValues][knapSackWeight]


if __name__ =="__main__":
    try:
                
        with open(sys.argv[1],"r") as file:
            print(f"{sys.argv[1]} Reading..")
            line=file.readline()
            knapSackWeight=int(line.split(" ")[1])
            noOfValues=int(line.split(" ")[3])
            
            weightValueList=[]
            line=file.readline()
            while line:
                list=line.split(" ")
                val=[]       
                for item in list:
                    item=item.strip('\n')
                    if item:
                        val.append(int(item))
                weightValueList.append(tuple(val))
                line=file.readline()

            print('Algorithm Started::')
            seconds = time.time()
            l=kuruskalAlgorithm(noOfValues,knapSackWeight,weightValueList)
            seconds = seconds-time.time()
            print('Answer to Knapsack problem :'+str(l))
            print('Finished::')
            print('Running Time in second'+str(seconds))
            
    except Exception as e:
        print(e)
        print('Invalid no of Arguments :: python Dpll.py <filename> ')