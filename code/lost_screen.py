import pygame
from settings import*

class LostScreen:
    
    def __init__(self, shared_data):
        self.shared_data = shared_data
        self.next_state = 'lost screen'
        
        self.player_surf = self.shared_data['player'][0]
   

        self.player_surf = pygame.transform.scale_by(self.player_surf, 1.5)
        self.player_surf = pygame.transform.grayscale(self.player_surf)
        self.rect = self.player_surf.get_frect(midtop = (WIDTH / 2, HEIGHT - 750))
        #font
        self.font = pygame.font.Font('fonts/pixel_font.ttf', 52)
        self.text_surf = self.font.render('YOU HAVE LOST. PRESS ENTER TO RESTART ', True, 'white')
        self.text_rect = self.text_surf.get_frect(midbottom = (WIDTH / 2, 350))



    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.next_state = 'quit'

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.next_state = 'quit'

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.next_state = 'main menu'
            

    def update(self, dt):

        pass

    def render(self, screen):

        screen.fill((30, 30, 30))

        screen.blit(self.text_surf, self.text_rect)
        screen.blit(self.player_surf, self.rect)

        pygame.display.update()
        

