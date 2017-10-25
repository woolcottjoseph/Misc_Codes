import matplotlib.pyplot as plt
import math

def playingwithsine():
    sinelist = []
    coslist = []
    for value in range(100):
        sinelist.append(math.sin((value/8)))
        coslist.append(math.cos((value/8)))
    plt.plot(sinelist, coslist)
    plt.show()

def drawingstuff(smallvalue,largevalue,printlistx,printlisty): # using recursion to draw weird shapes

    xlist = [math.sin(smallvalue),math.cos(smallvalue)]
    ylist = [math.cos(smallvalue),math.sin(largevalue)]
    printlistx.extend(xlist)
    printlisty.extend(ylist)
    print(printlistx)

    print(printlistx)

    smallvalue = smallvalue + 5
    print (smallvalue)
    largevalue = largevalue + 5
    print (largevalue)
    if largevalue >= 1000:
        plt.plot(printlistx,printlisty)
        plt.show()
    else:
        drawingstuff(smallvalue,largevalue,printlistx,printlisty)


drawingstuff(0, 0,[],[])