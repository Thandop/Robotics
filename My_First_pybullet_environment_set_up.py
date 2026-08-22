""" In this code ,I'm just setting up the environment for our code and load some assets

"""

import pybullet as p 
import time 
import pybullet_data as pb_d 

# We need to connect to the GUI server
Physics_Clients = p.connect(p.GUI)

# We need to tell our code where to fetch the assets like the floor and the robots.

p.setAdditionalSearchPath(pb_d.getDataPath())

# Our code goes here
# we need to make sure we reset our Client server by including reset simulation

p.resetSimulation()
"""
 We need to set up the gravity for the environment by using getGravity(x,y,z) and we use Earth's gravity which is 9.81
but using it as negative to show it pulling down.
"""
p.setGravity(0,0,-9.81)

# we need to set time for simulation which 240 Hz which is a standad for pyhsics

p.setTimeStep(1.0/240.0)

# We need to load our assets in the scene, lets start with floor. we be using p.loadURDF

# the loadURDF have two important paramete is the name of the asset you need and location on the environment
PlaneId = p.loadURDF("plane.urdf",basePosition=[0,0,0])

# the loadURDF have two important paramete is the name of the asset you need and location on the environment
robotId = p.loadURDF("r2d2.urdf",basePosition=[0,0,1.0])

# Lets step the simulation for 240 forward by using loops lets run it for 10 seconds so is gonna be 240 * 10

for _ in range(240*10):
    # by using stepSimulation()
    p.stepSimulation()
    time.sleep(1.0/240.0)
 





# This is the code to tell the system to close grateful
p.disconnect