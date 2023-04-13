
import pygame
pygame.init()
sc = pygame.display.set_mode((800, 450))
sc.fill((255, 255, 255))
pygame.display.flip()

color = (0, 0, 0)
rad = 10
stDraw = False
spos = None
tool = 3

f1 = pygame.font.SysFont('serif', 30)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rad -= 2
            elif event.key == pygame.K_RIGHT:
                rad += 2
            elif event.key == pygame.K_w:
                color = (200, 0, 0)
            elif event.key == pygame.K_r:
                color = (0, 0, 200)
            elif event.key == pygame.K_q:
                color = (0, 0, 0)
            elif event.key == pygame.K_e:
                color = (0, 200, 0)
            elif event.key == pygame.K_a:
                tool = 1
            elif event.key == pygame.K_s:
                tool = 2
            elif event.key == pygame.K_d:
                tool = 3
            elif event.key == pygame.K_f:
                tool = 4
            elif event.key == pygame.K_g:
                sc.fill((255, 255, 255))
                pygame.display.update()

        if tool == 2:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                stDraw = True
                spos = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if stDraw:
                    pos = event.pos

                    w = pos[0] - spos[0]
                    h = pos[1] - spos[1]

                    pygame.draw.rect(sc, color, (spos[0], spos[1], w, h))
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                stDraw = False

        if tool == 1:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                stDraw = True
                spos = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if stDraw:
                    pos = event.pos

                    w = pos[0] - spos[0]
                    h = pos[1] - spos[1]

                    pygame.draw.circle(sc, color, (spos[0], spos[1]), w//2)
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                stDraw = False

        if tool == 3:
            mouse_press = pygame.mouse.get_pressed()
            if mouse_press[0]:
                mPos = pygame.mouse.get_pos()
                pygame.draw.circle(sc, color, mPos, rad)
                pygame.display.flip()

        if tool == 4:
            mouse_press = pygame.mouse.get_pressed()
            if mouse_press[0]:
                mPos = pygame.mouse.get_pos()
                pygame.draw.circle(sc, (255, 255, 255), mPos, rad)
                pygame.display.flip()

        pygame.draw.rect(sc, (240, 240, 0), (0, 0, 140, 60))
        text1 = f1.render("Tool: " + str(tool), False, (0, 0, 0))
        sc.blit(text1, (0, 0))
        text2 = f1.render("Radius: " + str(rad), False, (0, 0, 0))
        sc.blit(text2, (0, 30))
        pygame.display.update()