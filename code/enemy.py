import pygame

from settings import*
from groups import all_sprites
from random import randint 


#attack image / sound


class Enemy(pygame.sprite.Sprite):
    def __init__ (self, groups, enemy_image, hp, weapon_damage, strength, dexterity, stamina, reward_weapon, reward_weapon_surf, name):
        super().__init__(groups)
        self.image = enemy_image
        self.rect = self.image.get_frect(center = (WIDTH , HEIGHT * 3/4 - 125))
        self.hp = hp
        self.weapon_damage = weapon_damage
      
        self.strength = strength
        self.damage = self.strength + self.weapon_damage
        self.dexterity = dexterity
        self.stamina =  stamina
         
        self.reward_weapon = reward_weapon
        self.reward_weapon_surf = reward_weapon_surf

        self.name = name
        
        self.speed = 400
        self.is_allive = True

        self.moves = 0
   
        self.alpha = 255
        
        #self.invincible = False
        self.blit_index = 0
    
        #shooting
        self.can_shoot = True
        #self.cooldown_duration = 500
        #self.laser_shoot_time = 0

        #mask
        self.mask = pygame.mask.from_surface(self.image)
 
 
    def update(self, dt):
        if self.rect.x >= 1200:
            self.rect.x -= dt * self.speed 

    def attack(self):
        pass


