import pygame
from imports import warrior_surf, barbarian_surf, bandit_surf, warrior_surf_picked, bandit_surf_picked, barbarian_surf_picked, sword_surf, dagger_surf, club_surf, select_sound, font35
from player import*
from settings import*
from groups import all_sprites, all_buffs



class Menu:
    
    def __init__(self, shared_data):
        self.shared_data = shared_data
        self.next_state = 'main menu'
        self.clean()

        #font
        self.font = pygame.font.Font('fonts/pixel_font.ttf', 60)
        self.text_surf = self.font.render('CHOOSE YOUR CHARACTER ', True, 'white')
        self.text_rect = self.text_surf.get_frect(midbottom = (WIDTH / 2, 300))

        self.warrior_description = font35.render('HP: 5, WEAPON: SWORD (3 DAMAGE)', True, 'yellow' )
        self.warrior_description1 = font35.render('X2 WEAPON DAMAGE FOR THE FIRST MOVE', True, 'yellow')

        self.barbarian_description = font35.render('HP: 6, WEAPON: CLUB (3 DAMAGE)', True, 'yellow' )
        self.barbarian_description1 = font35.render('DAMAGE + 2 FOR THE FIRST 2 MOVES, THEN -1', True, 'yellow')
       
        self.bandit_description = font35.render('HP: 4, WEAPON: DAGGER (2 DAMAGE)', True, 'yellow' )
        self.bandit_description1 = font35.render('+1 DAMAGE', True, 'yellow')
        #warrior
        self.warrior_surf = warrior_surf
        self.warrior_rect = self.warrior_surf.get_frect(midbottom = (WIDTH / 3, 800))
        self.cur_warrior_surf = self.warrior_surf
        self.warrior_surf_picked = warrior_surf_picked

        self.warrior_description_rect = self.warrior_description.get_frect(midtop = (self.warrior_rect.centerx, self.warrior_rect.centery + 250))
        self.warrior_description1_rect = self.warrior_description1.get_frect(midtop = (self.warrior_rect.centerx + 70 , self.warrior_rect.centery + 300))

        
        #barbarian
        self.barbarian_surf = barbarian_surf
        self.barbarian_rect = self.barbarian_surf.get_frect(midbottom = (WIDTH / 2, 800))
        self.cur_barbarian_surf = self.barbarian_surf
        self.barbarian_surf_picked = barbarian_surf_picked


        self.barbarian_description_rect = self.warrior_description.get_frect(midtop = (self.barbarian_rect.centerx, self.warrior_rect.centery + 250))
        self.barbarian_description1_rect = self.warrior_description1.get_frect(midtop = (self.barbarian_rect.centerx + 50, self.warrior_rect.centery + 300))


        #bandit
        self.bandit_surf = bandit_surf
        self.bandit_rect = self.bandit_surf.get_frect(midbottom = (WIDTH * 2 / 3, 810))
        self.cur_bandit_surf = self.bandit_surf
        self.bandit_surf_picked = bandit_surf_picked

        self.bandit_description_rect = self.bandit_description.get_frect(midtop = (self.barbarian_rect.centerx + 300, self.bandit_rect.centery + 250))
        self.bandit_description1_rect = self.bandit_description1.get_frect(midtop = (self.bandit_rect.centerx , self.bandit_rect.centery + 300))

        #etc
        self.was_collided = False

    def clean(self):
        all_sprites.empty()
        all_buffs.empty()
        self.shared_data.clear()
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.next_state = 'quit'

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.next_state = 'quit'

    def is_collided(self, x1, x2, x3):
        if (not(x1 or x2 or x3)):
            self.was_collided = False
            select_sound.stop()


            



    def update(self, dt):

        self.cursor_pos = pygame.mouse.get_pos()
        self.mouse_buttons = pygame.mouse.get_pressed()

        self.is_collided(self.bandit_rect.collidepoint(self.cursor_pos), self.warrior_rect.collidepoint(self.cursor_pos), self.barbarian_rect.collidepoint(self.cursor_pos))
    

        #warrior animation
        if self.warrior_rect.collidepoint(self.cursor_pos):
            self.cur_warrior_surf = self.warrior_surf_picked
  
        
            if not self.was_collided:
                select_sound.play(loops = 0)
            self.was_collided = True

        else:
            self.cur_warrior_surf = self.warrior_surf
        
        if self.warrior_rect.collidepoint(self.cursor_pos) and self.mouse_buttons[0]: 
            shared_data['player'] = [warrior_surf, 5, 'sword', sword_surf, 'warrior']
            shared_data['heart'] = []
            select_sound.stop()

            self.next_state = 'gameplay'


        #bandit animation
        if self.bandit_rect.collidepoint(self.cursor_pos):
            self.cur_bandit_surf = self.bandit_surf_picked
            if not self.was_collided:
                select_sound.play(loops = 0)
            self.was_collided = True

    
        else:
            self.cur_bandit_surf = self.bandit_surf
        
        if self.bandit_rect.collidepoint(self.cursor_pos) and self.mouse_buttons[0]: 
            shared_data['player'] = [ bandit_surf, 4, 'dagger', dagger_surf, 'bandit']
            shared_data['heart'] = []
            select_sound.stop()


            
            self.next_state = 'gameplay'

        #barbarian animation
        if self.barbarian_rect.collidepoint(self.cursor_pos):
            self.cur_barbarian_surf = self.barbarian_surf_picked
            #select_sound.play(loops = 1)
            if not self.was_collided:
                select_sound.play(loops = 0)
            self.was_collided = True            

        else:
            self.cur_barbarian_surf = self.barbarian_surf
        
        if self.barbarian_rect.collidepoint(self.cursor_pos) and self.mouse_buttons[0]: 
            shared_data['player'] = [ barbarian_surf, 6, 'club', club_surf, 'barbarian']
            shared_data['heart'] = []
            select_sound.stop()
            self.next_state = 'gameplay'

        

        


    def render(self, screen):

        screen.fill((30, 30, 30))

        screen.blit(self.text_surf, self.text_rect)
        screen.blit(self.cur_warrior_surf, self.warrior_rect)
        screen.blit(self.cur_barbarian_surf, self.barbarian_rect)
        screen.blit(self.cur_bandit_surf, self.bandit_rect)

        if self.warrior_rect.collidepoint(self.cursor_pos):
            screen.blit(self.warrior_description, self.warrior_description_rect)
            screen.blit(self.warrior_description1, self.warrior_description1_rect)

        if self.barbarian_rect.collidepoint(self.cursor_pos):
            screen.blit(self.barbarian_description, self.barbarian_description_rect)
            screen.blit(self.barbarian_description1, self.barbarian_description1_rect)

        if self.bandit_rect.collidepoint(self.cursor_pos):
            screen.blit(self.bandit_description, self.bandit_description_rect)
            screen.blit(self.bandit_description1, self.bandit_description1_rect)


        pygame.display.set_caption("Main Menu")
        pygame.display.update()
