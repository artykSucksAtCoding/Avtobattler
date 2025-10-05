import pygame


class PlayerWeapon(pygame.sprite.Sprite):
    def __init__(self, all_sprites, weapon_surf):
        super().__init__(all_sprites)
        self.image = weapon_surf
        self.rect = self.image.get_frect(center = (400, 400))

    
    def update(self, dt):
        pass

