import vrep
import sys
import numpy as np
print ('Program started')
vrep.simxFinish(-1) # just in case, close all opened connections

clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP

if clientID!=-1:
    print ('Connected to remote API server')



else:
    sys.exit('Failed connecting to remote API server')
#wheel joints

FBvalue = 0
RLvalue = 0
rotvalue = 0
joint1 = 500
joint2 = 0
joint3 = 250
joint4 = 500
joint5 = 500
trigger = 1
timer = 0


while(1):
    timer += 1
    if timer<=4500:
        rotvalue = 0
        joint1 = 500
        joint2 = 300
        joint3 = 300
        joint4 = 300
        joint5 = 500
        trigger = 0
    elif 14500<timer<=19000:
        FBvalue = 8
        RLvalue = 1
    elif 19000<timer<=20000:
        FBvalue = 0
        RLvalue = 0
        joint1 = 500
        joint2 = 200
        joint3 = 200
        joint4 = 300
        joint5 = 500
    elif 20000<timer<=23000:
        trigger = 1
    elif 23000<timer<=38000:
        joint1 = 900
        joint2 = 300
        joint3 = 300
        joint4 = 300
        joint5 = 500
    elif 38000<timer<=42000:
        FBvalue = -2
        RLvalue = -5
    elif 42000<timer<=43000:
        FBvalue = 0
        RLvalue = 0
    elif 43000<timer<=47000:
        joint1 = 900
        joint2 = 250
        joint3 = 250
        joint4 = 300
        joint5 = 500      
    elif 47000<timer<=48000:
        trigger = 0       

    vrep.simxSetIntegerSignal(clientID,"FBvalue",FBvalue,vrep.simx_opmode_oneshot)
    vrep.simxSetIntegerSignal(clientID,"RLvalue",RLvalue,vrep.simx_opmode_oneshot)
    vrep.simxSetIntegerSignal(clientID,"rotvalue",rotvalue,vrep.simx_opmode_oneshot)
    vrep.simxSetIntegerSignal(clientID,"joint1",joint1,vrep.simx_opmode_oneshot)
    vrep.simxSetIntegerSignal(clientID,"joint2",joint2,vrep.simx_opmode_oneshot)
    vrep.simxSetIntegerSignal(clientID,"joint3",joint3,vrep.simx_opmode_oneshot)
    vrep.simxSetIntegerSignal(clientID,"joint4",joint4,vrep.simx_opmode_oneshot)
    vrep.simxSetIntegerSignal(clientID,"joint5",joint5,vrep.simx_opmode_oneshot)
    vrep.simxSetIntegerSignal(clientID,"trigger",trigger,vrep.simx_opmode_oneshot)