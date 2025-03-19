)  

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
