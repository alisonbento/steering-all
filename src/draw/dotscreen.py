import pygame

class DotScreen:

  def __init__(self, screenWidth, screenHeight, fps = 60, screenMode = 0):
    pygame.init()
    self.width = screenWidth
    self.height = screenHeight
    self.fps = fps
    self.on = True

    windowDim = (int(screenWidth), int(screenHeight))
    self.displaysurf = pygame.display.set_mode(windowDim, screenMode)
    self.clock = pygame.time.Clock()

    self.world = None
    self.fillColor = (255, 255, 255)

    self.interacts = []

  def notifyInteracts(self):
    for interact in self.interacts:
      interact.checkInteraction()

  def addInteract(self, interact):
    self.interacts.append(interact)

  def setAllInteractsListener(self, listener):
    for interact in self.interacts:
      interact.setListener(listener)

  def setFPS(fps):
    self.fps = fps

  def setFillColor(color):
    self.fillColor = color

  def setWorld(self, world):
    world.setScreen(self)
    self.setAllInteractsListener(world)
    self.world = world

  def turnOff(self):
    self.on = False

  def step(self):
    self.notifyInteracts()
    self.clock.tick(self.fps)
    self.displaysurf.fill(self.fillColor)

    if self.world is not None:
      self.world.step()

    pygame.display.update()
