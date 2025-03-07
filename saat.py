import pygame
import math
from datetime import datetime

pygame.init()

GENISLIK, YUKSEKLIK = 760, 760
pencere = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
saat1 = pygame.image.load("saat1.png")
saat1 = pygame.transform.scale(saat1, (GENISLIK, YUKSEKLIK))
saat2 = pygame.image.load("saat2.png")
saat2 = pygame.transform.scale(saat2, (GENISLIK, YUKSEKLIK))
saat3 = pygame.image.load("saat3.png")
saat3 = pygame.transform.scale(saat3, (GENISLIK, YUKSEKLIK))
saat4 = pygame.image.load("saat4.png")
saat4 = pygame.transform.scale(saat4, (GENISLIK, YUKSEKLIK))
saat5 = pygame.image.load("saat5.png")
saat5 = pygame.transform.scale(saat5, (GENISLIK, YUKSEKLIK))
x = 0  # Global index for clock face
kadranlar = [saat1, saat2, saat3, saat4, saat5]
class Saat:
    def __init__(self):
        self.merkezx, self.merkezy = GENISLIK / 2, YUKSEKLIK / 2
        self.akrep_uzunluk = 150
        self.yelkovan_uzunluk = 200
        self.saniye_uzunluk = 220
    
    def cizgi_ciz(self, aci, uzunluk, renk, kalinlik):
        radians = math.radians(aci - 90)
        x = self.merkezx + uzunluk * math.cos(radians)
        y = self.merkezy + uzunluk * math.sin(radians)
        pygame.draw.line(pencere, renk, (self.merkezx, self.merkezy), (x, y), kalinlik)

    def guncelle(self):
        saat = datetime.now().hour % 12
        dakika = datetime.now().minute
        saniye = datetime.now().second

        akrep_aci = 30 * saat + dakika * 0.5
        yelkovan_aci = dakika * 6
        saniye_aci = saniye * 6

        self.cizgi_ciz(akrep_aci, self.akrep_uzunluk, (0, 0, 0), 6)
        self.cizgi_ciz(yelkovan_aci, self.yelkovan_uzunluk, (0, 0, 0), 6)
        self.cizgi_ciz(saniye_aci, self.saniye_uzunluk, (0, 0, 0), 3)
    
    def kadrandegistir(self):
        global x
        x += 1
        if x > 4:
            x = 0
        pencere.blit(kadranlar[x], (0,0))

saat = Saat()
durum = True
while durum:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            durum = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                saat.kadrandegistir()
    pencere.blit(kadranlar[x], (0,0))
    saat.guncelle()
    pygame.display.update()
pygame.quit()
