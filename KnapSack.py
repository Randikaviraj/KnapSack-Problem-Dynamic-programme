import sys
import time


def kuruskalAlgorithm(noOfValues: int,knapSackWeight: int,weightValueList: list):
    pass


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