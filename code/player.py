import pygame
from settings import*
from groups import all_sprites
from imports import heart_surf, sword_surf, font35
from random import randint 
from weapon import PlayerWeapon
from weapons_dict import weapons


class Player(pygame.sprite.Sprite):
    def __init__ (self, groups, player_image, hp, weapon, weapon_surf, player_name):
        super().__init__(groups)
        self.image = player_image
        self.rect = self.image.get_frect(center = (WIDTH / 3 - 100, HEIGHT * 3/4 - 125))
        self.hp = hp
    
        self.weapon = weapon
        self.weapon_surf = weapon_surf
        self.player_name = player_name
        self.player_weapon = PlayerWeapon(all_sprites, self.weapon_surf)
        self.classes_dict = {
            'warrior': 0,
            'barbarian': 0,
            'bandit': 0
        }
        if self.player_name == 'warrior':
            self.classes_dict[self.player_name] = 1

        if self.player_name == 'barbarian':
            self.classes_dict[self.player_name] = 1

        if self.player_name == 'bandit':
            self.classes_dict[self.player_name] = 1
     
        #params
        self.strength = randint(1, 3) + weapons[self.weapon][0]
        self.damage = self.strength
        self.stamina =  randint(1, 3)
        self.dexterity = randint(1, 3)
        self.hp += self.stamina
        self.weapon_damage = weapons[self.weapon][0]

        self.weapon_type =  weapons[self.weapon][1]


        #game_state
        self.player_level = 1
        self.move_count = 0
        self.turn = True

        self.original_hp = self.hp


    def update(self, dt):

        pass

        
class Heart(pygame.sprite.Sprite):
    def __init__(self, all_sprites):
        super().__init__(all_sprites)
        self.image = heart_surf
        self.rect = self.image.get_frect(center = (395, 205))

    
    def update(self, dt):
        pass

