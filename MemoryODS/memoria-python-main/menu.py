#menu

import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        
        self.state = "Level 1"
        self.L1x, self.L1y = self.mid_w, self.mid_h + 30
        self.L2x, self.L2y = self.mid_w, self.mid_h + 50
        self.L3x, self.L3y = self.mid_w, self.mid_h + 70
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.L1x + self.offset, self.L1y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Level 1", 20, self.L1x, self.L1y)
            self.game.draw_text("Level 2", 20, self.L2x, self.L2y)
            self.game.draw_text("Level 3", 20, self.L3x, self.L3y)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        
        if self.game.DOWN_KEY:
            if self.state == 'Level 1':
                self.cursor_rect.midtop = (self.L2x + self.offset, self.L2y)
                self.state = 'Level 2'
            
            elif self.state == 'Level 2':
                self.cursor_rect.midtop = (self.L3x + self.offset, self.L3y)
                self.state = 'Level 3'
            
            elif self.state == 'Level 3':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'

            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.L1x + self.offset, self.L1y)
                self.state = 'Level 1'
                
        elif self.game.UP_KEY:
            if self.state == 'Level 1':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            
            elif self.state == 'Level 3':
                self.cursor_rect.midtop = (self.L2x + self.offset, self.L2y)
                self.state = 'Level 2'
             
            elif self.state == 'Level 1':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'   
                
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.L3x + self.offset, self.L3y)
                self.state = 'Level 3'
                
            elif self.state == 'Level 2':
                self.cursor_rect.midtop = (self.L1x + self.offset, self.L1y)
                self.state = 'Level 1'


    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Level 1':
                self.game.playing = True
           
            elif self.state == 'Level 2':
                self.game.playing = True
            
            elif self.state == 'Level 3':
                self.game.playing = True
            
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by: Los Güifis #31', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text('Daniel Muñoz Lozano', 12, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 30)
            self.game.draw_text('Sofía Martínez Hernández', 12, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50)
            self.game.draw_text('Bella Elisabet Perales Meléndez y Alcocer', 12, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 70)
            self.blit_screen()