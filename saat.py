import pygame
import math
from datetime import datetime
pygame.init()
GENISLIK, YUKSEKLIK = 760, 760
pencere = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
arkaplan = pygame.image.load("kedisaat.jpg")
arkaplan = pygame.transform.scale(arkaplan, (GENISLIK, YUKSEKLIK))
akrepuzunluk = 150
yelkovanuzunluk = 200
saniyeuzunluk = 220
merkezx, merkezy = GENISLIK/2, YUKSEKLIK/2
durum = True
while durum:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            durum = False
    pencere.blit(arkaplan, (0,0))
    saat = datetime.now().hour % 12
    dakika = datetime.now().minute
    saniye =  datetime.now().second

    akrep = 30*saat-90 + dakika*0.5
    akrepradians = math.radians(akrep)
    akrepx = merkezx + akrepuzunluk*math.cos(akrepradians)
    akrepy = merkezy + akrepuzunluk*math.sin(akrepradians)

    yelkovan = dakika*6-90
    yelkovanradians = math.radians(yelkovan)
    yelkovanx = merkezx+yelkovanuzunluk*math.cos(yelkovanradians)
    yelkovany = merkezy + yelkovanuzunluk*math.sin(yelkovanradians)

    saniyeibresi = saniye*6-90
    saniyeradians = math.radians(saniyeibresi)
    saniyex = merkezx + saniyeuzunluk*math.cos(saniyeradians)
    saniyey = merkezy + saniyeuzunluk*math.sin(saniyeradians)
    
    pygame.draw.line(pencere, (0,0,0), (merkezx, merkezy), (akrepx, akrepy), 7)
    pygame.draw.line(pencere, (0,0,0), (merkezx, merkezy), (yelkovanx, yelkovany), 7)
    pygame.draw.line(pencere, (0,0,0), (merkezx, merkezy), (saniyex, saniyey), 3)
    pygame.display.update()
pygame.quit()
