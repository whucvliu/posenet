#!/usr/bin/python
#-*-coding:UTF-8-*-

import io
import os
import matplotlib.pyplot as plt


def main():
    lossfilePath=os.getcwd()+'/res/1123'
    outfilePath=os.getcwd()+'/res/1123.jpg'

    itrNumList=[]
    lossList = []

    file=open(lossfilePath,'r')
    aLine = file.readline()
    done=0
    while not done:
        aLine=file.readline()
        if (aLine!=''):
            strlist=aLine.split(':')
            strLen=len(strlist)
            str_tmp=strlist[strLen-1]
            itrNum=int(str_tmp)
            itrNumList.append(itrNum)

            aLine = file.readline()
            strlist = aLine.split(':')
            str_tmp=strlist[len(strlist)-1]
            lossVal=float(str_tmp)
            lossList.append(lossVal)

            #loss.append((itrNum,lossVal))
            if itrNum>0 and itrNum%5000==0:
                aLine=file.readline()
        else:
            done=1

    file.close()

    plt.figure()
    plt.plot(itrNumList,lossList)
    plt.xlabel('iteration number')
    plt.ylabel('loss value')
    plt.title('loss curver')
    plt.show()

    plt.savefig(outfilePath)


    liu=0




if __name__ == '__main__':
	main()