#simRemoteApi.start(19999)
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


errorCode, force_sensor_handle = vrep.simxGetObjectHandle(clientID, 'IRB140_connection', vrep.simx_opmode_blocking)
print("IRB140_connection", errorCode, force_sensor_handle)
errorCode, forceState, forceVector, torqueVector=vrep.simxReadForceSensor(clientID, force_sensor_handle, vrep.simx_opmode_streaming)
print("init force sensor", errorCode, forceState, forceVector, torqueVector)
timer = 0


while(1):
    errorCode, forceState, forceVector, torqueVector=vrep.simxReadForceSensor(clientID, force_sensor_handle, vrep.simx_opmode_buffer)
    timer += 1
    if (forceState>0 and timer % 8000 == 0):
        print("force sensor data", errorCode, forceState, forceVector)
                 
    