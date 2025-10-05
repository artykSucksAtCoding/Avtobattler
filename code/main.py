import pygame
import sys


from groups import all_sprites  
from settings import*

pygame.init()
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))


from menu import*
from gameplay import*
from lost_screen import LostScreen
from win_screen import WinScreen


clock = pygame.time.Clock()
state_classes = {
    'main menu': Menu,
    'gameplay': Gameplay,
    'lost screen': LostScreen,
    'win screen': WinScreen
}

def run():

    current_state_name = 'main menu'
    current_state = state_classes[current_state_name](shared_data)

    while current_state_name != 'quit':
        dt = clock.tick(60) / 1000
        events = pygame.event.get()

        current_state.handle_events(events)
        current_state.update(dt)
        current_state.render(display_surface)
        
    
        if current_state.next_state != current_state_name:
            current_state_name = current_state.next_state
            if current_state_name == 'quit':
                break
            current_state = state_classes[current_state_name](shared_data)

    pygame.quit()
    sys.exit()

run()
