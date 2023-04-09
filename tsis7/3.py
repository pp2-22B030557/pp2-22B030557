import pygame

# Initialize Pygame
pygame.init()

# Set screen size
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Set background color
bg_color = (255, 255, 255)

# Set ball size and color
ball_size = 50
ball_color = (255, 0, 0)

# Set ball position and speed
ball_pos = [screen_width // 2, screen_height // 2]
ball_speed = 20

# Define function to draw ball
def draw_ball():
    pygame.draw.circle(screen, ball_color, ball_pos, ball_size // 2)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_pos[1] -= ball_speed
            elif event.key == pygame.K_DOWN:
                ball_pos[1] += ball_speed
            elif event.key == pygame.K_LEFT:
                ball_pos[0] -= ball_speed
            elif event.key == pygame.K_RIGHT:
                ball_pos[0] += ball_speed

    # Keep ball on screen
    if ball_pos[0] < ball_size // 2:
        ball_pos[0] = ball_size // 2
    elif ball_pos[0] > screen_width - ball_size // 2:
        ball_pos[0] = screen_width - ball_size // 2
    if ball_pos[1] < ball_size // 2:
        ball_pos[1] = ball_size // 2
    elif ball_pos[1] > screen_height - ball_size // 2:
        ball_pos[1] = screen_height - ball_size // 2

    # Clear screen
    screen.fill(bg_color)

    # Draw ball
    draw_ball()

    # Update screen
    pygame.display.update()

# Quit Pygame
pygame.quit()