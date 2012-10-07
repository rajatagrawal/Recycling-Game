#this file handles the camera movement of the game

import direct.directbase.DirectStart

def setCameraControl():
	base.disableMouse()
	camera.setPos(-200,-800,300)
	camera.setHpr(0,-20,0)
	
	#camera.setPos(0,-250,50)
