import pygame_widgets
import pygame
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.dropdown import Dropdown
import subprocess
import os
import time

tem_filtro = [False]
pid = [""]
filtro = [""]
n_cpu = []
for i in range(int(subprocess.getoutput("nproc"))):
  n_cpu.append(str(i))
prioridade = []
for i in range(21):
  prioridade.append(str(i))


def selecionar_pid():
  a = 5
  pid[0] = textbox_filtro.getText()
  
def kill_processo():
  pid = textbox_filtro.getText()
  #os.system("kill -9 " + pid)
  os.system("kill -9 " + pid)
  
def stop_processo():
  pid = textbox_filtro.getText()
  os.system("kill -STOP" + pid)
  
def cont_processo():
  pid = textbox_filtro.getText()
  os.system("kill -CONT" + pid)

def filtrar():
  tem_filtro[0] = True
  filtro[0] = textbox_filtro.getText()
  
def limpar_filtro():
  tem_filtro[0] = False


pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Gerenciador de Processos")

fonte = pygame.font.SysFont('monospace', 18)

string_pid = "PID"
string_filtro = "Filtro"
texto_pid = fonte.render(string_pid, True, "black", "grey")
texto_filtro = fonte.render(string_filtro, True, "black", "grey")


textbox_pid = TextBox(screen, 120, 100, 100, 30, font=fonte,
                  borderColour=(255, 0, 0),
                  onSubmit=selecionar_pid)
                  
textbox_filtro = TextBox(screen, 120, 200, 100, 30, font=fonte,
                  borderColour=(255, 0, 0),
                  onSubmit=filtrar)

button_kill = Button(screen, 300, 100, 90, 30, text="kill", 
                     font=fonte, onClick=kill_processo)
button_stop = Button(screen, 400, 100, 90, 30, text="stop", 
                     font=fonte, onClick=stop_processo)
button_cont = Button(screen, 500, 100, 90, 30, text="cont", 
                     font=fonte, onClick=cont_processo)
button_limpar = Button(screen, 300, 200, 90, 30, text="limpar", 
                     font=fonte, onClick=limpar_filtro)

dropdown_cpu = Dropdown(screen, 600, 100, 90, 30, name='cpu', choices=n_cpu, 
                        direction='down', font = fonte)
                        
dropdown_prio = Dropdown(screen, 700, 100, 90, 30, name='prio', choices=prioridade, 
                         direction='down', font = fonte)

tempo = pygame.time.Clock()

run = True
while run:
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      pygame.quit()
      run = False
      quit()

  screen.fill('grey')
  screen.blit(texto_pid, (40, 100)) 
  screen.blit(texto_filtro, (40, 200)) 
  pygame.draw.rect(screen, 'white', [0, 290, 1000, 310])
  if tem_filtro[0] == True:
    comando = "ps -auf | grep " + filtro[0]
  else:
    comando = "ps -auf"
  proc_info = subprocess.getoutput(comando)
  proc_info = proc_info.split("\n")
  proc_texto = []
  for i in range(len(proc_info)):
    proc_texto.append(fonte.render(proc_info[i], True, "black", "white"))
    screen.blit(proc_texto[i], (40, 300+18*i)) 

  pygame_widgets.update(events)
  pygame.display.update()
  #time.sleep(1)
  tempo.tick(5)
