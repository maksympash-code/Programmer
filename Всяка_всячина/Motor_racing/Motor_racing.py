import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
car_width = 50
car_height = 100
road_width = 400

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
    def __init__(self):
        self.width = car_width
        self.height = car_height
        self.x = random.randint(
            (screen_width - road_width) // 2,
            (screen_width + road_width) // 2 - car_width,
        )
        self.y = -self.height
        self.speed = 5

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, red, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


def check_collision(car, obstacle):
    car_rect = pygame.Rect(car.x, car.y, car_width, car_height)
    obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
    return car_rect.colliderect(obstacle_rect)

def draw_road():
    road_x = (screen_width - road_width) // 2
    pygame.draw.rect(screen, black, (road_x, 0, road_width, screen_height))

def show_score(score):
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

def create_obstacle(obstacles):
    max_attempts = 10
    for i in range(max_attempts):
        new_obstacle = Obstacle()
        if not any(new_obstacle.get_rect().colliderect(ob.get_rect()) for ob in obstacles):
            return new_obstacle
    return None

def game_loop():
    car = Car()
    obstacles = []
    score = 0
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car.move_left()
        if keys[pygame.K_RIGHT]:
            car.move_right()

        if random.randint(1, 30) == 1:
            new_obstacle = create_obstacle(obstacles)
            if new_obstacle:
                obstacles.append(new_obstacle)


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
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

game_loop()
