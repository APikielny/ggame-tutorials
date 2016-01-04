"""
Final Project
Adam Pikielny
Roger Danilek
Tank Game
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset
from tank import Tank1, Tank2
from bullet import Bullet, Explosion
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class TankGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0x000000, 1)
        noline = LineStyle(1, black)
        mtn = RectangleAsset(50,150,noline,Color(0x074a36,1.0))
        self.mtn = Sprite(mtn, (270,200))
        bg = RectangleAsset(700,100,noline,Color(0x074a36,1.0))
        #bg=PolygonAsset([(0,0),(700,0),(700,200),(0,200),(0,0)],noline,Color(0x074a36,1.0))
        self.bg=Sprite(bg, (0,300))
        tankOne=Tank1((random.randint(20,150),265))
        tankTwo=Tank2((random.randint(350,500),265))
        print("This is the first tank's position.")
        print(tankOne.position)
        print("This is the second tank's position.")
        print(tankTwo.position)
        print("There is a wall in the middle. It is 100px high.")
        bulletOne=Bullet((tankOne.position),self)
        bulletTwo=Bullet((tankTwo.position),self)
        #tankTwo=Tank((400,300))
        #bulletTwo=Bullet((tankTwo.position))
        
        
    def step(self):
        for ship in self.getSpritesbyClass(Tank1):
            ship.step()
        for ship in self.getSpritesbyClass(Tank2):
            ship.step()
        for ship in self.getSpritesbyClass(Bullet):
            ship.step()
        for ship in self.getSpritesbyClass(Explosion):
            ship.step()
            
myapp = TankGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
