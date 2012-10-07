import direct.directbase.DirectStart
from direct.actor.Actor import Actor

duration = 5
actorList = []
def produceActor(task):
	actorList.append(Actor('models/ralph', {'walk':'models/ralph-walk'}))
	actorList[len(actorList) - 1].setPos(duration * (len(actorList) - 1),50,0)     
	actorList[len(actorList) - 1].reparentTo(render)
	return task.again

def testFile():
	taskMgr.doMethodLater(duration, produceActor, 'produceActorTask')

#base.disableMouse()
#camera.setPos(0,0,0)
#run()
