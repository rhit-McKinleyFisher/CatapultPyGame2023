import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((640, 480))

    right_eye_x = 398
    right_eye_y = 162

    left_eye_x = 242
    left_eye_y = 162

    is_nose_drawn = False
    while True:
        # TODO 4: Set the clock speed to 60 fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_nose_drawn = True
            if event.type == pygame.MOUSEBUTTONUP:
                is_nose_drawn = False
            # Done 3: Make the eye pupils move with Up, Down, Left, and Right keys
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_UP]:
                right_eye_y = right_eye_y - 15
            if pressed_keys[pygame.K_DOWN]:
                right_eye_y = right_eye_y + 15
            if pressed_keys[pygame.K_LEFT]:
                right_eye_x = right_eye_x - 15
            if pressed_keys[pygame.K_RIGHT]:
                right_eye_x = right_eye_x + 15

            if pressed_keys[pygame.K_UP]:
                left_eye_y = left_eye_y - 15
            if pressed_keys[pygame.K_DOWN]:
                left_eye_y = left_eye_y + 15
            if pressed_keys[pygame.K_LEFT]:
                left_eye_x = left_eye_x - 15
            if pressed_keys[pygame.K_RIGHT]:
                left_eye_x = left_eye_x + 15

        screen.fill((250, 250, 250))  # white

        # API --> pygame.draw.circle(screen, color, (x, y), radius, thickness)

        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (left_eye_x, left_eye_y), 7)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (right_eye_x, right_eye_y), 7)  # black pupil

        # Done 1: Draw a nose
        # Suggestion: color (80,0,0) location (320,245), radius 10
        if is_nose_drawn:
            pygame.draw.circle(screen, (80, 0, 0), (320, 245), radius=10)

        # Done 2: Draw a mouth
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        pygame.draw.rect(screen, (0, 0, 0), (230, 320, 180, 30))

        pygame.display.update()


main()
