import pygame
pygame.init()
genislik, yukseklik = 680, 680
pencere = pygame.display.set_mode((genislik, yukseklik))
palet = pygame.image.load("palet.png")
palet = pygame.transform.scale(palet, (150, 150))
paletrect = palet.get_rect()
paletrect.x, paletrect.y = 5, yukseklik-paletrect.height
durum = True
ciziyor = False
baslangic = None
renk = (0,0,0)
pencere.fill((255,255,255))
kalinlik = 4
while durum:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x, mouse_y)
    for ebrar in pygame.event.get():
        if ebrar.type == pygame.QUIT:
            durum = False
        if ebrar.type == pygame.MOUSEBUTTONDOWN:
            ciziyor = True
            baslangic = ebrar.pos
            if paletrect.collidepoint(mouse_x, mouse_y):
                if 25 <= mouse_x <= 46 and 598 <= mouse_y <= 618:
                    renk = (255,0,0)
                elif 83 <= mouse_x <= 102 and 586 <= mouse_y <= 606:
                    renk = (0,0,0)
                elif 43 <= mouse_x <= 62 and 571 <= mouse_y <= 590:
                    renk = (255,165,0)
                elif 70 <= mouse_x <= 89 and 553 <= mouse_y <= 574:
                    renk = (255,255,0)
                elif 101 <= mouse_x <= 123 and 552 <= mouse_y <= 574:
                    renk = (0,255,0)
                elif 121 <= mouse_x <= 140 and 579 <= mouse_y <= 597:
                    renk = (0,255,255)
                elif 111 <= mouse_x <= 128 and 608 <= mouse_y <= 628:
                    renk = (0,0,255)
                elif 79 <= mouse_x <= 100 and 620 <= mouse_y <= 640:
                    renk = (128,0,128)
            if 20 <= mouse_x <= 80 and 20 <= mouse_y <= 80:
                kalinlik = 10
            elif 25 <= mouse_x <= 75 and 95 <= mouse_y <= 145:
                kalinlik = 8
            elif 30 <= mouse_x <= 70 and 160 <= mouse_y <= 200:
                kalinlik = 6
            elif 35 <= mouse_x <= 65 and 215 <= mouse_y <= 245:
                kalinlik = 4

        if ebrar.type == pygame.MOUSEBUTTONUP:
            ciziyor = False
            baslangic = ebrar.pos
            
        if ebrar.type ==  pygame.MOUSEMOTION and ciziyor:
            pygame.draw.line(pencere, renk, baslangic, ebrar.pos, kalinlik)
            baslangic = ebrar.pos
            
    pygame.draw.circle(pencere, (0,0,0), (50, 50), 30, 0)
    pygame.draw.circle(pencere, (0,0,0), (50, 120), 25, 0)
    pygame.draw.circle(pencere, (0,0,0), (50, 180), 20, 0)
    pygame.draw.circle(pencere, (0,0,0), (50, 230), 15, 0)
    
    pencere.blit(palet, paletrect)
    pygame.display.update()
pygame.quit()
