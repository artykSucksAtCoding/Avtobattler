import pygame

def gob1(player, enemy):
    pass

def gob2(player, enemy):
    pass

def skeleton1(player, enemy):
    if player.weapon_type == 'drob':
        player.damage *= 2
        print("skeleton1 pl damage x2")

def skeleton2(player, enemy):
    if player.weapon_type == 'drob':
        player.damage = int(player.damage / 2)
        print("skeleton2 pl damage /2")

def slime1(player, enemy):
    if player.weapon_type == 'rub':
        print(f"prev pl damage slime1 {player.damage}")
        player.damage -= player.weapon_damage
        print(f"prev pl damage slime1 {player.damage}")
        

def slime2(player, enemy):
    if player.weapon_type == 'rub':
        player.damage += player.weapon_damage
        print(f"pl damage slime2 {player.damage}")
        
def ghost1(player, enemy):
    if enemy.dexterity > player.dexterity:
        enemy.damage +=1

def ghost2(player, enemy):
    if enemy.dexterity > player.dexterity:
        enemy.damage -= 1

def golem1(player, enemy):
    player.damage -= enemy.stamina


def golem2(player, enemy):
    player.damage += enemy.stamina

def dragon1(player, enemy):
    if enemy.moves % 3 == 0:
        enemy.damage += 3


def dragon2(player, enemy):
    if enemy.moves % 3 == 0:
        enemy.damage -= 3

monster_buffs_dict = {
    'goblin': [gob1, gob2],
    'slime': [slime1, slime2],
    'skeleton': [skeleton1, skeleton2],
    'ghost': [ghost1, ghost2],
    'golem': [golem1, golem2],
    'dragon': [dragon1, dragon2]
    
}