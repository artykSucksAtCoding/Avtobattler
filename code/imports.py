import pygame
import os
from settings import*

#background
background = pygame.image.load(os.path.join('images', 'background.jpg'))

#playable characters
hero_path = os.path.join('images', 'heros')
warrior_surf = pygame.image.load(os.path.join(hero_path, 'warrior.png')).convert_alpha()
warrior_surf_picked = pygame.image.load(os.path.join(hero_path, 'warriorpicked.png')).convert_alpha()
barbarian_surf = pygame.image.load(os.path.join(hero_path, 'barbarian.png')).convert_alpha()
barbarian_surf_picked = pygame.image.load(os.path.join(hero_path, 'barbarianpicked.png')).convert_alpha()
bandit_surf = pygame.image.load(os.path.join(hero_path, 'bandit.png')).convert_alpha()
bandit_surf_picked = pygame.image.load(os.path.join(hero_path, 'banditpicked.png')).convert_alpha()

#etc
heart_surf = pygame.image.load(os.path.join('images', 'heart.png')).convert_alpha()

#fonts
font_path = os.path.join('fonts', 'pixel_font.ttf')
font35 = pygame.font.Font(font_path, 35)
font60 = pygame.font.Font(font_path, 60)
font45 = pygame.font.Font(font_path, 45)
font40 = pygame.font.Font(font_path, 40)

#weapons
weapon_path = os.path.join('images', 'weapons')
sword_surf = pygame.image.load(os.path.join(weapon_path, 'sword.png')).convert_alpha()
dagger_surf = pygame.image.load(os.path.join(weapon_path, 'dagger.png')).convert_alpha()
club_surf = pygame.image.load(os.path.join(weapon_path, 'club.png')).convert_alpha()
spear_surf = pygame.image.load(os.path.join(weapon_path, 'spear.png')).convert_alpha()
legenadary_sword_surf = pygame.image.load(os.path.join(weapon_path, 'legendary_sword.png')).convert_alpha()
axe_surf = pygame.image.load(os.path.join(weapon_path, 'axe.png')).convert_alpha()

#enemies
enemy_path = os.path.join('images', 'enemies')
goblin_surf = pygame.image.load(os.path.join(enemy_path, 'goblin.png')).convert_alpha()
golem_surf = pygame.image.load(os.path.join(enemy_path, 'golem.png')).convert_alpha()
ghost_surf = pygame.image.load(os.path.join(enemy_path, 'ghost.png')).convert_alpha()
skeleton_surf = pygame.image.load(os.path.join(enemy_path, 'skeleton.png')).convert_alpha()
slime_surf = pygame.image.load(os.path.join(enemy_path, 'slime.png')).convert_alpha()
dragon_surf = pygame.image.load(os.path.join(enemy_path, 'dragon2.png')).convert_alpha()

#music
select_sound = pygame.mixer.Sound(os.path.join('sound', 'select.mp3'))
select_sound.set_volume(0.5)

battle_music = pygame.mixer.Sound(os.path.join('sound', 'battle_music.mp3'))
battle_music.set_volume(0.5)

lose_music = pygame.mixer.Sound(os.path.join('sound', 'lose.wav'))
lose_music.set_volume(1)

