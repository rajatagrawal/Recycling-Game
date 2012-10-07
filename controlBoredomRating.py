import direct.directbase.DirectStart
from loadButtons import restaurant1
from generatePeople import peopleList
from showGameMessages import showMessage
from gameVariables import setBoredomRating

totalCapacity = 0
boredomRating = 0
bRValue = 3

def updateBoredomRating():
	
	global totalCapacity,boredomRating,bRValue

	totalCapacity = 0
	boredomRating = 0

	for i in range(len(restaurant1)):
		
		if restaurant1[i].type =='entertainment':
			
			totalCapacity = totalCapacity + restaurant1[i].capacity

	noOfPeople = len(peopleList)

	if len(peopleList)<totalCapacity:
		
		j = 0
		while noOfPeople>0:
			if restaurant1[j].type =='entertainment':
				if noOfPeople > restaurant1[j].capacity:
					
					boredomRating = boredomRating + (bRValue * restaurant1[j].capacity)
					noOfPeople = noOfPeople - restaurant[j].capacity
				else:
					boredomRating = boredomRating + (bRValue * noOfPeople)
					noOfPeople = 0
			j = j + 1

		boredomRating = boredomRating / len(peopleList)

		#showMessage('boredom Rating is ' + str(boredomRating),'blue')
		setBoredomRating(boredomRating)
		return boredomRating

	elif len(peopleList)>totalCapacity:
		
		excessPeople = len(peopleList) - totalCapacity
		k = 0

		while totalCapacity > 0:
			if restaurant1[k].type=='entertainment':
				boredomRating = boredomRating + (bRValue * restaurant1[k].capacity)
				totalCapacity = totalCapacity - restaurant1[k].capacity
				k = k + 1

		boredomRating = boredomRating - (bRValue * excessPeople)
		boredomRating = boredomRating / len(peopleList)

		showMessage('The citizens are getting bored. They cannot find any place to amuse. Build Cinema Halls','red')
		setBoredomRating(boredomRating)
		return boredomRating


