import direct.directbase.DirectStart
from direct.gui.DirectGui import *
from panda3d.core import Vec3
from direct.showbase import DirectObject
from showGameMessages import showMoneyValue, showEnvironmentRating
from gameVariables import getMoney, setMoney
from gameVariables import setEnvironmentRating, getEnvironmentRating

restaurant1 =[]
buttonRestaurant1_Pressed = False

buttonImage_restaurant1 = loader.loadModel('models/restaurantButton1.egg')
cinemaHallButtonImage = loader.loadModel('models/cinema1.egg')
buttonPlant = loader.loadModel('models/plant.egg')
buttonIndustry = loader.loadModel('models/industryButton.egg')

class restaurants:

	#model = loader.loadModel()
	fRValue = 0
	eRValue = 0
	capacity = 0
	cost = 0
	type = ''
	def __init__(self,modelName):
		
		self.model = loader.loadModel(modelName)	
class mouseFunctionalityButtons(DirectObject.DirectObject):
	

	def __init__(self):
		self.accept('mouse1',self.dropRestaurant1)

	def dropRestaurant1(self):
		global buttonRestaurant1_Pressed
		taskMgr.remove('moveRestaurant1')
		buttonRestaurant1_Pressed = False


def moveRestaurant1(task):
	global restaurant1
	restaurant1[len(restaurant1)-1].model.setPos(base.mouseWatcherNode.getMouseX()*(base.win.getXSize()/2),0,(base.mouseWatcherNode.getMouseY()*(base.win.getYSize()/2))+100)

	return task.cont

def action_restaurantButton1():

	global buttonRestaurant1_Pressed,restaurant1,money
	buttonRestaurant1_Pressed = True
	restaurant1.append(restaurants('models/restaurant1/tetris-building.egg'))

	#restaurant1[len(restaurant1)-1].model = (loader.loadModel('models/restaurant1/tetris-building.egg'))
	restaurant1[len(restaurant1)-1].capacity = 10
	restaurant1[len(restaurant1)-1].fRValue = 2
	restaurant1[len(restaurant1)-1].eRValue = -1
	restaurant1[len(restaurant1)-1].cost = 200
	restaurant1[len(restaurant1)-1].type='eating'

	restaurant1[len(restaurant1)-1].model.reparentTo(render)
	restaurant1[len(restaurant1)-1].model.setScale(5)

	setMoney( getMoney() - restaurant1[len(restaurant1)-1].cost)

	showMoneyValue(getMoney())
	restaurant1[len(restaurant1)-1].model.setPos(0,0,100)
	taskMgr.add(moveRestaurant1,'moveRestaurant1')
	startMouseFunctionRestaurant1 = mouseFunctionalityButtons()


def action_plantButton1():
	
		
	global buttonRestaurant1_Pressed,restaurant1,money
        buttonRestaurant1_Pressed = True
        restaurant1.append(restaurants('models/plant/plants3.egg'))

        #restaurant1[len(restaurant1)-1].model = (loader.loadModel('models/restaurant1/tetris-building.egg'))
        restaurant1[len(restaurant1)-1].capacity = 1
        restaurant1[len(restaurant1)-1].fRValue = .01
        restaurant1[len(restaurant1)-1].eRValue = .1
        restaurant1[len(restaurant1)-1].cost = 10
        restaurant1[len(restaurant1)-1].type='environment'

        restaurant1[len(restaurant1)-1].model.reparentTo(render)
        restaurant1[len(restaurant1)-1].model.setScale(0.5)

        setMoney( getMoney() - restaurant1[len(restaurant1)-1].cost)

        showMoneyValue(getMoney())
	setEnvironmentRating(getEnvironmentRating() + 0.1)
	showEnvironmentRating(getEnvironmentRating())
        restaurant1[len(restaurant1)-1].model.setPos(0,0,100)
        taskMgr.add(moveRestaurant1,'moveRestaurant1')
        startMouseFunctionRestaurant1 = mouseFunctionalityButtons()



def action_industryButton1():

        global buttonRestaurant1_Pressed,restaurant1,money
        buttonRestaurant1_Pressed = True
        restaurant1.append(restaurants('models/industryBuilding/building.egg'))

        #restaurant1[len(restaurant1)-1].model = (loader.loadModel('models/restaurant1/tetris-building.egg'))
        restaurant1[len(restaurant1)-1].capacity = 10
        restaurant1[len(restaurant1)-1].fRValue = 5
        restaurant1[len(restaurant1)-1].eRValue = -4
        restaurant1[len(restaurant1)-1].cost = 500
        restaurant1[len(restaurant1)-1].type='finance'

        restaurant1[len(restaurant1)-1].model.reparentTo(render)
        restaurant1[len(restaurant1)-1].model.setScale(0.4)
	restaurant1[len(restaurant1)-1].model.setHpr(-90,0,0)

        setMoney( getMoney() - restaurant1[len(restaurant1)-1].cost)

        showMoneyValue(getMoney())
        restaurant1[len(restaurant1)-1].model.setPos(0,0,100)
        taskMgr.add(moveRestaurant1,'moveRestaurant1')
        startMouseFunctionRestaurant1 = mouseFunctionalityButtons()


def action_cinemaHallButton1():
	
	global buttonRestaurant1_Pressed,restaurant1,money
        buttonRestaurant1_Pressed = True
        restaurant1.append(restaurants('models/cinemaHall/beachhouse2.egg'))
        #restaurant1[len(restaurant1)-1].model = (loader.loadModel('models/restaurant1/tetris-building.egg'))
        restaurant1[len(restaurant1)-1].capacity = 15
        restaurant1[len(restaurant1)-1].fRValue = 2
        restaurant1[len(restaurant1)-1].eRValue = -1.5
        restaurant1[len(restaurant1)-1].cost = 200
        restaurant1[len(restaurant1)-1].type='entertainment'

        restaurant1[len(restaurant1)-1].model.reparentTo(render)
        restaurant1[len(restaurant1)-1].model.setScale(2.5)
        #restaurant1[len(restaurant1)-1].model.setHpr(-90,0,0)

        setMoney( getMoney() - restaurant1[len(restaurant1)-1].cost)

        showMoneyValue(getMoney())
        restaurant1[len(restaurant1)-1].model.setPos(0,0,100)
        taskMgr.add(moveRestaurant1,'moveRestaurant1')
        startMouseFunctionRestaurant1 = mouseFunctionalityButtons()

def loadButtons():

	global buttonImage_restaurant1, buttonPlant, buttonIndustry

	buttonRestaurant1 = DirectButton(pos=Vec3(0,0,.9),scale=0.1,command=action_restaurantButton1, geom=(buttonImage_restaurant1.find('**/restaurant1'),buttonImage_restaurant1.find('**/restaurant1'),buttonImage_restaurant1.find('**/restaurant1'),buttonImage_restaurant1.find('**/restaurant1')))


	buttonPlant = DirectButton(pos=Vec3(.26,0,.90),scale=0.1,command=action_plantButton1, geom=(buttonPlant.find('**/plant'),buttonPlant.find('**/plant'),buttonPlant.find('**/plant'),buttonPlant.find('**/plant')))

	buttonIndustry = DirectButton(pos=Vec3(.52,0,.90),scale=0.1,command=action_industryButton1, geom=(buttonIndustry.find('**/industry'),buttonIndustry.find('**/industry'),buttonIndustry.find('**/industry'),buttonIndustry.find('**/industry')))

	buttonCinemaHall = DirectButton(pos=Vec3(-0.22,0,.90),scale=0.1,command=action_cinemaHallButton1, geom=(cinemaHallButtonImage.find('**/cinemaHall1'),cinemaHallButtonImage.find('**/cinemaHall1'),cinemaHallButtonImage.find('**/cinemaHall1'),cinemaHallButtonImage.find('**/cinemaHall1')))

