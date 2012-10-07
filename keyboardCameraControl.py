# this file contains function for moving the camera with the help of keyboard arrow keys

import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from direct.showbase import DirectObject
#from loadButtons import buttonRestaurant1_Pressed

cameraStepSize = 250
class enableKeyboardInteraction(DirectObject.DirectObject):
	
	global cameraStepSize
	mouseKeyPressed = False
	def __init__(self):

		self.accept('arrow_up-repeat', self.moveCameraUp)
		self.accept('arrow_up', self.moveCameraUp)

		self.accept('arrow_down-repeat', self.moveCameraDown)
		self.accept('arrow_down', self.moveCameraDown)

		self.accept('arrow_left-repeat', self.moveCameraLeft)
		self.accept('arrow_left', self.moveCameraLeft)

		self.accept('arrow_right-repeat',self.moveCameraRight)
		self.accept('arrow_right', self.moveCameraRight)
		
		self.accept('mouse1',self.activateMouseFunction)
		self.accept('mouse1-up', self.deactivateMouseFunction)


	def moveCameraUp(self):

		if self.mouseKeyPressed == True:
			#camera.setPos(camera.getX(), camera.getY() + cameraStepSize, camera.getZ() - cameraStepSize/2)

			camera.setPos(camera.getX(), camera.getY() + (globalClock.getDt() * cameraStepSize), camera.getZ() - (globalClock.getDt() * (cameraStepSize/2)))

		else:
			#camera.setPos(camera.getX(), camera.getY() + cameraStepSize, camera.getZ())
			
			camera.setPos(camera.getX(),camera.getY() + (cameraStepSize * globalClock.getDt()), camera.getZ())
	def moveCameraDown(self):

		if self.mouseKeyPressed == True:
			camera.setPos(camera.getX(), camera.getY() - cameraStepSize, camera.getZ() + cameraStepSize/2)

		else:
			camera.setPos(camera.getX(), camera.getY() - cameraStepSize, camera.getZ())

	def moveCameraLeft(self):

		if self.mouseKeyPressed == True:
			camera.setHpr(camera.getH() + cameraStepSize/2, camera.getP(), camera.getR())
		else:
			camera.setPos(camera.getX() - cameraStepSize, camera.getY(), camera.getZ())	

	def moveCameraRight(self):

		if self.mouseKeyPressed == True:
			camera.setHpr(camera.getH() - cameraStepSize/2, camera.getP(), camera.getR())
		else:
			camera.setPos(camera.getX() + cameraStepSize, camera.getY(), camera.getZ())

	def activateMouseFunction(self):
		self.mouseKeyPressed = True

		#this part of the code checks if any of the buttons on the 
		#screen is pressed or not. If it is so, it executes its 
		#corresponding function

		#if buttonRestaurant1_Pressed == True:
		#	self.dropRestaurant1()
		#	buttonRestaurant1_Pressed = False

	def deactivateMouseFunction(self):
		self.mouseKeyPressed = False

	#def dropRestaurant1(self):
		#taskMgr.remove('moveRestaurant1')


