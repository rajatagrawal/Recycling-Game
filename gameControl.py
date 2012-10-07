#this file controls the game parameters such as city rating, environment rating

import direct.directbase.DirectStart
from loadButtons import restaurant1
from generatePeople import peopleList
from showGameMessages import  *
from controlHungerRating import updateHungerRating
from controlDevelopmentRating import updateDevelopmentRating
from controlEnvironmentRating import updateEnvironmentRating
from controlBoredomRating import updateBoredomRating
from controlMoneyRating import updateMoneyRating

from showGameMessages import showMoneyValue,showCityRating,showDevelopmentRating,showHappinessRating, showEnvironmentRating, showNoOfCitizens

from gameVariables import setMoney,setEnvironmentRating, setHappinessRating,setDevelopmentRating, setNumberOfCitizens,setCityRating

from gameVariables import getMoney,getEnvironmentRating, getHappinessRating, getDevelopmentRating, getNumberOfCitizens, getCityRating

from gameVariables import getBoredomRating, getNeedMoneyRating, getHungerRating

def updateCityRating():
	setCityRating((getDevelopmentRating() + getEnvironmentRating() + getHappinessRating())/3)	
	showCityRating(getCityRating())
	
def updateBoredomRating_1(task):
	setHappinessRating((getNeedMoneyRating() + updateBoredomRating() + getHungerRating()))
	showHappinessRating(getHappinessRating())
	updateCityRating()
	return task.again

def updateNeedMoneyRating_1(task):
        setHappinessRating((updateMoneyRating() + getBoredomRating() + getHungerRating()))
        showHappinessRating(getHappinessRating())
        updateCityRating()
        return task.again

def updateHungerRating_1(task):
        setHappinessRating((getNeedMoneyRating() + getBoredomRating() + updateHungerRating()))
        showHappinessRating(getHappinessRating())
        updateCityRating()
        return task.again



def updateDevelopmentRating_1(task):

	setDevelopmentRating(updateDevelopmentRating())
	showDevelopmentRating(getDevelopmentRating())
	updateCityRating()

	return task.again

def updateEnvironmentRating_1(task):

	setEnvironmentRating(updateEnvironmentRating())	
	showEnvironmentRating(getEnvironmentRating())
	updateCityRating()

	return task.again
def initializeGameControls(task):
	global showMoneyValue,showCityRating,showDevelopmentRating,showHappinessRating, showEnvironmentRating, showNoOfCitizens, showMessage
	setCityRating(0)
	setEnvironmentRating(0)
	setDevelopmentRating(0)
	setHappinessRating(0)
	setNumberOfCitizens(0)
	setMoney(10000)
	
	showCityRating(getCityRating())
	showDevelopmentRating(getDevelopmentRating())
	showHappinessRating(getHappinessRating())
	showEnvironmentRating(getEnvironmentRating())
	showNoOfCitizens(getNumberOfCitizens())
	showMoneyValue(getMoney())

	showMessage('Welcome to my game! Your target is to achieve a city rating of 5 by the end of December','white')
	return task.done

def startGameControl():
	taskMgr.add(initializeGameControls,'initialize Game Controls')
	taskMgr.doMethodLater(20,updateHungerRating_1,'updateHungerRating_1')
	taskMgr.doMethodLater(30, updateBoredomRating_1,'updateBoredomRating_1')
	taskMgr.doMethodLater (50, updateNeedMoneyRating_1,'updateNeedMoneyRating_1')	
	taskMgr.doMethodLater(30,updateDevelopmentRating_1,'updateDevelopmentRating_1')
	taskMgr.doMethodLater(40,updateEnvironmentRating_1,'updateEnvironmentRating_1')
