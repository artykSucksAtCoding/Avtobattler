import pygame
from imports import goblin_surf, ghost_surf, golem_surf, slime_surf, skeleton_surf, dragon_surf

enemies = {
    'goblin': [goblin_surf, 5, 2, 1, 1, 1, 'dagger', 'goblin'],
    'skeleton': [skeleton_surf, 10, 2, 2, 2, 1, 'club', 'skeleton'],
    'slime': [slime_surf, 8, 1, 3, 1, 2, 'spear', 'slime'],
    'ghost': [ghost_surf, 6, 3, 1, 3, 1, 'sword', 'ghost'],
    'golem': [golem_surf, 10, 1, 3, 1, 3, 'axe', 'golem'],
    'dragon': [dragon_surf, 20, 4, 3, 3, 3, 'legendary sword', 'dragon']
}

