# import the pybullet library and other necessary modules
import pybullet as pyb
import time
import pybullet_data

# Connect to the PyBullet physics server with a graphical user interface (GUI) 


ClientId = pyb.connect(pyb.GUI)  # This is for graphical version
# check if the connection was successful
if ClientId < 0:
    raise RuntimeError("Unable to connect to the PyBullet GUI")

pyb.setAdditionalSearchPath(pybullet_data.getDataPath())  # this is optional if you have pybullet_data installed
pyb.setGravity(0,0,-9.81)  # Set the gravity in the simulation

# Load a simple plane as the ground and a robot model (R2D2) at position (0, 0, 1)
planeId = pyb.loadURDF("plane.urdf") # Load a simple plane as the ground
robotId = pyb.loadURDF("r2d2.urdf", [0, 0, 1]) # Load a robot model (R2D2) at position (0, 0, 1)

# Get the number of joints in the robot
num_joints = pyb.getNumJoints(robotId)
print(f"Number of joints in the robot: {num_joints}")

# get joint information for each joint in the robot and print it
for joint_index in range(num_joints):
    joint_info = pyb.getJointInfo(robotId, joint_index)
    print("Joint Index:", joint_info[0:2])  # Print the first 15 elements of joint_info for brevity

# use list to have right wheel joints 2,3 & left wheel joints 6,7 
joint_indices = [2, 3, 6, 7]

"""
2 - Right wheel joint 1
3 - Right wheel joint 2
6 - Left wheel joint 1
7 - Left wheel joint 2
"""
maxforce = 10  # Maximum force to apply to the joints
mode = pyb.VELOCITY_CONTROL  # Control mode for the joints

pyb.setJointMotorControlArray(robotId, joint_indices, controlMode=mode,targetVelocities=[20, 10, 10, 10], forces=[maxforce]*len(joint_indices))  # Set the target velocities for the joints 



#To control the simulation, we can use a loop to step through the simulation and apply forces or control the robot'  joints. For this example, we will just run the simulation for a few seconds.

for i in range(24000):  # Run the simulation for 2400 steps (approximately 10 seconds at 240 Hz)
    pyb.stepSimulation()  # Step the simulation
    time.sleep(1./240.)  # Sleep to match real-time (assuming 240 Hz simulation frequency)

    pyb.disconnect()  # Disconnect from the PyBullet server when done   