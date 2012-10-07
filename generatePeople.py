#this file generates people at a fixed interval of time and provides them with intelligence to wander in the environment

import direct.directbase.DirectStart
from direct.actor.Actor import Actor
import random
from ai_people import wander
from panda3d.core import Point3
from gameVariables import setMoney,getMoney
from showGameMessages import showNoOfCitizens, showMoneyValue, showMessage,showHappinessRating, showEnvironmentRating, showDevelopmentRating, showCityRating

from gameVariables import setMoney,setEnvironmentRating, setHappinessRating,setDevelopmentRating, setNumberOfCitizens,setCityRating

from gameVariables import getMoney,getEnvironmentRating, getHappinessRating, getDevelopmentRating, getNumberOfCitizens, getCityRating

interval = 10
entranceFees = 5
peopleList = []
eRStepSize = 0.1

def producePeople_backbone(task):
	global peopleList, interval, entranceFees, eRStepSize
	actorType = random.randint(1,3)
	if actorType == 1:
		peopleList.append(Actor('models/ralph',{'walk':'models/ralph-walk'}))
		peopleList[len(peopleList)-1].setScale(5)
	
	elif actorType ==2:
		peopleList.append(Actor('models/eve/eve',{'walk':'models/eve/eve-walk'}))
		peopleList[len(peopleList)-1].setScale(5)

	elif actorType ==3:
		peopleList.append(Actor('models/nik-dragon',{'walk':'models/nik-dragon'}))
		peopleList[len(peopleList)-1].setScale(1.5)
		

	peopleList[len(peopleList)-1].setHpr(90,0,0)
	peopleList[len(peopleList)-1].loop('walk')
	peopleList[len(peopleList) - 1].reparentTo(render)
	wander(peopleList[len(peopleList)-1],Point3(-500,0,10))



	# update the environment Rating of the city

	setEnvironmentRating(getEnvironmentRating() - eRStepSize)
	showEnvironmentRating(getEnvironmentRating())

	# update the correspoding cityRating
	
	setCityRating((getEnvironmentRating() + getDevelopmentRating() + getHappinessRating())/3)
	showCityRating(getCityRating())

	# intimate game control to increase the total money

	setMoney(getMoney() + entranceFees)

	showMoneyValue(getMoney())
	# show the number of citizens on the screen

	showNoOfCitizens(len(peopleList))
	return task.again
	#return task.done



def generatePeople():
	taskMgr.doMethodLater(interval, producePeople_backbone, 'producePeopleTask')
