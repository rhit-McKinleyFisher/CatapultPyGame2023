import pygame, sys
import math
import random

def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    # Done 4: Return the actual distance between point 1 and point 2.
    #  Hint: you will need the math library for the sqrt function.
    #       distance = sqrt(   (delta x) ** 2 + (delta y) ** 2  )
    num = math.sqrt((point1_x - point2_x) ** 2 + (point1_y - point2_y) ** 2)
    return num


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Mouse click positions")
    font = pygame.font.Font(None, 25)

    # Done 8: Load the "drums.wav" file into the pygame music mixer
    pygame.mixer.music.load("drums.wav")

    instruction_text = 'Click the circle'
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)

    circle_color = (154, 58, 212)
    circle_center = (random.randint(0, 400), random.randint(0, 400))
    circle_radius = 10


    message_text = ''

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Done 2: For a MOUSEBUTTONDOWN event get the click position.
            if event.type == pygame.MOUSEBUTTONDOWN:
                distance_from_circle = distance(circle_center, event.pos)
                # print(distance_from_circle)
                # Done 3: Determine the distance between the click position and the circle_center using the distance
                # Done 3:   function and save the result into a variable called distance_from_circle
                # Done 5: If distance_from_circle is less than or equal to circle_radius, set message_text to 'Bullseye!'
                if distance_from_circle <= circle_radius:
                    message_text = "Bullseye!"
                    pygame.mixer.music.play(-1)
                    print('yayy')
                # Done 5: If distance_from_circle is greater than the circle_radius, set the message_text to 'You missed!'
                else:
                    message_text = "Miss!"
                    pygame.mixer.music.stop()
                    print('booo')
                # Done 9: Start playing the music mixer looping forever if the click is within the circle

                # Done 10: Stop playing the music if the click is outside the circle

        screen.fill(pygame.Color("Black"))

        # Done 1: Draw the circle using the screen, circle_color, circle_center, circle_radius, and circle_border_width
        pygame.draw.circle(screen, circle_color, circle_center, circle_radius)
        # Done 6: Create a text image (render the text) based on the message_text with the color (122, 237, 201)
        caption1 = font.render(message_text, True, (122, 237, 201))

        screen.blit(instructions_image, (25, 25))
        # Done 7: Draw (blit) the message to the user that says 'Bullseye!' or 'You missed!'
        screen.blit(caption1, (20, 200))

        pygame.display.update()


main()
