import pygame
import constants as const

class input_box:

    def __init__(self, x, y, width, height, text = ''):
        self.box = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_surface = const.FONT.render(text, True, const.TEXT_COLOR)
        self.active = False
        self.tabbed = False
        self.color = const.TEXT_BOX_UNFOCUSED
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.box.collidepoint(event.pos):
                self.active = not self.active
            else: self.active = False
            if self.active: self.color = const.HIGHLIGHT_COLOR
            else: self.color = const.TEXT_BOX_UNFOCUSED
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    pass
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[: - 1]
                else:
                    self.text += event.unicode
                self.text_surface = const.FONT.render(self.text, True, const.TEXT_COLOR)
        
    def draw(self, screen):
       #Text 
        screen.blit(self.text_surface, (self.box.x + 5, self.box.y + 5))
        pygame.draw.rect(screen, self.color, self.box, 2)
    def user_input(self):
        return self.text
