import pygame
import sys
import time
import random

import pygame.time


class Raindrop:
    def __init__(self, screen: pygame.Surface, x, y):

        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 15)

    def move(self):
        self.y += self.speed

    def is_off_screen(self):
        return self.y > self.screen.get_height() + 6

    def draw(self):
        pygame.draw.line(self.screen, (0, 0, 220), (self.x, self.y), (self.x, self.y - 5), 2)


class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_without_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0

    def draw(self):
        self.screen.blit(self.image_without_umbrella, (self.x, self.y))
        if time.time() < self.last_hit_time + 1:
            self.screen.blit(self.image_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_without_umbrella, (self.x, self.y))

    def is_hit_by(self, raindrop):
        hitbox = pygame.Rect(self.x, self.y, self.image_umbrella.get_width(), self.image_umbrella.get_height())
        return hitbox.collidepoint(raindrop.x, raindrop.y)


class Cloud:
    def __init__(self, screen, x, y, image_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)

        self.raindrops = []

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        new_drops = Raindrop(self.screen,
                             random.randint(self.x, self.x + self.image.get_width()),
                             self.y + self.image.get_height() - 20)
        self.raindrops.append(new_drops)


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Mike's Rainy Day")
    clock = pygame.time.Clock()
    mike = Hero(screen, 200, 400, 'Mike_umbrella.png', 'Mike.png')
    alyssa = Hero(screen, 700, 400, "Alyssa_umbrella.png", 'Alyssa.png')
    cloud = Cloud(screen, 300, 50, "another_cloud.png")
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            cloud.y -= 5
        if keys_pressed[pygame.K_LEFT]:
            cloud.x -= 5
        if keys_pressed[pygame.K_DOWN]:
            cloud.y += 5
        if keys_pressed[pygame.K_RIGHT]:
            cloud.x += 5
        screen.fill((255, 255, 255))

        cloud.rain()
        for drop in cloud.raindrops:
            drop.move()
            drop.draw()
            if mike.is_hit_by(drop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(drop)
            if alyssa.is_hit_by(drop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(drop)
            if drop.is_off_screen:
                cloud.raindrops.remove(drop)

        mike.draw()
        alyssa.draw()
        cloud.draw()

        pygame.display.update()


main()
