import pygame
import random

from imports import background, font35, font60, font45, font40, battle_music, lose_music
from groups import all_sprites, enemy_group, all_buffs, buff_text
from settings import*
from player import Player, Heart
from enemies_dict import enemies
from enemy import Enemy
from weapons_dict import weapons 
from player_buffs import*
from weapon import PlayerWeapon

from monster_buff import*


class Gameplay:
    def __init__(self, shared_data):
        self.shared_data = shared_data
        self.next_state = 'gameplay'
        self.move_opportunity = False
        self.is_missed = False
        self.number_of_moves = 0
        self.buffs_called = False
        self.fall_speed = 300

        self.battle_music = battle_music

        self.battle_music.play(loops = -1)
        self.flag = True

        #timers
        self.miss_time = 0
        self.curr_time = 0
        self.hit_time = 0

        self.t1 = font60.render("PLAYER'S TURN", True, (255, 255, 255))
        self.t2 = font60.render("ENEMY'S TURN", True, (255, 255, 255))
        self.t3= font60.render("ENEMY'S TURN", True, (255, 255, 255))
        self.t4 = font60.render("PLAYER'S TURN", True, (255, 255, 255))
        self.t5 = font45.render("missed", True, (48, 5, 2))
        self.t6 = font40.render("TO CHOOSE NEW WEAPON PRESS Y. OTHERWISE N",  True, (255, 255, 255))
        self.t7= font40.render("TAP A CORRESPONDING NUMBER TO GET A NEW BUFF",  True, (255, 255, 255))
        self.t8 = font60.render("PRESS ENTER TO CONTINUE", True, (255, 255, 255))



        self.text_list = [self.t1, self.t2, self.t3, self.t4, self.t5, self.t6, self.t7]

        

        #managing states
        self.is_window = False
        self.window_called = False
       
        self.buff_choice = False
        self.weapon_chosen = False
        self.is_set = False
    
        
        #events
        self.attack_event = pygame.event.custom_type()
        pygame.time.set_timer(self.attack_event, 2000)

        self.damage_event = pygame.event.custom_type()
        pygame.time.set_timer(self.damage_event, 1000)


        if 'player' in shared_data:
            params = shared_data['player']
            self.player = Player(all_sprites, params[0], params[1], params[2], params[3], params[4])
            
        if 'heart' in shared_data:
            self.heart = Heart(all_sprites)

        self.random_keys = random.sample(list(enemies), 3)
        self.enemy_list = list()
        for i in range(0, 3):
            self.params1 = enemies[self.random_keys[i]]
            self.enemy = Enemy(enemy_group, self.params1[0], self.params1[1], self.params1[2], self.params1[3], self.params1[4], self.params1[5], self.params1[6], weapons[self.params1[6]][2], self.params1[7])
            self.enemy_list.append(self.enemy)
        

        self.who_first()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.next_state = 'quit'
            elif event.type == self.attack_event and not self.is_window and  self.enemy_list[self.player.player_level - 1].rect.x <= 1200:
                self.move_opportunity = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.next_state = 'main menu'
                self.battle_music.stop()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.is_window == True and self.is_set == True:
                self.is_window = False
                self.is_set = False
                self.window_called = False
                self.weapon_chosen = False
                self.buff_choice = False
                self.number_of_moves = 0
                self.player.move_count = 0
                self.flag = True
                self.battle_music.set_volume(0.5)
        


                self.fall_speed = 300

                self.who_first()

                print(self.player.player_level)
                buff_text.empty()


    def game_lost(self):
        if self.player.hp <= 0:
            self.next_state = 'lost screen'
            if self.flag:
                lose_music.play(loops = 0)
                self.flag = False
              
            self.battle_music.stop()

    def game_won(self):
        if self.player.player_level >= 4:
            self.next_state = 'win screen'
            self.battle_music.stop()


    def who_first(self):
        self.player.turn = True

        self.attacker = self.player
        self.defender = self.enemy_list[self.player.player_level - 1]
        if self.player.dexterity < self.enemy_list[self.player.player_level - 1].dexterity:
            self.attacker = self.enemy_list[self.player.player_level - 1]
            self.defender = self.player
            self.player.turn = False
        


    def buffs_add(self):
        all_buffs.empty()
        for key, value in self.player.classes_dict.items():
            sublist = player_buffs_dict[key][0:value]
            for item in sublist:
                item(all_buffs, self.player, self.enemy_list[self.player.player_level - 1])
        
       
    def update(self,  dt):

        self.game_lost()
        self.game_won()

        if self.is_window and not self.window_called:
            self.battle_music.set_volume(0.25)
            self.window_actions()
            self.window_called = True



        #getting to the next state
        if not self.is_window:
            if self.enemy_list[self.player.player_level - 1].hp <= 0:
                self.enemy_list[self.player.player_level - 1].is_allive = False
                self.is_window = True
            

            if not self.buffs_called:
                self.buffs_add()
                self.buffs_called = True

            if self.move_opportunity and self.enemy_list[self.player.player_level - 1].is_allive:
                self.attack()
                self.move_opportunity = False
            all_sprites.update(dt)
            self.enemy_list[self.player.player_level - 1].update(dt)

        else:
            if hasattr(self, "reward_rect"):
                if self.reward_rect.centery <= HEIGHT  - 300:
                    self.reward_rect.y += dt * self.fall_speed
                    self.fall_speed += 10

                keys = pygame.key.get_pressed()
                if keys[pygame.K_y]:
                    self.player.player_weapon = PlayerWeapon(all_sprites, self.enemy.reward_weapon_surf)
                    self.player.weapon = self.enemy.reward_weapon
                    self.player.strength -= self.player.weapon_damage 
                    self.player.strength += weapons[self.player.weapon][0]
                    self.player.weapon_damage = weapons[self.player.weapon][0]
                    self.player.weapon_type = weapons[self.player.weapon][1]
                    del self.reward_rect
                    self.weapon_chosen = True
                if keys[pygame.K_n]:
                    del self.reward_rect
                    self.weapon_chosen = True

                

            if self.is_window and self.weapon_chosen and not self.buff_choice:
                x = 1
                h = 290
                self.help_list = []
                self.buffs_available_list = []
                for key, value in self.player.classes_dict.items():
                    if value < 3:
                        self.temp = font60.render(f"{x}. {key.upper()} BUFF {value + 1}", True, (255, 255, 255))
                        self.buffs_available_list.append(key)
                        BuffText(buff_text, self.temp, h)
                        h += 70
                        self.help_list.append(self.temp)
                        x += 1
            
                self.buff_choice = True
                print(self.buffs_available_list)

            if hasattr(self, "help_list") and self.weapon_chosen:
                keys = pygame.key.get_pressed()
        
                if keys[pygame.K_1]:
                    key = self.buffs_available_list[0]
                   
                    self.player.classes_dict[key] += 1

                    print(self.player.classes_dict)
                
                    del self.help_list
                    
                    self.weapon_chosen = False
                    self.is_set = True
                
                
                elif keys[pygame.K_2]:
                    key = self.buffs_available_list[1]
                    self.player.classes_dict[key] += 1
                    
             
                    del self.help_list
                    self.weapon_chosen = False
                    self.is_set = True

                elif keys[pygame.K_3]:
                    if len(self.buffs_available_list) == 3:
                        key = self.buffs_available_list[2]
                        self.player.classes_dict[key] += 1
                        
                        del self.help_list
                        self.weapon_chosen = False
                        self.is_set = True

    #window between fights
    def window_actions(self):

        self.player.hp = self.player.original_hp
        self.enemy = self.enemy_list[self.player.player_level - 1]
        self.reward_rect = self.enemy.reward_weapon_surf.get_frect(center = (self.enemy.rect.x, self.enemy.rect.y))
        self.player.player_level += 1
        self.move_count = 0
        
        for buff in all_buffs:
            buff.revert()
        self.buffs_called = False


    def attack(self):
        self.number_of_moves += 1
        
        self.is_missed = False

        #chance of attack
        num = random.randint(1, self.attacker.dexterity+self.defender.dexterity)
        print(f"Move number {self.number_of_moves}")
        print(f"The attacker: {self.attacker}, The defender: {self.defender}")
        print(f"The rolled number is {num}")
        print(f"Rolled number will be compared to {self.defender.dexterity}")

        #miss
        if num <= self.defender.dexterity:
            self.attacker, self.defender = self.defender, self.attacker
            print("attack missed") 
            self.miss_time = pygame.time.get_ticks()
            self.is_missed = True

        #attack logic
        else:
            if self.attacker == self.player:
                for buff in all_buffs:
                    buff.buff_apply()
                monster_buffs_dict[self.defender.name][0](self.player, self.defender)
                
                print(f"All buffs are {all_buffs}")
                if self.attacker.damage > 0:
                    print(f"The damage dealed to a monster is {self.attacker.damage}")
                    print(f"Hp before { self.defender.hp}")
                    self.prev_hp = self.defender.hp
                    self.defender.hp -= self.attacker.damage 
                    if self.defender.hp <= 0:
                        self.defender.hp = 0
                    print(f"Hp after { self.defender.hp}")
                    monster_buffs_dict[self.defender.name][1](self.player, self.defender)
                    self.hit_time = pygame.time.get_ticks()
                self.player.move_count += 1

                self.attacker, self.defender = self.defender, self.attacker
            

            else:
                self.attacker.moves += 1
                for buff in all_buffs:
                    buff.buff_apply()
                monster_buffs_dict[self.attacker.name][0](self.player, self.attacker)
                print(f"Previous player hp {self.player.hp}")
                self.prev_hp = self.player.hp
                self.defender.hp -= self.attacker.damage 
                print(f"New player hp is {self.player.hp}")
                print(f"The attacker damage is {self.attacker.damage}")
                monster_buffs_dict[self.attacker.name][1](self.player, self.attacker)
                self.hit_time = pygame.time.get_ticks()
                self.attacker, self.defender = self.defender, self.attacker
            

        self.move_opportunity = False
        self.player.turn = not self.player.turn


    def render(self, screen):

        screen.blit(background, (0, 0))
        pygame.display.set_caption("Gameplay")
        all_sprites.draw(screen)

        #main game
        if not self.is_window:
            if self.enemy_list[self.player.player_level - 1].is_allive:
           
                screen.blit(self.enemy_list[self.player.player_level - 1].image, self.enemy_list[self.player.player_level - 1].rect)
        
        #windows
        if hasattr(self, "reward_rect"):
            screen.blit(self.enemy.reward_weapon_surf, (self.reward_rect.x, self.reward_rect.y))
        
        self.display_text(screen)

        
    

        pygame.display.update()
    
    
    def display_text(self, screen):
        player_text_surf = font35.render(str(self.player.hp), True, (255, 0, 0))
        player_text_rect = player_text_surf.get_frect(midtop = (self.heart.rect.midbottom))
        screen.blit(player_text_surf, player_text_rect)

        #main game
        if not self.is_window:
            if self.enemy_list[self.player.player_level - 1].is_allive:
                enemy_text_surf = font35.render(str(self.enemy_list[self.player.player_level - 1].hp), True, (255, 0, 0))
                enemy_text_rect = enemy_text_surf.get_frect(midtop = (self.enemy_list[self.player.player_level - 1].rect.midtop))
                screen.blit(enemy_text_surf, enemy_text_rect)

                self.curr_time = pygame.time.get_ticks()

                if (self.player.turn):
                    turn_text_surf = self.text_list[0]
                else:
                    turn_text_surf = self.text_list[1]

                    #miss logic
                if (self.is_missed):
                    if self.defender == self.player:
                        turn_text_surf = self.text_list[2]
                    else:
                        turn_text_surf = self.text_list[3]

                    if self.curr_time - self.miss_time <= 500:
                        miss_text = self.text_list[4]
                        if self.defender == self.player:
                            #miss_text_rect = miss_text_surf.get_frect(midright = (enemy_text_rect.left - 20, enemy_text_rect.centery ))
                            miss_text_rect = miss_text.get_frect(midbottom = (enemy_text_rect.midtop))
                        else:
                            miss_text_rect = miss_text.get_frect(midleft = (player_text_rect.right + 20, player_text_rect.centery))
                        screen.blit(miss_text, miss_text_rect)

                #minus damage
                if self.curr_time - self.hit_time <= 500:
                    damage_text = font35.render(f"-{str(self.prev_hp - self.attacker.hp)}", True, (140, 34, 28))


                    if self.defender == self.player:
                        damage_text_rect = damage_text.get_frect(midright = (enemy_text_rect.centerx + 10, enemy_text_rect.centery - 35))
                    
                    else:
                        damage_text_rect = damage_text.get_frect(midleft = (player_text_rect.right + 20, player_text_rect.centery))

                    screen.blit(damage_text,damage_text_rect)

                


                turn_text_rect = turn_text_surf.get_frect(midtop = (WIDTH / 2, 200))
                screen.blit(turn_text_surf, turn_text_rect)
        else:
            if hasattr(self, "reward_rect"):
                weapon_choice = self.text_list[5]
                choice_text_rect = weapon_choice.get_frect(midtop = (WIDTH / 2 + 50, 200))
                screen.blit(weapon_choice, choice_text_rect)

            if hasattr(self, "help_list") and self.weapon_chosen:
                pos = 200
                choice_text_rect = self.t7.get_frect(midtop = (WIDTH / 2 + 80, pos))

                screen.blit(self.t7, choice_text_rect)

                buff_text.draw(screen)

            if self.is_set:
                rect = self.t8.get_frect(midtop = (WIDTH / 2, 200))
                screen.blit(self.t8, rect)
                


class BuffText(pygame.sprite.Sprite):
    def __init__(self, buff_text, text_image, pos):
        super().__init__(buff_text)
        self.image = text_image
        self.pos = pos
        self.rect = self.image.get_frect(center = (WIDTH / 2 + 20, self.pos))

    
    def update(self, dt):
        pass

    


