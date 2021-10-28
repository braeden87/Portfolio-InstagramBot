import pygame
import constants as const


class submit_button:
######################################################################
# Constructor
######################################################################  
    def __init__(self, x, y, width, height, text= 'Submit'):
        self.button = pygame.Rect(x, y, width, height)
        self.text = text    
        self.active = False
        self.color = const.TEXT_BOX_UNFOCUSED
        self.text_surface = const.FONT.render(text, True, const.TEXT_COLOR)
######################################################################
# Handle Event Method
#
# This method is accepts an event as an argument and decides what to  
#do inside of the text box based on what event was passed in
######################################################################  
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.collidepoint(event.pos):
                self.active = not self.active
            else: self.active = False
            if self.active: self.color = const.HIGHLIGHT_COLOR
            else: self.color = const.TEXT_BOX_UNFOCUSED
######################################################################
# Draw Method
#
# This method will add the submit button to the window
######################################################################  
    def draw(self, screen):
       #Text 
        screen.blit(self.text_surface, (self.button.x + (self.button.width / 2 - self.text_surface.get_width() / 2), self.button.y + (self.button.height / 2 - self.text_surface.get_height() / 2)))
        pygame.draw.rect(screen, self.color, self.button, 2)
