from gpiozero import MCP3008
import gaugette.ssd1306
import time
import os

pot = MCP3008(0)
pot1 = MCP3008(1)
pot2 = MCP3008(2)
pot3 = MCP3008(3)
pot4 = MCP3008(4)

# OLED screen stuff
RESET_PIN = 15
DC_PIN = 16
led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()

led.clear_display()
text = 'BrightSign'
led.draw_text2(0,0,text,2)
led.display()

print(pot.value,pot1.value,pot2.value,pot3.value,pot4.value)

#while True:
    #print(pot4.value)
    #print(pot.value,pot1.value,pot2.value,pot3.value,pot4.value)
    

while True:
    if(pot.value)>0.7 and (pot1.value)>0.7:
        print("Hi")
        led.clear_display()
        text = 'Hi'
        led.draw_text2(0,0,text,2)
        led.display()

        #os.system("aplay 1.wav")

    if(pot.value)<0.7 and (pot1.value)<0.7:
        print ("OK")
        led.clear_display()
        text = 'OK'
        led.draw_text2(0,0,text,2)
        led.display()

        #os.system("aplay 2.wav") 
