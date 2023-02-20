import pygame
import sys
from bullet import Bullet
from aliens import Aliens
import time

def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.right = True
            elif event.key == pygame.K_LEFT:
                gun.left = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.right = False
            elif event.key == pygame.K_LEFT:
                gun.left = False


def update(bg_color, screen, gun, aliens, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw()
    gun.output()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


def gun_kill(stats, screen, gun, aliens, bullets):
    stats.guns_left -= 1
    aliens.empty()
    bullets.empty()
    army_aliens(screen, aliens)
    gun.create_gun()
    time.sleep(3)


def update_aliens(gun, aliens, stats, screen, bullets):
    aliens.update()
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, gun, aliens, bullets)


def army_aliens(screen, aliens):
    alien = Aliens(screen)
    alien_width = alien.rect.width
    number_alien_x = int((700 - 2*alien_width)/alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((800 - 100 - 2*alien_height)/alien_height)

    for row_number in range(number_alien_y-1):
        for alien_number in range(number_alien_x):
            alien = Aliens(screen)
            alien.x = alien_width + (alien_width * alien_number)
            alien.y = alien_height + alien_height * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height * row_number
            aliens.add(alien)
