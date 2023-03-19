import pygame
import random


class game:
    def __init__(self, WIDTH = 800, HEIGHT = 600, FPS = 60) -> None:
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.FPS = FPS
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.ball = pygame.image.load("minecraft.png")
        self.player1 = pygame.image.load("diamond_sword.png")
        self.player2 = pygame.image.load("diamond_sword.png")
        self.y_1 = HEIGHT // 2 - 25
        self.y_2 = HEIGHT // 2 - 25
        self.y_1_change = 0
        self.y_2_change = 0
        self.score_limit = 10
        self.score_1 = 0
        self.score_2 = 0
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

    def reset_ball(self):
        if random.randint(0,1) == 0:
            self.ball_dx = random.randrange(1,5)
        else:
            self.ball_dx = random.randrange(-5,-1)
        self.ball_dy = random.randrange(-5,5)
        self.ball_x = self.WIDTH // 2
        self.ball_y = self.HEIGHT // 2

    def render_score(self):
        self.counter1 = self.myfont.render(str(self.score_1), False, (0,0,0))
        self.counter2 = self.myfont.render(str(self.score_2), False, (0,0,0))


    
    def play(self): 
        self.reset_ball()
        self.render_score()
        self.running = True
        while self.running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.y_2_change -= 5
                    if event.key == pygame.K_DOWN:
                        self.y_2_change += 5
                    if event.key == pygame.K_w:
                        self.y_1_change -= 5
                    if event.key == pygame.K_s:
                        self.y_1_change += 5
                
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.y_2_change = 0
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        self.y_1_change = 0
            self.ball_x = self.ball_dx + self.ball_x
            self.ball_y = self.ball_dy + self.ball_y

            if self.ball_y <= 0 or self.ball_y + self.ball.get_height() >= self.HEIGHT:
                self.ball_dy *= -1

            if self.ball_x <= 0:
                self.score_2 += 1
                self.reset_ball()
                self.render_score()
                if self.score_2 > self.score_limit:
                    file = open("scoreboard.txt", 'w')
                    file.write('Player 2 won!')
                    file.write(f'{self.score_1}\t{self.score_2}')



            if self.ball_x + self.ball.get_height() >= self.WIDTH:
                self.score_1 += 1
                self.ball_dx = random.randrange(-5,5)
                self.ball_dy = random.randrange(-5,5)
                self.ball_x = self.WIDTH // 2
                self.ball_y = self.HEIGHT // 2
                self.counter1 = self.myfont.render(str(self.score_1), False, (0,0,0))
            if (self.ball_x <= self.player1.get_width() and self.ball_y >= self.y_1 and self.y_1 + self.player1.get_height() >= self.ball_y + self.ball.get_height()):
                self.ball_dx = abs(self.ball_dx)

            if (self.ball_x + self.ball.get_width() >= 755 and self.ball_y >= self.y_2 and self.y_2 + self.player2.get_height() >= self.ball_y + self.ball.get_height()):
                self.ball_dx = -abs(self.ball_dx)

            self.y_2 += self.y_2_change
            if self.y_2 <= 0:
                self.y_2 = 0
            elif self.y_2 >= self.HEIGHT - 85:
                self.y_2 = self.HEIGHT - 85

            self.y_1 += self.y_1_change
            if self.y_1 <= 0:
                self.y_1 = 0
            elif self.y_2 >= self.HEIGHT - 85:
                self.y_2 = self.HEIGHT - 85

            self.screen.fill((255,255,255))
            self.screen.blit(self.ball,(self.ball_x, self.ball_y))
            self.screen.blit(self.player1,(1, self.y_1))
            self.screen.blit(self.player1,(755, self.y_2))
            self.screen.blit(self.counter1, (self.WIDTH*0.4, self.HEIGHT*0.1))
            self.screen.blit(self.counter2, (self.WIDTH*0.6, self.HEIGHT*0.1))
            pygame.display.flip()
        pygame.quit()
if __name__ == "__main__":
    mygame = game()
    mygame.play() 
