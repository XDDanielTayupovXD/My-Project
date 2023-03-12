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
        self.score_limit = 3
        self.score_1 = 0
        self.score_2 = 0
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

    def reset_ball(self):
        if random.randint(0, 1) == 0:
            self.ball_dx = random.randrange(1,5)
        else:
            self.ball_dx = random.randrange(-5,-1)
        self.ball_dy = random.randrange(-5,5)
        self.ball_x = self.WIDTH // 2
        self.ball_y = self.HEIGHT // 2

    def render_score(self):
        self.counter1 = self.myfont.render(str(self.score_1), False, (0, 0, 0))
        self.counter2 = self.myfont.render(str(self.score_2), False, (0, 0, 0))

    def play(self):
        self.reset_ball()
        self.render_score()
        running = True
        y_1_change = 0
        y_2_change = 0
        while running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        y_2_change -= 5
                    if event.key == pygame.K_DOWN:
                        y_2_change += 5
                    if event.key == pygame.K_w:
                        y_1_change -= 5
                    if event.key == pygame.K_s:
                        y_1_change += 5
                
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        y_2_change += 5
                    if event.key == pygame.K_DOWN:
                        y_2_change -= 5
                    if event.key == pygame.K_w:
                        y_1_change += 5
                    if event.key == pygame.K_s:
                        y_1_change -= 5

            self.y_2 += y_2_change
            if self.y_2 <= 0:
                self.y_2 = 0
            elif self.y_2 >= self.HEIGHT - 85:
                self.y_2 = self.HEIGHT - 85

            self.y_1 += y_1_change
            if self.y_1 <= 0:
                self.y_1 = 0
            elif self.y_1 >= self.HEIGHT - 85:
                self.y_1 = self.HEIGHT - 85

            self.ball_x += self.ball_dx
            self.ball_y += self.ball_dy

            if self.ball_y <= 0 or self.ball_y + self.ball.get_height() >= self.HEIGHT:
                self.ball_dy *= -1
                # ball_dy = -ball_dy

            # left score
            if self.ball_x <= 0:
                self.reset_ball()

                self.score_2 += 1
                self.render_score()

                if self.score_2 > self.score_limit:
                    file = open('scoreboard.txt', 'w') #TODO append instead of rewrite
                    file.write('Player 2 won!')
                    file.write(f'{self.score_1}\t{self.score_2}')
                    
            # right score
            if self.ball_x + self.ball.get_width() >= self.WIDTH:
                self.reset_ball()

                self.score_1 += 1
                self.render_score()
                
                if self.score_1 > self.score_limit:
                    file = open('scoreboard.txt', 'w') #TODO append instead of rewrite
                    file.write('Player 1 won!')
                    file.write(f'{self.score_1}\t{self.score_2}')


            if (self.ball_x <= self.player1.get_width() and self.ball_y >= self.y_1 and
                self.y_1 + self.player1.get_height() >= self.ball_y + self.ball.get_height()):
                self.ball_dx = abs(self.ball_dx)
                
            if (self.ball_x + self.ball.get_width() >= 755 and self.ball_y >= self.y_2 and
                self.y_2 + self.player2.get_height() >= self.ball_y + self.ball.get_height()):
                self.ball_dx = -abs(self.ball_dx)

            self.screen.fill((255,255,255))
            self.screen.blit(self.ball,(self.ball_x, self.ball_y))
            self.screen.blit(self.player1,(1, self.y_1))
            self.screen.blit(self.player2,(755, self.y_2))
            self.screen.blit(self.counter1, (self.WIDTH*0.4, self.HEIGHT*0.1))
            self.screen.blit(self.counter2, (self.WIDTH*0.6, self.HEIGHT*0.1))
            pygame.display.flip()
        pygame.quit()
    
if __name__ == "__main__":
    mygame = game()
    mygame.play()