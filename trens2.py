#import random as rd
import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
pygame.init()
screen = pygame.display.set_mode((820,700))
pygame.display.set_caption("Controle de malha ferroviaria")
running = True

# Localizacao
verde_l1 = [False]
verde_l2 = [True]
verde_l3 = [False]
verde_l4 = [False]
roxo_l3 = [False]
roxo_l7 = [False]
roxo_l5 = [False]
roxo_l6 = [False]
vermelho_l5 = [False]
vermelho_l8 = [False]
vermelho_l9 = [False]
vermelho_l10 = [False]
azul_l11 = [False]
azul_l4_l6_l10 = [False]
azul_l12 = [False]
azul_l13 = [False]

# Velocidade dos trens
velocidade = {'verde': 0.5, 'roxo': 0, 'vermelho': 0, 'azul': 0}

# Posicao e dimensao dos trens
lado = 15
posicaox = {'verde': 83, 'roxo': 303, 'vermelho': 523, 'azul': 303}
posicaoy = {'verde': 43, 'roxo': 43, 'vermelho': 43, 'azul': 213}

fonte = pygame.font.SysFont('monospace', 27)
font1 = pygame.font.SysFont('monospace', 27)
#title = "Nas bolas azuis, aperte R"
rotulo = ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "L10", "L11", "L12", "L13"]
#text_title = font1.render(title, True, "black", "white")
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
  
#slider = Slider(screen, 100, 100, 400, 40, min=0, max=99, step=1)
#output = TextBox(screen, 475, 200, 50, 50, fontSize=30)

#output.disable()  # Act as label instead of textbox



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
    
def verde_percorre_l():
  restante = posicaox['verde'] - 83
  if posicaox['verde'] - velocidade['verde'] >= 83:
    posicaox['verde'] -= velocidade['verde']
  elif restante > 0:
    posicaox['verde'] -= restante
  else:
    verde_l4[0] = False
    verde_l1[0] = True
    
def roxo_percorre_l3():
  restante = posicaoy['verde'] - 43
  if posicaoy['verde'] - velocidade['verde'] >= 43:
    posicaoy['verde'] -= velocidade['verde']
  elif restante > 0:
    posicaoy['verde'] -= restante
  else:
    verde_l1[0] = False
    verde_l2[0] = True
    

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  # Tela de fundo
  screen.fill('grey')
  
  # Escreve rotulos
  escreve_rotulos()

  # Trilhos
  pygame.draw.polygon(screen, 'skyblue3', [[90,50],[290,50],[290,200],[90,200]], 5)  
  pygame.draw.polygon(screen, 'white', [[310,50],[510,50],[510,200],[310,200]], 5) 
  #pygame.draw.polygon(screen, 'red', [[90,220],[290,220],[290,370],[90,370]], 5) 
  #pygame.draw.polygon(screen, 'green', [[310,220],[510,220],[510,370],[310,370]], 5)
  pygame.draw.polygon(screen, 'yellow', [[530,50],[730,50],[730,200],[530,200]], 5) 
  pygame.draw.polygon(screen, 'royalblue', [[90,220], [730,220], [730,370], [90,370]], 5)
  
  
  if verde_l2[0] == True:
    verde_percorre_l2()
  if verde_l3[0] == True:
    verde_percorre_l3()
  if verde_l4[0] == True:
    verde_percorre_l4()
  if verde_l1[0] == True:
    verde_percorre_l1()

  # Trens
  pygame.draw.rect(screen, 'mediumseagreen', [posicaox['verde'], posicaoy['verde'], lado, lado])
  pygame.draw.rect(screen, 'purple', [posicaox['roxo'], posicaoy['roxo'], lado, lado])
  pygame.draw.rect(screen, 'red', [posicaox['vermelho'], posicaoy['vermelho'], lado, lado])
  pygame.draw.rect(screen, 'blue', [posicaox['azul'], posicaoy['azul'], lado, lado])

  #output.setText(slider.getValue())

  #pygame_widgets.update(event)

  pygame.display.update()

pygame.quit()
