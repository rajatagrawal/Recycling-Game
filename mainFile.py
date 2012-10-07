#this is the main file where all modules are imported and executed

import direct.directbase.DirectStart
from loadEnvironment import loadEnvironment
from setCameraControl import setCameraControl
from keyboardCameraControl import enableKeyboardInteraction
from generatePeople import generatePeople
from loadButtons import loadButtons
from gameControl import startGameControl
from showGameMessages import loadMessageScreen
#from generatePeople import initializeGameControls

loadEnvironment()
setCameraControl()
enableKeyboardInteraction()
generatePeople()
loadButtons()
#initializeGameControls()
startGameControl()
loadMessageScreen()
base.setBackgroundColor(0,0,0)
backgroundMusic = loader.loadSfx('soundTrack.mp3')
backgroundMusic.setLoop(True)
backgroundMusic.play()
run()
