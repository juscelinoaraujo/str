#import random as rd
import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
pygame.init()
screen = pygame.display.set_mode((600,700))
pygame.display.set_caption("Controle de malha ferroviaria")
running = True

# True = sinal verde
# Falso = sinal vermelho
conversao = {'l2l3': True, 'l3l4': True, 'l6l7': True, 'l7l3': True, 'l12l9': True, 'l9l7': True, 'l8l4': True, 'l4l9': True}

# Velocidade dos trens
velocidade = {'amarelo': 0.5, 'azul': 0, 'vermelho': 0, 'verde': 0}

# Posicao e dimensao dos trens
lado = 15
posicaox = {'amarelo': 83, 'azul': 303, 'vermelho': 83, 'verde': 303}
posicaoy = {'amarelo': 43, 'azul': 43, 'vermelho': 213, 'verde': 213}

#slider = Slider(screen, 100, 100, 400, 40, min=0, max=99, step=1)
#output = TextBox(screen, 475, 200, 50, 50, fontSize=30)

#output.disable()  # Act as label instead of textbox

def amarelo_percorre_l2(posicaox, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante

def amarelo_percorre_l3(posicaoy, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante

def amarelo_percorre_l2(posicaox, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante

def amarelo_percorre_l2(posicaox, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante

def amarelo_percorre_l2(posicaox, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante

def amarelo_percorre_l2(posicaox, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante

def amarelo_percorre_l2(posicaox, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante

def amarelo_percorre_l2(posicaox, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante

def amarelo_percorre_l2(posicaox, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante

def amarelo_percorre_l2(posicaox, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante

def amarelo_percorre_l2(posicaox, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante

def amarelo_percorre_l2(posicaox, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante

def amarelo_percorre_l2(posicaox, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante

def amarelo_percorre_l2(posicaox, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante

def amarelo_percorre_l2(posicaox, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante

def amarelo_percorre_l2(posicaox, velocidade):
  restante = 284 - posicaox['amarelo']
  if posicaox['amarelo'] + velocidade['amarelo'] <= 284:
    posicaox['amarelo'] += velocidade['amarelo']
  elif restante > 0:
    posicaox['amarelo'] += restante
  


while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  # Tela de fundo
  screen.fill('grey')

  # Trilhos
  pygame.draw.polygon(screen, 'yellow', [[90,50],[290,50],[290,200],[90,200]], 5)  
  pygame.draw.polygon(screen, 'blue', [[310,50],[510,50],[510,200],[310,200]], 5) 
  pygame.draw.polygon(screen, 'red', [[90,220],[290,220],[290,370],[90,370]], 5) 
  pygame.draw.polygon(screen, 'green', [[310,220],[510,220],[510,370],[310,370]], 5) 
  
  #amarelo_percorre_l3(posicaoy, velocidade)

  # Trens
  pygame.draw.rect(screen, 'yellow', [posicaox['amarelo'], posicaoy['amarelo'], lado, lado])
  pygame.draw.rect(screen, 'blue', [posicaox['azul'], posicaoy['azul'], lado, lado])
  pygame.draw.rect(screen, 'red', [posicaox['vermelho'], posicaoy['vermelho'], lado, lado])
  pygame.draw.rect(screen, 'green', [posicaox['verde'], posicaoy['verde'], lado, lado])

  #output.setText(slider.getValue())

  #pygame_widgets.update(event)

  pygame.display.update()

pygame.quit()
