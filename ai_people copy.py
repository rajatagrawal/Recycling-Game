import direct.directbase.DirectStart
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *
from panda3d.core import Point3
import random
base.disableMouse()
camera.setPos(0,-80,40)
camera.setHpr(0,-30,0)

ralph = Actor('../models/ralph', {'walk':'../models/ralph-walk'})
ralph.reparentTo(render)
ralph.loop('walk')
ralph.setHpr(90,0,0)
ralph.setPos(0,0,0)

environ = loader.loadModel('../models/world')
environ.reparentTo(render)


xCoordinates = [-10, 10]
yCoordinates = [10,-10]
direction = 'right'
heading='right'
duration = 5
distance = 20

moveRightInterval = ralph.posInterval(duration, Point3(ralph.getX()+distance,ralph.getY(), ralph.getZ()), startPos = Point3(ralph.getX(),ralph.getY(),ralph.getZ()))



def wander(actor_name, startCoordinate):
	
	global distance, duration
	actor_name.setPos(startCoordinate)	
	moveRightInterval = actor_name.posInterval(duration, Point3(actor_name.getX()+distance, actor_name.getY(),actor_name.getZ()),startPos = Point3(actor_name.getX(),actor_name.getY(),actor_name.getZ()))
	sequenceGoingRightForward = Sequence(moveRightInterval,Func(moveMyCharacter,actor_name),name='goingRightForwardSequence')
	sequenceGoingRightForward.start()



def chooseRandomDirection():
	global direction
	randomNumber = random.randint(1,4)
	if randomNumber ==1:
		direction = 'right'

	elif randomNumber ==2:
		direction = 'left'
	
	elif randomNumber ==3:
		direction =='forward'
	
	elif randomNumber ==4:
		direction=='backward'

def moveMyCharacter(actor_to_move):
	
	global heading,direction,distance,ralph

	chooseRandomDirection()

	if heading == 'right':
		if direction == 'right':
			
			moveDownInterval = ralph.posInterval(duration, Point3(ralph.getX(),ralph.getY()-distance, ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))
			turnRightInterval = ralph.hprInterval(duration, Point3(ralph.getH()-90,ralph.getP(), ralph.getR()),startHpr=Point3(ralph.getH(),ralph.getP(),ralph.getR()))
			sequenceGoingRightRight = Sequence(turnRightInterval,moveDownInterval,Func(moveMyCharacter),name='goingRightRightSequence')
			sequenceGoingRightRight.start()
			heading = 'down'
			return

		elif direction =='left':
			moveUpInterval = ralph.posInterval(duration, Point3(ralph.getX(),ralph.getY()+distance, ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))
			turnLeftInterval = ralph.hprInterval(duration, Point3(ralph.getH()+90,ralph.getP(), ralph.getR()),startHpr=Point3(ralph.getH(),ralph.getP(),ralph.getR()))
			sequenceGoingRightLeft = Sequence(turnLeftInterval,moveUpInterval,Func(moveMyCharacter),name='goingRightLeftSequence')

			sequenceGoingRightLeft.start()
			heading='up'
			return

		elif direction =='forward':
			moveRightInterval = ralph.posInterval(duration, Point3(ralph.getX() + distance,ralph.getY(), ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))
			
			sequenceGoingRightForward = Sequence(moveRightInterval,Func(moveMyCharacter),name='goingRightForwardSequence')

			sequenceGoingRightForward.start()
			heading='right'
			return

		elif direction =='backward':
			moveLeftInterval = ralph.posInterval(duration, Point3(ralph.getX() - distance,ralph.getY(), ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))
			turnBackwardInterval = ralph.hprInterval(duration, Point3(ralph.getH()-180,ralph.getP(), ralph.getR()),startHpr=Point3(ralph.getH(),ralph.getP(),ralph.getR()))
			sequenceGoingRightBackward = Sequence(turnBackwardInterval,moveLeftInterval,Func(moveMyCharacter),name='goingRightBackwardSequence')

			sequenceGoingRightBackward.start()
			heading='left'
			return

	if heading == 'down':
		if direction == 'right':
			moveLeftInterval = ralph.posInterval(duration, Point3(ralph.getX() - distance,ralph.getY(), ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))					
			turnRightInterval = ralph.hprInterval(duration, Point3(ralph.getH()-90,ralph.getP(), ralph.getR()),startHpr=Point3(ralph.getH(),ralph.getP(),ralph.getR()))
			sequenceGoingDownRight = Sequence(turnRightInterval,moveLeftInterval,Func(moveMyCharacter),name='goingDownRightSequence')

			sequenceGoingDownRight.start()
			heading = 'left'
			return

		elif direction =='left':

			moveRightInterval = ralph.posInterval(duration, Point3(ralph.getX() + distance,ralph.getY(), ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))
			turnLeftInterval = ralph.hprInterval(duration, Point3(ralph.getH()+90,ralph.getP(), ralph.getR()),startHpr=Point3(ralph.getH(),ralph.getP(),ralph.getR()))
			sequenceGoingDownLeft = Sequence(turnLeftInterval,moveRightInterval,Func(moveMyCharacter),name='goingDownLeftSequence')
			sequenceGoingDownLeft.start()
			heading='right'
			return

		elif direction =='forward':
			moveDownInterval = ralph.posInterval(duration, Point3(ralph.getX(),ralph.getY() - distance, ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))						
			sequenceGoingDownForward = Sequence(moveDownInterval,Func(moveMyCharacter),name='goingDownForwardSequence')
			sequenceGoingDownForward.start()
			heading='down'
			return

		elif direction =='backward':
			moveUpInterval = ralph.posInterval(duration, Point3(ralph.getX(),ralph.getY() +distance, ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))
			turnBackwardInterval = ralph.hprInterval(duration, Point3(ralph.getH()-180,ralph.getP(), ralph.getR()),startHpr=Point3(ralph.getH(),ralph.getP(),ralph.getR()))
			sequenceGoingDownBackward = Sequence(turnBackwardInterval,moveUpInterval,Func(moveMyCharacter),name='goingDownBackwardSequence')
 
			sequenceGoingDownBackward.start()
			heading='up'
			return
		
	if heading == 'left':
		if direction == 'right':
			moveUpInterval = ralph.posInterval(duration, Point3(ralph.getX(),ralph.getY() + distance, ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))
			turnRightInterval = ralph.hprInterval(duration, Point3(ralph.getH()-90,ralph.getP(), ralph.getR()),startHpr=Point3(ralph.getH(),ralph.getP(),ralph.getR()))
			sequenceGoingLeftRight = Sequence(turnRightInterval,moveUpInterval,Func(moveMyCharacter),name='goingLeftRightSequence')

			sequenceGoingLeftRight.start()
			heading = 'up'
			return

		elif direction =='left':
			moveDownInterval = ralph.posInterval(duration, Point3(ralph.getX(),ralph.getY() - distance, ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))
			turnLeftInterval = ralph.hprInterval(duration, Point3(ralph.getH()+90,ralph.getP(), ralph.getR()),startHpr=Point3(ralph.getH(),ralph.getP(),ralph.getR()))
			sequenceGoingLeftLeft = Sequence(turnLeftInterval,moveDownInterval,Func(moveMyCharacter),name='goingLeftLeftSequence')

			sequenceGoingLeftLeft.start()
			heading='down'
			return

		elif direction =='forward':
			moveLeftInterval = ralph.posInterval(duration, Point3(ralph.getX() -distance,ralph.getY(), ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))						
			sequenceGoingLeftForward = Sequence(moveLeftInterval,Func(moveMyCharacter),name='goingLeftForwardSequence')

			sequenceGoingLeftForward.start()
			heading='left'
			return

		elif direction =='backward':
			moveRightInterval = ralph.posInterval(duration, Point3(ralph.getX() + distance,ralph.getY(), ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))	
			turnBackwardInterval = ralph.hprInterval(duration, Point3(ralph.getH()-180,ralph.getP(), ralph.getR()),startHpr=Point3(ralph.getH(),ralph.getP(),ralph.getR()))
			sequenceGoingDownLeft = Sequence(turnBackwardInterval,moveRightInterval,Func(moveMyCharacter),name='goingDownLeftBackward')

			sequenceGoingLeftBackward.start()
			heading='right'
			return
	
	if heading == 'up':
		if direction == 'right':

			moveRightInterval = ralph.posInterval(duration, Point3(ralph.getX() + distance,ralph.getY(), ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))
			turnRightInterval = ralph.hprInterval(duration, Point3(ralph.getH()-90,ralph.getP(), ralph.getR()),startHpr=Point3(ralph.getH(),ralph.getP(),ralph.getR()))
			sequenceGoingUpRight = Sequence(turnRightInterval,moveRightInterval,Func(moveMyCharacter),name='goingUpRightSequence')

			sequenceGoingUpRight.start()
			
			heading = 'right'
			return

		elif direction =='left':
			
			moveLeftInterval = ralph.posInterval(duration, Point3(ralph.getX() - distance,ralph.getY(), ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))
			turnLeftInterval = ralph.hprInterval(duration, Point3(ralph.getH()+90,ralph.getP(), ralph.getR()),startHpr=Point3(ralph.getH(),ralph.getP(),ralph.getR()))
			sequenceGoingUpLeft = Sequence(turnLeftInterval,moveLeftInterval,Func(moveMyCharacter),name='goingUpLeftSequence')

			sequenceGoingUpLeft.start()
			heading='left'
			return

		elif direction =='forward':
			moveForwardInterval = ralph.posInterval(duration, Point3(ralph.getX(),ralph.getY() + distance, ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))						
			sequenceGoingUpForward = Sequence(moveForwardInterval,Func(moveMyCharacter),name='goingUpForwardSequence')
	
			sequenceGoingUpForward.start()
			heading='up'
			return

		elif direction =='backward':
			moveDownInterval = ralph.posInterval(duration, Point3(ralph.getX(),ralph.getY() - distance, ralph.getZ()), startPos=Point3(ralph.getX(),ralph.getY(),ralph.getZ()))
			turnBackwardInterval = ralph.hprInterval(duration, Point3(ralph.getH()-180,ralph.getP(), ralph.getR()),startHpr=Point3(ralph.getH(),ralph.getP(),ralph.getR()))
			sequenceGoingUpBackward = Sequence(turnBackwardInterval,moveDownInterval,Func(moveMyCharacter),name='goingUpBackwardSequence')

			sequenceGoingUpBackward.start()
			heading='down'
			return


#sequenceGoingRightForward = Sequence(moveRightInterval,Func(moveMyCharacter),name='goingRightForwardSequence')
#sequenceGoingRightForward.start()
#run()
