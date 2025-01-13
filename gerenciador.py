import pygame_widgets
import pygame
import time
import os
import subprocess
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Gerenciador de Processos")

running = True
fonte = pygame.font.SysFont('monospace', 18)
button_kill = Button(screen, 300, 100, 50, 25, text="kill")
button_stop = Button(screen, 400, 100, 50, 25, text="stop")
button_continue = Button(screen, 500, 100, 70, 25, text="continue")

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  # Tela de fundo
  screen.fill('grey')
  pygame.draw.rect(screen, 'white', [0, 290, 1000, 310])
  proc_info = subprocess.getoutput("ps -auf")
  proc_info = proc_info.split("\n")
  proc_texto = []
  for i in range(len(proc_info)):
    proc_texto.append(fonte.render(proc_info[i], True, "black", "white"))
    screen.blit(proc_texto[i], (40, 300+18*i)) 
  #proc_texto = fonte.render(proc_info, True, "black", "white")
  #screen.blit(proc_texto, (30, 300))
  pygame_widgets.update(event)
  pygame.display.update()
  time.sleep(1)

# Fecha a tela
pygame.quit()

