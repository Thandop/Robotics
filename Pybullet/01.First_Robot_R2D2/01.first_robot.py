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

# Run the simulation for a short, observable period, then close it cleanly.
try:
	for _ in range(24000):
		pyb.stepSimulation()
		time.sleep(1 / 240)
		print(_)
finally:
	pyb.disconnect(physicsClient)