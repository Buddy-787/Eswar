import pygame
import random
import sys

pygame.init()


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

BALLOON_RADIUS = 20
BALLOON_SPEED = 5


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Balloon Pop")


font = pygame.font.Font(None, 36)


score = 0
time_remaining = 120  


clock = pygame.time.Clock()


def create_balloon():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    x = random.randint(BALLOON_RADIUS, SCREEN_WIDTH - BALLOON_RADIUS)
    y = SCREEN_HEIGHT + BALLOON_RADIUS
    return {'rect': pygame.Rect(x, y, BALLOON_RADIUS * 2, BALLOON_RADIUS * 2), 'color': color}


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


def main():
    global score, time_remaining

    balloons = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        screen.fill(WHITE)

        
        time_remaining -= 1 / 60  
        if time_remaining <= 0:
            time_remaining = 0

        
        if random.randint(0, 100) < 3:
            balloons.append(create_balloon())

        
        for balloon in balloons:
            balloon['rect'].move_ip(0, -BALLOON_SPEED)
            pygame.draw.circle(screen, balloon['color'], balloon['rect'].center, BALLOON_RADIUS)

        
        balloons = [balloon for balloon in balloons if balloon['rect'].bottom > 0]

        
        draw_text(f'Score: {score}', font, BLACK, screen, SCREEN_WIDTH // 2, 50)

       
        minutes = int(time_remaining / 60)
        seconds = int(time_remaining % 60)
        draw_text(f'Time: {minutes:02d}:{seconds:02d}', font, BLACK, screen, SCREEN_WIDTH // 2, 20)

        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for balloon in balloons:
                    if balloon['rect'].collidepoint(pos):
                        score += 2
                        balloons.remove(balloon)
                        break
                else:
                    score -= 1

        
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()