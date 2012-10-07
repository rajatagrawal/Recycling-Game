import direct.directbase.DirectStart
from loadButtons import restaurant1
from generatePeople import peopleList
from showGameMessages import showMessage



dRating  = 0
totalCapacity = 0
dRValue = 3

def updateDevelopmentRating():
	
	global totalCapacity,dRating,dRValue

	totalCapacity = 0
	dRating = 0


	# this part should be modified to include more number of building built in the game

	for i in range(len(restaurant1)):

		totalCapacity = totalCapacity + restaurant1[i].capacity

	
	noOfPeople = len(peopleList)

	if len(peopleList)<totalCapacity:
		j = 0

		while noOfPeople >0:
			if noOfPeople > restaurant1[j].capacity:
				dRating = dRating + (restaurant1[j].fRValue * restaurant1[j].capacity)
				noOfPeople = noOfPeople - restaurant1[j].capacity

			else :
				dRating = dRating + (restaurant1[j].fRValue * noOfPeople)
				noOfPeople = 0

			j = j + 1

		dRating = dRating / len(peopleList)

		#showMessage('dRating is ' + str(dRating),'red')
		return dRating

	elif len(peopleList)>totalCapacity:
		
		excessPeople = len(peopleList) - totalCapacity
		k = 0

		while totalCapacity>0:
			
			dRating = dRating + (restaurant1[k].fRValue * restaurant1[k].capacity)

			totalCapacity = totalCapacity - restaurant1[k].capacity

			k = k + 1

		dRating = dRating - (dRValue * excessPeople)

		dRating = dRating / len(peopleList)

		#showMessage('dRating is a ' + str(dRating),'red')

		return dRating
