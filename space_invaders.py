import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats


def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space Invaders by Anara", "S_I")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controls.army_aliens(screen, aliens)
    stats = Stats()

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update_bullets(aliens, bullets)
        controls.update(bg_color, screen, gun, aliens, bullets)
        controls.update_aliens(gun, aliens, screen, stats, bullets)


run()
