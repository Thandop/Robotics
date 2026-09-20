
import pybullet as pyb
import time
import pybullet_data

physicsClient = pyb.connect(pyb.GUI)  # This is for graphical version
if physicsClient < 0:
	raise RuntimeError("Unable to connect to the PyBullet GUI")

pyb.setAdditionalSearchPath(pybullet_data.getDataPath())  # this is optional if you have pybullet_data installed

pyb.setGravity(0, 0, -9.81)  # Set the gravity in the simulation

planeID = pyb.loadURDF("plane.urdf") # Load a simple plane as the ground
robotID = pyb.loadURDF("r2d2.urdf", [0, 0, 1]) # Load a robot model (R2D2) at position (0, 0, 1)

#Get the number of joints in the robot

num_joints = pyb.getNumJoints(robotID)
print(f"Number of joints in the robot: {num_joints}")

# use for loop to print joint information
for joint_index in range(num_joints):
	joint_info = pyb.getJointInfo(robotID, joint_index)
	print("Joint Index:", joint_info[0:2])  # Print the first 15 elements of joint_info for brevity

# Move the robot forward by setting the velocity of the wheels
# we be using the setJointMotorControl2(objUId, jointIndex, controlMode, targetVelocity, maxForce) function to control the wheel joints of the robot. The wheel joints are typically at indices 2 and 3 for R2D2.
# The robot has four wheels , the right wheels are at joint indices 2 and 3, and the left wheels are at joint indices 6 and 7. To move the robot forward, we will set a positive velocity for both the left and right wheels.
maxForce = 10 # Maximum force to apply to the wheels

mode = pyb.VELOCITY_CONTROL

front_right_wheel_index = 2
back_right_wheel_index = 3
front_left_wheel_index = 6
back_left_wheel_index = 7

velocity = 5 #This is the target velocity for the wheels. You can adjust this value to make the robot move faster or slower.

pyb.setJointMotorControl2(robotID, front_right_wheel_index, mode, targetVelocity=velocity, force=maxForce)  # Right Front wheel
pyb.setJointMotorControl2(robotID, back_right_wheel_index, mode, targetVelocity=velocity, force=maxForce)  # Right Back wheel
pyb.setJointMotorControl2(robotID, front_left_wheel_index, mode, targetVelocity=velocity, force=maxForce)  # Left Front wheel
pyb.setJointMotorControl2(robotID, back_left_wheel_index, mode, targetVelocity=velocity, force=maxForce)  # Left Back wheel

# Run the simulation for a short, observable period, then close it cleanly.
try:
	for _ in range(24000):
		pyb.stepSimulation()
		time.sleep(1 / 240)
	
finally:
	pyb.disconnect(physicsClient)