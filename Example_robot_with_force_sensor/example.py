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

errorCode, force_sensor_handle = vrep.simxGetObjectHandle(clientID, 'Force_sensor', vrep.simx_opmode_blocking)
print("Force_sensor", errorCode, force_sensor_handle)
errorCode, forceState, forceVector, torqueVector=vrep.simxReadForceSensor(clientID, force_sensor_handle, vrep.simx_opmode_streaming)
print("init force sensor", errorCode, forceState, forceVector, torqueVector)
FBvalue = 0
RLvalue = 0
rotvalue = 0
joint1 = 300
joint2 = 450
joint3 = 130
joint4 = 140
joint5 = 500
timer = 0


while(1):
    errorCode, forceState, forceVector, torqueVector=vrep.simxReadForceSensor(clientID, force_sensor_handle, vrep.simx_opmode_buffer)
    timer += 1
    if (forceState>0 and timer % 10000 == 0):
        print("force sensor data", errorCode, forceState, forceVector)
        #joint2 -= 10
            
    vrep.simxSetIntegerSignal(clientID,"FBvalue",FBvalue,vrep.simx_opmode_oneshot)
    vrep.simxSetIntegerSignal(clientID,"RLvalue",RLvalue,vrep.simx_opmode_oneshot)
    vrep.simxSetIntegerSignal(clientID,"rotvalue",rotvalue,vrep.simx_opmode_oneshot)
    vrep.simxSetIntegerSignal(clientID,"joint1",joint1,vrep.simx_opmode_oneshot)
    vrep.simxSetIntegerSignal(clientID,"joint2",joint2,vrep.simx_opmode_oneshot)
    vrep.simxSetIntegerSignal(clientID,"joint3",joint3,vrep.simx_opmode_oneshot)
    vrep.simxSetIntegerSignal(clientID,"joint4",joint4,vrep.simx_opmode_oneshot)
    vrep.simxSetIntegerSignal(clientID,"joint5",joint5,vrep.simx_opmode_oneshot)