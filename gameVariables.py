import direct.directbase.DirectStart
import os

# order of parameter in the file is 

#money 0
#cityRating 1
#environment Rating 2
#development Rating 3
#happiness rating 4
#number of Citizens 5
# hunger RAting 6
# boredom Rating 7
# needMoneyRating 8

def getNumberOfCitizens():
	return getValue(5)

def getMoney():
	return getValue(0)

def getEnvironmentRating():
	return getValue(2)

def getDevelopmentRating():
	return getValue(3)

def getHappinessRating():
	return getValue(4)

def getCityRating():
        return getValue(1)

def getHungerRating():
	return getValue(6)

def getBoredomRating():
	return getValue(7)

def getNeedMoneyRating():
	return getValue(8)

def setValue(valueToSet, lineNo):
	
	parameterFileHandler = open('gameParameters.txt','r')
	parameterFile_tempHandler = open('gameParameters_temp.txt','w')
	i = 0
	for line in parameterFileHandler:
		if lineNo == i:
			parameterFile_tempHandler.write(str(valueToSet) + '\n')

		else:
			parameterFile_tempHandler.write(line)
		i = i + 1

	parameterFileHandler.close()
	parameterFile_tempHandler.close()
	os.system('mv gameParameters_temp.txt gameParameters.txt')

def setMoney(valueToSet):
	setValue(valueToSet,0)

def setCityRating(valueToSet):
	setValue(valueToSet,1)

def setEnvironmentRating(valueToSet):
	setValue(valueToSet,2)

def setDevelopmentRating(valueToSet):
	setValue(valueToSet,3)

def setHappinessRating(valueToSet):
	setValue(valueToSet,4)

def setNumberOfCitizens(valueToSet):
	setValue(valueToSet,5)

def setHungerRating(valueToSet):
	setValue(valueToSet,6)

def setBoredomRating(valueToSet):
	setValue(valueToSet,7)

def setNeedMoneyRating(valueToSet):
	setValue(valueToSet,8)


def getValue(lineNo):
	
	parameterFileHandler = open('gameParameters.txt','r')
	i = 0
	for line in parameterFileHandler:
		if lineNo == i:
			return float(line)

		i = i + 1
	
	parameterFileHandler.close()

