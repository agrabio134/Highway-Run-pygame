import pygame
import time
import random
import os

pygame.init()

screen_width = 400
screen_height = 600

btn_starting_x = 75
nw_gm_y = 400
set_y = 20
set_y1 = 60
exit_y = 450
btn_width = 242
btn_height = 50

btn_width_set = 50
btn_height_set = 50

black_color = (0, 0, 0)
white_color = (255, 255, 255)
red_color = (255, 0, 0)
redLight_color = (255, 21, 21)
gray_color = (112, 128, 144)
green_color = (0, 255, 0)
greenLight_color = (51, 255, 51)
blue_color = (0, 0, 255)

game_layout_display= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('HIGH WAY RUN')
time_clock=pygame.time.Clock()

car_photo = pygame.image.load(os.getcwd() + '\\img/car.png')
car_god_photo = pygame.image.load(os.getcwd() + '\\img/godmode-car.png')
left_c = pygame.image.load(os.getcwd() + '\\img/car-left.png')
right_c = pygame.image.load(os.getcwd() + '\\img/car-right.png')
photo_obstacle = pygame.image.load(os.getcwd() + '\\img/enemy_car_1.png')
image_background  = pygame.image.load(os.getcwd() + '\\img/back_ground.png')
(c_width, c_height) = car_photo.get_rect().size
# (c_width, c_height) = car_god_photo.get_rect().size
(c_left_width, c_left_height) = left_c.get_rect().size
(c_right_width, c_right_height) = right_c.get_rect().size
(t_width, t_height) = photo_obstacle.get_rect().size
(txtwidth, txtheight) = image_background .get_rect().size



icon = pygame.image.load(os.getcwd() + '\\img/logo.png')
pygame.display.set_icon(icon)

bckgrndRect = image_background.get_rect()

welcome_1 = pygame.mixer.Sound(os.getcwd() + '\\audio/intro.mp3')
welcome_2 = pygame.mixer.Sound(os.getcwd() + '\\audio/intro2.wav')
audio_crash = pygame.mixer.Sound(os.getcwd() + '\\audio/car_crash.wav')
audio_god_mode = pygame.mixer.Sound(os.getcwd() + '\\audio/highwayrun.mp3')
audio_ignition = pygame.mixer.Sound(os.getcwd() + '\\audio/ignition.wav')
pygame.mixer.music.load(os.getcwd()+'\\audio/running.wav')



flag = True
# pygame.mixer.music.load(os.getcwd()+'\\audio/running-bg.mp3')

def things_dodged(counting, highest_score, everything_speed):
	fnt = pygame.font.SysFont(None, 25)
	score = fnt.render("Dodged: " + str(counting), True, green_color)
	h_score = fnt.render("High Score: " + str(highest_score), True, green_color)
	speed = fnt.render("Speed: " + str(everything_speed) + "Km/h", True, green_color)
	game_layout_display.blit(score, (10, 0))
	game_layout_display.blit(h_score, (10, 27))
	game_layout_display.blit(speed, (screen_width - 125, 0))




def audio_volume():
	
	volume = 0.2
	pygame.mixer.Sound.set_volume(welcome_1, volume)
	pygame.mixer.Sound.set_volume(audio_ignition, volume)
	pygame.mixer.Sound.set_volume(audio_god_mode, volume)
	pygame.mixer.Sound.set_volume(audio_crash, volume)
	pygame.mixer.music.set_volume(0.1)     

def audio_volume_up():
	
	volume = 0.8
	pygame.mixer.Sound.set_volume(welcome_1, volume)
	pygame.mixer.Sound.set_volume(audio_ignition, volume)
	pygame.mixer.Sound.set_volume(audio_god_mode, volume)
	pygame.mixer.Sound.set_volume(audio_crash, volume)
	pygame.mixer.music.set_volume(0.5)   


     

def high_score_update(dodged):
	high_scores = open(os.getcwd()+'\\textfile/high_score.txt', 'w')
	temperd = str(dodged)
	high_scores.write(temperd)

def things(th_x, th_y):
	game_layout_display.blit(photo_obstacle, (th_x, th_y))

def car(x, y, direction):
	if direction==0:
			game_layout_display.blit(car_photo, (x, y))	
		# god_mode_function() == True:
		# 	game_layout_display.blit(car_god_photo, (x, y))

	if direction==-1:
		game_layout_display.blit(left_c, (x, y))
	if direction==1:
		game_layout_display.blit(right_c, (x, y))
	# if direction==1:
	# 	game_layout_display.blit(car_god_photo, (x, y))

	# if god_mode_function() == 0:
	# 	game_layout_display.blit(car_god_photo, (x, y))
	


def text_objects(text, font, color):
	txtSurf = font.render(text, True, color)
	return txtSurf, txtSurf.get_rect()

def message_display_screen(txt, sh_x, sh_y, color, time_sleeping):
	lar_txt = pygame.font.Font('freesansbold.ttf',50)
	txtSurf, TxtRect = text_objects(txt, lar_txt, color)
	TxtRect.center = ((screen_width / 2 - sh_x), (screen_height / 2 - sh_y))
	game_layout_display.blit(txtSurf, TxtRect)
	pygame.display.update()
	time.sleep(time_sleeping)

def title_message_display(sh_x, sh_y, color):
	menu_txt = pygame.font.Font('freesansbold.ttf',50)
	txtSurf, TxtRect = text_objects("HIGHWAY RUN", menu_txt, color)
	TxtRect.center = ((screen_width / 2 - sh_x), (screen_height / 3 - sh_y))
	game_layout_display.blit(txtSurf, TxtRect)
	time.sleep(0.15)
	pygame.display.update()

def title_msg():
	animation_height=screen_height
	pygame.mixer.Sound.play(welcome_1)
	
	while animation_height > -600:
		game_layout_display.fill(white_color)
		things(screen_width / 2 - t_width / 2, animation_height)
		animation_height-=1.5
		pygame.display.update()
	title_message_display(0, 0, black_color)
	time.sleep(0.1)
	pygame.mixer.Sound.play(welcome_2)


def motion_texture(th_starting):
	game_layout_display.blit(image_background , (0, th_starting - 470))
	game_layout_display.blit(image_background , (0, th_starting))
	game_layout_display.blit(image_background , (0, th_starting + 470))

def crash_function():

	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(audio_crash)
	message_display_screen("CRASHED", 0, 0, red_color, 0)

	while (flag):
		playAgain = button("Play Again", btn_starting_x, nw_gm_y, btn_width, btn_height, greenLight_color, green_color)
		exit_game = button("Quit", btn_starting_x, exit_y, btn_width, btn_height, redLight_color, red_color)
		for event in pygame.event.get():
			if event.type == pygame.QUIT or exit_game == 1 or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				quit()
			if playAgain== 1 or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
				looping_gameplay()
		pygame.display.update()
		time_clock.tick(15)

# shouldRun = True
def god_mode_function():
	pygame.mixer.Sound.play(audio_god_mode)	
	message_display_screen ("Invincible!", 0, 0, green_color, 0.01)
	s

def button(messages, x, y, wid, hei, in_act_color, act_color, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x + wid > mouse[0] > x and y+hei > mouse[1] > y:
		pygame.draw.rect(game_layout_display, act_color, (x, y, wid, hei))
		if click[0] == 1:
			return 1
	else:
		pygame.draw.rect(game_layout_display, in_act_color, (x, y, wid, hei))

	small_txt = pygame.font.Font('freesansbold.ttf',20)
	TxtSurf, TxtRect = text_objects(messages, small_txt, white_color)
	TxtRect.center = ((x + wid / 2), (y + hei / 2))
	game_layout_display.blit(TxtSurf, TxtRect)

def welcome_gameplay():
	welcome = True
	game_layout_display.fill(white_color)
	title_msg()
	exit_game=0
	while welcome:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or exit_game == 1 or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				quit()
		playGame = button("Start game", btn_starting_x, nw_gm_y, btn_width, btn_height, greenLight_color, green_color)
		
		exit_game = button("Quit", btn_starting_x, exit_y, btn_width, btn_height, redLight_color, red_color)
		volup = button("+", btn_starting_x, set_y, btn_width_set, btn_height_set, gray_color, black_color)
		voldown = button("-", btn_starting_x, set_y1, btn_width_set, btn_height_set, gray_color, black_color)
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				exit_game = 1
		if playGame or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
			welcome = False
		if voldown:
			audio_volume()
			game_layout_display.fill(white_color)
		if volup:
			audio_volume_up()
			game_layout_display.fill(white_color)
		pygame.display.update()
		time_clock.tick(15)


def counting_three_two_one():
	counting = 3
	pygame.mixer.music.pause()
	pygame.mixer.Sound.play(audio_ignition)
	while counting >= 0:
		game_layout_display.blit(image_background, bckgrndRect)
		car(screen_width * 0.40, screen_height * 0.6, 0)
		if counting == 0:
			message_display_screen ("GO!", 0, 0, green_color, 0.75)
			pygame.mixer.music.play(-1)
		else:
			message_display_screen (str(counting), 0, 0, red_color, 0.75)
		counting -= 1
	time_clock.tick(15)





def gameplay_paused():
	pygame.mixer.music.pause()
	pause = True
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):  
				pygame.quit()
				quit()
			message_display_screen("PAUSE", 0, 0, blue_color, 1.5)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pygame.mixer.music.unpause()
					return
		pygame.display.update()
		time_clock.tick(15)

def looping_gameplay():
	pygame.mixer.music.play(-1)
	# display = 0
	width_x=(screen_width * 0.4)
	height_y=(screen_height * 0.6)
	ch_x=0

	th_st_x = random.randrange(6, screen_width - t_width - 8)
	th_st_y = -500
	th_speed = 8

	# tracking_y = 0
	# tracking_speed = 25

	dodg=0
	direction = 0

	highest_score_txtfile = open(os.getcwd()+'/textfile/high_score.txt','r')
	high_score = highest_score_txtfile.read()

	gameExit = False
	counting_three_two_one()

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					ch_x = -10
					direction = -1
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					ch_x = 10
					direction = 1
               
				if event.key == pygame.K_SPACE:
					gameplay_paused()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
					ch_x = 0 
					direction = 0
		width_x+=ch_x
		game_layout_display.blit(image_background, bckgrndRect)

		motion_texture(th_st_y)
		things(th_st_x, th_st_y)
		th_st_y += th_speed
		car(width_x,height_y,direction)

		things_dodged(dodg, high_score, th_speed)
		if width_x > screen_width - c_width or width_x < 0:
			collision = True
			if dodg >= 5 and dodg <= 15 :
				collision = False
				god_mode_function()
					
				# game_layout_display.blit(car_god_photo, ())	
			elif dodg >= 30 and dodg <= 45 :
				collision = False
				god_mode_function()
			elif dodg >= 60 and dodg <= 80 :
				collision = False
				god_mode_function()	
			elif dodg >= 100 and dodg <= 120 :
				collision = False
				god_mode_function()	
			elif dodg >= 170 and dodg <= 200 :
				collision = False
				god_mode_function()
	
				# time.sleep(2.4)

			elif collision == True:
				crash_function()
			


	
			print("invincible")
		if height_y < th_st_y+t_height-15 and width_x > th_st_x-c_width-5 and width_x < th_st_x+t_width-5:
			collision = True
			if dodg >= 5 and dodg <= 15 :
				collision = False
				god_mode_function()
					# message_display_screen ("Invincible!", 0, 0, green_color, 0.01)
				
				# god_mode_function()
				# collision = False
				# message_display_screen ("Invincible!", 0, 0, green_color, 0.01)

				# game_layout_display.blit(car_god_photo, ())	

			elif dodg >= 30 and dodg <= 45 :
				collision = False
				god_mode_function()
			elif dodg >= 60 and dodg <= 80 :
				collision = False
				god_mode_function()	
			elif dodg >= 100 and dodg <= 120 :
				collision = False
				god_mode_function()	
			elif dodg >= 170 and dodg <= 200 :
				collision = False
				god_mode_function()
			elif collision == True:
				crash_function()
			
			print("invincible")

		if dodg > int(high_score):
			high_score_update(dodg)

		if th_st_y > screen_height:
			th_st_y = 0 - t_height
			th_st_x = random.randrange(0, screen_width)
			dodg += 1
			th_speed += 1
		
		
        # if dodg == 3:
        #     crash_function()

		pygame.display.update()
		time_clock.tick(60)

welcome_gameplay()
looping_gameplay()
pygame.quit()
quit()
