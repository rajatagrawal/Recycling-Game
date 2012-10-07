import direct.directbase.DirectStart


restaurant1 = []

def moveRestaurant1(task):

	global restaurant1
	restaurant1[len(restaurant1)-1].setPos(base.mouseWatcherNode.getMouseX()*(base.win.getXSize()/2),0,(base.mouseWatcherNode.getMouseY()*(base.win.getYSize()/2))+100)

	return task.cont
def loadABuilding():
	global restaurant1

	#restaurant1.append(loader.loadModel('models/art/cat-buildings/bvw-f2004--pueblo/pueblo'))

	restaurant1.append(loader.loadModel('models/restaurant1/tetris-building.egg'))
	restaurant1[len(restaurant1)-1].reparentTo(render)
	restaurant1[len(restaurant1)-1].setScale(5)

	restaurant1[len(restaurant1)-1].setPos(0,0,100)
	taskMgr.add(moveRestaurant1,'moveRestaurant1')
	


