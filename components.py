import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
GREEN = (0, 255, 0)

class Cell(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None, w=None, h=None, color=None, value=None):
        super().__init__()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, w, h)
        self.surf = pygame.Surface((w, h))
        self.surf.fill((255, 255,255))
        self.value = value
        self.originalColor = color
        self.color = color
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 20 if self.color != GREEN else 0)
    
    def updateColor(self, surface, color):
        self.color = color
        pygame.draw.rect(surface, self.color, self.rect, 20 if self.color != GREEN else 0)
    
    def resetColor(self, surface):
        self.color = self.originalColor
        pygame.draw.rect(surface, self.color, self.rect, 20 if self.color != GREEN else 0)