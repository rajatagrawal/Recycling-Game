#this file load the environment

import direct.directbase.DirectStart


#xOffset = 200
#yOffset = 0
#zOffset =-0 
def loadEnvironment():
	#global xOffset, yOffset, zOffset

	environ = loader.loadModel('models/world')
	environ.setScale(4)
	environ.setPos(0,0,0)
	environ.reparentTo(render)
