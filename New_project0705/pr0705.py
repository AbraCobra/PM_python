import pygame, random
vector = pygame.math.Vector2
pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption('Hunting eggs')

FPS = 60
clock = pygame.time.Clock()

class Game():
    def __init__(self):
        self.STARTING_ROUND_TIME = 30
        self.score = 0
        self.round_number = 1
        self.frame_count = 0
        self.round_time = self.STARTING_ROUND_TIME

        self.title_font = pygame.font.Font('fonts/Poultrygeist.ttf', 48)
        self.HUD_font = pygame.font.Font('fonts/Pixel.ttf', 24)

    def update(self):
        self.frame_count +=1
        if self.frame_count%FPS == 0:
            self.round_time -= 1
            self.frame_count = 0

    def draw(self):
        WHITE = (255, 255, 255)
        GREEN = (25, 200, 25)

        score_text = self.HUD_font.render('Score: ' + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, WINDOW_HEIGHT  - 50)

        health_text = self.HUD_font.render("Health: " + str(100),True, WHITE )
        health_rect = health_text.get_rect()
        health_rect.topleft = (10, WINDOW_HEIGHT - 25)

        title_text = self.title_font.render("ZOMBIE", True, GREEN)
        title_rect = title_text.get_rect()
        title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT - 25)

        round_text = self.HUD_font.render("Night: " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 50) 
    
        time_text = self.HUD_font.render("Sunrise In: " + str(self.round_time), True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 25)
    
        display_surface.blit(score_text,  score_rect)
        display_surface.blit(health_text, health_rect)
        display_surface.blit(title_text, title_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(time_text, time_rect)
        
    
    def add_monsters(self):
        pass

    def check_collisions(self):
        pass

    def check_round_completion(self):
        pass

    def check_game_over(self):
        pass

    def start_new_round(self):
        pass

    def pause_game(self):
        pass

    def reset(self):
        pass


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image_int, main_group, sub_group = ''):
        super().__init__()
        if image_int == 1:
            self.image = pygame.transform.scale(pygame.image.load('Images/tiles/Tile (1).png'), (32,32))
        elif image_int == 2:
            self.image = pygame.transform.scale(pygame.image.load('Images/tiles/Tile (2).png'), (32,32))
            sub_group.add(self)
        elif image_int == 3:
            self.image = pygame.transform.scale(pygame.image.load('Images/tiles/Tile (3).png'), (32,32))
            sub_group.add(self)
        elif image_int == 4:
            self.image = pygame.transform.scale(pygame.image.load('Images/tiles/Tile (4).png'), (32,32))
            sub_group.add(self)
        elif image_int == 5:
            self.image = pygame.transform.scale(pygame.image.load('Images/tiles/Tile (5).png'), (32,32))
            sub_group.add(self)
        main_group.add(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Player(pygame.sprite.Sprite):
    def __init__(self,x, y, plaform_group, portal_group, bullet_group):
        super().__init__()
        self. HORIZONTAL_ACCELERATION = 0.8
        self.HORIZONTAL_FRICTION = 0.15
        self.VERTICAL_ACCELERATION = 0.5
        self.VERTICAL_JUMP_SPEED = 18
        self.STARTING_HEALTH = 100

        self.move_right_sprites = []
        self.move_left_sprites  = []
        self.idle_right_sprites = []
        self.idle_left_sprites  = []
        self.jump_right_sprites = []
        self.jump_left_sprites  = []
        self.attack_right_sprites = []
        self.attack_left_sprites  = []

        #Moving
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/run/Run (1).png'), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/run/Run (2).png'), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/run/Run (3).png'), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/run/Run (4).png'), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/run/Run (5).png'), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/run/Run (6).png'), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/run/Run (7).png'), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/run/Run (8).png'), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/run/Run (9).png'), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/run/Run (10).png'), (64, 64)))
        for sprite in self.move_right_sprites:
            self.move_left_sprites.append(pygame.transform.flip(sprite, True, False))

        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/idle/Idle (1).png'), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/idle/Idle (2).png'), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/idle/Idle (3).png'), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/idle/Idle (4).png'), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/idle/Idle (5).png'), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/idle/Idle (6).png'), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/idle/Idle (7).png'), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/idle/Idle (8).png'), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/idle/Idle (9).png'), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/idle/Idle (10).png'), (64, 64)))
        for sprite in self.idle_right_sprites:
            self.idle_left_sprites.append(pygame.transform.flip(sprite, True, False))

        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/jump/Jump (1).png'), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/jump/Jump (2).png'), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/jump/Jump (3).png'), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/jump/Jump (4).png'), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/jump/Jump (5).png'), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/jump/Jump (6).png'), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/jump/Jump (7).png'), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/jump/Jump (8).png'), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/jump/Jump (9).png'), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/jump/Jump (10).png'), (64, 64)))
        for sprite in self.jump_right_sprites:
            self.jump_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/attack/Attack (1).png'), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/attack/Attack (1).png'), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/attack/Attack (1).png'), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/attack/Attack (1).png'), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/attack/Attack (1).png'), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/attack/Attack (1).png'), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/attack/Attack (1).png'), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/attack/Attack (1).png'), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/attack/Attack (1).png'), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/player/attack/Attack (1).png'), (64, 64)))
        for sprite in self.attack_right_sprites:
            self.attack_left_sprites.append(pygame.transform.flip(sprite, True, False))

        self.current_sprite = 0
        self.image = self.idle_right_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        self.platform_group = plaform_group
        self.portal_group = portal_group
        self.bullet_group = bullet_group

        self.animate_jump = False
        self.animate_fire = False

        self.jump_sound = pygame.mixer.Sound('sounds/jump_sound.wav')
        self.slash_sound = pygame.mixer.Sound('sounds/slash_sound.wav')
        self.portal_sound = pygame.mixer.Sound('sounds/portal_sound.wav')
        self.hit_sound = pygame.mixer.Sound('sounds/player_hit.wav')

        #Kinematics vectors
        self. position = vector(x, y)
        self.velocity  = vector(0, 0)
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

        self.health = self.STARTING_HEALTH
        self.starting_x = x
        self.starting_y = y


    def update(self):
        self.move()
        self.check_collisions()
        self.check_animations()

    def move(self):
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -1*self.HORIZONTAL_ACCELERATION
            self.animate(self.move_left_sprites, .5)
        elif keys[pygame.K_RIGHT]:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION
            self.animate(self.move_right_sprites, .5)
        else:
            if self.velocity.x > 0:
                self.animate(self.idle_right_sprites, .5)
            else:
                self.animate(self.idle_left_sprites, .5) 
        
        self.acceleration.x -= self.velocity.x*self.HORIZONTAL_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5*self.acceleration
    
        if self.position.x < 0 :
            self.position.x = WINDOW_WIDTH
        elif self.position.x > WINDOW_WIDTH:
            self.position.x = 0
        self.rect.bottomleft = self.position
   
    def check_collisions(self):
        if self.velocity.y > 0:
            collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
            if collided_platforms:
                self.position.y = collided_platforms[0].rect.top + 5
                self.velocity.y = 0
        if self.velocity.y <  0:
            collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
            if collided_platforms:
                self.velocity.y = 0
                while pygame.sprite.spritecollide(self, self.platform_group, False):
                    self.position.y += 1
                    self.rect.bottomleft = self.position
        #Collisions check for portalls
        if pygame.sprite.spritecollide(self, self.portal_group, False):
            self.portal_sound.play()
            if self.position.x > WINDOW_WIDTH//2:
                self.position.x = 80
            else:
                self.position.x = WINDOW_WIDTH - 150
            if self.position.y > WINDOW_HEIGHT//2:
                self.position.y = 64
            else:
                self.position.y = WINDOW_HEIGHT - 132
            self.rect.bottomleft = self.position



    def check_animations(self):
        if self.animate_jump:
            if self.velocity.x > 0:
                self.animate(self.jump_right_sprites, .1)
            else:
                self.animate(self.jump_left_sprites, .1)
        if self.animate_fire:
            if self.velocity.x > 0:
                self.animate(self.attack_right_sprites, .3)
            else:
                self.animate(self.attack_left_sprites, .3)


    def jump(self):
        if pygame.sprite.spritecollide(self, self.platform_group, False):
            self. jump_sound.play()
            self.velocity.y = -1*self.VERTICAL_JUMP_SPEED
            self.animate_jump = True

    def fire(self):
        self.slash_sound.play()
        Bullet(self.rect.centerx, self.rect.centery, self.bullet_group, self)
        self.animate_fire = True

    def reset(self):
       self.position = vector(self.starting_x, self.starting_y)
       self.rect.bottomleft = self.position


    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list)-1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
            if self.animate_jump:
                self.animate_jump = False
            if self.animate_fire:
                self.animate_fire = False
        self.image = sprite_list[int(self.current_sprite)]


class Bullet(pygame. sprite.Sprite):
    def __init__(self, x, y, bullet_group, player):
        super().__init__()
        self.VELOCITY = 20
        self.RANGE = 500
        if player.velocity.x > 0:
            self.image = pygame.transform.scale(pygame.image.load('Images/player/slash.png'), (32, 32))
        else:
            self.image = pygame.transform.scale(pygame. transform.flip(pygame.image.load('Images/player/slash.png'), True, False), (32, 32))
            self.VELOCITY = -1*self.VELOCITY
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.starting_x = x
        bullet_group.add(self)


    def update(self):
        self.rect.x += self.VELOCITY
        if abs(self.rect.x - self.starting_x) > self.RANGE:
            self.kill()


class Monster(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def update(self):
        pass

    def move(self):
        pass

    def check_collisions(self):
        pass

    def check_aninmations(self):
        pass

    def animate(self):
        pass


class RubyMaker(pygame.sprite.Sprite):
    def __init__(self, x, y, main_group):
        super().__init__()
        self.ruby_sprites = []
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load('Images/ruby/tile000.png'), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load('Images/ruby/tile001.png'), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load('Images/ruby/tile002.png'), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load('Images/ruby/tile003.png'), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load('Images/ruby/tile004.png'), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load('Images/ruby/tile005.png'), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load('Images/ruby/tile006.png'), (64, 64)))

        self.current_sprite = 0
        self.image = self.ruby_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        main_group.add(self)
    def update(self):
        self.animate(self.ruby_sprites, 0.25)

    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list)-1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
        self.image = sprite_list[int(self.current_sprite)]


class Ruby(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def update(self):
        pass

    def move(self):
        pass

    def check_collisions(self):
        pass

    def animate(self):
        pass


class Portal(pygame.sprite.Sprite):
    def __init__(self,x, y, color, portal_group):
        super().__init__()
        self.portal_sprites = []
        if color == 'green':
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile000.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile001.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile002.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile003.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile004.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile005.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile006.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile007.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile008.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile009.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile010.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile011.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile012.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile013.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile014.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile015.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile016.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile017.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile018.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile019.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile020.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/green/tile021.png'), (72,72)))
        else:
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile000.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile001.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile002.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile003.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile004.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile005.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile006.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile007.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile008.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile009.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile010.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile011.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile012.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile013.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile014.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile015.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile016.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile017.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile018.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile019.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile020.png'), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('Images/portals/purple/tile021.png'), (72,72)))
        self.current_sprite = random.randint(0, len(self.portal_sprites)-1)
        self.image = self.portal_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        portal_group.add(self)
    def update(self):
        self.animate(self.portal_sprites, 0.2)

    def animate(self, sprite_list, speed):
        if self.current_sprite < len(self.portal_sprites) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
        self.image = self.portal_sprites[int(self.current_sprite)]
#Create group
my_main_tile_group = pygame.sprite.Group()
my_platform_group = pygame.sprite.Group()

my_player_group = pygame.sprite.Group()
my_bullet_group = pygame.sprite.Group()

my_zombie_group = pygame.sprite.Group()

my_portal_group = pygame.sprite.Group()
my_ruby_group = pygame.sprite.Group()
#create tile map
# 0 -> no tile, 1=> dirt, 2-5 => platforms, 6=> ruby maker,  7-8=> portals, 9=> player
#23 rows and 40 columns
tile_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

#generate tile object
for i in range (len(tile_map)):
    for j in range (len(tile_map[i])):
        #dirt tile
        if tile_map[i][j] == 1:
            Tile(j*32, i*32, 1, my_main_tile_group) 
        elif tile_map[i][j] == 2:
            Tile(j*32, i*32, 2, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 3:
            Tile(j*32, i*32, 3, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 4:
            Tile(j*32, i*32, 4, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 5:
            Tile(j*32, i*32, 5, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 6:
            RubyMaker(j*32, i*32, my_main_tile_group)
        elif tile_map[i][j] == 7:
            Portal(j*32, i*32, 'green', my_portal_group)
        elif tile_map[i][j] == 8:
            Portal(j*32, i*32, 'purple', my_portal_group)
        elif tile_map[i][j] == 9:
            my_player = Player(j*32, i*32, my_platform_group, my_portal_group, my_bullet_group)
            my_player_group.add(my_player)
background_image = pygame.transform.scale(pygame.image.load('Images/cave.png'), (1280, 736))
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

my_game = Game()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.jump()
            if event.key == pygame.K_UP:
                my_player.fire()
    display_surface.blit(background_image, background_rect)
    my_main_tile_group.update()
    my_main_tile_group.draw(display_surface)

    my_portal_group.update()
    my_portal_group.draw(display_surface)

    my_player_group.update()
    my_player_group.draw(display_surface)
    my_bullet_group.update()
    my_bullet_group.draw(display_surface)
    my_game.update()
    my_game.draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()