import pygame
import os

pygame.init()

win = pygame.display.set_mode((500, 500))

music_files = ["DVRST - Close Eyes (256  kbps).mp3", "DVRST - Close Eyes (256  kbps).mp3", "DVRST - Close Eyes (256  kbps).mp3"]
current_song_index = 0

def play_music():
    pygame.mixer.music.load(music_files[current_song_index])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(music_files)
    play_music()

def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(music_files)
    play_music()

font = pygame.font.Font(None, 36)

play_text = font.render("PLAY", True, (255, 255, 255))
stop_text = font.render("STOP", True, (255, 255, 255))
next_text = font.render("NEXT", True, (255, 255, 255))
prev_text = font.render("PREV", True, (255, 255, 255))

play_rect = play_text.get_rect(center=(125, 250))
stop_rect = stop_text.get_rect(center=(250, 250))
next_rect = next_text.get_rect(center=(375, 250))
prev_rect = prev_text.get_rect(center=(250, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                prev_song()

    pygame.draw.rect(win, (0, 255, 0), play_rect)
    pygame.draw.rect(win, (255, 0, 0), stop_rect)
    pygame.draw.rect(win, (0, 0, 255), next_rect)
    pygame.draw.rect(win, (255, 255, 0), prev_rect)

    win.blit(play_text, play_rect)
    win.blit(stop_text, stop_rect)
    win.blit(next_text, next_rect)
    win.blit(prev_text, prev_rect)

    pygame.display.update()