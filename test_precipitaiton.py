# -*- coding: utf-8 -*-
#x=1.0
#y=1.5
#diff=0.5

#for i in range(001,077):
    #print("%03d"%i)
    #print(str(x)+"to"+str(y))

    #x=y+0.1


    #if i%2==0:
        #if diff==0.5:
            #diff=1
        #else:
            #diff=0.5
        #y=x+diff
    #else:
        #y=x+0.8

x=1


for i in range(002,990):
    #print("%03d"%i)

    y=x+1

    if i%2==0:
        print(str(x)+".6"+" to "+str(y)+".4")

    else:
        print(str(x)+".5"+" to "+str(y)+".5")
    x=y