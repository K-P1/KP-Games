import pygame
import sys
import random

class SnakeGame:
    def __init__(self, speed=7, wrap=True, food_multiplier=1):
        pygame.init()
        self.speed = speed  # Lower FPS = slower game; adjust for difficulty.
        self.wrap_mode = wrap
        self.food_multiplier = food_multiplier  # Number of food items simultaneously.
        self.screen_width = 600
        self.screen_height = 400
        self.block_size = 20
        self.display = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 25)
        self.reset()
        # Define button rectangles for in-game controls.
        self.pause_button_rect = pygame.Rect(self.screen_width - 150, 10, 70, 30)
        self.quit_button_rect = pygame.Rect(self.screen_width - 70, 10, 60, 30)
        # For the pause menu:
        self.resume_button_rect = pygame.Rect(self.screen_width//2 - 80, self.screen_height//2 + 30, 70, 30)
        self.pause_quit_button_rect = pygame.Rect(self.screen_width//2 + 10, self.screen_height//2 + 30, 70, 30)

    def reset(self):
        # Reset game state.
        self.snake = [(self.screen_width // 2, self.screen_height // 2)]
        self.direction = "RIGHT"
        self.score = 0
        self.foods = []
        self.spawn_foods()

    def spawn_foods(self):
        # Spawn a number of food items based on food_multiplier.
        self.foods = []
        num_foods = int(self.food_multiplier)
        if self.food_multiplier - num_foods >= random.random():
            num_foods += 1
        for _ in range(num_foods):
            self.foods.append(self.place_food())

    def place_food(self):
        x = random.randrange(0, self.screen_width, self.block_size)
        y = random.randrange(0, self.screen_height, self.block_size)
        return (x, y)

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.display, (0, 255, 0), 
                             (segment[0], segment[1], self.block_size, self.block_size))

    def draw_food(self):
        for food in self.foods:
            pygame.draw.rect(self.display, (255, 0, 0), 
                             (food[0], food[1], self.block_size, self.block_size))

    def display_score(self):
        score_text = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.display.blit(score_text, [0, 0])

    def game_over(self):
        over_text = self.font.render("Game Over! Score: " + str(self.score), True, (255, 0, 0))
        self.display.blit(over_text, [self.screen_width // 6, self.screen_height // 3])
        pygame.display.update()
        pygame.time.wait(2000)
        self.reset()

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "RIGHT":
            head_x += self.block_size
        elif self.direction == "LEFT":
            head_x -= self.block_size
        elif self.direction == "UP":
            head_y -= self.block_size
        elif self.direction == "DOWN":
            head_y += self.block_size

        if self.wrap_mode:
            head_x %= self.screen_width
            head_y %= self.screen_height

        new_head = (head_x, head_y)
        self.snake.insert(0, new_head)

        # Check if any food is eaten.
        food_eaten = False
        for food in self.foods:
            if new_head == food:
                food_eaten = True
                self.score += 1
                self.foods.remove(food)
                break
        if food_eaten:
            self.foods.append(self.place_food())
        else:
            self.snake.pop()

    def check_collisions(self):
        head = self.snake[0]
        if not self.wrap_mode:
            if head[0] < 0 or head[0] >= self.screen_width or head[1] < 0 or head[1] >= self.screen_height:
                return True
        if head in self.snake[1:]:
            return True
        return False

    def pause_game(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # Pressing P resumes.
                        paused = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.resume_button_rect.collidepoint(pos):
                        paused = False
                    elif self.pause_quit_button_rect.collidepoint(pos):
                        return True  # Quit from pause menu.
            self.display.fill((50, 50, 50))
            pause_text = self.font.render("Paused", True, (255, 255, 255))
            self.display.blit(pause_text, 
                              (self.screen_width//2 - pause_text.get_width()//2, self.screen_height//2 - 50))
            # Draw Resume button.
            pygame.draw.rect(self.display, (0, 200, 0), self.resume_button_rect)
            resume_text = self.font.render("Resume", True, (0, 0, 0))
            self.display.blit(resume_text, 
                              (self.resume_button_rect.x + (self.resume_button_rect.width - resume_text.get_width())//2,
                               self.resume_button_rect.y + (self.resume_button_rect.height - resume_text.get_height())//2))
            # Draw Quit button.
            pygame.draw.rect(self.display, (200, 0, 0), self.pause_quit_button_rect)
            quit_text = self.font.render("Quit", True, (0, 0, 0))
            self.display.blit(quit_text, 
                              (self.pause_quit_button_rect.x + (self.pause_quit_button_rect.width - quit_text.get_width())//2,
                               self.pause_quit_button_rect.y + (self.pause_quit_button_rect.height - quit_text.get_height())//2))
            pygame.display.update()
            self.clock.tick(5)
        return False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break
                    elif event.key == pygame.K_p:
                        # Pause when 'P' is pressed.
                        if self.pause_game():
                            running = False
                            break
                    elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                        self.direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                        self.direction = "RIGHT"
                    elif event.key == pygame.K_UP and self.direction != "DOWN":
                        self.direction = "UP"
                    elif event.key == pygame.K_DOWN and self.direction != "UP":
                        self.direction = "DOWN"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.pause_button_rect.collidepoint(pos):
                        if self.pause_game():
                            running = False
                            break
                    elif self.quit_button_rect.collidepoint(pos):
                        running = False
                        break

            self.move_snake()
            if self.check_collisions():
                self.game_over()

            self.display.fill((0, 0, 0))
            self.draw_snake()
            self.draw_food()
            self.display_score()
            # Draw Pause and Quit buttons.
            pygame.draw.rect(self.display, (100, 100, 100), self.pause_button_rect)
            pause_btn_text = self.font.render("Pause", True, (255, 255, 255))
            self.display.blit(pause_btn_text, (self.pause_button_rect.x + 5, self.pause_button_rect.y + 5))
            pygame.draw.rect(self.display, (100, 100, 100), self.quit_button_rect)
            quit_btn_text = self.font.render("Quit", True, (255, 255, 255))
            self.display.blit(quit_btn_text, (self.quit_button_rect.x + 5, self.quit_button_rect.y + 5))
            pygame.display.update()
            self.clock.tick(self.speed)
        pygame.quit()
        sys.exit()
