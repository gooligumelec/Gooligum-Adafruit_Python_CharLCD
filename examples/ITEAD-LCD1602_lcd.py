#!/usr/bin/python
#
# Example using an "ITEAD RPi LCD1602 v2.0" character LCD
#
# Based on Adafruit_Python_CharLCD/examples/char_lcd.py example
# backlight fade added  20/10/15
#   v1.1    20/10/15
#
#   David Meiklejohn
#   Gooligum Electronics

import time
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

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 
                            lcd_columns, lcd_rows, lcd_backlight,
                            invert_polarity=False, enable_pwm=True)

# Print a two line message
lcd.message('Hello\nworld!')

# Wait 5 seconds
time.sleep(5.0)

# Demo showing the cursor.
lcd.clear()
lcd.show_cursor(True)
lcd.message('Show cursor')

time.sleep(5.0)

# Demo showing the blinking cursor.
lcd.clear()
lcd.blink(True)
lcd.message('Blink cursor')

time.sleep(5.0)

# Stop blinking and showing cursor.
lcd.show_cursor(False)
lcd.blink(False)

# Demo scrolling message right/left.
lcd.clear()
message = 'Scroll'
lcd.message(message)
for i in range(lcd_columns-len(message)):
	time.sleep(0.5)
	lcd.move_right()
for i in range(lcd_columns-len(message)):
	time.sleep(0.5)
	lcd.move_left()

# Demo fading backlight off and on.
lcd.clear()
lcd.message('Fade backlight\noff then on...')
time.sleep(1.0)
# Fade backlight off.
for p in range(100, 0, -2):
    lcd.set_backlight(p/100.0)
    time.sleep(0.04)     # 50 steps x 0.04 sec = 2 sec
lcd.set_backlight(0)
time.sleep(0.5)
# Fade backlight on.
for p in range(0, 100, 2):
    lcd.set_backlight(p/100.0)
    time.sleep(0.04)     # 50 steps x 0.04 sec = 2 sec
lcd.set_backlight(1)
# Change message.
lcd.clear()
lcd.message('Goodbye!')
