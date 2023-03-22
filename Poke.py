# Importamos aqui a biblioteca time, para utilizar funçoes como o sleep e deley.

import time

# Importamos aqui a biblioteca pygame:

import pygame

pygame.init ( )


# Aqui criamos a classe Janela, sendo ela a nossa tela do jogo.

class Janela :
    __altura = 0
    __largura = 0
    __cor = (0 , 0 , 0)

    def __init__ ( self , altura , largura ) :
        self.__altura = altura
        self.__largura = largura

    # Esta funçao retorna as dimençoes da tela.
    def get_dimensoes ( self ) :
        return (self.__altura , self.__largura)

    # E aqui é retornado a cor utilizada.
    def get_cor ( self ) :
        return self.__cor


# Damoms então as dimençoes para se criar a tela, sendo respectivamente largura e altura.
j = Janela ( 800 , 600 )

janela = pygame.display.set_mode ( j.get_dimensoes ( ) )  # criando a janela

pygame.display.set_caption ( 'PokePy' )  # dando um nome à janela

janela.fill ( j.get_cor ( ) )  # colorindo a janela


# Nesta classe é definido os pokemons, assim como seu dano, vida, PP, etc.

class Pokemon :
    nome = None
    vida = 0
    ataque1 = None
    dano1 = 0
    pp1 = 0
    ataque2 = None
    dano2 = 0
    pp2 = 0
    ataque3 = None
    dano3 = 0
    pp3 = 0
    ataque4 = None
    dano4 = 0
    pp4 = 0
    frente = None
    costa = None
    potion = 0
    bigmac = 0
    combo = 0

    # E aqui a função construtora, que posteriormente ira receber cada valor desses atributos.

    def __init__ ( self , nome , vida , ataque1 , dano1 , pp1 , ataque2 , dano2 , pp2 , ataque3 , dano3 , pp3 ,
                   ataque4 , dano4 ,
                   pp4 , frente , costa , potion, bigmac, combo ) :
        self.nome = nome
        self.vida = vida
        self.ataque1 = ataque1
        self.dano1 = dano1
        self.pp1 = pp1
        self.ataque2 = ataque2
        self.dano2 = dano2
        self.pp2 = pp2
        self.ataque3 = ataque3
        self.dano3 = dano3
        self.pp3 = pp3
        self.ataque4 = ataque4
        self.dano4 = dano4
        self.pp4 = pp4
        self.frente = frente
        self.costa = costa
        self.potion = potion
        self.bigmac = bigmac
        self.combo = combo

    def ataca ( self , pokemon , dano ) :
        pokemon.vida -= dano

# E aqui é passado as informaçãos sobre cada pokemon utilizado.

pokemon1 = Pokemon ( 'BULBASAUR' , 150 , 'TACKLE' , 5 , 10 , 'VINE WHIP' , 7 , 10 , 'SEED BOMB' , 55 , 10 ,
                     'SLUDGE BOMB' , 80 , 10 ,
                     "bulbasaur_f.png" , "bulbasaur_c.png", 3, 2, 1)

pokemon2 = Pokemon ( 'CHARIZARD' , 150 , 'DRAGON CLAW' , 50 , 10 , 'FIRE BLAST' , 10 , 10 , 'OVERHEAT' , 16 , 10 ,
                     'FLAMETHROWER' ,
                     70 , 10 , "charizard_f.png" , "charizard_c.png" , 3, 2, 1 )

pokemon3 = Pokemon ( 'CHARMANDER' , 150 , 'GROWL' , 50 , 10 , 'FLAME BURST' , 10 , 10 , 'FIRE FANG' , 16 , 10 ,
                     'METAL CLAW' ,
                     70 , 10 , "charmander_f.png" , "charmander_c.png" , 3, 2, 1 )

pokemon4 = Pokemon ( 'DRAGONITE' , 150 , 'DRAGON TAIL' , 15 , 10 , 'OUTRAGE' , 80 , 10 , 'STEEL WING' , 20 , 10 ,
                     'HYPER BEAM' ,
                     70 , 10 , "dragonite_f.png" , "dragonite_c.png" , 3, 2, 1 )

pokemon5 = Pokemon ( 'DRATINI' , 150 , 'DRAGON BREATH' , 6 , 10 , 'IRON TAIL' , 15 , 10 , 'AQUA TAIL' , 50 , 10 ,
                     'TWISTER' , 45 , 10 ,
                     "dratini_f.png" , "dratini_c.png" , 3, 2, 1 )

pokemon6 = Pokemon ( 'MEWTWO' , 150 , 'CONFUSION' , 20 , 10 , 'PSYCHIC' , 90 , 10 , 'FOCUS BLAST' , 14 , 10 ,
                     'ICE BEAM' , 90 , 10 ,
                     "mewtwo_f.png" , "mewtwo_c.png" , 3, 2, 1 )

pokemon7 = Pokemon ( 'PIKACHU' , 150 , 'THUNDER SHOCK' , 5 , 10 , 'WILD CHARGE' , 90 , 10 , 'DISCHARGE' , 65 , 10 ,
                     'QUICK ATTACK' , 8 , 10 , "pikachu_f.png" , "pikachu_c.png" , 3, 2, 1 )

pokemon8 = Pokemon ( 'SQUIRTLE' , 150 , 'BUBBLE' , 12 , 10 , 'AQUA JET' , 45 , 10 , 'WATER PULSE' , 50 , 10 ,
                     'TACKLE' , 10 , 10 ,
                     "squirtle_f.png" , "squirtle_c.png" , 3, 2, 1 )


# As funçoes abaixo irão criar os textos utilizados no jogo.

def textosJoy ( mensagem , cor , posX , posY , tam ) :
    fonte = pygame.font.Font ( 'joystix monospace.ttf' , tam )
    t = fonte.render ( mensagem , True , cor )
    t_rect = t.get_rect ( )
    t_rect.center = ((posX) , (posY))
    janela.blit ( t , t_rect )


def textosRed ( mensagem , cor , posX , posY , tam ) :
    fonte = pygame.font.Font ( 'pokemon_fire_red.ttf' , tam )
    t = fonte.render ( mensagem , True , cor )
    janela.blit ( t , (posX , posY) )


# Textos =>

titulo = textosJoy ( 'CHOOSE YOUR POKÉMON' , (255 , 255 , 255) , 400 , 30 , 30 )

# Nomes dos pokemons do menu principal.

p1 = textosJoy ( pokemon1.nome , (204 , 0 , 0) , 400 , 110 , 20 )
p2 = textosJoy ( pokemon2.nome , (204 , 102 , 0) , 400 , 170 , 20 )
p3 = textosJoy ( pokemon3.nome , (255 , 255 , 26) , 400 , 230 , 20 )
p4 = textosJoy ( pokemon4.nome , (0 , 204 , 0) , 400 , 290 , 20 )
p5 = textosJoy ( pokemon5.nome , (0 , 172 , 230) , 400 , 350 , 20 )
p6 = textosJoy ( pokemon6.nome , (0 , 51 , 204) , 400 , 410 , 20 )
p7 = textosJoy ( pokemon7.nome , (115 , 0 , 153) , 400 , 470 , 20 )
p8 = textosJoy ( pokemon8.nome , (204 , 0 , 153) , 400 , 530 , 20 )

# Utilizando-se do pygame.draw criamos um retangulo que tera dentro dele os nomes dos pokemons

pygame.draw.lines ( janela , (255 , 255 , 255) , True , [ (240 , 75) , (560 , 75) , (560 , 565) , (240 , 565) ] , 5 )


# A função abaixo é utilizada para inserir as imagens:

def imagens ( imagem , scaleX , scaleY ) :
    imagem = imagem
    x = scaleX
    y = scaleY

    nome = pygame.image.load ( imagem )
    nome = pygame.transform.scale ( nome , (x , y) )
    return nome


# Definições =>

capa_de_inicio = imagens ( 'capa.jpg' , 800 , 600 )

Imagem_Fundo = imagens ( 'background_floresta.png' , 800 , 425 )  # background

Barra = imagens ( 'text_bar.png' , 800 , 175 )  # barra verde de baixo

Barra_Opcoes = imagens ( 'fgt_options.png' , 380 , 180 )  # barra de opções

barra_ataques = imagens ( 'pp_bar.png' , 800 , 175 )

lapide_ao_perder = imagens ('lapide.png', 304 , 303 )

# Mochila : Background e itens.

item1 = imagens ( 'simple_potion.png' , 72 , 92 )
item2 = imagens ( 'big_mac.png' , 107 , 99 )
item3 = imagens ( 'combo_do_mac.jpg' , 90 , 90 )
close_bag = imagens ( 'close_bag1.png' , 100 , 90 )
bag = imagens ( 'bag.png' , 800 , 600 )

janela.blit ( bag , (0 , 0) )
janela.blit ( item2 , (13 , 262) )
janela.blit ( item3 , (20 , 270) )

# Animação de ataque =>

img1 = pygame.image.load ( 'atk1.png' )
img2 = pygame.image.load ( 'atk2.png' )
img3 = pygame.image.load ( 'atk3.png' )
img4 = pygame.image.load ( 'atk4.png' )
img5 = pygame.image.load ( 'atk5.png' )

# Lista das animações dos ataques, que será lida para exibir as imagens.

animacao_de_ataque = [ img1 , img2 , img3 , img4 , img5 ]

# Cores =>
# red, green, blue

red = (200 , 0 , 0)
green = (0 , 200 , 0)
yellow = (200 , 200 , 0)

color1 = green
color = green

# Barra de vida =>
status_do_pokemon1 = imagens ( 'barra_1.png' , 318 , 105 )
status_do_pokemon2 = imagens ( 'barra_2.png' , 327 , 127 )

barra_sem_vida1 = imagens ( 'barra_sem_vida.png' , 150 , 11 )
barra_sem_vida2 = imagens ( 'barra_sem_vida.png' , 150 , 11 )


# A função (barra_de_vida) exibe algumas vezes no codigo as barras de vida após serem modificadas pelo dano.

def barra_de_vida ( player , id ) :
    if id == 0 :
        barra_frente = pygame.draw.line ( janela , color1 , (187 , 123) , ((187 + player.vida) , 123) , 11 )
    else :
        barra_costa = pygame.draw.line ( janela , color , (601 , 359) , ((601 + player.vida) , 359) , 11 )


# Audios do jogo =>

theme_pokemon = pygame.mixer.Sound ( 'pokemon_theme.wav' )

audio_de_selecao = pygame.mixer.Sound ( 'firered_0005.wav' )

audio_de_batalha = pygame.mixer.Sound ( 'batalha.wav' )

audio_de_enter = pygame.mixer.Sound ( 'firered_0030.wav' )

# Capa de inicio de jogo =>

Pressionado = True
while Pressionado :

    for event in pygame.event.get ( ) :

        janela.blit ( capa_de_inicio , (0 , 0) )

        textosJoy ( 'Press "Enter" ' , (0 , 0 , 0) , 421 , 400 , 30 )
        textosJoy ( 'Press "Enter" ' , (255 , 255 , 255) , 418 , 400 , 30 )

        textosJoy ( 'to start the game.' , (0 , 0 , 0) , 421 , 450 , 30 )
        textosJoy ( 'to start the game.' , (255 , 255 , 255) , 418 , 450 , 30 )

        # iniciando audio tema.

        theme_pokemon.play ( )
        theme_pokemon.set_volume ( 0.03 )

        pygame.display.update ( )

        if event.type == pygame.KEYDOWN :

            if event.key == pygame.K_ESCAPE :
                Pressionado = False
                pygame.quit ( )
                quit ( )

            if event.key == pygame.K_RETURN :
                Pressionado = False
                theme_pokemon.stop ( )


# Seta para escolher pokemon

class seta :
    x = 0
    y = 0

    def __init__ ( self , x , y ) :

        self.x = x
        self.y = y

    def pokebola ( self ) :

        poke = pygame.image.load ( 'pokeball32.png' )
        poke_rect = poke.get_rect ( )
        poke_rect.center = ((self.x) , (self.y))

        escolhendo = True

        while escolhendo :

            for event in pygame.event.get ( ) :

                if event.type == pygame.QUIT :
                    escolhendo = False
                    pygame.quit ( )
                    quit ( )

                elif event.type == pygame.KEYDOWN :

                    if event.key == pygame.K_ESCAPE :
                        escolhendo = False
                        pygame.quit ( )
                        quit ( )

                    elif event.key == pygame.K_UP and self.y > 110 :

                        audio_de_selecao.play ( )
                        audio_de_selecao.set_volume ( 0.5 )

                        self.y -= 60
                        poke_rect = poke.get_rect ( )
                        poke_rect.center = ((self.x) , (self.y))

                    elif event.key == pygame.K_DOWN and self.y < 530 :

                        audio_de_selecao.play ( )
                        audio_de_selecao.set_volume ( 0.3 )

                        self.y += 60
                        poke_rect = poke.get_rect ( )
                        poke_rect.center = ((self.x) , (self.y))

                    elif event.key == pygame.K_RETURN :

                        audio_de_enter.play ( )
                        audio_de_enter.set_volume ( 0.3 )

                        if self.y == 110 :
                            return pokemon1

                        elif self.y == 170 :
                            return pokemon2

                        elif self.y == 230 :
                            return pokemon3

                        elif self.y == 290 :
                            return pokemon4

                        elif self.y == 350 :
                            return pokemon5

                        elif self.y == 410 :
                            return pokemon6

                        elif self.y == 470 :
                            return pokemon7

                        elif self.y == 530 :
                            return pokemon8

                        escolhendo = False

            # Reprintando a janela

            back = pygame.image.load ( 'menu.png' )
            back_rect = back.get_rect ( )
            back_rect.center = ((400) , (300))
            janela.blit ( back , back_rect )

            # printando a setinha

            janela.blit ( poke , poke_rect )

            pygame.display.update ( )

    def setinha ( self , rodada ) :

        triangulo = pygame.image.load ( 'le_setinha.png' )
        triangulo = pygame.transform.scale ( triangulo , (12 , 20) )

        escolhendo = True

        while escolhendo :

            for event in pygame.event.get ( ) :

                if event.type == pygame.KEYDOWN :

                    if event.key == pygame.K_ESCAPE :
                        escolhendo = False
                        pygame.quit ( )
                        quit ( )

                        audio_de_selecao.play ( )
                        audio_de_selecao.set_volume ( 0.5 )

                    elif event.key == pygame.K_UP and self.y > 500 :
                        self.y -= 60

                    elif event.key == pygame.K_DOWN and self.y < 500 :
                        self.y += 60

                    elif event.key == pygame.K_RIGHT and self.x < 500 :
                        self.x += 180

                    elif event.key == pygame.K_LEFT and self.x > 500 :
                        self.x -= 180

                    elif event.key == pygame.K_RETURN :

                        if (self.x == 455 and self.y == 474) :

                            return 'fight'

                        elif (self.x == 635 and self.y == 474) :

                            return 'bag'

                        elif (self.x == 455 and self.y == 534) :

                            return 'newpokemon'

                        elif (self.x == 635 and self.y == 534) :

                            return 'runaway'

                        escolhendo = False

            triangulo_rect = triangulo.get_rect ( )
            triangulo_rect.center = ((self.x) , (self.y))

            # reprintando a barra

            janela.blit ( capa_de_inicio , (0 , 0) )
            janela.blit ( Imagem_Fundo , (0 , 0) )
            janela.blit ( player1_imagem , (100 , 270) )
            janela.blit ( player2_imagem , (440 , 118) )
            janela.blit ( Barra , (0 , 420) )
            janela.blit ( Barra_Opcoes , (430 , 420) )

            if rodada == True :
                text1 = textosJoy ( 'What will %s do?' % (player1.nome) , (255 , 255 , 255) , 230 , 500 , 19 )

            else :
                text1 = textosJoy ( 'What will %s do?' % (player2.nome) , (255 , 255 , 255) , 230 , 500 , 19 )

            # Vida dos Personagens.
            janela.blit ( status_do_pokemon1 , (60 , 60) )
            janela.blit ( status_do_pokemon2 , (450 , 292) )
            janela.blit ( barra_sem_vida1 , (187 , 118) )
            janela.blit ( barra_sem_vida2 , (602 , 354) )

            barra_frente = pygame.draw.line ( janela , color1 , (187 , 123) , ((187 + player2.vida) , 123) , 11 )
            barra_costa = pygame.draw.line ( janela , color , (601 , 359) , ((601 + player1.vida) , 359) , 11 )

            # printando a setinha

            janela.blit ( triangulo , (self.x , self.y) )

            pygame.display.update ( )

    # Função que exibe a setinha dentro da bag.


    def setinhaDaBag ( self , rodada ) :

        triangulo = pygame.image.load ( 'setinha.png' )
        triangulo = pygame.transform.scale ( triangulo , (16 , 20) )

        escolhendo_item = True

        while escolhendo_item :

            for event in pygame.event.get ( ) :

                if event.type == pygame.KEYDOWN :

                    if event.key == pygame.K_ESCAPE :
                        escolhendo_item = False
                        pygame.quit ( )
                        quit ( )

                    elif event.key == pygame.K_UP and self.y > 85 :

                        audio_de_selecao.play ( )
                        audio_de_selecao.set_volume ( 0.5 )

                        self.y -= 42
                        triangulo_rect = triangulo.get_rect ( )
                        triangulo_rect.center = ((self.x) , (self.y))

                    elif event.key == pygame.K_DOWN and self.y < 205 :

                        audio_de_selecao.play ( )
                        audio_de_selecao.set_volume ( 0.3 )

                        self.y += 42
                        triangulo_rect = triangulo.get_rect ( )
                        triangulo_rect.center = ((self.x) , (self.y))

                    elif event.key == pygame.K_RETURN :

                        if (self.x == 390 and self.y == 85) :

                            if rodada == True :

                                if player1.vida < 150 - 10 and player1.potion > 0:
                                    player1.vida += 10
                                    player1.potion -= 1


                                else :
                                    player1.vida = 150


                            else :

                                if player2.vida < 150 - 10 and player2.potion > 0:
                                    player2.vida += 10
                                    player2.potion -= 1

                                else :
                                    player1.vida = 150


                            escolhendo_item = False

                        elif (self.x == 390 and self.y == 127) :

                            if rodada == True :

                                if player1.vida < 150 - 30 and player1.bigmac > 0 :
                                    player1.vida += 30
                                    player1.bigmac -= 1

                                else :
                                    player1.vida = 150



                            else :

                                if player2.vida < 150 - 30 and player2.bigmac > 0:
                                    player2.vida += 30


                                else :
                                    player1.vida = 150


                            escolhendo_item = False


                        elif (self.x == 390 and self.y == 169) :

                            if rodada == True :

                                if player1.vida < 150 - 50 and player1.combo > 0 :
                                    player1.vida += 50
                                    player1.combo -= 1

                                else :
                                    player1.vida = 150


                            else :

                                if player2.vida < 150 - 50 and player2.combo > 0 :
                                    player2.vida += 50
                                    player2.combo -= 1

                                else :
                                    player1.vida = 150


                            escolhendo_item = False

                        elif (self.x == 390 and self.y == 211) :

                            escolhendo_item = False

            triangulo_rect = triangulo.get_rect ( )
            triangulo_rect.center = ((self.x) , (self.y))

            # background da mochila
            janela.blit ( bag , (0 , 0) )

            # itens exibidos dentro da mochila.

            textosJoy ( 'POTION' , (0 , 0 , 0) , 480 , 90 , 25 )

            textosJoy ( 'COMBO DO MAC' , (0 , 0 , 0) , 540 , 170 , 25 )

            textosJoy ( 'BIG MAC' , (0 , 0 , 0) , 490 , 130 , 25 )

            textosJoy ( 'CLOSE BAG' , (0 , 0 , 0) , 510 , 210 , 25 )

            if rodada == True:

                textosJoy ( 'x %d' % player1.potion, (0 , 0 , 0) , 730 , 90 , 25 )

                textosJoy ( 'x %d' % player1.bigmac , (0 , 0 , 0) , 730 , 130 , 25 )

                textosJoy ( 'x %d' % player1.combo , (0 , 0 , 0) , 730 , 170 , 25 )

            elif rodada == False:

                textosJoy ( 'x %d' % player2.potion, (0 , 0 , 0) , 730 , 90 , 25 )

                textosJoy ( 'x %d' % player2.bigmac , (0 , 0 , 0) , 730 , 130 , 25 )

                textosJoy ( 'x %d' % player2.combo , (0 , 0 , 0) , 730 , 170 , 25 )



            janela.blit ( triangulo , triangulo_rect )

            if self.x == 390 and self.y == 85 :

                janela.blit ( item1 , (30 , 270) )

            elif self.x == 390 and self.y == 127 :

                janela.blit ( item2 , (13 , 262) )

            elif self.x == 390 and self.y == 169 :

                janela.blit ( item3 , (20 , 270) )

            elif self.x == 390 and self.y == 211 :

                janela.blit ( close_bag , (20 , 270) )

            pygame.display.update ( )


# chamando a classe

pokebola_escolha = seta ( 270 , 110 )

# chamando a função pokebola

player1 = pokebola_escolha.pokebola ( )
player2 = pokebola_escolha.pokebola ( )

player1_imagem = imagens ( player1.costa , 200 , 200 )
player2_imagem = imagens ( player2.frente , 200 , 200 )


def batalha ( player1 , player2 , posX , posY , rodada ) :
    triangulo2 = pygame.image.load ( 'le_setinha.png' )
    triangulo2 = pygame.transform.scale ( triangulo2 , (12 , 20) )

    escolhendo = True

    while escolhendo :

        for event in pygame.event.get ( ) :

            if event.type == pygame.KEYDOWN :

                if event.key == pygame.K_ESCAPE :
                    escolhendo = False
                    pygame.quit ( )
                    quit ( )

                elif event.key == pygame.K_UP and posY > 475 :
                    posY -= 60

                elif event.key == pygame.K_DOWN and posY < 535 :
                    posY += 60

                elif event.key == pygame.K_RIGHT and posX < 250 :
                    posX += 220

                elif event.key == pygame.K_LEFT and posX > 30 :
                    posX -= 220


                elif event.key == pygame.K_RETURN :

                    if (posX == 30 and posY == 475) and player1.pp1 > 0 :

                        if rodada == True :
                            player1.pp1 -= 1
                        else :
                            player2.pp1 -= 1

                        return 'ataque1'


                    elif (posX == 250 and posY == 475) and player1.pp2 > 0 :

                        if rodada == True :
                            player1.pp2 -= 1
                        else :
                            player2.pp2 -= 1

                        return 'ataque2'


                    elif (posX == 30 and posY == 535) and player1.pp3 > 0 :

                        if rodada == True :
                            player1.pp3 -= 1
                        else :
                            player2.pp3 -= 1

                        return 'ataque3'


                    elif (posX == 250 and posY == 535) and player1.pp4 > 0 :

                        if rodada == True :
                            player1.pp4 -= 1
                        else :
                            player2.pp4 -= 1

                        return 'ataque4'

                    else :
                        
                        if rodada == True :
                            janela.blit ( Barra , (0 , 420) )
                            nao_pode_usar = textosJoy ( "%s can't use this attack anymore!" % (player1.nome) ,
                                                    (255 , 255 , 255) , 400 , 512.5 , 20 )
                        else :
                            janela.blit ( Barra , (0 , 420) )
                            nao_pode_usar = textosJoy ( "%s can't use this attack anymore!" % (player2.nome) ,
                                                    (255 , 255 , 255) , 400 , 512.5 , 20 )
                        pygame.display.update ( )
                        pygame.time.delay ( 1000 )

        # reprintando a setinha e o cenário

        janela.blit ( barra_ataques , (0 , 420) )

        if rodada == True :
            player1_ataque1 = textosRed ( player1.ataque1 , (0 , 0 , 0) , 50 , 465 , 40 )
            player1_ataque2 = textosRed ( player1.ataque2 , (0 , 0 , 0) , 270 , 465 , 40 )
            player1_ataque3 = textosRed ( player1.ataque3 , (0 , 0 , 0) , 50 , 525 , 40 )
            player1_ataque4 = textosRed ( player1.ataque4 , (0 , 0 , 0) , 270 , 525 , 40 )

        else :
            player2_ataque1 = textosRed ( player2.ataque1 , (0 , 0 , 0) , 50 , 465 , 40 )
            player2_ataque2 = textosRed ( player2.ataque2 , (0 , 0 , 0) , 270 , 465 , 40 )
            player2_ataque3 = textosRed ( player2.ataque3 , (0 , 0 , 0) , 50 , 525 , 40 )
            player2_ataque4 = textosRed ( player2.ataque4 , (0 , 0 , 0) , 270 , 525 , 40 )

        janela.blit ( triangulo2 , (posX , posY) )

        if (posX == 30 and posY == 475) :

            if rodada == True :
                quant_ataques = textosRed ( '%d    10' % (player1.pp1) , (0 , 0 , 0) , 676 , 464 , 45 )

            else :
                quant_ataques = textosRed ( '%d    10' % (player2.pp1) , (0 , 0 , 0) , 676 , 464 , 45 )

        elif (posX == 250 and posY == 475) :
            if rodada == True :
                quant_ataques = textosRed ( '%d    10' % (player1.pp2) , (0 , 0 , 0) , 676 , 464 , 45 )

            else :
                quant_ataques = textosRed ( '%d    10' % (player2.pp2) , (0 , 0 , 0) , 676 , 464 , 45 )


        elif (posX == 30 and posY == 535) :
            if rodada == True :
                quant_ataques = textosRed ( '%d    10' % (player1.pp3) , (0 , 0 , 0) , 676 , 464 , 45 )

            else :
                quant_ataques = textosRed ( '%d    10' % (player2.pp3) , (0 , 0 , 0) , 676 , 464 , 45 )


        elif (posX == 250 and posY == 535) :
            if rodada == True :
                quant_ataques = textosRed ( '%d    10' % (player1.pp4) , (0 , 0 , 0) , 676 , 464 , 45 )

            else :
                quant_ataques = textosRed ( '%d    10' % (player2.pp4) , (0 , 0 , 0) , 676 , 464 , 45 )

        pygame.display.update ( )


# loop do jogo

run = True
rodada = True

while run :

    audio_de_batalha.play ( )
    audio_de_batalha.set_volume ( 0.1 )

    for event in pygame.event.get ( ) :

        if event.type == pygame.QUIT :
            run = False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                run = False

        if player1.vida > 0 and player2.vida > 0 :

            seta_escolha = seta ( 455 , 474 )
            opcao_escolhida = seta_escolha.setinha ( rodada )

            # Caso esta opção seja escolhida o pokemon foge e encerra o jogo.

            if opcao_escolhida == 'runaway' :
                janela.blit ( Barra , (0 , 420) )
                pokemon_fugiu = textosJoy ( '%s ran away!' % (player1.nome) , (255 , 255 , 255) , 400 , 512.5 , 25 )
                run = False

            # Nesta é aberta a bag, mostrando os itens consumiveis.
            elif opcao_escolhida == 'bag' :

                bag_aberta = True

                while bag_aberta :

                    for event in pygame.event.get ( ) :

                        janela.blit ( bag , (0 , 0) )

                        seta_escolha = seta ( 390 , 85 )

                        opcao_escolhida = seta_escolha.setinhaDaBag ( rodada )

                        pygame.display.update ( )

                        # b = player1
                        # player1 = player2
                        # player2 = b

                        barra_de_vida ( player1 , 1 )
                        barra_de_vida ( player2 , 0 )

                        if rodada == True :
                            rodada = False

                        elif rodada == False :
                            rodada = True

                        bag_aberta = False

            # Nesse os pokemons escolhem os ataques.

            elif opcao_escolhida == 'fight' :

                ataque_usado = batalha ( player1 , player2 , 30 , 475 , rodada )

                for imagem in animacao_de_ataque :

                    if rodada == True:

                        janela.blit ( imagem , (425 , 140) )

                    else:

                        janela.blit ( imagem , (200 , 300) )

                        rodada = False

                pygame.time.Clock ( )

                if ataque_usado == 'ataque1' :

                    if rodada == True :
                        player1.ataca ( player2 , player1.dano1 )
                        janela.blit ( Barra , (0 , 420) )
                        pokemon_usou = textosJoy ( '%s used %s!' % (player1.nome , player1.ataque1) ,
                                                   (255 , 255 , 255) ,
                                                   400 , 512.5 , 25 )
                        pygame.display.update ( )
                        pygame.time.delay ( 1000 )
                        rodada = False

                    else :
                        player2.ataca ( player1 , player2.dano1 )
                        janela.blit ( Barra , (0 , 420) )
                        pokemon_usou = textosJoy ( '%s used %s!' % (player2.nome , player2.ataque1) ,
                                                   (255 , 255 , 255) ,
                                                   400 , 512.5 , 25 )
                        pygame.display.update ( )
                        pygame.time.delay ( 1000 )
                        rodada = True

                elif ataque_usado == 'ataque2' :

                    if rodada == True :
                        player1.ataca ( player2 , player1.dano2 )
                        janela.blit ( Barra , (0 , 420) )
                        pokemon_usou = textosJoy ( '%s used %s!' % (player1.nome , player1.ataque2) ,
                                                   (255 , 255 , 255) ,
                                                   400 , 512.5 , 25 )
                        pygame.display.update ( )
                        pygame.time.delay ( 1000 )
                        rodada = False

                    else :
                        player2.ataca ( player1 , player2.dano2 )
                        janela.blit ( Barra , (0 , 420) )
                        pokemon_usou = textosJoy ( '%s used %s!' % (player2.nome , player2.ataque2) ,
                                                   (255 , 255 , 255) ,
                                                   400 , 512.5 , 25 )
                        pygame.display.update ( )
                        pygame.time.delay ( 1000 )
                        rodada = True


                elif ataque_usado == 'ataque3' :

                    if rodada == True :
                        player1.ataca ( player2 , player1.dano3 )
                        janela.blit ( Barra , (0 , 420) )
                        pokemon_usou = textosJoy ( '%s used %s!' % (player1.nome , player1.ataque3) ,
                                                   (255 , 255 , 255) ,
                                                   400 , 512.5 , 25 )
                        pygame.display.update ( )
                        pygame.time.delay ( 1000 )
                        rodada = False

                    else :
                        player2.ataca ( player1 , player2.dano1 )
                        janela.blit ( Barra , (0 , 420) )
                        pokemon_usou = textosJoy ( '%s used %s!' % (player2.nome , player2.ataque1) ,
                                                   (255 , 255 , 255) ,
                                                   400 , 512.5 , 25 )
                        pygame.display.update ( )
                        pygame.time.delay ( 1000 )
                        rodada = True


                elif ataque_usado == 'ataque4' :

                    if rodada == True :
                        player1.ataca ( player2 , player1.dano4 )
                        janela.blit ( Barra , (0 , 420) )
                        pokemon_usou = textosJoy ( '%s used %s!' % (player1.nome , player1.ataque4) ,
                                                   (255 , 255 , 255) ,
                                                   400 , 512.5 , 25 )
                        pygame.display.update ( )
                        pygame.time.delay ( 1000 )
                        rodada = False

                    else :
                        player2.ataca ( player1 , player2.dano4 )
                        janela.blit ( Barra , (0 , 420) )
                        pokemon_usou = textosJoy ( '%s used %s!' % (player2.nome , player2.ataque4) ,
                                                   (255 , 255 , 255) ,
                                                   400 , 512.5 , 25 )
                        pygame.display.update ( )
                        pygame.time.delay ( 1000 )
                        rodada = True

                pygame.display.update ( )
                pygame.time.delay ( 1000 )

                # trocando players para a função
                # a = player1
                # player1 = player2
                # player2 = a

                barra_de_vida ( player1 , 1 )
                barra_de_vida ( player2 , 0 )


        elif 0 >= player1.vida :


            #janela.blit (lapide_ao_perder, (70, 180))
            janela.fill ( j.get_cor ( ) )
            winner = textosJoy ( 'And the winner is %s!!!' % (player2.nome) , (255 , 255 , 255) , 400 , 300 , 20 )
            pygame.display.update ( )
            pygame.time.delay ( 2000 )
            run = False



        elif 0 >= player2.vida :

            #janela.blit (lapide_ao_perder, (440, 50))
            janela.fill ( j.get_cor ( ) )
            winner = textosJoy ( 'And the winner is %s!!!' % (player1.nome) , (255 , 255 , 255) , 400 , 300 , 20 )
            pygame.display.update ( )
            pygame.time.delay ( 2000 )
            run = False

        pygame.display.update ( )
    continue

pygame.quit ( )
quit ( )
