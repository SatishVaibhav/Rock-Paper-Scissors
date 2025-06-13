#Rock, Paper, Scissors game created by Vaibhav Satish 
import pygame
import random 

#This allows for the UI to be created 
pygame.init()
background = pygame.image.load("RPS.jpg")
background = pygame.transform.scale(background, (1000, 500))
screen = pygame.display.set_mode((1000, 500))
screen.blit(background, (0,0))
pygame.display.set_caption('Rock, Paper, Scissors Game')
font = pygame.font.Font(None, 72)
font2 = pygame.font.Font(None, 36)
text = font.render("Welcome to Rock Paper Scissors!" , True, (0, 0, 0)) 
text2 = font2.render("Press R, P, or S on your keyboard to Play Your First Round", True, (0,0,0))
text3 = font2.render("!GOOD LUCK!", True, (0,0,0))
screen.blit(text, (60, 0))
screen.blit(text2, (55, 295))
screen.blit(text3, (55, 380))
pygame.display.update()  

#main class
class RPS:
    
    def __init__(self, round_num):
        self.checker = True
        self.choice = ""
        self.all_choices = ["Rock", "Paper", "Scissors"]
        self.user_response = None
        self.location = None
        self.computer_response = None
        self.player_score = 0
        self.computer_score = 0 
        self.round = round_num
        
    def display_result(self): 
        result = ""
        if self.player_score > self.computer_score: 
            result = "YOU WON!!! :)"
        elif self.player_score < self.computer_score: 
            result = "YOU LOST :( "
        else: 
            result = "IT'S A TIE!!!"
        result_text = font.render(result, True, (0,0,0))
        screen.blit(result_text, (100, 200))
        pygame.display.flip()
        
    def main(self): 
        running = True
        clock = pygame.time.Clock()
        while running: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.user_response = "Rock"
                    elif event.key == pygame.K_p:
                        self.user_response = "Paper"
                    elif event.key == pygame.K_s:
                        self.user_response = "Scissors"
                    else:
                        continue
                    self.location = random.randint(0, len(self.all_choices)-1)
                    self.computer_response = self.all_choices[self.location]
                    screen.fill((255, 255, 255))
                    self.game()
                    score_text = font.render(f"Scoreboard: {self.player_score} - {self.computer_score}", True, (0,0,0))
                    self.round -= 1
                    round_text = font.render(f"Remaining Rounds: " + str(self.round), True, (0,0,0))
                    screen.blit(score_text, (100, 100))
                    screen.blit(round_text, (50, 50))
                    pygame.display.flip()
                    if self.round == 0:
                        self.display_result()
                        pygame.time.wait(2000)
                        running = False
            clock.tick(60)
        pygame.quit()
        
    def game(self):
        if self.user_response == "Rock" and self.computer_response == "Scissors":
                self.checker = True
                self.player_score += 1 
        elif self.user_response == "Scissors" and self.computer_response == "Rock": 
                self.checker = False 
                self.computer_score += 1
        elif self.user_response == "Paper" and self.computer_response == "Scissors": 
                self.checker = False 
                self.computer_score += 1
        elif self.user_response == "Scissors" and self.computer_response == "Paper": 
                self.checker = True
                self.player_score += 1 
        elif self.user_response == "Rock" and self.computer_response == "Paper": 
                self.checker = True 
                self.player_score += 1 
        elif self.user_response == "Paper" and self.computer_response == "Rock": 
                self.checker = False
                self.computer_score += 1
        else: 
                self.checker = False
                self.computer_score += 1
            
#This allows for the game to be played            
class testing(): 
    
    rps_game_test = RPS(10)
    rps_game_test.main()




