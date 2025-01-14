import pygame_widgets
import pygame
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.dropdown import Dropdown
import subprocess
import os
import time

#from pygame_widgets.progressbar import ProgressBar

#startTime = time.time()

tem_filtro = [False]
#pid = [""]
filtro = [""]

n_cpu = []
for i in range(int(subprocess.getoutput("nproc"))):
  n_cpu.append(str(i))
n_cpu.append("desfazer")
#prioridade = []
#for i in range(21):
#  prioridade.append(str(i))
  
def kill_processo():
  pid = textbox_pid.getText()
  print("kill -9 " + pid)
  os.system("kill -9 " + pid)
  
def stop_processo():
  pid = textbox_pid.getText()
  print("kill -19 " + pid)
  os.system("kill -19 " + pid)
  
def cont_processo():
  pid = textbox_pid.getText()
  os.system("kill -18 " + pid)
  
def aplicar():
  pid = textbox_pid.getText()
  cpu = dropdown_cpu.getSelected()
  #prio = dropdown_prio.getSelected()
  prio = str(slider_prio.getValue())
  if cpu != None:
    print("cpu = " + cpu)
    if cpu == "desfazer":
      print("taskset -p " + pid)
      os.system("taskset -p " + pid)
    else:
      print("taskset -pc --cpu-list " + cpu + " " + pid)
      os.system("taskset -pc --cpu-list " + cpu + " " + pid)
    #os.system("tasket ")
  if prio != None:
    print("renice " + prio + " " + pid)
    os.system("renice " + prio + " " + pid)

def filtrar():
  tem_filtro[0] = True
  filtro[0] = textbox_filtro.getText()
  
def limpar_filtro():
  tem_filtro[0] = False


pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 670
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Gerenciador de Processos")

fonte = pygame.font.SysFont('monospace', 15)

#progressBar = ProgressBar(screen, 100, 100, 500, 40, lambda: 1 - (time.time() - startTime) / 10, curved=True)

string_pid = "PID"
string_filtro = "Filtro"
texto_pid = fonte.render(string_pid, True, "black", "grey")
texto_filtro = fonte.render(string_filtro, True, "black", "grey")


textbox_pid = TextBox(screen, 120, 50, 100, 30, font=fonte,
                  borderColour=(255, 0, 0))
                  
textbox_filtro = TextBox(screen, 120, 150, 100, 30, font=fonte,
                  borderColour=(255, 0, 0),
                  onSubmit=filtrar)

button_kill = Button(screen, 300, 50, 90, 30, text="kill", 
                     font=fonte, onClick=kill_processo)
button_stop = Button(screen, 400, 50, 90, 30, text="stop", 
                     font=fonte, onClick=stop_processo)
button_cont = Button(screen, 500, 50, 90, 30, text="cont", 
                     font=fonte, onClick=cont_processo)
button_limpar = Button(screen, 300, 150, 90, 30, text="limpar", 
                     font=fonte, onClick=limpar_filtro)

dropdown_cpu = Dropdown(screen, 670, 50, 90, 30, name='cpu', choices=n_cpu, 
                        direction='down', font = fonte)
                        
#dropdown_prio = Dropdown(screen, 770, 50, 90, 30, name='prio', choices=prioridade, 
#                         direction='down', font = fonte)
                         
slider_prio = Slider(screen, 770, 100, 90, 10, min=0, max=19, step=1, 
                     initial = 0, handleColour=(255,255,255), colour =(0,0,0))

output_prio = TextBox(screen, 770, 50, 90, 30, font=fonte)
output_prio.disable()  # Act as label instead of textbox
                         
button_aplicar = Button(screen, 870, 50, 90, 30, text="aplicar", 
                     font=fonte, onClick=aplicar)                         

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
  output_prio.setText(slider_prio.getValue())
  screen.blit(texto_pid, (40, 50)) 
  screen.blit(texto_filtro, (40, 150)) 
  pygame.draw.rect(screen, 'white', [0, 240, 1000, SCREEN_HEIGHT - 240])
  if tem_filtro[0] == True:
    #print("ps -eo user,pid,ppid,ni,pcpu,pmem,stat,comm --sort=-pcpu | grep -E '" + filtro[0] + "|^USER' | head -n 21")
    comando = "ps -eo user,pid,ppid,ni,pcpu,pmem,stat,comm --sort=-pcpu | grep -E '" + filtro[0] + "|^USER' | head -n 21"   
  else:
    comando = "ps -eo user,pid,ppid,ni,pcpu,pmem,stat,comm --sort=-pcpu | head -n 21"
  proc_info = subprocess.getoutput(comando)
  proc_info = proc_info.split("\n")
  proc_texto = []
  for i in range(len(proc_info)):
    proc_texto.append(fonte.render(proc_info[i], True, "black", "white"))
    screen.blit(proc_texto[i], (40, 250+18*i)) 

  pygame_widgets.update(events)
  pygame.display.update()
  #time.sleep(1)
  tempo.tick(5)
