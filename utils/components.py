import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
GREEN = (0, 255, 0)

class Cell(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None, w=None, h=None, color=None, value=None, is_circle=None, radius=None):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)
        self.surf = pygame.Surface((w, h))
        self.surf.fill((255, 255,255))
        self.value = value
        self.originalColor = color
        self.color = color
        self.is_circle = is_circle 
        self.radius = radius
    
    def draw(self, surface):
        if self.is_circle:
            pygame.draw.rect(surface, self.color, self.rect, 20 if self.color != GREEN else 0)
        else:
            pygame.draw.circle(surface, self.color, (self.w, self.h), self.radius, 15)
    
    def updateColor(self, surface, color):
        self.color = color
        self.draw()
    
    def resetColor(self, surface):
        self.color = self.originalColor
        self.draw()
    


