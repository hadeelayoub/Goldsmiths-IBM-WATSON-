import gaugette.ssd1306
import time
import sys
from gpiozero import Button
import os

state = -1

def increment_state():
    global state
    state += 1
    print "red pressed"

def power_off():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output

red_button = Button(5)
black_button = Button(21)

red_button.when_pressed = increment_state
black_button.when_pressed = power_off

# Define which GPIO pins the reset (RST) and DC signals on the OLED display are connected to on the
# Raspberry Pi. The defined pin numbers must use the WiringPi pin numbering scheme.
RESET_PIN = 15 # WiringPi pin 15 is GPIO14.
DC_PIN = 16 # WiringPi pin 16 is GPIO15.




# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()

led.clear_display()
text = 'READY'
led.draw_text2(0,0,text,1)

while state == -1:
    pass

led.clear_display()
text = 'Today we present'
led.draw_text2(0,0,text,1)
text2 = 'Bright Sign'
led.draw_text2(0,16,text2,2)
led.display()

os.system("aplay 1.wav")

while state == 0:
    pass

led.clear_display()
text = 'This glove is'
led.draw_text2(0,0,text,1)
text2 = 'designed to help'
led.draw_text2(0,9,text2,1)
text3 = 'speech disblaed people'
led.draw_text2(0,17,text3,1)
text4 = 'with daily communication'
led.draw_text2(0,25,text4,1)
led.display()

os.system("aplay 2.wav")

while state == 1:
    pass

led.clear_display()
text = 'One day we'
led.draw_text2(0,0,text,1)
text2 = 'hope to give a'
led.draw_text2(0,9,text2,1)
text3 = 'voice to those'
led.draw_text2(0,17,text3,1)
text4 = 'who cannot speak'
led.draw_text2(0,25,text4,1)
led.display()

os.system("aplay 3.wav")

while state == 2:
    pass
