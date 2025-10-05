import pygame
from groups import all_buffs

class Buff(pygame.sprite.Sprite):
    def __init__(self, all_buffs, player, enemy):
        super().__init__()
        self.all_buffs = all_buffs
        self.can_be_applied = True
        self.is_revertable = True
        self.player = player
        self.enemy = enemy


class BanditBuff1(Buff): #once a fight
    def __init__(self, all_buffs, player, enemy):
        super().__init__(all_buffs, player, enemy)
        self.all_buffs.add(self)
        self.is_revertable = True
        self.is_applied = False

    def buff_apply(self):
        if self.player.dexterity > self.enemy.dexterity:
            if self.is_applied:
                self.player.damage -= 1
            self.player.damage += 1
            print('bandit buff1 applied')
            self.is_applied = True
    
    def revert(self):
        if self.is_revertable and self.is_applied:
            self.player.damage -= 1
            print('bandit buff1 reverted')


class BanditBuff2(Buff): #once a game
    def __init__(self, all_buffs, player, enemy):
        super().__init__(all_buffs, player, enemy)
        self.all_buffs.add(self)
        self.is_revertable = False

    def buff_apply(self):
        if self.can_be_applied == True:
            self.player.dexterity += 1
            print('bandit buff2 applied')
            self.can_be_applied = False

    def revert(self):
        self.player.dexterity -= 1
        print('bandit buff1 reversed')


class BanditBuff3(Buff): #once a move opportunity
    def __init__(self, all_buffs, player, enemy):
        super().__init__(all_buffs, player, enemy)
        self.all_buffs.add(self)
        self.is_revertable = True
        self.count = 0

    def buff_apply(self):
        if self.can_be_applied == True:
            if self.player.move_count >= 2:
                self.player.damage += 1
                self.count += 1
                
            print('bandit buff3 applied: +1 more damage')
           
    def revert(self):
        if self.is_revertable:
            self.player.damage -= self.count
            self.count = 0
            print('bandit buff3 reverted')


class WarriorBuff1(Buff): #once a fight
    def __init__(self, all_buffs, player, enemy):
        super().__init__(all_buffs, player, enemy)
        self.all_buffs.add(self)
        self.is_revertable = True

    def buff_apply(self):
        if self.can_be_applied == True:
            print(f"Weapon damage {self.player.weapon_damage}")
            print(f"Player damage {self.player.damage}")
            self.player.damage += self.player.weapon_damage
            print('warrior buff1 applied')
            self.can_be_applied = False
    
    def revert(self):
        if self.is_revertable:
            self.player.damage -= self.player.weapon_damage
            print('warrior buff1 reverted')


class WarriorBuff2(Buff): #once a move opportunity
    def __init__(self, all_buffs, player, enemy):
        super().__init__(all_buffs, player, enemy)
        self.all_buffs.add(self)
        self.is_revertable = True
        self.is_applied = False

    def buff_apply(self): 
        if self.is_applied:
            self.enemy.damage += 3
        if self.can_be_applied == True:
                
                if self.player.damage > self.enemy.damage:
                    self.enemy.damage -= 3
                    self.is_applied = True
                    print('warrior buff2 applied')
            
                    

    def revert(self):
        if self.is_applied:
            self.enemy.damage += 3
        

class WarriorBuff3(Buff): #once a game
    def __init__(self, all_buffs, player, enemy):
        super().__init__(all_buffs, player, enemy)
        self.all_buffs.add(self)
        self.is_revertable = False

    def buff_apply(self):
        if self.can_be_applied == True:
            self.player.strength += 1
            print('warrior buff3 applied')
            self.can_be_applied = False

    def revert(self):
        self.player.strength -= 1
        print('warrior buff3 removed')


class BarbarianBuff1(Buff): #once a move opportunity
    def __init__(self, all_buffs, player, enemy):
        super().__init__(all_buffs, player, enemy)
        self.all_buffs.add(self)
        self.is_revertable = True
        self.debuff_aplied = False
        

    def buff_apply(self): 
        if self.can_be_applied == True:
            self.player.damage += 2
            print('Barbarian buff1 applied')
            self.can_be_applied = False
            
         
        if self.player.move_count > 3 and not self.debuff_aplied:
            self.player.damage -= 3
            print('Barbarian debuff1 applied')
            self.debuff_aplied = True
                

    def revert(self):
        if self.is_revertable == True:
            self.debuff_aplied = False
            if self.player.move_count <= 3:
                self.player.damage -= 2
            else:
                self.player.damage += 1


class BarbarianBuff2(Buff): #once a fight
    def __init__(self, all_buffs, player, enemy):
        super().__init__(all_buffs, player, enemy)
        self.all_buffs.add(self)
        self.is_revertable = True
        self.is_applied = False

    def buff_apply(self):
        if self.can_be_applied == True:
            if self.is_applied:
                self.enemy.damage += self.player.stamina

            self.enemy.damage -= self.player.stamina
            print('barbarian buff2 applied')
            self.is_applied = True
           
    def revert(self):
        pass


class BarbarianBuff3(Buff): #once a game
    def __init__(self, all_buffs, player, enemy):
        super().__init__(all_buffs, player, enemy)
        self.all_buffs.add(self)
        self.is_revertable = False

    def buff_apply(self):
        if self.can_be_applied == True:
            self.player.stamina += 1
            print('barbarian buff3 applied')
            self.can_be_applied = False

    def revert(self):
        self.player.stamina -= 1
        print('barbarian buff3 reverted')


player_buffs_dict = {
    'warrior': [WarriorBuff1, WarriorBuff2, WarriorBuff3],
    'barbarian': [BarbarianBuff1, BarbarianBuff2, BarbarianBuff3],
    'bandit': [BanditBuff1, BanditBuff2, BanditBuff3]
}