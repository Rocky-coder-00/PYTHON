import pygame
import random
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

class Fruit:
    def __init__(self, x, y, fruit_type):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-8, -4)
        self.fruit_type = fruit_type
        self.radius = 25
        self.sliced = False
        self.slice_time = 0
        self.colors = {
            'apple': RED,
            'banana': YELLOW,
            'orange': ORANGE,
            'grapes': PURPLE
        }
    
    def update(self):
        if not self.sliced:
            self.x += self.vx
            self.y += self.vy
            self.vy += 0.3  # gravity
            
            # Bounce off walls
            if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
                self.vx *= -0.8
            if self.y - self.radius <= 0:
                self.vy *= -0.8
            
            # Remove if off screen
            if self.y > SCREEN_HEIGHT + 50:
                return False
        
        else:
            self.slice_time += 1
            if self.slice_time > 30:  # Remove sliced fruit after animation
                return False
        
        return True
    
    def draw(self, screen):
        if self.sliced:
            # Draw sliced fruit effect
            pygame.draw.circle(screen, self.colors[self.fruit_type], 
                             (int(self.x), int(self.y)), self.radius)
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius, 4)
            # Slice line
            pygame.draw.line(screen, WHITE, 
                           (self.x - self.radius//2, self.y - self.radius//2),
                           (self.x + self.radius//2, self.y + self.radius//2), 5)
        else:
            pygame.draw.circle(screen, self.colors[self.fruit_type], 
                             (int(self.x), int(self.y)), self.radius)
            pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.radius, 2)
    
    def is_clicked(self, pos):
        distance = math.sqrt((pos[0] - self.x)**2 + (pos[1] - self.y)**2)
        return distance <= self.radius and not self.sliced

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Fruit Cutting Game 🍎")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)
        
        self.fruits = []
        self.score = 0
        self.misses = 0
        self.game_time = 0
        self.game_over = False
        
        # Spawn fruits
        self.spawn_timer = 0
        self.fruit_types = ['apple', 'banana', 'orange', 'grapes']
    
    def spawn_fruit(self):
        x = random.randint(50, SCREEN_WIDTH - 50)
        fruit_type = random.choice(self.fruit_types)
        self.fruits.append(Fruit(x, -50, fruit_type))
    
    def handle_click(self, pos):
        for fruit in self.fruits[:]:
            if fruit.is_clicked(pos):
                fruit.sliced = True
                self.score += 10
                self.fruits.remove(fruit)
                break
    
    def update(self):
        if not self.game_over:
            self.game_time += 1
            
            # Spawn fruits more frequently over time
            self.spawn_timer += 1
            if self.spawn_timer > max(20 - self.game_time//1000, 10):
                self.spawn_fruit()
                self.spawn_timer = 0
            
            # Update fruits
            self.fruits = [fruit for fruit in self.fruits if fruit.update()]
            
            # Check misses
            for fruit in self.fruits:
                if fruit.y > SCREEN_HEIGHT and not fruit.sliced:
                    self.misses += 1
                    self.fruits.remove(fruit)
                    break
            
            # Game over condition
            if self.misses >= 5:
                self.game_over = True
    
    def draw(self):
        self.screen.fill((135, 206, 235))  # Sky blue background
        
        # Draw grass
        pygame.draw.rect(self.screen, GREEN, (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
        
        # Draw fruits
        for fruit in self.fruits:
            fruit.draw(self.screen)
        
        # Draw score
        score_text = self.small_font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (20, 20))
        
        misses_text = self.small_font.render(f"Misses: {self.misses}/5", True, BLACK)
        self.screen.blit(misses_text, (20, 60))
        
        time_text = self.small_font.render(f"Time: {self.game_time//60}", True, BLACK)
        self.screen.blit(time_text, (SCREEN_WIDTH - 150, 20))
        
        if self.game_over:
            # Game over overlay
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            game_over_text = self.font.render("GAME OVER", True, WHITE)
            final_score_text = self.small_font.render(f"Final Score: {self.score}", True, WHITE)
            
            # Center text
            go_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
            fs_rect = final_score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 20))
            
            self.screen.blit(game_over_text, go_rect)
            self.screen.blit(final_score_text, fs_rect)
            
            restart_text = self.small_font.render("Press R to Restart or ESC to Quit", True, WHITE)
            r_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80))
            self.screen.blit(restart_text, r_rect)
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.game_over:
                        self.handle_click(pygame.mouse.get_pos())
                
                elif event.type == pygame.KEYDOWN:
                    if self.game_over:
                        if event.key == pygame.K_r:
                            # Restart game
                            self.__init__()
                        elif event.key == pygame.K_ESCAPE:
                            running = False
            
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()