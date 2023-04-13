import random

import pygame

pygame.init()
WIDTH, HEIGHT = 400, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Street Racer v0')
background = pygame.image.load("AnimatedStreet.png")
score_font = pygame.font.SysFont("Verdana", 30)
SCORE = 0
# coin_img = pygame.image.load("Coin2.png")


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load("Coin2.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(0, 350),
            self.rect.height // 2
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randint(0, 350)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(0, WIDTH - self.rect.width),
            self.rect.height // 2,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        global SCORE

        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            SCORE += 1
            self.speed += 5
            self.rect.y = 0
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            # self.rect.y = random.randint()

        # pressed = pygame.key.get_pressed()
        # if pressed[pygame.K_LEFT] and self.rect.x >= self.speed:
        #     self.rect.x -= self.speed
        # if pressed[pygame.K_RIGHT] and self.rect.x + self.rect.width + self.speed <= WIDTH:
        #     self.rect.x += self.speed


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.count_coins = 0
        self.image = pygame.image.load('Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x >= self.speed:
            self.rect.x -= self.speed
        if pressed[pygame.K_RIGHT] and self.rect.x + self.rect.width + self.speed <= WIDTH:
            self.rect.x += self.speed

# def generate_coin_position():
#     x = random.randint(8, 340)
#     y = random.randint(0, 600)
#     return (x, y)

# def draw_coin(surface, pos):
#     surface.blit(coin_img, pos)

def main():
    running = True
    player = Player()
    enemy = Enemy()
    coin = Coin()

    # coins = []
    # coin_spawn_rate = 0.01

    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    enemies.add(enemy)
    coins.add(coin)

    while running:
        SCREEN.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # if random.random() < coin_spawn_rate:
        #     coin_pos = generate_coin_position()
        #     coins.append(pygame.Rect(coin_pos[0], coin_pos[1], 50, 50))

        player.update()
        enemy.update()
        coin.update()

        player.draw(SCREEN)
        enemy.draw(SCREEN)
        coin.draw(SCREEN)

        score = score_font.render(f" Your Score: {str(SCORE)}", True, (0, 0, 0))
        count_coins = score_font.render(str(player.count_coins), True, (0, 0, 0))
        SCREEN.blit(score, (0, 0))
        SCREEN.blit(count_coins, (350, 2))

        
        # for coin in coins:
        #     coin.move_ip(0, 5)
        
        # for coin in coins:
        #     draw_coin(SCREEN, coin)

        if pygame.sprite.spritecollideany(player, enemies):
            running = False

        if pygame.sprite.spritecollideany(player, coins):
            player.count_coins += 1
            coin.rect.y = 0

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()