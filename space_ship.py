class spaceship:
    def __init__(self, x, y, image_path)
        super().__init__()
        self.image = pygame.image.load(image_path)
    
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x += self.speed
        if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed

        if self.rect.left < 0:
                self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
