import pygame, random 
vector = pygame.math.Vector2
pygame.init()

WINDOW_WIDTH  = 960
WINDOW_HEIGHT = 640
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Making a tiles map')

FPS = 60
clock = pygame.time.Clock()
#Define classes
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image_int, main_group, sub_group = ""):
        super().__init__()
        #load image and add in correct group
        if image_int == 1:
            self.image = pygame.transform.scale(pygame.image.load('Images/Dirt1.png'), (32,32))
        elif image_int == 2:
            self.image = pygame.transform.scale(pygame.image.load('Images/Tile_middle.png'), (32,32))
            self.mask = pygame.mask.from_surface(self.image)
            sub_group.add(self)
        elif image_int ==  3:
            self.image = pygame.image.load('Images/water.png')
            sub_group.add(self)
        elif image_int == 8:
            self.image = pygame.transform.scale(pygame.image.load('Images/Tree_2.png'), (64, 64))
        elif image_int == 9:
            self.image = pygame.transform.scale(pygame.image.load('Images/Tile_edg_left.png'), (32,32))
        elif image_int == 10:
            self.image = pygame.transform.scale(pygame.image.load('Images/Tile_edge_right.png'), (32,32))
        elif image_int == 11:
            self.image = pygame.transform.scale(pygame.image.load('Images/Dirt2.png'), (32,32))
        elif image_int == 12:
            self.image = pygame.transform.scale(pygame.image.load('Images/Block.png'), (32,32))
            sub_group.add(self)

        
        main_group.add(self)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def update(self):
        #pygame.draw.rect(display_surface, (0, 0, 255), self.rect, 1)
        pass
                
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, grass_tiles, water_tiles):
        super().__init__()
        #Animation
        self.move_right_sprites = []
        self.move_left_sprites  = []
        self.idle_right_sprites = []
        self.idle_left_sprites  = []
        self.jump_right_sprites = []
        self.jump_left_sprites  = []

        self.animate_jump = False

        #moving right
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/run/Run1.png'), (84, 84)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/run/Run2.png'), (84, 84)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/run/Run3.png'), (84, 84)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/run/Run4.png'), (84, 84)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/run/Run5.png'), (84, 84)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/run/Run6.png'), (84, 84)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/run/Run7.png'), (84, 84)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/run/Run8.png'), (84, 84)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/run/Run9.png'), (84, 84)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/run/Run10.png'),(84, 84)))

        #moving left
        for sprite in self.move_right_sprites:
            self.move_left_sprites.append(pygame.transform.flip(sprite, True, False))

        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/idle/Idle1.png'), (84, 84)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/idle/Idle2.png'), (84, 84)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/idle/Idle3.png'), (84, 84)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/idle/Idle4.png'), (84, 84)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/idle/Idle5.png'), (84, 84)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/idle/Idle6.png'), (84, 84)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/idle/Idle7.png'), (84, 84)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/idle/Idle8.png'), (84, 84)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/idle/Idle9.png'), (84, 84)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/idle/Idle10.png'),(84, 84)))
        
        for sprite in self.idle_right_sprites:
            self.idle_left_sprites.append(pygame.transform.flip(sprite, True, False))                          
        

        #jump
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/jump/Jump (1).png'),  (84, 84)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/jump/Jump (2).png'),  (84, 84)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/jump/Jump (3).png'),  (84, 84)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/jump/Jump (4).png'),  (84, 84)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/jump/Jump (5).png'),  (84, 84)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/jump/Jump (6).png'),  (84, 84)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/jump/Jump (7).png'),  (84, 84)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/jump/Jump (8).png'),  (84, 84)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/jump/Jump (9).png'),  (84, 84)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load('Images/jump/Jump (10).png'), (84, 84)))
        
        for sprite in self.jump_right_sprites:
            self.jump_left_sprites.append(pygame.transform.flip(sprite, True, False)) 

        self.current_sprite = 0
        self.image = self.move_right_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        self.starting_x = x
        self.starting_y = y
        self.grass_tiles = grass_tiles
        self.water_tiles = water_tiles

        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0,0)

        self.HORIZONTAL_ACCELERATION = 2
        self.HORIZONTAL_FRICTION = 0.15
        self.VERTICAL_ACCELERATION = 0.5
        self.VERTICAL_JUMP_SPEED = 15
         
    def update(self):
        #pygame.draw.rect(display_surface, (255,255,0), self.rect, 1)
        self.mask = pygame.mask.from_surface(self.image)
        #draw mask
        mask_outline = self.mask.outline()
        #pygame.draw.lines(self.image, (255,0,0),True, mask_outline, )
        self.move()
        self.check_collisions()
        #self.check_animation()
    
    def move(self):
        self.acceleration= vector(0, self.VERTICAL_ACCELERATION)
        keys = pygame.key.get_pressed()
        #if the user is pressing a key, set the x - component of the acceleration vector to a non zero value
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -1*self.HORIZONTAL_ACCELERATION
            self.animate(self.move_left_sprites, 0.5)
        elif keys[pygame.K_RIGHT]:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION
            self.animate(self.move_right_sprites, 0.5)
        elif keys[pygame.K_SPACE]:
            my_player.jump()
        else:
            self.animate_jump = False
            if self.velocity.x > 0:
                self.animate(self.idle_right_sprites, 0.5)
            else:
                self.animate(self.idle_left_sprites, 0.5)
        
        #Calculate new kinematics values
        self.acceleration.x -= self.velocity.x*self.HORIZONTAL_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 *self.acceleration
        #update new rect
        if self.position.x < 0:
            self.position.x = WINDOW_WIDTH
        elif self.position.x > WINDOW_WIDTH:
            self.position.x = 0
        self.rect.bottomleft = self.position

    def check_collisions(self):
        collided_platforms = pygame.sprite.spritecollide(self, self.grass_tiles, False, pygame.sprite.collide_mask)
        if collided_platforms:
            #only move to the platform if the player is falling down
            if self.velocity.y > 0:
                self.position.y = collided_platforms[0].rect.top + 6
                self.velocity.y = 0
        if pygame.sprite.spritecollide(self, self.water_tiles, False):
            self.position = vector(self.starting_x, self.starting_y)
            self.velocity = vector(9, 0)

    def jump(self):
        #jumping only on a grass tiles
        self.animate_jump = True
        if self.velocity.x > 0:
            self.animate(self.jump_right_sprites, 0.5)
        else:
            self.animate(self.jump_left_sprites, 0.5)
        if pygame.sprite.spritecollide(self, self.grass_tiles, False):
            self.velocity.y = -1*self.VERTICAL_JUMP_SPEED
            
    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite  += speed
        else:
            self.current_sprite = 0
           
        self.image = sprite_list[int(self.current_sprite)]
   
class RubyMaker(pygame.sprite.Sprite):
    def __init__(self, x, y, main_group):
        super().__init__()
        self.ruby_sprites = []
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load('ruby/tile000.png'),(64,64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load('ruby/tile001.png'),(64,64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load('ruby/tile002.png'),(64,64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load('ruby/tile003.png'),(64,64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load('ruby/tile004.png'),(64,64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load('ruby/tile005.png'),(64,64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load('ruby/tile006.png'),(64,64)))

        self.current_sprite = 0
        self.image = self.ruby_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        main_group.add(self)

    def update(self):
        self.animate(self.ruby_sprites, 0.25)

    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
        self.image = sprite_list[int(self.current_sprite)]

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y, color, portal_group):
        super().__init__()
        self.portal_sprites = []
        if color == 'green':
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile000.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile001.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile002.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile003.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile004.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile005.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile006.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile007.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile008.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile009.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile010.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile011.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile012.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile013.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile014.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile015.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile016.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile017.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile018.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile019.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile020.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/green/tile021.png'),(84,84)))
        else:
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile000.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile001.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile002.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile003.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile004.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile005.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile006.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile007.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile008.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile009.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile010.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile011.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile012.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile013.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile014.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile015.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile016.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile017.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile018.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile019.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile020.png'),(84,84)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load('portals/purple/tile021.png'),(84,84)))

        self.current_sprite = random.randint(0, len(self.portal_sprites) - 1)
        self.image = self.portal_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        portal_group.add(self)

    def update(self):
        self.animate(self.portal_sprites, 0.2)

    def animate(self, sprite_list, speed):
        if self.current_sprite<len(self.portal_sprites) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
        self.image = self.portal_sprites[int(self.current_sprite)]
        
#Create a sprite_group
main_tile_group  = pygame.sprite.Group()
grass_tile_group = pygame.sprite.Group()
water_tile_group = pygame.sprite.Group()
my_player_group  = pygame.sprite.Group()
my_portal_group  = pygame.sprite.Group()

#Creating the map: 0 -> no tile, 1 - dirt, 2 - grass,  3- water, 4-> player, 5->ruby, 6-7-> portals, 8-> tree, 9-10 ->edges
tile_map = [[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  7,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  6],
            [ 2,  2,  2,  2,  2,  2,  2,  2, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9,  2,  2,  2,  2],
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9,  2,  2,  2,  2, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  9,  2,  2,  2,  2,  2,  2, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  6,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  7],
            [ 2,  2,  2,  2, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9,  2,  2,  2],
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  8,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  6,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  7],
            [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,  0,  0,  0,  0,  0,  0,  0,  0, 12, 12, 12, 12, 12, 12],
            [ 1, 11,  1, 11,  1, 11,  1, 11,  1, 11,  1, 11,  1, 11,  1, 11,  3,  3,  3,  3,  3,  3,  3,  3,  1, 11,  1, 11,  1, 11],
            [11,  1, 11,  1, 11,  1, 11,  1, 11,  1, 11,  1, 11,  1, 11,  1,  3,  3,  3,  3,  3,  3,  3,  3, 11,  1, 11,  1, 11,  1]]

for i in range (len(tile_map)):
    for j in range (len(tile_map[i])):
        if tile_map[i][j] == 1:
            Tile(j*32, i*32, 1, main_tile_group)
        elif tile_map[i][j] == 2:
            Tile(j*32, i*32, 2, main_tile_group, grass_tile_group)
        elif tile_map[i][j] == 3:
            Tile(j*32, i*32, 3, main_tile_group, water_tile_group)
        elif tile_map[i][j] == 4:
            my_player  = Player(j*32, i*32 + 32, grass_tile_group, water_tile_group)
            my_player_group.add(my_player)
        elif tile_map[i][j] == 5:
            RubyMaker(j*32, i*32, main_tile_group)
        elif tile_map[i][j] == 6:
            Portal(j*32, i*32,'green', my_portal_group)
        elif tile_map[i][j] == 7:
            Portal(j*32, i*32, 'purple', my_portal_group)
        elif tile_map[i][j] == 8:
            Tile(j*32, i*32, 8, main_tile_group)
        elif tile_map[i][j] == 9:
            Tile(j*32, i*32, 9, main_tile_group)
        elif tile_map[i][j] == 10:
            Tile(j*32, i*32, 10, main_tile_group)
        elif tile_map[i][j] == 11:
            Tile(j*32, i*32, 11, main_tile_group)
        elif tile_map[i][j] == 12:
            Tile(j*32, i*32, 12, main_tile_group,grass_tile_group)
            
background_image = pygame.image.load("Images/background.png")
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if player wants to jump
        #if event.type == pygame.KEYDOWN:
           # if event.key == pygame.K_SPACE:
            #    my_player.jump()
            
    #display_surface.fill((10, 75, 75))
    display_surface.blit(background_image, background_rect)
    main_tile_group.draw(display_surface)
    main_tile_group.update()
    my_player_group.update()
    my_player_group.draw(display_surface)
    my_portal_group.update()
    my_portal_group.draw(display_surface)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit() 