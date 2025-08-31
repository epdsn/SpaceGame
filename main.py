import pygame, sys
from player import Player
import obstacle

class Game:
    def __init__(self):
        #Player setup
        player_sprite = Player((screen_width/2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        
        #obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstable_amount = 4
        self.obstacle_x_positions = [num * (screen_width / self.obstable_amount) for num in range(self.obstable_amount)]
        self.create_multiple_obstacles(*self.obstacle_x_positions, x_start = 0, y_start = 430 )
    
    def create_obstacle(self, x_start, y_start, offset_x): 
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'X':
                    x = x_start + col_index * self.block_size + 50 + offset_x
                    y = y_start + row_index * self.block_size + 50
                    block = obstacle.Block(self.block_size, (200,200,200), x, y)
                    self.blocks.add(block)
        
    def create_multiple_obstacles(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)

        self.blocks.draw(screen)
    # update all sprite groups
    # draw all sprite groups

if __name__ == "__main__":
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock();
    pygame.display.set_caption("Space Game")
    game = Game()


    # Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
        
        screen.fill((30,30,30))  # Dark background
        game.run()

        pygame.display.flip()
        clock.tick(60)