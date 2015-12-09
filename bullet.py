from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from tank import Tank
import math

 
class Bullet(Sprite):
    asset = ImageAsset("images/300px-BM_Grenade.png", Frame(100,20,100,115), 1, 'vertical')

    def __init__(self, position):
        super().__init__(Bullet.asset, position)
        t = 1.57
        V = 4
        self.vx=V*math.cos(t)
        self.vy=-V*math.sin(t)
        self.scale=.5
        self.vr=0
        self.fxcenter = .5
        self.fycenter = .5
        self.away = False


    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += .05
        self.rotation += .1
        colliding = self.collidingWithSprites(Tank)
        if colliding and self.away == True:  
            self.destroy()
            #print("COLLIDING")
            #if self.away == True:
                #print("AWAY")
                #self.away = False
        elif not colliding and self.away == False:
            #print("NOT AWAY")
            self.away = True
