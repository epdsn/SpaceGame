import pygame, sys
from player import Player
import obstacle
from random import choice, randint
from alien import Alien, ExtraAlien
from laser import Laser
from crt import CRT

class Game:
    def __init__(self):
        
        # Health and score setup
        self.lives = 3
        self.lives_surface  = pygame.image.load('assets/player.png').convert_alpha()
        self.lives_x_start_pos = screen_width - (self.lives_surface.get_size()[0] * 2 + 20) 
        self.score = 0
        self.font = pygame.font.Font('assets/fonts/ARCADECLASSIC.TTF', 20)
        self.text_color = (255,255,255) 
             
        
        #Player setup
        player_sprite = Player((screen_width/2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        
        # Obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstable_amount = 4
        self.obstacle_x_positions = [num * (screen_width / self.obstable_amount) for num in range(self.obstable_amount)]
        self.create_multiple_obstacles(*self.obstacle_x_positions, x_start = 0, y_start = 430 )

        # Alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.alient_setup(rows = 5, cols = 8, x_distance = 80, y_distance = 60, x_offset = 70, y_offset = 100)
        self.alien_direction = 1 

        # E.T. setup
        self.et_alien = pygame.sprite.GroupSingle()
        self.et_spawn_time = randint(40, 80)

        # Audio
        music = pygame.mixer.Sound('assets/sounds/music.wav')
        music.set_volume(0.2)
        music.play(loops = -1)  
        self.laser_sound = pygame.mixer.Sound('assets/sounds/laser.wav')
        self.laser_sound.set_volume(0.2)
        self.explosion_sound = pygame.mixer.Sound('assets/sounds/explosion.wav')
        self.explosion_sound.set_volume(0.2) 

        # Backbround image
        self.background = pygame.image.load('assets/background.png').convert()           
             
    def alient_setup(self, rows, cols, x_distance = 80, y_distance = 55, x_offset = 70, y_offset = 100):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                if row_index == 0: alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2: alien_sprite = Alien('green', x, y)
                else: alien_sprite = Alien('red', x, y)
                self.aliens.add(alien_sprite)
    
    def alien_direction_change(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width:
                self.alien_direction = -1
                self.alien_move_down(2)
            if alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_down(2)
    
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

    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien =  choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, 6, screen_height)
            self.alien_lasers.add(laser_sprite)
            self.laser_sound.play()  
            
    def et_timer(self):
        self.et_spawn_time -= 1
        if self.et_spawn_time <= 0:
            self.et_alien.add(ExtraAlien(choice(['right', 'left']), screen_width) )
            self.et_spawn_time = randint(400, 800)

    def collision_checks(self):
         # Player lasers
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                # Alien collision
                alien_hit = pygame.sprite.spritecollide(laser, self.aliens, True)  
                if alien_hit:
                    for alien in alien_hit:
                        self.score += alien.value 
                    laser.kill()
                    self.explosion_sound.play()
                # Obstacle collision
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()
                # E.T. collision
                if pygame.sprite.spritecollide(laser, self.et_alien, True):
                    self.score += 500 
                    laser.kill()
                    self.explosion_sound.play() 
                    
        # Alien lasers
        if self.alien_lasers:
            for laser in self.alien_lasers:
                # Player collision
                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.lives -= 1
                # Obstacle collision
                if pygame.sprite.spritecollide(laser, self.blocks, True): 
                    laser.kill()
        # E.T. collision with player
        if self.aliens:
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.blocks, True) 

                if pygame.sprite.spritecollide(alien, self.player, False): 
                    self.lives = 0  # Set lives to 0 instead of quitting immediately
    
    def display_lives(self):
        for live in range(self.lives - 1):
            x = self.lives_x_start_pos + (live * (self.lives_surface.get_size()[0] + 10))
            screen.blit(self.lives_surface, (x,8))   
    
    def display_score(self):
        score_surf = self.font.render(f'Score {self.score}', True, self.text_color)
        score_rect = score_surf.get_rect(topleft = (10,10))
        screen.blit(score_surf, score_rect)

    def game_over_message(self):
        if self.lives <= 0:
            game_over_surf = self.font.render('GAME OVER!', True, 'red')
            game_over_rect = game_over_surf.get_rect(center = (screen_width/2, screen_height/2 - 50))
            screen.blit(game_over_surf, game_over_rect)
            
            score_surf = self.font.render(f'Final Score: {self.score}', True, 'white')
            score_rect = score_surf.get_rect(center = (screen_width/2, screen_height/2 + 20))
            screen.blit(score_surf, score_rect)
            
            restart_surf = self.font.render('Press SPACE to restart or ESC to quit', True, 'yellow')
            restart_rect = restart_surf.get_rect(center = (screen_width/2, screen_height/2 + 60))
            screen.blit(restart_surf, restart_rect)
            
            pygame.display.flip()
            return True
        return False 

    def victory_message(self):
        if not self.aliens.sprites():
            victory_surf = self.font.render('YOU WIN!', True, 'green')
            victory_rect = victory_surf.get_rect(center = (screen_width/2, screen_height/2 - 50))
            screen.blit(victory_surf, victory_rect)
            
            score_surf = self.font.render(f'Final Score: {self.score}', True, 'white')
            score_rect = score_surf.get_rect(center = (screen_width/2, screen_height/2 + 20))
            screen.blit(score_surf, score_rect)
            
            restart_surf = self.font.render('Press SPACE to restart or ESC to quit', True, 'yellow')
            restart_rect = restart_surf.get_rect(center = (screen_width/2, screen_height/2 + 60))
            screen.blit(restart_surf, restart_rect)
            
            pygame.display.flip()
            return True
        return False 
    
    def run(self):
        self.player.update()
        self.alien_lasers.update()
        self.et_alien.update()

        self.aliens.update(self.alien_direction)
        self.alien_direction_change()
        self.et_timer()
        self.collision_checks()
        
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen) 
        self.blocks.draw(screen)
        self.aliens.draw(screen)   
        self.alien_lasers.draw(screen)
        self.et_alien.draw(screen)
        self.display_lives()  
        self.display_score()



if __name__ == "__main__": 
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock();
    pygame.display.set_caption("Space Game")
    game = Game()
    crt = CRT(screen_width, screen_height) 

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)    

    # Game Loop
    running = True
    game_over = False
    victory = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
            if event.type == ALIENLASER and not game_over and not victory:
                game.alien_shoot()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and (game_over or victory):
                    # Restart the game
                    game = Game()
                    game_over = False
                    victory = False
                elif event.key == pygame.K_ESCAPE and (game_over or victory):
                    pygame.quit()
                    sys.exit()
                    running = False
        
        screen.fill((30,30,30))  # Dark background
        screen.blit(game.background, (0,0))
        
        if not game_over and not victory:
            game.run()
            crt.draw(screen)
            
            # Check for game over or victory
            if game.lives <= 0:
                game_over = True
            elif not game.aliens.sprites():
                victory = True
        else:
            # Show game over or victory screen
            if game_over:
                game.game_over_message()
            elif victory:
                game.victory_message()

        pygame.display.flip()
        clock.tick(60)