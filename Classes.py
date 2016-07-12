from math import *
from TOBASettings import keydic, globalvars

class Entity:
    def __init__(self, shape, health, maxhealth, collisiondamage, movX, movY):
        self.shape = shape
        self.maxX = shape[0][0]
        self.maxY = shape[0][1]
        self.minX = shape[0][0]
        self.minY = shape[0][1]
        for c in shape:
            if c[0] > self.maxX:
                self.maxX = c[0]
            elif c[0] < self.minX:
                self.minX = c[0]
            if c[0] > self.maxY:
                self.maxY = c[0]
            elif c[0] < self.minY:
                self.minY = c[0]
        self.health = health
        self.maxhealth = maxhealth
        self.collisiondamage = collisiondamage
        self.radius = math.sqrt(((self.maxX - self.minX)/2)**2 + ((self.maxY - self.minY)/2)**2)
        self.center = [self.maxX - (self.maxX - self.minX)/2, self.maxY - (self.maxY - self.minY)/2 ]
        self.movX = movX
        self.movY = movY
    def colides(self, e):
        return math.sqrt((self.center[0] - e.center[0]) ** 2 + (self.center[1] - e.center[1]) ** 2)
    def collsionHandle(self, e):
        e.health -= self.collisiondamage
        self.health -= e.collisiondamage
    def update(self, deltaT):
        namblaX = movX * deltaT
        namblaY = movY * deltaT
        self.maxX += namblaX
        self.minX += namblaX
        self.minY += namblaY
        self.maxY += namblaY
        for i in range(len(shape)):
            shape[i][0] += namblaX
            shape[i][1] += namblaY

class ClientToaster(Entity):
    def handle_keypress(self, k):
        if k in [keydic['w'], keydic['a'], keydic['s'], keydic['d']]
            if k == keydic['w']:
                self.movY += globalvars["movspeed"]
            elif k == keydic['a']:
                self.movX -= globalvars["movspeed"]
            elif k == keydic['s']:
                self.movY -= globalvars["movspeed"]
            else:
                self.movX += globalvars["movspeed"]
    def handle_keyrelease(self, k):
        if k in [keydic['w'], keydic['a'], keydic['s'], keydic['d']]
            if k == keydic['w']:
                self.movY = 0
            elif k == keydic['a']:
                self.movX = 0
            elif k == keydic['s']:
                self.movY = 0
            else:
                self.movX = 0

class ServerToaster(Entity):
    def getCurrentInfo(self, x, y, movX, movY):
        namblaX = x - self.center[0]
        namblaY = y - self.center[1]
        self.maxX += namblaX
        self.minX += namblaX
        self.maxY += namblaY
        self.minY += namblaY
        for i in range(len(shape)):
            shape[i][0] += namblaX
            shape[i][1] += namblaY
        self.movX = movX
        self.movY = movY
