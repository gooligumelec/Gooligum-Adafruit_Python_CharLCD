#!/usr/bin/python
#
# Example of using buttons on an "ITEAD RPi LCD1602 v2.0" board
#
# Based on Adafruit_Python_CharLCD/examples/char_lcd_plate.py example
#   v1.0    20/10/15
#
#   David Meiklejohn
#   Gooligum Electronics

import time
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD

# ITEAD RPi LCD1602 v2.0 pin configuration:
lcd_rs        = 22
lcd_en        = 23
lcd_d4        = 24
lcd_d5        = 25
lcd_d6        = 26
lcd_d7        = 27
lcd_backlight = 21

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Define pushbutton switch GPIOs
buttonIO = [16, 17, 18, 19, 20]    # SW1..5


# configure I/O
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonIO, GPIO.IN)

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight,
                           invert_polarity=False, enable_pwm=True)


# Show button state.
lcd.clear()
lcd.message('Press buttons...')

# Text associated with each button
button_text = [ 'SW1\nButton one',
                'SW2\nButton two',
                'SW3\nButton three',
                'SW4\nButton four',
                'SW5\nButton five' ]

print 'Press Ctrl-C to quit.'
while True:
	# Loop through each button and check if it is pressed.
	for b in range(5):
		if GPIO.input(buttonIO[b])==0 :
			# Button is pressed, change the message
			lcd.clear()
			lcd.message(button_text[b])
