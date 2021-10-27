import pygame
import constants as const

class header_box:

    def __init__(self, x, y, width, height, text):
        self.header = pygame.Rect(x, y, width, height)
        self.text = text    
        self.color = const.BACKGROUND_COLOR
        self.text_surface = const.FONT.render(text, True, const.TEXT_COLOR)


    def draw(self, screen):
       #Text 
        screen.blit(self.text_surface, (self.header.x + 5, self.header.y + 5))
        pygame.draw.rect(screen, self.color, self.header, 2)