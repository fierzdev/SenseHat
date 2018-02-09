#!/usr/bin/env python3
"""Messing arround"""

#imports
from sense_hat import SenseHat
from datetime import datetime
from time import sleep
import random
import fibonacci

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json




#####################
#####Functions#######
#####################

"""Print the current time"""
def show_time():
	time = datetime.now().strftime('%H:%M');
	sense.show_message(time,scroll_speed=0.15,text_colour=dark_colour)
	return
"""Print the current date"""
def show_date():
	time = datetime.now().strftime('%d.%m');
	sense.show_message(time,scroll_speed=0.15,text_colour=dark_colour,
	back_colour=(20,20,20))
	return

"""Print some random pixels"""
def random_pixels():
	for i in range(2*64):
		sense.set_pixel(random.randrange(0,8),random.randrange(0,8),(0,150,0))
		sleep(0.1)

"""Choose fibonacci and display it"""
def show_fibonacci():
	fibo = fibonacci.Fibonacci()
	i = 1;
	choosing = True;
	while choosing:
		option = sense.stick.wait_for_event(emptybuffer=True)
		if (option.action =="pressed"):
			if(option.direction =="up" or option.direction=="right") and i<64:
				i+=1
			if(option.direction=="down" or option.direction=="left") and (i>0):
				i-=1
			if(option.direction=="middle"):
				choosing = False;
		result = []
		for n in range(i):
			result.append((100,100,100))
		for n in range(64-i):		#64 being max size.
			result.append((9,9,9)) 
		sense.set_pixels(result)
	sense.show_message('Calculating fib from: ' + str(i))
	sense.show_message(str(fibo.fib(i)),scroll_speed=0.15,text_colour=dark_colour)

"""Choose a color"""
def choose_color():
	choosing = True
	result = [0,0,0]
	position = 0;
	while choosing:
		option = sense.stick.wait_for_event(emptybuffer=True);
		if (option.action == "pressed"):
			if (option.direction == "up" and result[position]<255):
				result[position] += 1
			elif (option.direction == "down" and result[position]>0):
				result[position] -= 1
			elif (option.direction == "left" and position!=0):
				position -= 1;
				sleep(0.3)
			elif (option.direction == "right" and position!=2):
				position += 1;
				sleep(0.3)
			elif (option.direction == "middle"):
				choosing = False
				sleep(0.5)
			print(result)
			x = result;
			x = [x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x]
			sense.set_pixels(x)
			sense.set_pixel(0,0,result)
	return

"""Log button pressed"""
def log_pressed():
	with open('pressed_logging.txt','a') as f:
		f.write(datetime.now().strftime('%H:%M')+'\n')
	sleep(0.3)

def get_openweathermap_api_key():
	with open('apikeys.txt','r') as f:
		data = f.read()
		return json.loads(data)['openweathermap']

"""Get Temperature in winterthur from openweathermap.org"""
def get_temp_for_winterthur():
	url = "http://api.openweathermap.org/data/2.5/weather?q=Winterthur,ch&mode=json&units=metric&appid=" + get_openweathermap_api_key()
	response = urlopen(url)
	data = response.read().decode("utf-8")
	jsondata = json.loads(data)
	return jsondata['main']['temp']

"""Displays the current temperature for Winterthur"""
def show_temperature():
	message = "Temp:" + str(get_temp_for_winterthur()) + "C"
	sense.show_message(message,scroll_speed=0.15,text_colour=dark_colour)





####################
####Variables#######
####################

no_colour = (0,0,0)
dark_colour = (50,50,50)
red_colour = (255,0,0)
green_colour = (0,255,0)
blue_colour = (0,0,255)
bright_colour = (255,255,255)
sense = SenseHat();


###################
###Program start###
###################
 
#sense.show_message("test",scroll_speed=0.12,back_colour=[40,40,40],text_colour=[100,0,0]);


event = sense.stick.wait_for_event(emptybuffer=True)
print("The joystick was {} {}".format(event.action, event.direction))
# if (event.action=="pressed" and event.direction=="up"):
# 	show_date()
# if (event.action=="pressed" and event.direction=="down"):
# 	show_time()
# if (event.action=="pressed" and event.direction=="left"):
# 	sleep(0) 
# if (event.action=="pressed" and event.direction=="right"):
#  	sleep(0)
# sleep(5)
event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))


sense.set_pixel(0,0,(0,0,255))
while True:
	event = sense.stick.wait_for_event(emptybuffer=True)
	#Switch case substitute
	options = {
#		"up": show_date,
		"up":show_temperature,
		"down": show_time,
		#"right": random_pixels,
		"right": show_fibonacci,
		"left": choose_color,
		"middle": log_pressed,
	}
	direction = str(event.direction)
	options[direction]()
