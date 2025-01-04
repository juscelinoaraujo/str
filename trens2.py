#import random as rd
import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
pygame.init()
screen = pygame.display.set_mode((820,700))
pygame.display.set_caption("Controle de malha ferroviaria")
running = [True]

# Localizacao
verde_l1 = [False]
verde_l2 = [True]
verde_l3 = [False]
verde_l4 = [False]
roxo_l3 = [False]
roxo_l7 = [True]
roxo_l5 = [False]
roxo_l6 = [False]
vermelho_l5 = [False]
vermelho_l8 = [True]
vermelho_l9 = [False]
vermelho_l10 = [False]
azul_l11 = [False]
azul_l4_l6_l10 = [True]
azul_l12 = [False]
azul_l13 = [False]

# Velocidade dos trens
velocidade = {'verde': 2, 'roxo': 3, 'vermelho': 5, 'azul': 1}

# Vetor auxiliar de controle
aux = [False, False, False, False, False, False, False, False]

# Posicao e dimensao dos trens
lado = 15
posicaox = {'verde': 83, 'roxo': 303, 'vermelho': 523, 'azul': 303}
posicaoy = {'verde': 43, 'roxo': 43, 'vermelho': 43, 'azul': 213}

fonte = pygame.font.SysFont('monospace', 27)
rotulo = ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "L10", "L11", "L12", "L13"]
texto_trilho = []
for i in range(len(rotulo)):
  texto_trilho.append(fonte.render(rotulo[i], True, "black", "grey"))
  
def escreve_rotulos():
  screen.blit(texto_trilho[0], (100, 110))
  screen.blit(texto_trilho[1], (175, 60))
  screen.blit(texto_trilho[2], (320, 110))
  screen.blit(texto_trilho[3], (175, 160))
  screen.blit(texto_trilho[4], (540, 110))
  screen.blit(texto_trilho[5], (395, 160))
  screen.blit(texto_trilho[6], (395, 60))
  screen.blit(texto_trilho[7], (615, 60))
  screen.blit(texto_trilho[8], (685, 110))
  screen.blit(texto_trilho[9], (605, 160))
  screen.blit(texto_trilho[10], (100, 280))
  screen.blit(texto_trilho[11], (670, 280))
  screen.blit(texto_trilho[12], (385, 330))
  
titulo1 = "Visualização da dinâmica dos trens"
titulo2 = "Painel de controle de velocidade"
texto_titulo1 = fonte.render(titulo1, True, "black", "grey")
texto_titulo2 = fonte.render(titulo2, True, "black", "grey")

def escreve_titulos():
  screen.blit(texto_titulo1, (140, 10))
  screen.blit(texto_titulo2, (150, 400))

indicador = ["T", "G", "Y", "H", "U", "J", "I", "K"]
texto_indicador = []
for i in range(len(indicador)):
  texto_indicador.append(fonte.render(indicador[i], True, "black", "grey"))
  
def escreve_indicadores():
  screen.blit(texto_indicador[0], (297, 430))
  screen.blit(texto_indicador[1], (297, 670))
  screen.blit(texto_indicador[2], (364, 430))
  screen.blit(texto_indicador[3], (364, 670))
  screen.blit(texto_indicador[4], (430, 430))
  screen.blit(texto_indicador[5], (430, 670))
  screen.blit(texto_indicador[6], (497, 430))
  screen.blit(texto_indicador[7], (497, 670))

def controle():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running[0] = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_t and velocidade['verde'] <= 9.5:
        velocidade['verde'] += 0.5
      if event.key == pygame.K_g and velocidade['verde'] >= 0.5:
        velocidade['verde'] -= 0.5
      if event.key == pygame.K_y and velocidade['roxo'] <= 9.5:
        velocidade['roxo'] += 0.5
      if event.key == pygame.K_h and velocidade['roxo'] >= 0.5:
        velocidade['roxo'] -= 0.5
      if event.key == pygame.K_u and velocidade['vermelho'] <= 9.5:
        velocidade['vermelho'] += 0.5
      if event.key == pygame.K_j and velocidade['vermelho'] >= 0.5:
        velocidade['vermelho'] -= 0.5  
      if event.key == pygame.K_i and velocidade['azul'] <= 9.5:
        velocidade['azul'] += 0.5  
      if event.key == pygame.K_k and velocidade['azul'] >= 0.5:
        velocidade['azul'] -= 0.5

def verde_percorre_l2():
  restante = 283 - posicaox['verde']
  if posicaox['verde'] + velocidade['verde'] <= 283:
    posicaox['verde'] += velocidade['verde']
  elif restante > 0:
    posicaox['verde'] += restante
  else:
    verde_l2[0] = False
    verde_l3[0] = True

def verde_percorre_l3():
  restante = 193 - posicaoy['verde']
  if posicaoy['verde'] + velocidade['verde'] <= 193:
    posicaoy['verde'] += velocidade['verde']
  elif restante > 0:
    posicaoy['verde'] += restante
  else:
    verde_l3[0] = False
    verde_l4[0] = True
    
def verde_percorre_l4():
  restante = posicaox['verde'] - 83
  if posicaox['verde'] - velocidade['verde'] >= 83:
    posicaox['verde'] -= velocidade['verde']
  elif restante > 0:
    posicaox['verde'] -= restante
  else:
    verde_l4[0] = False
    verde_l1[0] = True
    
def verde_percorre_l1():
  restante = posicaoy['verde'] - 43
  if posicaoy['verde'] - velocidade['verde'] >= 43:
    posicaoy['verde'] -= velocidade['verde']
  elif restante > 0:
    posicaoy['verde'] -= restante
  else:
    verde_l1[0] = False
    verde_l2[0] = True

def roxo_percorre_l7():
  restante = 503 - posicaox['roxo']
  if posicaox['roxo'] + velocidade['roxo'] <= 503:
    posicaox['roxo'] += velocidade['roxo']
  elif restante > 0:
    posicaox['roxo'] += restante
  else:
    roxo_l7[0] = False
    roxo_l5[0] = True

def roxo_percorre_l5():
  restante = 193 - posicaoy['roxo']
  if posicaoy['roxo'] + velocidade['roxo'] <= 193:
    posicaoy['roxo'] += velocidade['roxo']
  elif restante > 0:
    posicaoy['roxo'] += restante
  else:
    roxo_l5[0] = False
    roxo_l6[0] = True
    
def roxo_percorre_l6():
  restante = posicaox['roxo'] - 303
  if posicaox['roxo'] - velocidade['roxo'] >= 303:
    posicaox['roxo'] -= velocidade['roxo']
  elif restante > 0:
    posicaox['roxo'] -= restante
  else:
    roxo_l6[0] = False
    roxo_l3[0] = True
    
def roxo_percorre_l3():
  restante = posicaoy['roxo'] - 43
  if posicaoy['roxo'] - velocidade['roxo'] >= 43:
    posicaoy['roxo'] -= velocidade['roxo']
  elif restante > 0:
    posicaoy['roxo'] -= restante
  else:
    roxo_l3[0] = False
    roxo_l7[0] = True

def vermelho_percorre_l8():
  restante = 723 - posicaox['vermelho']
  if posicaox['vermelho'] + velocidade['vermelho'] <= 723:
    posicaox['vermelho'] += velocidade['vermelho']
  elif restante > 0:
    posicaox['vermelho'] += restante
  else:
    vermelho_l8[0] = False
    vermelho_l9[0] = True

def vermelho_percorre_l9():
  restante = 193 - posicaoy['vermelho']
  if posicaoy['vermelho'] + velocidade['vermelho'] <= 193:
    posicaoy['vermelho'] += velocidade['vermelho']
  elif restante > 0:
    posicaoy['vermelho'] += restante
  else:
    vermelho_l9[0] = False
    vermelho_l10[0] = True
    
def vermelho_percorre_l10():
  restante = posicaox['vermelho'] - 523
  if posicaox['vermelho'] - velocidade['vermelho'] >= 523:
    posicaox['vermelho'] -= velocidade['vermelho']
  elif restante > 0:
    posicaox['vermelho'] -= restante
  else:

    vermelho_l10[0] = False
    vermelho_l5[0] = True
    
def vermelho_percorre_l5():
  restante = posicaoy['vermelho'] - 43
  if posicaoy['vermelho'] - velocidade['vermelho'] >= 43:
    posicaoy['vermelho'] -= velocidade['vermelho']
  elif restante > 0:
    posicaoy['vermelho'] -= restante
  else:
    vermelho_l5[0] = False
    vermelho_l8[0] = True

def azul_percorre_l4_l6_l10():
  restante = 723 - posicaox['azul']
  if posicaox['azul'] + velocidade['azul'] <= 723:

    posicaox['azul'] += velocidade['azul']
  elif restante > 0:
    posicaox['azul'] += restante
  else:
    azul_l4_l6_l10[0] = False
    azul_l12[0] = True
    
def azul_percorre_l12():
  restante = 363 - posicaoy['azul']
  if posicaoy['azul'] + velocidade['azul'] <= 363:
    posicaoy['azul'] += velocidade['azul']
  elif restante > 0:
    posicaoy['azul'] += restante
  else:
    azul_l12[0] = False
    azul_l13[0] = True
    
def azul_percorre_l13():
  restante = posicaox['azul'] - 83

  if posicaox['azul'] - velocidade['azul'] >= 83:
    posicaox['azul'] -= velocidade['azul']
  elif restante > 0:
    posicaox['azul'] -= restante
  else:
    azul_l13[0] = False
    azul_l11[0] = True

def azul_percorre_l11():
  restante = posicaoy['azul'] - 213
  if posicaoy['azul'] - velocidade['azul'] >= 213:
    posicaoy['azul'] -= velocidade['azul']
  elif restante > 0:
    posicaoy['azul'] -= restante
  else:
    azul_l11[0] = False
    azul_l4_l6_l10[0] = True
    
def movimento_verde():
  if verde_l2[0] == True:
    verde_percorre_l2()
  if verde_l3[0] == True:
    verde_percorre_l3()
  if verde_l4[0] == True:
    verde_percorre_l4()
  if verde_l1[0] == True:
    verde_percorre_l1()  
    
def movimento_roxo():
  if roxo_l7[0] == True:
    roxo_percorre_l7()
  if roxo_l5[0] == True:
    roxo_percorre_l5()
  if roxo_l6[0] == True:
    roxo_percorre_l6()
  if roxo_l3[0] == True:
    roxo_percorre_l3()
    
def movimento_vermelho():
  if vermelho_l8[0] == True:
    vermelho_percorre_l8()
  if vermelho_l9[0] == True:
    vermelho_percorre_l9()
  if vermelho_l10[0] == True:
    vermelho_percorre_l10()
  if vermelho_l5[0] == True:
    vermelho_percorre_l5()
    
def movimento_azul():
  if azul_l4_l6_l10[0] == True:
    azul_percorre_l4_l6_l10()
  if azul_l12[0] == True:
    azul_percorre_l12()
  if azul_l13[0] == True:
    azul_percorre_l13()
  if azul_l11[0] == True:
    azul_percorre_l11()


while running[0]:
  # Controle
  controle()
  
  # Tela de fundo
  screen.fill('grey')
  
  # Escreve textos
  escreve_titulos()
  escreve_rotulos()
  escreve_indicadores()

  # Trilhos
  pygame.draw.polygon(screen, 'skyblue3', [[90,50],[290,50],[290,200],[90,200]], 5)  
  pygame.draw.polygon(screen, 'white', [[310,50],[510,50],[510,200],[310,200]], 5) 
  #pygame.draw.polygon(screen, 'red', [[90,220],[290,220],[290,370],[90,370]], 5) 
  #pygame.draw.polygon(screen, 'green', [[310,220],[510,220],[510,370],[310,370]], 5)
  pygame.draw.polygon(screen, 'yellow', [[530,50],[730,50],[730,200],[530,200]], 5) 
  pygame.draw.polygon(screen, 'royalblue', [[90,220], [730,220], [730,370], [90,370]], 5)
  
  # movimentos
  movimento_verde()
  movimento_roxo()
  movimento_vermelho()
  movimento_azul()

  # Trens
  pygame.draw.rect(screen, 'mediumseagreen', [posicaox['verde'], posicaoy['verde'], lado, lado])
  pygame.draw.rect(screen, 'purple', [posicaox['roxo'], posicaoy['roxo'], lado, lado])
  pygame.draw.rect(screen, 'red', [posicaox['vermelho'], posicaoy['vermelho'], lado, lado])
  pygame.draw.rect(screen, 'blue', [posicaox['azul'], posicaoy['azul'], lado, lado])

  pygame.draw.rect(screen, 'skyblue3', [300, 460, 10, 210])
  pygame.draw.rect(screen, 'mediumseagreen', [290, 660 - 20*velocidade['verde'], 30, 10])
  pygame.draw.rect(screen, 'white', [367, 460, 10, 210])
  pygame.draw.rect(screen, 'purple', [357, 660 - 20*velocidade['roxo'], 30, 10])
  pygame.draw.rect(screen, 'yellow', [433, 460, 10, 210])
  pygame.draw.rect(screen, 'red', [423, 660 - 20*velocidade['vermelho'], 30, 10])
  pygame.draw.rect(screen, 'royalblue', [500, 460, 10, 210])
  pygame.draw.rect(screen, 'blue', [490, 660 - 20*velocidade['azul'], 30, 10])
  
  pygame.display.update()

pygame.quit()
