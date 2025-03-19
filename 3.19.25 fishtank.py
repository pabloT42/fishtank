import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Fish Tank")
clock = pygame.time.Clock()

# Initialize mixer for sound
pygame.mixer.init()

# Load bubble sound
bubble_sound = pygame.mixer.Sound("bubble.wav")

# Mouse input
mousePos = (0, 0)
chest = 1
ticker = 0

# Load images and make transparent
chestImg1 = pygame.image.load("chest1.jpg").convert_alpha()
chestImg1.set_colorkey([123, 232, 137])

chestImg2 = pygame.image.load("chest2.jpg").convert_alpha()
chestImg2.set_colorkey([255, 0, 255])


class Fish:
    def __init__(self):
        self.fishImage = pygame.image.load("Redfish.png").convert_alpha()
        self.fishImage.set_colorkey([255, 0, 255])
        self.xpos = 0
        self.ypos = random.randint(0, 550)
        self.speed = 1
        self.xDir = 1
        self.yDir = random.randint(-1,1)
        self.last_change_time = time.time() #grab starting time
        self.frameWidth = 128
        self.frameHeight = 128
        self.frameNum = 0

    def move(self):
        # Move the fish
        self.xpos += self.xDir* self.speed

        # Check for collision with walls and change direction
        if self.xpos >= 800:
            self.xpos = -100
        if self.ypos <= 0 or self.ypos>= 550:
            self.ypos == 300

    def draw(self, screen):
        #screen.blit(self.fishImage, (self.xpos, self.ypos))
        screen.blit(bluefish, (fish.xpos, fish.ypos), (self.frameWidth*frameNum,0, self.frameWidth, self.frameHeight))

    def draw(self, screen):
        screen.blit(self.fishImage, (self.xpos, self.ypos))

#----------------------------class snowflake (bubble)------------------------------------------
class Snowflake:
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y + 500

    def move(self):
        self.xpos += random.randrange(-2, 3)  
        self.ypos -= random.randrange(0, 3)  

        if self.ypos <= 0:  # When bubble reaches top, reset to bottom
            self.ypos = 500  # Restart from bottom of the screen
            bubble_sound.play()  # Play bubble sound

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 220, 255), (self.xpos, self.ypos), 10, 1)  # Blue bubbles

# Create bubbles (flakes)
flakeBag = [Snowflake(random.randrange(0, 800), random.randrange(0, 500)) for _ in range(500)]

# Instantiate fish before game loop
fish = Fish()

running = True
while running:
    clock.tick(60)

    # Input/event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos  # Update mouse position

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = event.pos  # Ensure latest position is used
            if 238 < mousePos[0] < 355 and 130 < mousePos[1] < 230:
                chest = 2

    # Physics updates--------------------------------------------------------------------------------
    fish.move()

    # Keep chest open for 50 game loops
    if chest == 2:
        ticker += 1
        if ticker >= 10:
            ticker = 0
            chest = 1

    for flake in flakeBag:
        flake.move()

    # Rendering
    screen.fill((0, 0, 255))  # Background color
   

    fish.draw(screen)  # Draw fish

    if chest == 1:
        screen.blit(chestImg1, (240, 140))
    else:
        screen.blit(chestImg2, (240, 140))

    for flake in flakeBag:
        flake.draw(screen)  

    pygame.display.flip()

pygame.quit()
