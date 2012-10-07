import direct.directbase.DirectStart
from loadButtons import restaurant1
from generatePeople import peopleList
from showGameMessages import showMessage
from gameVariables import setNeedMoneyRating

totalCapacity = 0
moneyRating = 0
mRValue = 4

def updateMoneyRating():
	
	global totalCapacity,moneyRating, mRValue

	totalCapacity = 0
	moneyRating = 0

	for i in range(len(restaurant1)):
		
		if restaurant1[i].type =='finance':
			
			totalCapacity = totalCapacity + restaurant1[i].capacity

	noOfPeople = len(peopleList)

	if len(peopleList)<totalCapacity:
		j = 0
		while noOfPeople > 0:
			if restaurant1[j].type =='finance':
				if noOfPeople > restaurant1[j].capacity:
					
					moneyRating = moneyRating + (mRValue * restaurant1[j].capacity)
					noOfPeople = noOfPeople - restaurant1[j].capacity
				else:
					moneyRating = moneyRating + (mRValue * noOfPeople)
					noOfPeople = 0
			j = j + 1

		moneyRating = moneyRating / len(peopleList)

		#showMessage('money Rating is ' + str(moneyRating),'blue')
		setNeedMoneyRating(moneyRating)
		return moneyRating

	elif len(peopleList)>totalCapacity:
		
		excessPeople = len(peopleList) - totalCapacity
		k = 0

		while totalCapacity > 0:
			
			if restaurant1[k].type =='finance':
				moneyRating = moneyRating + (mRValue * restaurant1[k].capacity)
				totalCapacity = totalCapacity - restaurant1[k].capacity

				k = k + 1

		moneyRating = moneyRating - (mRValue * excessPeople)
		moneyRating = moneyRating / len(peopleList)

		showMessage(' The citizens don\'t have money to spend. Build industries for them to earn money.','red')
		setNeedMoneyRating(moneyRating)
		return moneyRating
