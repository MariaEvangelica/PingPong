import pygame

pygame.init()
display = pygame.display.set_mode((1000,700))
pygame.display.set_caption("PING!")
background=pygame.image.load("bg7.jpg")
display.blit(background,(0,0))
start=pygame.image.load("START1.png")
display.blit(start,(700,200))

setting=pygame.image.load("SETTING1.png")
display.blit(setting,(700,400))

judul=pygame.image.load("ping1.png")
display.blit(judul,(50,-80))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            if 700<pos[0]<950 and 200<pos[1]<300:

                import pygame

                pygame.init()
                display = pygame.display.set_mode((950, 570))
                pygame.display.set_caption("PING!")

                background = pygame.image.load("bg7.jpg")
                display.blit(background, (0, 0))

                bola = pygame.image.load("raket1.png")
                display.blit(bola, (0, 250))

                bola = pygame.image.load("raket2.png")
                display.blit(bola, (830, 250))

                bola = pygame.image.load("bolatenis1.png")
                display.blit(bola, (90, 270))

                exit = pygame.image.load("exit2.png")
                display.blit(exit, (0, 0))

            elif 0 < pos[0] < 100 and 0 < pos[1] < 100:
                import pygame

                pygame.init()
                display = pygame.display.set_mode((1000, 700))
                pygame.display.set_caption("PING!")

                background = pygame.image.load("bg.jpg")
                display.blit(background, (0, 0))

                start = pygame.image.load("START1.png")
                display.blit(start, (700, 200))

                setting = pygame.image.load("SETTING1.png")
                display.blit(setting, (700, 400))

                judul = pygame.image.load("ping1.png")
                display.blit(judul, (50, -80))

                done = False
                while not done:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            if 700 < pos[0] < 950 and 200 < pos[1] < 300:

                                import pygame

                                pygame.init()
                                display = pygame.display.set_mode((950, 570))
                                pygame.display.set_caption("PING!")

                                background = pygame.image.load("bg7.jpg")
                                display.blit(background, (0, 0))

                                bola = pygame.image.load("raket1.png")
                                display.blit(bola, (0, 250))

                                bola = pygame.image.load("raket2.png")
                                display.blit(bola, (830, 250))

                                bola = pygame.image.load("bolatenis1.png")
                                display.blit(bola, (90, 270))

                                exit = pygame.image.load("exit2.png")
                                display.blit(exit, (10, 10))



                            elif 720 < pos[0] < 925 and 400 < pos[1] < 490:
                                import pygame

                                pygame.init()
                                display = pygame.display.set_mode((700, 400))
                                pygame.display.set_caption("PING!")

                                background = pygame.image.load("bg6.png")
                                display.blit(background, (0, 0))

                                set = pygame.image.load("gui.jpg")
                                display.blit(set, (160, 150))

                                set2 = pygame.image.load("sound.jpg")
                                display.blit(set2, (160, 250))

                                set3 = pygame.image.load("setting2.png")
                                display.blit(set3, (300, 30))

                        pygame.display.update()




            elif 720 < pos[0] < 925 and 400 < pos[1] < 490:
                import pygame

                pygame.init()
                display = pygame.display.set_mode((700, 400))
                pygame.display.set_caption("PING!")

                background = pygame.image.load("bg6.png")
                display.blit(background, (0, 0))

                set = pygame.image.load("gui.jpg")
                display.blit(set, (160, 150))

                set2 = pygame.image.load("sound.jpg")
                display.blit(set2, (160, 250))

                set3 = pygame.image.load("setting2.png")
                display.blit(set3, (300, 30))






        pygame.display.update()

