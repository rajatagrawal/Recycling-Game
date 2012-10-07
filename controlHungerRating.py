import direct.directbase.DirectStart
from loadButtons import restaurant1
from generatePeople import peopleList
from showGameMessages import showMessage
#from gameControl import hRating
from gameVariables import getHungerRating,setHungerRating

totalCapacity =0
hungerRating = 0
hRValue = 3
def updateHungerRating():

	global totalCapacity,hungerRating,hRValue

	totalCapacity = 0
	hungerRating = 0

	for i in range(len(restaurant1)):
		
		if restaurant1[i].type =='eating':

			totalCapacity = totalCapacity + restaurant1[i].capacity

	
	noOfPeople = len(peopleList)

	if len(peopleList)<totalCapacity:
		j=0
		while noOfPeople >0 :
			if restaurant1[j].type == 'eating':

				if noOfPeople > restaurant1[j].capacity:
					hungerRating = hungerRating + (hRValue * restaurant1[j].capacity)

					noOfPeople = noOfPeople - restaurant1[j].capacity


				else :
					hungerRating = hungerRating + (hRValue * noOfPeople)
					noOfPeople = 0

			j = j + 1

		hungerRating = hungerRating / len(peopleList)

		#showMessage('hungerRating is ' + str(hungerRating),'blue')
		setHungerRating(hungerRating)
		return hungerRating


	elif len(peopleList)>totalCapacity:

		excessPeople = len(peopleList) - totalCapacity
		k = 0
		while totalCapacity >0:
			
			if restaurant1[k].type == 'eating':

				hungerRating = hungerRating + (hRValue * restaurant1[k].capacity)

				totalCapacity = totalCapacity - restaurant1[k].capacity

				k = k + 1

		hungerRating = hungerRating - (hRValue*excessPeople)

		hungerRating = hungerRating / len(peopleList)

		showMessage('Citizens are feeling hungry. They cannot find enough places to eat. Build Restaurants. ','red')
		setHungerRating(hungerRating)
		return hungerRating
