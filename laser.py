import pygame

class Laser(pygame.sprite.Sprite):
    
    def __init__(self, pos, speed, screen_height):
        super().__init__()
        self.image = pygame.Surface((4,20))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.screen_contraint = screen_height
    
    def destroy(self):
        if self.rect.y <= -50 or  self.rect.y >= self.screen_contraint + 50:
            self.kill()

    def update(self):
        self.rect.y += self.speed
        self.destroy()
        
    

         