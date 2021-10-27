import pygame
from GUI.GUI_Input_Box import input_box
import constants as const
from GUI.GUI_Submit_Button import submit_button
from GUI.GUI_Header import header_box
pygame.init()

screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption('Instagram Bot')

def main():
    clock = pygame.time.Clock()
    input_box1 = input_box(50, 300, const.INPUTBOX_WIDTH, const.INPUTBOX_HEIGHT)
    input_box2 = input_box(50, 400, const.INPUTBOX_WIDTH, const.INPUTBOX_HEIGHT)
    input_box3 = input_box(50, 500, const.INPUTBOX_WIDTH, const.INPUTBOX_HEIGHT)
    input_boxes = [input_box1, input_box2, input_box3]
    header1 = header_box(50, 260, const.INPUTBOX_WIDTH, const.INPUTBOX_HEIGHT, 'Username:')
    header2 = header_box(50, 360, const.INPUTBOX_WIDTH, const.INPUTBOX_HEIGHT, 'Password:')
    header3 = header_box(50, 460, const.INPUTBOX_WIDTH, const.INPUTBOX_HEIGHT, 'Hashtags:')
    headers = [header1, header2, header3]
    submit = submit_button(200, 560, 200, const.INPUTBOX_HEIGHT)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for box in input_boxes:
                box.handle_event(event)
            submit.handle_event(event)
            if submit.active:
                user_answers = list()
                for box in input_boxes:
                    user_answers.append(box.user_input())
                return user_answers

        screen.fill(const.BACKGROUND_COLOR)
        instagram_logo = pygame.image.load('./images/Instagram-logo.png')
        logo_rectangle = pygame.Rect(150, 0, 300, 300)
        instagram_logo_small = pygame.transform.scale(instagram_logo, (300, 300))
        screen.blit(instagram_logo_small, logo_rectangle)
        pygame.draw.rect(screen, const.BACKGROUND_COLOR, logo_rectangle, 1)

        for box in input_boxes:
            box.draw(screen)
        for header in headers:
            header.draw(screen)
        submit.draw(screen)

            

        pygame.display.flip()
        clock.tick(30)