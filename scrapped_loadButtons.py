import direct.directbase.DirectStart
from direct.gui.DirectGui import *
from panda3d.core import Vec3
from direct.showbase import DirectObject


building1 = loader.loadModel('models/art/cat-buildings/bvw-f2004--pueblo/pueblo')

#building1 = loader.loadModel('models/restaurant1/tetris-building.egg')
building1.setScale(.1)
buttonPhoto = loader.loadModel('../buildingButton.egg')
base.disableMouse()
camera.setPos(0,-250,50)

class mouseListener(DirectObject.DirectObject):

	def __init__(self):
		self.accept('mouse1', self.dropTheModel)

	def dropTheModel(self):
		print('in the drop the model function')
		taskMgr.remove('movingTheBuilding')



def moveTheObject(task):
	building1.setPos(base.mouseWatcherNode.getMouseX()* (base.win.getXSize()/2),0, base.mouseWatcherNode.getMouseY()*(base.win.getYSize()/2) )


	print base.mouseWatcherNode.getMouseX()* (base.win.getXSize()/2), 0 , base.mouseWatcherNode.getMouseY()*(base.win.getYSize()/2)
	#building1.setPos(20,0,0)
	#print(base.mouseWatcherNode.getMouseX())
	
	return task.cont

def buttonAction():
	building1.reparentTo(render)
	taskMgr.add(moveTheObject, 'movingTheBuilding')
	function = mouseListener()



buildingButton1 = DirectButton(pos = Vec3(0,0,.95), scale = 0.1, command=buttonAction, geom = (buttonPhoto.find('**/photo2'),buttonPhoto.find('**/photo2'),buttonPhoto.find('**/photo2'), buttonPhoto.find('**/photo2')))

run()
