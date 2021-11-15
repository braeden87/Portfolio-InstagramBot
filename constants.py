import pygame
pygame.font.init()

##################################################
# Constants
##################################################
BASE_URL = 'https://www.instagram.com'
COMMENTS = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']
COUNT = 2

#GUI Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 825
INPUTBOX_WIDTH = 500
INPUTBOX_HEIGHT = 50
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (32, 32, 32)
HIGHLIGHT_COLOR = (225, 225, 225)
FONT = pygame.font.SysFont('arial', 32)
TEXT_BOX_UNFOCUSED = (245, 245, 245)
