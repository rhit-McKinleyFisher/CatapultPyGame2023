import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    # Done 1: Create an image with the 2dogs.JPG image
    dogs = pygame.image.load('2dogs.JPG')
    # Done 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
    dogs = pygame.transform.scale(dogs, (IMAGE_SIZE, IMAGE_SIZE))
    # Prepare the text caption(s)
    # Done 4: Create a font object with a size 28 font.
    font1 = pygame.font.SysFont('arieal', 28)
    # DONE 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
    caption1 = font1.render('Two Dogs', True, BLACK)

    font2 = pygame.font.SysFont('arieal', 46)
    caption2 = font2.render('Get your paws out of my face!', True, WHITE)

    # Prepare the music
    # Done 8: Create a Sound object from the "bark.wav" file.
    barking = pygame.mixer.Sound("bark.wav")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Done 9: Play the music (bark) if there's a mouse click.
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Bark")
                barking.play()
        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # Done 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(dogs, (0, 0))
        # Draw the text onto the screen
        # Done 6: Draw (blit) the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()
        screen.blit(caption1, (screen.get_width() / 2 - (caption1.get_width() / 2), 475))
        # Done 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.
        screen.blit(caption2, (screen.get_width() / 2 - (caption2.get_width() / 2), 10))
        # Update the screen
        pygame.display.update()


main()
