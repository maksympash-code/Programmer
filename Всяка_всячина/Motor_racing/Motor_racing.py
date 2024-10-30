import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
car_width = 50
car_height = 100
road_width = 400
num_columns = 4
column_width = road_width // num_columns

fps = 60

white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
red = (255, 0, 0)

car_img = pygame.image.load('car.png')
car_img = pygame.transform.scale(car_img, (car_width, car_height))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Motor Racing")

font = pygame.font.SysFont("Arial", 36)

class Car:
    def __init__(self):
        self.image = car_img
        self.x = (screen_width - car_width) // 2
        self.y = (screen_height - car_height) - 10
        self.speed = 5

    def move_left(self):
        if self.x > (screen_width - road_width) // 2:
            self.x -= self.speed

    def move_right(self):
        if self.x < (screen_width + road_width) // 2 - car_width:
            self.x += self.speed

    def draw_car(self):
        screen.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, column, speed):
        self.width = column_width - 10
        self.height = car_height
        self.x = (screen_width - road_width) // 2 + column * column_width + 5
        self.y = -self.height
        self.speed = speed

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, red, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

def check_collision(car, obstacle):
    car_rect = pygame.Rect(car.x, car.y, car_width, car_height)
    return car_rect.colliderect(obstacle.get_rect())

def draw_road():
    road_x = (screen_width - road_width) // 2
    pygame.draw.rect(screen, black, (road_x, 0, road_width, screen_height))

def show_score(score):
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

def create_obstacles(speed):
    free_columns = list(range(num_columns))
    random.shuffle(free_columns)

    num_obstacles = random.choice([2, 3])  # Інколи генеруємо 3 перешкоди
    obstacles = []

    for _ in range(num_obstacles):
        column = free_columns.pop()
        obstacles.append(Obstacle(column, speed))

    return obstacles

def game_loop():
    car = Car()
    obstacles = []
    score = 0
    clock = pygame.time.Clock()
    running = True
    obstacle_timer = 0
    obstacle_speed = 5
    speed_increase_interval = 5000
    last_speed_increase = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car.move_left()
        if keys[pygame.K_RIGHT]:
            car.move_right()

        current_time = pygame.time.get_ticks()
        if current_time - last_speed_increase >= speed_increase_interval:
            obstacle_speed += 0.5  # Збільшуємо швидкість на 0.5
            last_speed_increase = current_time

        if obstacle_timer <= 0 and len(obstacles) < 4:
            new_obstacles = create_obstacles(obstacle_speed)
            obstacles.extend(new_obstacles)
            obstacle_timer = 120

        screen.fill(gray)
        draw_road()
        car.draw_car()

        for obstacle in obstacles[:]:
            obstacle.move()
            obstacle.draw()

            if obstacle.y > screen_height:
                obstacles.remove(obstacle)
                score += 1

            if check_collision(car, obstacle):
                print("Аварія! Гра закінчена.")
                running = False

        show_score(score)

        obstacle_timer -= 1
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

game_loop()
