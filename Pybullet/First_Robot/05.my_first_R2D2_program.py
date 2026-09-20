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

