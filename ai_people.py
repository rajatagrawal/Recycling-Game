import direct.directbase.DirectStart
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *
from panda3d.core import Point3
import random
base.disableMouse()
camera.setPos(0,-80,40)
camera.setHpr(0,-30,0)

#actor_to_move = Actor('../models/actor_to_move', {'walk':'../models/actor_to_move-walk'})
#actor_to_move.reparentTo(render)
#actor_to_move.loop('walk')
#actor_to_move.setHpr(90,0,0)
#actor_to_move.setPos(0,0,0)

#environ = loader.loadModel('../models/world')
#environ.reparentTo(render)


xCoordinates = [-10, 10]
yCoordinates = [10,-10]
direction = 'right'
heading='right'
duration = 7
distance = 150




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


counter = 0
def moveMyCharacter(actor_to_move):
	
	global heading,direction,distance, counter
	
	counter = counter + 1
	print counter

	chooseRandomDirection()

	if heading == 'right':
		if direction == 'right':
			
			moveDownInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX(),actor_to_move.getY()-distance, actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))
			turnRightInterval = actor_to_move.hprInterval(duration, Point3(actor_to_move.getH()-90,actor_to_move.getP(), actor_to_move.getR()),startHpr=Point3(actor_to_move.getH(),actor_to_move.getP(),actor_to_move.getR()))
			#sequenceGoingRightRight =
			Sequence(turnRightInterval,moveDownInterval,Func(moveMyCharacter,actor_to_move),name='goingRightRightSequence'+str(counter)).start()
			#sequenceGoingRightRight.start()
			heading = 'down'
			return

		elif direction =='left':
			moveUpInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX(),actor_to_move.getY()+distance, actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))
			turnLeftInterval = actor_to_move.hprInterval(duration, Point3(actor_to_move.getH()+90,actor_to_move.getP(), actor_to_move.getR()),startHpr=Point3(actor_to_move.getH(),actor_to_move.getP(),actor_to_move.getR()))
			#sequenceGoingRightLeft = 
			Sequence(turnLeftInterval,moveUpInterval,Func(moveMyCharacter,actor_to_move),name='goingRightLeftSequence'+str(counter)).start()

			#sequenceGoingRightLeft.start()
			heading='up'
			return

		elif direction =='forward':
			moveRightInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX() + distance,actor_to_move.getY(), actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))
			
			#sequenceGoingRightForward = 
			Sequence(moveRightInterval,Func(moveMyCharacter,actor_to_move),name='goingRightForwardSequence'+str(counter)).start()

			#sequenceGoingRightForward.start()
			heading='right'
			return

		elif direction =='backward':
			moveLeftInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX() - distance,actor_to_move.getY(), actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))
			turnBackwardInterval = actor_to_move.hprInterval(duration, Point3(actor_to_move.getH()-180,actor_to_move.getP(), actor_to_move.getR()),startHpr=Point3(actor_to_move.getH(),actor_to_move.getP(),actor_to_move.getR()))
			#sequenceGoingRightBackward = 
			Sequence(turnBackwardInterval,moveLeftInterval,Func(moveMyCharacter,actor_to_move),name='goingRightBackwardSequence'+str(counter)).start()

			#sequenceGoingRightBackward.start()
			heading='left'
			return

	if heading == 'down':
		if direction == 'right':
			moveLeftInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX() - distance,actor_to_move.getY(), actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))					
			turnRightInterval = actor_to_move.hprInterval(duration, Point3(actor_to_move.getH()-90,actor_to_move.getP(), actor_to_move.getR()),startHpr=Point3(actor_to_move.getH(),actor_to_move.getP(),actor_to_move.getR()))
			#sequenceGoingDownRight = 
			Sequence(turnRightInterval,moveLeftInterval,Func(moveMyCharacter,actor_to_move),name='goingDownRightSequence'+str(counter)).start()

			#sequenceGoingDownRight.start()
			heading = 'left'
			return

		elif direction =='left':

			moveRightInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX() + distance,actor_to_move.getY(), actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))
			turnLeftInterval = actor_to_move.hprInterval(duration, Point3(actor_to_move.getH()+90,actor_to_move.getP(), actor_to_move.getR()),startHpr=Point3(actor_to_move.getH(),actor_to_move.getP(),actor_to_move.getR()))
			#sequenceGoingDownLeft = 
			Sequence(turnLeftInterval,moveRightInterval,Func(moveMyCharacter,actor_to_move),name='goingDownLeftSequence'+str(counter)).start()
			#sequenceGoingDownLeft.start()
			heading='right'
			return

		elif direction =='forward':
			moveDownInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX(),actor_to_move.getY() - distance, actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))						
			#sequenceGoingDownForward = 
			Sequence(moveDownInterval,Func(moveMyCharacter,actor_to_move),name='goingDownForwardSequence'+str(counter)).start()
			#sequenceGoingDownForward.start()
			heading='down'
			return

		elif direction =='backward':
			moveUpInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX(),actor_to_move.getY() +distance, actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))
			turnBackwardInterval = actor_to_move.hprInterval(duration, Point3(actor_to_move.getH()-180,actor_to_move.getP(), actor_to_move.getR()),startHpr=Point3(actor_to_move.getH(),actor_to_move.getP(),actor_to_move.getR()))
			#sequenceGoingDownBackward = 
			Sequence(turnBackwardInterval,moveUpInterval,Func(moveMyCharacter,actor_to_move),name='goingDownBackwardSequence'+str(counter)).start()
 
			#sequenceGoingDownBackward.start()
			heading='up'
			return
		
	if heading == 'left':
		if direction == 'right':
			moveUpInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX(),actor_to_move.getY() + distance, actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))
			turnRightInterval = actor_to_move.hprInterval(duration, Point3(actor_to_move.getH()-90,actor_to_move.getP(), actor_to_move.getR()),startHpr=Point3(actor_to_move.getH(),actor_to_move.getP(),actor_to_move.getR()))
			#sequenceGoingLeftRight = 
			Sequence(turnRightInterval,moveUpInterval,Func(moveMyCharacter,actor_to_move),name='goingLeftRightSequence'+str(counter)).start()

			#sequenceGoingLeftRight.start()
			heading = 'up'
			return

		elif direction =='left':
			moveDownInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX(),actor_to_move.getY() - distance, actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))
			turnLeftInterval = actor_to_move.hprInterval(duration, Point3(actor_to_move.getH()+90,actor_to_move.getP(), actor_to_move.getR()),startHpr=Point3(actor_to_move.getH(),actor_to_move.getP(),actor_to_move.getR()))
			#sequenceGoingLeftLeft = 
			Sequence(turnLeftInterval,moveDownInterval,Func(moveMyCharacter,actor_to_move),name='goingLeftLeftSequence'+str(counter)).start()

			#sequenceGoingLeftLeft.start()
			heading='down'
			return

		elif direction =='forward':
			moveLeftInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX() -distance,actor_to_move.getY(), actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))						
			#sequenceGoingLeftForward = 
			Sequence(moveLeftInterval,Func(moveMyCharacter,actor_to_move),name='goingLeftForwardSequence'+str(counter)).start()

			#sequenceGoingLeftForward.start()
			heading='left'
			return

		elif direction =='backward':
			moveRightInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX() + distance,actor_to_move.getY(), actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))	
			turnBackwardInterval = actor_to_move.hprInterval(duration, Point3(actor_to_move.getH()-180,actor_to_move.getP(), actor_to_move.getR()),startHpr=Point3(actor_to_move.getH(),actor_to_move.getP(),actor_to_move.getR()))
			#sequenceGoingDownLeft = 
			Sequence(turnBackwardInterval,moveRightInterval,Func(moveMyCharacter,actor_to_move),name='goingDownLeftBackward'+str(counter)).start()

			#sequenceGoingLeftBackward.start()
			heading='right'
			return
	
	if heading == 'up':
		if direction == 'right':

			moveRightInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX() + distance,actor_to_move.getY(), actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))
			turnRightInterval = actor_to_move.hprInterval(duration, Point3(actor_to_move.getH()-90,actor_to_move.getP(), actor_to_move.getR()),startHpr=Point3(actor_to_move.getH(),actor_to_move.getP(),actor_to_move.getR()))
			#sequenceGoingUpRight = 
			Sequence(turnRightInterval,moveRightInterval,Func(moveMyCharacter,actor_to_move),name='goingUpRightSequence'+str(counter)).start()

			#sequenceGoingUpRight.start()
			
			heading = 'right'
			return

		elif direction =='left':
			
			moveLeftInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX() - distance,actor_to_move.getY(), actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))
			turnLeftInterval = actor_to_move.hprInterval(duration, Point3(actor_to_move.getH()+90,actor_to_move.getP(), actor_to_move.getR()),startHpr=Point3(actor_to_move.getH(),actor_to_move.getP(),actor_to_move.getR()))
			#sequenceGoingUpLeft = 
			Sequence(turnLeftInterval,moveLeftInterval,Func(moveMyCharacter,actor_to_move),name='goingUpLeftSequence'+str(counter)).start()

			#sequenceGoingUpLeft.start()
			heading='left'
			return

		elif direction =='forward':
			moveForwardInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX(),actor_to_move.getY() + distance, actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))						
			#sequenceGoingUpForward = 
			Sequence(moveForwardInterval,Func(moveMyCharacter,actor_to_move),name='goingUpForwardSequence'+str(counter)).start()
	
			#sequenceGoingUpForward.start()
			heading='up'
			return

		elif direction =='backward':
			moveDownInterval = actor_to_move.posInterval(duration, Point3(actor_to_move.getX(),actor_to_move.getY() - distance, actor_to_move.getZ()), startPos=Point3(actor_to_move.getX(),actor_to_move.getY(),actor_to_move.getZ()))
			turnBackwardInterval = actor_to_move.hprInterval(duration, Point3(actor_to_move.getH()-180,actor_to_move.getP(), actor_to_move.getR()),startHpr=Point3(actor_to_move.getH(),actor_to_move.getP(),actor_to_move.getR()))
			#sequenceGoingUpBackward = 
			Sequence(turnBackwardInterval,moveDownInterval,Func(moveMyCharacter,actor_to_move),name='goingUpBackwardSequence'+str(counter)).start()

			#sequenceGoingUpBackward.start()
			heading='down'
			return


#sequenceGoingRightForward = Sequence(moveRightInterval,Func(moveMyCharacter),name='goingRightForwardSequence')
#sequenceGoingRightForward.start()
#run()
