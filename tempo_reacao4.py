import random as rd
import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Teste de Reação")
#clock = pygame.time.Clock()
running = True

state = 0
step = 0
reacted = False
score = 0
start_time = 0
total_time = 0

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
  pygame.draw.rect(screen, "white", (200, 100, 400, 300))
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
  pygame.display.flip()
  pygame.time.delay(2000)
  state = 2

def test_screen():
  global state, target, start_time, reacted
  screen.fill("black")
  reacted = False
  target = draw_circle()
  pygame.display.flip()
  start_time = pygame.time.get_ticks()
  state = 3
  print(score)

def end_screen():
  global state, score, total_time
  screen.fill("black")
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
