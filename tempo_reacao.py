import random as rd
import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Teste de Reação")
running = True

state = 0
step = 0
reacted = False
score = 0
start_time = 0
total_time = 0

def show_text(state):
  global score, total_time
  font1 = pygame.font.SysFont('monospace', 27)
  font2 = pygame.font.SysFont('monospace', 20)
  if state == 0: 
    title = "Teste de tempo de reação"
    inst1 = "Nas bolas azuis, aperte R"
    inst2 = "Nas bolas verdes, aperte T"
    inst3 = "Nas bolas amarelas, aperte Y"
    inst4 = "Nas bolas vvermelhas, aperte U"
    note = "Para iniciar o teste, aperte W"
    text_title = font1.render(title, True, "black", "white")
    text_inst1 = font2.render(inst1, True, "black", "white")
    text_inst2 = font2.render(inst2, True, "black", "white")
    text_inst3 = font2.render(inst3, True, "black", "white")
    text_inst4 = font2.render(inst4, True, "black", "white")
    text_note = font1.render(note, True, "white", "black")
    screen.blit(text_title, (205, 100))
    screen.blit(text_inst1, (205, 200))
    screen.blit(text_inst2, (205, 250))
    screen.blit(text_inst3, (205, 300))
    screen.blit(text_inst4, (205, 350))	
    screen.blit(text_note, (150, 500))
  elif state == 1:
    note = "Prepare-se"
    text_note = font1.render(note, True, "white", "black")
    screen.blit(text_note, (325, 250))
  elif (state == 2):
    note = "Para parar o teste, aperte Q"
    text_note = font1.render(note, True, "white", "black")
    screen.blit(text_note, (175, 500))
  elif (state == 4):
    show_score = "Score: " + str(score) + "/20"
    text_score = font1.render(show_score, True, "white", "black")
    note = "Para reiniciar o teste, aperte W"
    if score != 0:
      average = round(0.001*total_time/score, 3)
    else:
      average = 0
    show_average = "Média de tempo de reação: " + str(average) + "s"
    text_score = font1.render(show_score, True, "white", "black")
    text_average = font1.render(show_average, True, "white", "black")
    text_note = font1.render(note, True, "white", "black")
    screen.blit(text_score, (150, 200))
    screen.blit(text_average, (150, 250))
    screen.blit(text_note, (150, 500))

def show_time(step):
	return 2000 - 50*step

def draw_circle():
  x = rd.uniform(60, 740)
  y = rd.uniform(60, 340)
  color_number = rd.randint(1, 4)
  if color_number == 1:
    color = "blue"
  if color_number == 2:
    color = "green"
  if color_number == 3:
    color = "yellow"
  if color_number == 4:
    color = "red"
  pygame.draw.circle(screen, color, (x, y), 40)
  return color_number

def test_action(start, target):
  global state, step, score, reacted, total_time
  keys = pygame.key.get_pressed()
  q = keys[pygame.K_q]
  r = keys[pygame.K_r]
  t = keys[pygame.K_t]
  y = keys[pygame.K_y]
  u = keys[pygame.K_u]
  if (reacted == False):
    if ((r and target == 1) or (t and target == 2) or (y and target == 3) or (u and target == 4)):     
      total_time = total_time + pygame.time.get_ticks() - start
      score = score + 1
      reacted = True
  if q:
    state = 0
  elif (pygame.time.get_ticks() - start < show_time(step)):
    state = 3
  elif step < 20:
    state = 2
    step = step + 1
  else:
    state = 4
  
def start_screen():
  global state
  screen.fill("black")
  center_rect = pygame.draw.rect(screen, "white", (200, 100, 400, 300))
  show_text(state)
  pygame.display.flip()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    state = 1

def test_start():
  global state, step, score, total_time
  step = 1
  score = 0
  total_time = 0
  screen.fill("black")
  show_text(state)
  pygame.display.flip()
  pygame.time.delay(2000)
  state = 2

def test_screen():
  global state, target, start_time, reacted
  screen.fill("black")
  reacted = False
  show_text(state)
  target = draw_circle()
  pygame.display.flip()
  start_time = pygame.time.get_ticks()
  state = 3

def end_screen():
  global state, score, total_time
  screen.fill("black")
  show_text(state)
  pygame.display.flip()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    state = 1
    
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  if state == 0:
    start_screen()
  elif state == 1:
    test_start()
  elif state == 2:
    test_screen()
  elif state == 3:
    test_action(start_time, target)
  elif state == 4:
    end_screen()

pygame.quit()
