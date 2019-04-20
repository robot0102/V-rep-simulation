#simRemoteApi.start(19999)
#add this to V-rep script
import vrep
import sys
import numpy as np
print ('Program started')
vrep.simxFinish(-1) # just in case, close all opened connections

clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP

if clientID!=-1:#confirm connection
    print ('Connected to remote API server')

else:
    sys.exit('Failed connecting to remote API server')

#Setup the force sensor
errorCode, force_sensor_handle = vrep.simxGetObjectHandle(clientID, 'IRB140_connection', vrep.simx_opmode_blocking)
print("IRB140_connection", errorCode, force_sensor_handle)
errorCode, forceState, forceVector, torqueVector=vrep.simxReadForceSensor(clientID, force_sensor_handle, vrep.simx_opmode_streaming)
print("init force sensor", errorCode, forceState, forceVector, torqueVector)

#integer signals
Apimode = 1 #work under api mode or UI mode
movementMode = 0 #work under FK(0) or IK(1)
#float signals
Joint = [500,500,500,500,500,500] #FK mode joint values
#IK mode position X
pos_X = 0
pos_Y = 0 
pos_Z = 0 
Alpha = 0
Beta = 0
Gamma = 0

vrep.simxSetIntegerSignal(clientID,"Apimode",Apimode,vrep.simx_opmode_oneshot)
vrep.simxSetIntegerSignal(clientID,"movementMode",movementMode,vrep.simx_opmode_oneshot)
if (movementMode):
    vrep.simxSetFloatSignal(clientID,"pos_X",pos_X,vrep.simx_opmode_oneshot)
    vrep.simxSetFloatSignal(clientID,"pos_Y",pos_Y,vrep.simx_opmode_oneshot)
    vrep.simxSetFloatSignal(clientID,"pos_Z",pos_Z,vrep.simx_opmode_oneshot)
    vrep.simxSetFloatSignal(clientID,"Alpha",Alpha,vrep.simx_opmode_oneshot)
    vrep.simxSetFloatSignal(clientID,"Beta",Beta,vrep.simx_opmode_oneshot)
    vrep.simxSetFloatSignal(clientID,"Gamma",Gamma,vrep.simx_opmode_oneshot)
else:
    vrep.simxSetFloatSignal(clientID,"Joint1",Joint[0],vrep.simx_opmode_oneshot)
    vrep.simxSetFloatSignal(clientID,"Joint2",Joint[1],vrep.simx_opmode_oneshot)
    vrep.simxSetFloatSignal(clientID,"Joint3",Joint[2],vrep.simx_opmode_oneshot)
    vrep.simxSetFloatSignal(clientID,"Joint4",Joint[3],vrep.simx_opmode_oneshot)
    vrep.simxSetFloatSignal(clientID,"Joint5",Joint[4],vrep.simx_opmode_oneshot)
    vrep.simxSetFloatSignal(clientID,"Joint6",Joint[5],vrep.simx_opmode_oneshot)


while(1):
    #read force sensor
    errorCode, forceState, forceVector, torqueVector=vrep.simxReadForceSensor(clientID, force_sensor_handle, vrep.simx_opmode_buffer)
    #if (forceState>0):
       # print("force sensor data", errorCode, forceState, forceVector)