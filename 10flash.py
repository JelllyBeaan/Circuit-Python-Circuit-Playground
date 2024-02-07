import time
import board
import neopixel

# Calls the circuit Python neopixel library, specifies the default board 
# pins for the Neopixels, and the number of neopixels to access.  Returns a 
# list 'pixels' of indexable neopixles
x = 10
i = 0
colorsfill = [230,200,20,30,160,255,140,70,90,220]
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = 0.2)

while True:  # indexes the first element of the 'pixels' list and points to the 
    # first (and only) Neopixel in the 'pixels' list
   
    pixels[i]=(0, 255, 0)
    pixels[i+1]= (200, 0, 200)
    pixels[i+2] = (60,200,70)
    pixels[i+3] = (50,10,70)
    pixels[i+4] = (230,200,70)
    pixels[i+5] = (210,30,200)
    pixels[i+6] = (150,10,255)
    pixels[i+7] = (230,200,70)
    pixels[i+8] = (55,130,20)
    time.sleep(0.5)
    pixels.fill((255, 255, 255))
    time.sleep(0.5)
    if i >= 1 :
        i = -1
        print ("reset")
    i += 1
    
