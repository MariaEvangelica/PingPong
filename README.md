# PingPong
python code for ALPRO project
import pygame
import sys
import math
import random
from pygame.locals import*

pygame.init()
pygame.mixer.pre_init(11025, -16, 2, 256)
pygame.mixer.init()
 
# FPS
 
FPS      = 30
fpsClock = pygame.time.Clock()
 
# Warna
 
HITAM    = (0,   0,   0)
PUTIH    = (255, 255, 255)
MERAH    = (255,   0,   0)
HIJAU    = (0, 255,   0)
BIRU     = (0,   0, 255)
COKLAT   = (128,  64,  64)
UNGU     = (138, 43,  226)
SIENA    = (255, 130, 71)
 
# Konstanta2 tetap
 
LAYAR_X  = 500
LAYAR_Y  = 600
 
ATAS     = "atas"
BAWAH    = "bawah"
KANAN    = "kanan"
KIRI     = "kiri"
 
BESAR    = "besar"
SEDANG   = "sedang"
KECIL    = 'kecil'
 
phi      = math.pi
 
posisi_garis_tengah_awal  = (0, LAYAR_Y / 2)
posisi_garis_tengah_akhir = (LAYAR_X, LAYAR_Y / 2)
 
# Variabel2 untuk permainan
 
ukuran_zona_mati      = 50
jarak_zona_papan      = 10
 
kecepatan_gerak_papan = 10
warna_player_1        = BIRU
warna_player_2        = HIJAU
jarak_text_skor       = 20
 
kecepatan_bola        = 6
percepatan_bola       = 8 / 10
konstanta_kemiringan_pantul = phi/5  # Jarak simpangan  maks, 39 derajat
 
 
# WINDOWS
 
WARNA_BACKGROUND = PUTIH
LAYAR            = pygame.display.set_mode((LAYAR_X, LAYAR_Y), 0, 32)
pygame.display.set_caption("Pong!")
 
# Font
 
fontObj               = pygame.font.SysFont('ComicSans.ttf', 50)
fontObjKecil          = pygame.font.SysFont('ComicSans.ttf', 25)
fontObjLebihKecilLagi = pygame.font.SysFont("system/Arial.ttf", 20)
 
jalan = True
 
""" Jangan dipakai dulu!
# Persuaraan
 
Daftar_Musik     = ["sound1.ogg", "sound2.ogg", "sound3.ogg", "sound4.ogg", "sound5.ogg", "sound6.ogg"]
#Suara_Mantul = pygame.mixer.Sound("BolaMantul.wav")
Suara_Cetak_Skor = pygame.mixer.Sound("CetakSkor.ogg")
Suara_Menang     = pygame.mixer.Sound("Menang.ogg")
Musik_Sekarang   = None
"""
 
def tabrakan_bola_papan(bola, papan):
    # Ngecek apakah bola nabrak sama papan dan lalu ngitung sudut pantulnya
 
    if papan.y - bola.radius <= bola.y <= (papan.y + papan.tebal + bola.radius):
        if papan.x - bola.radius/2 <= bola.x <= (papan.x + papan.panjang) + bola.radius/2:
            # Ngambil posisi jatuhnya bola di papan x, kemungkinan letak jatuhnya pada bagian papan -> -5 ... 0 ... 5
            posisi = bola.x - papan.x
            posisi /= 10
            posisi -= 5
 
            # Maks kemiringan
            if posisi != 0:
                kemiringan = (posisi/5) * konstanta_kemiringan_pantul
            else:
                kemiringan = 0
 
            if papan.posisi == ATAS:
                # Gak begitu yakin kenapa ini bisa kerja, tapi hasilnya bagus kok
                bola.y     = 2*(bola.radius + papan.y + papan.tebal) - bola.y
                bola.sudut = -(bola.sudut) + kemiringan
            else:
                bola.y     = 2*(papan.y - bola.radius) - bola.y
                bola.sudut = -(bola.sudut) - kemiringan
 
 
 
def pemenang(player):
    # Tulisan "Player" Menang
    teks               = player.nama + " Menang!"
    winTeks            = fontObj.render(teks, True, player.warna)
    winTeksRect        = winTeks.get_rect()
    winTeksRect.center = (int(LAYAR_X / 2), int(LAYAR_Y / 2))
 
    # Kotak di sekitar tulisan "Pemenang"
    margin             = 15
    winRect            = winTeks.get_rect()
    winRect.center     = (int(LAYAR_X / 2), int(LAYAR_Y / 2))
    # Perluas kotaknyaaa
    winRect.x          -= margin
    winRect.y          -= margin
    winRect.width      += 2*margin
    winRect.height     += 2*margin
 
    winRect.x += 10
    winRect.y -= 10
    pygame.draw.rect(LAYAR, PUTIH, winRect)
    pygame.draw.rect(LAYAR, HITAM, (winRect), 5)
 
    winRect.x -= 10
    winRect.y += 10
    pygame.draw.rect(LAYAR, PUTIH, winRect)
    pygame.draw.rect(LAYAR, HITAM, (winRect), 5)
    LAYAR.blit(winTeks, winTeksRect)
 
    # Suara_Menang.play()
 
 
def pause_game():
    # Teks Pause
    teks                 = "PAUSE"
    pauseTeks            = fontObj.render(teks, True, MERAH)
    pauseTeksRect        = pauseTeks.get_rect()
    pauseTeksRect.center = (int (LAYAR_X/2), int(LAYAR_Y/4))
 
    # Teks keteranngan
    teks                 = "Tekan P untuk melanjutkan"
    insTeks              = fontObjKecil.render(teks, True, HITAM)
    insTeksRect          = insTeks.get_rect()
    insTeksRect.center   = (int (LAYAR_X/2), int(LAYAR_Y/4) + 50)
 
    # Frame
    frame = pygame.Rect(10, 10, 300, 100)
    frame.center = (int (LAYAR_X/2), int(LAYAR_Y/4) + 25)
    pygame.draw.rect(LAYAR, PUTIH, frame)
    pygame.draw.rect(LAYAR, MERAH, frame, 5)
 
    LAYAR.blit(pauseTeks, pauseTeksRect)
    LAYAR.blit(insTeks, insTeksRect)
 
def instruksi():
    # Ini untuk layar intro setelah game baru jalan
    LAYAR.fill(WARNA_BACKGROUND)
 
    margin = 25
 
    # Inisialisasi Teks
    judul     = Teks("PyPong", UNGU, margin+20, 50, BESAR)
    judul.init_frame(20, HITAM)
    judul.gambar_frame()
 
    pencipta   = Teks("Oleh: Agnes, Katia, Dean", SIENA, 220, 75, SEDANG)
    pencipta.underline()
 
    kalimat_1  = Teks("Game clone Pong dengan menggunakan Python"           , HITAM, margin, 120, SEDANG)
    kalimat_2  = Teks("Cara Bermain :"                                      , HITAM, margin, 150, SEDANG)
    kalimat_3  = Teks("Kendalikan papan dengan menggunakan tombol"          , HITAM, margin*2, 180, KECIL)
    kalimat_4  = Teks("Panah Kanan dan Kiri - Player 1"                     , warna_player_1, margin*2, 200, KECIL)
    kalimat_5  = Teks("Tombol \"A\" dan \"D\"    - Player 2"                , warna_player_2, margin*2, 220, KECIL)
    kalimat_6  = Teks("Pause game dengan \"P\""                             , HITAM, margin*2, 250, KECIL)
    kalimat_7  = Teks("Menang -> skor lebih dari 5, dan"                    , HITAM, margin, 330, SEDANG)
    kalimat_8  = Teks("          skor lebih banyak 2 point dari pemain lain", HITAM, 3*margin-3, 360, SEDANG)
    kalimat_9  = Teks("Selamat bermain!"                                    , HITAM, margin, 400, SEDANG)
    kalimat_10 = Teks("Tekan sembarang tombol untuk melanjutkan..."         , MERAH, margin, 500, SEDANG)
 
 
 
class Teks:
    def __init__(self, teks, warna, x, y, ukuran, tampil = True):
        self.teks  = teks
        self.warna = warna
        self.x     = x
        self.y     = y
 
        if ukuran == BESAR:
            self.teksObj = fontObj.render(self.teks, True, self.warna)
        elif ukuran == SEDANG:
            self.teksObj = fontObjKecil.render(self.teks, True, self.warna)
        if ukuran == KECIL:
            self.teksObj = fontObjLebihKecilLagi.render(self.teks, True, self.warna)
 
        self.rect   = self.teksObj.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_warna  = self.warna
 
        if tampil == True:
            LAYAR.blit(self.teksObj, self.rect)
 
    def gambar(self):
        LAYAR.blit(self.teksObj, self.rect)
 
    def init_frame(self, margin, warna = HITAM):
        self.rect.x      -= margin
        self.rect.y      -= margin
        self.rect.height += 2*margin
        self.rect.width  += 2*margin
        self.rect_warna   = warna
 
    def gambar_frame(self):
        pygame.draw.rect(LAYAR, self.rect_warna, self.rect, 5)
 
    def underline(self, warna = HITAM):
        pygame.draw.line(LAYAR, warna, (self.x, self.y+15), (self.x+self.rect.width, self.y+15), 2)
 
 
 
class Zona_Mati:
 
    def __init__(self, letak, tinggi):
        self.x = 0
        if letak == "atas":
            self.y  = 0
        if letak == "bawah":
            self.y  = LAYAR_Y - tinggi
        self.warna  = MERAH
        self.tinggi = tinggi
 
        self.letak  = letak
 
    def gambar(self):
        pygame.draw.rect(LAYAR, self.warna, pygame.Rect(self.x, self.y, LAYAR_X, self.tinggi))
 
 
class Papan:
 
    def __init__(self, letak, warna):
        self.panjang = 100
        self.tebal   = 20
        self.x       = LAYAR_X / 2 - self.panjang / 2
 
        # Nentuin posisi Y
        if letak == ATAS:
            self.y   = ukuran_zona_mati + jarak_zona_papan
        elif letak == BAWAH:
            self.y   = LAYAR_Y - ukuran_zona_mati - jarak_zona_papan - self.tebal
 
        self.warna   = warna
        self.posisi  = letak
 
        # Gerakan papan
        self.gerakan = None
 
        # Kode2 untuk nampilin skor Player
        self.skor    = 0
 
        self.textSkor = str(self.skor)
        self.textObj  = fontObj.render(self.textSkor, True, self.warna)
        self.text_x   = jarak_text_skor
        if letak == ATAS:
            self.nama       = "Player 2"
            self.text_y     = LAYAR_Y / 2 - 2 * jarak_text_skor
            self.textNama_y = self.text_y - 25
        elif letak == BAWAH:
            self.nama       = "Player 1"
            self.text_y     = LAYAR_Y / 2 + jarak_text_skor
            self.textNama_y = self.text_y + 45
 
        self.textNama     = str(self.nama)
        self.textNamaObj  = fontObjKecil.render(self.textNama, True, self.warna)
        # self.textNama_x = LAYAR_X - jarak_text_skor - self.textNamaObj.get_width()
        self.textNama_x   = self.text_x
 
 
    def gambar(self):
        # Tampilin papan
        pygame.draw.rect(LAYAR, self.warna, pygame.Rect(self.x, self.y, self.panjang, self.tebal))
 
        # Untuk nggambar garis2 di papan, code testing
        """
        for posisi in range(0, self.panjang+1, 10):
            pygame.draw.line(LAYAR, HITAM, (self.x + posisi, self.y), (self.x + posisi, self.y + self.tebal - 1), 2)
        """
 
        # Tampilin skor
        if self.textSkor != str(self.skor):
            self.textSkor = str(self.skor)
            self.textObj  = fontObj.render(self.textSkor, True, self.warna)
        LAYAR.blit(self.textObj, (self.text_x, self.text_y))
 
        # Tampilin nama player
        LAYAR.blit(self.textNamaObj, (self.textNama_x, self.textNama_y))
 
    def gerak(self, arah):
        if 0 < self.x < LAYAR_X - self.panjang:
            if arah == KANAN:
                self.x += kecepatan_gerak_papan
            elif arah == KIRI:
                self.x -= kecepatan_gerak_papan
        else:
            self.gerakan = None
            if self.x <= 0:
                self.x = 1
            elif self.x >= LAYAR_X - self.panjang:
                self.x = LAYAR_X - self.panjang - 1
 
 
class Ball:
 
    def __init__(self):
        self.x          = int(LAYAR_X / 2)
        self.y          = int(LAYAR_Y / 2)
        self.radius     = 12
        self.warna      = HITAM
 
        self.kecepatan  = kecepatan_bola
        self.percepatan = percepatan_bola
        self.sudut      = 1 * phi / 2
 
    def gambar(self):
        pygame.draw.circle(LAYAR, self.warna, (self.x, self.y), self.radius)
 
    def gerak(self):
        self.x += int(math.cos(self.sudut) * self.kecepatan)
        self.y -= int(math.sin(self.sudut) * self.kecepatan)
        if self.kecepatan < 100:
            self.kecepatan += self.percepatan / FPS
 
    def reset(self, arah=BAWAH):
        # Untuk mereset arah & kecepatan bola, kalau habis ada yg nyetak
        # skor...
        self.x = int(LAYAR_X / 2)
        self.y = int(LAYAR_Y / 2)
        self.kecepatan = kecepatan_bola
        if arah == BAWAH:
            self.sudut = 3 * phi / 2
        elif arah == ATAS:
            self.sudut = 1 * phi / 2
 
        # Suara_Cetak_Skor.play()
 
    def pantul_tembok(self):
        if self.x <= 0 + self.radius:
            self.x = 2 * self.radius - self.x
            self.sudut = -(self.sudut) - phi
        elif self.x >= LAYAR_X - self.radius:
            self.x = 2 * (LAYAR_X - self.radius) - self.x
            self.sudut = -(self.sudut) - phi
 
        elif self.y <= 0 + self.radius:
            self.y = 2 * self.radius - self.y
            self.sudut = -(self.sudut)
        elif self.y >= LAYAR_Y - self.radius:
            self.y = 2 * (LAYAR_Y - self.radius) - self.y
            self.sudut = -(self.sudut)
 
# Inisialisasi
 
# Zona Kematian
 
Zona_Bawah     = Zona_Mati(BAWAH, ukuran_zona_mati)
Zona_Atas      = Zona_Mati(ATAS, ukuran_zona_mati)
list_zona_mati = [Zona_Bawah, Zona_Atas]
 
# Pemain
 
Player_1       = Papan(BAWAH, warna_player_1)
Player_2       = Papan( ATAS, warna_player_2)
list_player    = [Player_1, Player_2]
 
# Bola
 
Bola    = Ball()
 
# Game
 
menang  = None
pause   = False
intro   = True
counter = 0      # Untuk ngekeep.. ah ngejelasinnya susah, pokoknya ini penting.
                 # Biar klo masuk ke game state khusus (pause, menang), gak ngeloop berlebihan
 
"""
    +===========================+
    |                           |
    |    Game Mulai dari sini   |
    |                           |
    +===========================+
"""
while jalan:

    # Input2 dari Keyboard
    for event in pygame.event.get():
        if event.type == QUIT:
            jalan = False
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            intro = False # Sembarang tombol untuk keluar dari menu Intro

            # Kontrol Player 1
            if event.key == K_RIGHT:
                Player_1.gerakan = KANAN
            elif event.key == K_LEFT:
                Player_1.gerakan = KIRI

            # Kontrol Player 2
            elif event.key == K_a:
                Player_2.gerakan = KIRI
            elif event.key == K_d:
                Player_2.gerakan = KANAN

            # Kontrol game

            elif event.key == K_r:
                Bola.reset()
            elif event.key == K_t:
                Player_1.skor += 100
            elif event.key == K_p:
                pause = False if (pause is True) else True
                if pause:
                    counter = 0

        elif event.type == KEYUP:
            if event.key == K_RIGHT and Player_1.gerakan == KANAN:
                Player_1.gerakan = None
            elif event.key == K_LEFT and Player_1.gerakan == KIRI:
                Player_1.gerakan = None

            elif event.key == K_d and Player_2.gerakan == KANAN:
                Player_2.gerakan = None
            elif event.key == K_a and Player_2.gerakan == KIRI:
                Player_2.gerakan = None

    # Intro awal
    if intro:
        if counter == 0:
            instruksi()
            counter = 1

    # Jika udah ada yg menang
    elif menang:
        if counter == 0:
            pemenang(menang)
            counter = 1

    # Untuk mempause game
    elif pause and not intro:
        if counter == 0:
            pause_game()
            counter = 1


    # Kalau permainannya belum selesai, jalanin game secara normal
    elif not menang and not pause:
        LAYAR.fill(WARNA_BACKGROUND)

         # Garis tengah
        pygame.draw.line   (LAYAR, COKLAT, (posisi_garis_tengah_awal), (posisi_garis_tengah_akhir), 1)
        pygame.draw.circle (LAYAR, COKLAT, (int(LAYAR_X / 2), int(LAYAR_Y / 2)), 20)

        # Kode untuk player/papan
        for player in list_player:
            player.gambar()
            if player.gerakan:
                player.gerak(player.gerakan)

            if Bola.y < 2*ukuran_zona_mati or Bola.y > LAYAR_Y - 2*ukuran_zona_mati:
                tabrakan_bola_papan(Bola, player)


        # Kode untuk zona kematian
        for zona in list_zona_mati:
            zona.gambar()

            if zona.y - Bola.radius <= Bola.y <= zona.y + ukuran_zona_mati + Bola.radius:
                # Ngecek apakah bolanya udah masuk ke zona
                # Sekalian ngecek udah ada skor yg menang belum

                # Skor untuk Player_1
                if zona.letak == ATAS:
                    Player_1.skor += 1
                    if Player_1.skor > 5 and Player_1.skor > Player_2.skor + 2:
                        menang  = Player_1
                        counter = 0
                        break
                    Bola.reset(BAWAH)

                # Skor untuk Player_2
                elif zona.letak == BAWAH:
                    Player_2.skor += 1
                    if Player_2.skor > 5 and Player_2.skor > Player_1.skor + 2:
                        menang  = Player_2
                        counter = 0
                        break
                    Bola.reset(ATAS)


        # Kode untuk bolanya
        Bola.gerak()
        Bola.pantul_tembok()
        Bola.gambar()
 
    pygame.display.update()
    fpsClock.tick(FPS)
