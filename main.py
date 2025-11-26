import pygame

from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_TURN_SPEED
from player import Player

def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while(True):
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60)/1000
        player.update(dt)
        
        screen_update(screen, [player,])

        

def screen_update(screen, objects_to_draw):
        screen.fill("black")

        for object in objects_to_draw:        
            object.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
