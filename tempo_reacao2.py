import random as rd
import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Teste de Reação")
#clock = pygame.time.Clock()
running = True

state = 0
step = 0
target = 4
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
  screen.fill("black")
  pygame.draw.circle(screen, color, (x, y), 40)
  pygame.display.flip()
  return color_number

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
  pygame.time.delay(2000)
  state = 2
    
#def test_screen():
#  global state, step, score, total_time
#  show_time = 2000 - 50*step
#  keys = pygame.key.get_pressed()
#  r = keys[pygame.K_r]
#  t = keys[pygame.K_t]
#  y = keys[pygame.K_y]
#  u = keys[pygame.K_u]
#  target = draw_circle()
#  start_time = pygame.time.get_ticks()
#  while (pygame.time.get_ticks() - start_time < show_time):
#    if keys[pygame.K_q]:
#      state = 0
#      break
#    #elif ((r and target == 0) or (t and target == 1) or (y and target == 2) or (u and target == 3)):
#    elif r:
#      total_time = total_time + pygame.time.get_ticks() - start_time
#      score = score + 1
#      break
#  if step < 20:
#    step = step + 1
#  elif state != 0:
#    state = 3
#  print(score)
#  print(total_time)

def test_screen():
  global state, step, target, reacted, score, start_time, total_time
  keys = pygame.key.get_pressed()
  r = keys[pygame.K_r]
  t = keys[pygame.K_t]
  y = keys[pygame.K_y]
  u = keys[pygame.K_u]
  if (pygame.time.get_ticks() - start_time < show_time(step)):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
      state = 0
    elif ((reacted == False) and r):
      #total_time = total_time + pygame.time.get_ticks()
      score = score + 1
      reacted = True
  else:
    if step < 20:
      step = step + 1
      target = draw_circle()
      start_time = pygame.time.get_ticks()
      reacted = False
    else:
      state = 3
   
def end_screen():
  global state, score, total_time
  screen.fill("black")
  pygame.display.flip()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    state = 1
  print(score)
    
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
    end_screen()

pygame.quit()
