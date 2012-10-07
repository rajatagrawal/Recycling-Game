import direct.directbase.DirectStart
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText



messageFrame = DirectFrame()
messageBox = OnscreenText()
timeInterval = 5
errorSound = loader.loadSfx("beep.mp3")

cityRatingBox = OnscreenText()
environmentRatingBox = OnscreenText()
developmentRatingBox = OnscreenText()
happinessRatingBox = OnscreenText()
numberOfCitizensRatingBox = OnscreenText()
moneyRatingBox = OnscreenText()


def loadMessageScreen():

	global messageFrame,messageBox,cityRatingBox, environmentRatingBox,developmentRatingBox, happinessRatingBox, numberOfCitizensRatingBox,moneyRatingBox

	messageFrame = DirectFrame(frameColor=(0,0,0,1),frameSize=(-1,3,0,.1),pos = (-1,0,-1))


	messageBox = OnscreenText(text = 'Citizens are feeling hungry. They cannot find enough place to eat. Build restaurants', pos = (0.2,0.04,0), mayChange=True,parent=messageFrame,scale=0.05,fg=(1,0.4,0,1),align=TextNode.ALeft)
	

	cityRatingBox = OnscreenText(text='City Rating : 4', pos = (-.85,.065,0), fg=(0,1,0,1), mayChange=True,parent=messageFrame, scale=0.04,align=TextNode.ALeft)

	environmentRatingBox = OnscreenText(text ='Environment Rating : 4', pos = (-.85,0.02,0),fg = (0,1,0,1),mayChange = True, parent=messageFrame, scale = 0.04,align=TextNode.ALeft)

	developmentRatingBox = OnscreenText(text = 'Development Rating : 4', pos = (-0.30,.065,0), fg = (0,1,0,1), mayChange=True, parent=messageFrame,scale = 0.04,align=TextNode.ALeft)

	happinessRatingBox = OnscreenText(text = 'Happiness Rating : 4',pos = (-0.30,.02,0), fg= (0,1,0,1),mayChange=True, parent=messageFrame, scale=0.04,align=TextNode.ALeft)

	numberOfCitizensRatingBox = OnscreenText(text = 'Citizen Count : 20',pos=(2.5,.065,0),fg=(0,1,0,1),mayChange=True,parent=messageFrame,scale=0.04,align=TextNode.ALeft)
	
	
	moneyRatingBox = OnscreenText(text = 'Money : 10000', pos=(2.5,0.02,0),fg=(0,1,0,1),mayChange=True, parent=messageFrame, scale=0.04,align=TextNode.ALeft)

	return

	

def clearText(task):
	global messageBox

	messageBox.setText('')
	return task.done

def showCityRating(ratingValue):

	global cityRatingBox
	cityRatingBox.setText('City Rating : ' + str(ratingValue))

def showDevelopmentRating(ratingValue):

	global developmentRatingBox
        developmentRatingBox.setText('Development Rating : ' + str(ratingValue))

def showHappinessRating(ratingValue):

	global happinessRatingBox
        happinessRatingBox.setText('Happiness Rating : ' + str(ratingValue))

def showEnvironmentRating(ratingValue):

	global environmentRatingBox
        environmentRatingBox.setText('Environment Rating : ' + str(ratingValue))

def showNoOfCitizens(countValue):

	global numberOfCitizensRatingBox
        numberOfCitizensRatingBox.setText('Citizen Count : ' + str(countValue))

def showMoneyValue(moneyValue):

	global moneyRatingBox
        moneyRatingBox.setText('Money : ' + str(moneyValue))

def showMessage(textToShow,color):
	global messageBox,timeInterval,errorSound
	
	errorSound.play()
	messageBox.setText(textToShow)
	if color=='red':

		messageBox['fg']=(1,0,0,1)

	elif color=='blue':
		messageBox['fg']=(0,0,1,1)

	elif color=='white':
		messageBox['fg'] = (1,1,1,1)	

	elif color=='orange':
		messageBox['fg'] = (1,0.4,0,1)

	taskMgr.doMethodLater(timeInterval, clearText,'clearText')
	return

#showMessage('Welcome to my game!','white')
#showCityRating(7)
#showMoneyValue(20000)
#showMessage('hi123','blue')
#run()

