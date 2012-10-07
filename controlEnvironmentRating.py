import direct.directbase.DirectStart
from loadButtons import restaurant1
from generatePeople import peopleList
from showGameMessages import showMessage

eRating = 0
totalCapacity = 0

def updateEnvironmentRating():
	
	global totalCapacity,eRating

	totalCapacity = 0
	eRating = 0

	#this part should be modified to include more number of building built in the game

	for i in range(len(restaurant1)):
		totalCapacity = totalCapacity + restaurant1[i].capacity

	noOfPeople = len(peopleList)

	if len(peopleList)<totalCapacity:

		j = 0
		while noOfPeople >0:
			if noOfPeople > restaurant1[j].capacity:
				eRating = eRating + (restaurant1[j].eRValue * restaurant1[j].capacity)
				noOfPeople = noOfPeople - restaurant1[j].capacity

			else:
				eRating = eRating + (restaurant1[j].eRValue * noOfPeople)
				noOfPeople = 0

			j = j + 1

		eRating = eRating / len(peopleList)

		#showMessage('eRating is ' + str(eRating),'red')
		return eRating

	elif len(peopleList)>totalCapacity:
		
		k = 0

		while totalCapacity>0:
			
			eRating = eRating + (restaurant1[k].eRValue * restaurant1[k].capacity)
			totalCapacity = totalCapacity - restaurant1[k].capacity
			k = k + 1

		eRating = eRating / len(peopleList)

		#showMessage('eRating is a ' + str(eRating),'blue')

		return eRating
		

